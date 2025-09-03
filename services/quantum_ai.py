# services/quantum_ai.py

# ✅ Real cancer drugs with brief descriptions
cancer_drugs = [
    "Carboplatin – Platinum-based chemotherapy (ovarian, lung, head & neck cancers)",
    "Fluorouracil (5-FU) – Antimetabolite (colon, gastric, pancreatic cancers)",
    "Doxorubicin – Anthracycline (breast, bladder, lymphoma, leukemia)",
    "Etoposide – Topoisomerase inhibitor (lung cancer, testicular cancer)",
    "Vincristine – Vinca alkaloid (leukemia, lymphoma, pediatric cancers)",
    "Vinblastine – Vinca alkaloid (lymphoma, testicular cancer, breast cancer)",
    "Ifosfamide – Alkylating agent (sarcoma, testicular cancer, lymphoma)",
    "Topotecan – Topoisomerase I inhibitor (ovarian, cervical, lung cancers)",
    "Cisplatin – Platinum chemotherapy (lung, ovarian, bladder, testicular cancer)",
    "Cyclophosphamide – Alkylating agent (breast cancer, lymphoma, leukemia)",
    "Paclitaxel – Taxane (breast, ovarian, lung cancer, Kaposi sarcoma)",
    "Methotrexate – Antimetabolite (breast, lymphoma, leukemia, osteosarcoma)",
    "Trastuzumab – Targeted therapy (HER2+ breast & gastric cancer)",
    "Prednisone – Corticosteroid (leukemia, lymphoma supportive therapy)",
    "Bleomycin – Antibiotic chemotherapy (testicular cancer, lymphoma, cervical cancer)",
    "Leucovorin – Folinic acid, enhances 5-FU efficacy (colorectal cancer)",
    "Erlotinib – Targeted therapy (non-small cell lung cancer, pancreatic cancer)"
]


def quantum_genetic_drug_optimizer(patient, meds):
    # Dummy scoring function for optimization
    best_combo = meds[:2] if len(meds) >= 2 else meds
    best_score = 0.85
    return best_combo, best_score

def predict_effectiveness(patient, meds):
    return 0.7 + 0.1 * (len(meds) % 3)

def tensor_network_score(patient, meds):
    return 0.6 + 0.05 * len(meds)
