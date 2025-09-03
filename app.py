import streamlit as st
import pandas as pd
import plotly.express as px

from services.drug_interactions import check_drug_interactions
from services.notes_generator import generate_notes
from services.explainable_ai import explain
from services.quantum_ai import (
    quantum_genetic_drug_optimizer,
    predict_effectiveness,
    tensor_network_score,
    cancer_drugs
)
from services.body_simulation import body_simulation
from services.genetic_graph import genetic_graph

# ---------------- Session State ---------------- #
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "users" not in st.session_state: st.session_state.users = {}
if "current_user" not in st.session_state: st.session_state.current_user = None
if "patients" not in st.session_state: st.session_state.patients = []

cancer_types = [
    "Lung Cancer", "Breast Cancer", "Leukemia", "Colon Cancer",
    "Lymphoma", "Prostate Cancer", "Ovarian Cancer",
    "Liver Cancer", "Pancreatic Cancer", "Melanoma"
]

# ---------------- Auth ---------------- #
def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username", key="signup_user")
    password = st.text_input("Password", type="password", key="signup_pass")
    confirm = st.text_input("Confirm Password", type="password", key="signup_confirm")
    if st.button("Sign Up"):
        if not username or not password or not confirm:
            st.warning("Fill all fields")
        elif password != confirm:
            st.warning("Passwords do not match")
        elif username in st.session_state.users:
            st.warning("Username exists")
        else:
            st.session_state.users[username] = password
            st.success("Signup successful! Please login.")

def login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.rerun()
        else:
            st.error("Invalid username or password")

# ---------------- Patient Entry ---------------- #
def patient_entry():
    st.subheader("Add Patient")
    with st.form("patient_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", 0, 120, 50)
        condition = st.selectbox("Disease / Cancer Type", cancer_types)
        meds = st.multiselect("Medications", cancer_drugs)
        smoking = st.slider("Nicotin (%)", 0, 100, 10)
        alcohol = st.slider("Alcohol (%)", 0, 100, 5)
        obesity = st.slider("Obesity (%)", 0, 100, 0)
        submitted = st.form_submit_button("Add Patient")

    if submitted:
        if not name or not condition or not meds:
            st.warning("Fill all fields")
        else:
            patient = {
                "name": name,
                "age": age,
                "condition": condition,
                "meds": meds,
                "lifestyle": {
                    "smoking": smoking / 100,
                    "alcohol": alcohol / 100,
                    "obesity": obesity / 100
                },
                "genes": ["BRCA1", "TP53", "EGFR", "KRAS"],
                "user": st.session_state.current_user
            }
            st.session_state.patients.append(patient)
            st.success(f"Patient {name} added!")

# ---------------- CSV Upload ---------------- #
def csv_upload():
    st.subheader("Upload CSV")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        for _, row in df.iterrows():
            patient = {
                "name": row['name'],
                "age": row['age'],
                "condition": row['condition'],
                "meds": row['meds'].split(","),
                "genes": ["BRCA1", "TP53", "EGFR", "KRAS"],
                "user": st.session_state.current_user,
                "lifestyle": {"smoking": 0, "alcohol": 0, "obesity": 0}
            }
            st.session_state.patients.append(patient)
        st.success(f"{len(df)} patients added")

# ---------------- Display ---------------- #
def display_patients():
    st.subheader("Patient List")
    user_patients = [p for p in st.session_state.patients if p["user"] == st.session_state.current_user]
    if user_patients:
        df = pd.DataFrame(user_patients)
        st.dataframe(df[["name", "age", "condition", "meds"]])
    else:
        st.info("No patients yet")

# ---------------- Analytics ---------------- #
def analyze_patient():
    user_patients = [p for p in st.session_state.patients if p["user"] == st.session_state.current_user]
    if not user_patients: return
    patient_index = st.selectbox("Select Patient", range(len(user_patients)), format_func=lambda i: user_patients[i]["name"])
    patient = user_patients[patient_index]

    st.write("### Quantum-Inspired AI Analysis")
    best_combo, best_score = quantum_genetic_drug_optimizer(patient, patient["meds"])
    st.write(f"Optimal Drug Combo: {best_combo} | Score: {best_score:.2f}")
    effectiveness = predict_effectiveness(patient, patient["meds"])
    st.write(f"Predicted Effectiveness: {effectiveness:.2f}")
    tensor_score = tensor_network_score(patient, patient["meds"])
    st.write(f"Tensor Network Score: {tensor_score:.2f}")

    # Drug Alerts
    alerts = check_drug_interactions(patient['meds'], patient['lifestyle'])
    if alerts:
        st.warning("⚠️ Risky Drug Interactions Detected")
        for a in alerts:
            st.write(f"{a['drug1']} + {a['drug2']} → {a['risk']}")
    else:
        st.success("✅ No risky interactions")

    # Genetic Graph
    fig = genetic_graph(patient)
    st.plotly_chart(fig, use_container_width=True)

    # Explanation
    explanation = explain(patient)
    st.markdown("**Explanation:**")
    st.write(explanation['reasoning'])
    st.write("Reference:", explanation.get('reference', ''))

    # Body Simulation
    st.subheader("🧍 Digital Body Simulation")
    body_fig = body_simulation(patient)
    st.plotly_chart(body_fig, use_container_width=True)

def show_charts():
    st.subheader("Analytics Charts")
    user_patients = [p for p in st.session_state.patients if p["user"] == st.session_state.current_user]
    if not user_patients: return
    df = pd.DataFrame(user_patients)

    # Pie Chart - Disease distribution
    disease_count = df['condition'].value_counts()
    fig = px.pie(names=disease_count.index, values=disease_count.values, title="Patients by Disease")
    st.plotly_chart(fig)

    # Bar Chart - Medication frequency
    med_counts = {}
    for meds in df['meds']:
        for m in meds:
            med_counts[m] = med_counts.get(m, 0) + 1
    med_df = pd.DataFrame({"Drug": list(med_counts.keys()), "Count": list(med_counts.values())})
    fig2 = px.bar(med_df, x="Drug", y="Count", title="Medications Count")
    st.plotly_chart(fig2)

# ---------------- Main App ---------------- #
def main_app():
    st.title("Qubitry AI : Quantum-Inspired Oncology Assistant")
    st.subheader(f"Welcome, {st.session_state.current_user}!")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.rerun()

    tabs = st.tabs(["Manual Entry", "CSV Upload", "Patients Table", "Analytics"])
    with tabs[0]: patient_entry()
    with tabs[1]: csv_upload()
    with tabs[2]:
        display_patients()
        analyze_patient()
    with tabs[3]: show_charts()

# ---------------- App Flow ---------------- #
if not st.session_state.logged_in:
    st.title("Oncology Assistant Login/Signup")
    auth_option = st.radio("Choose Option", ["Login", "Sign Up"])
    if auth_option == "Login": login()
    else: signup()
else:
    main_app()
