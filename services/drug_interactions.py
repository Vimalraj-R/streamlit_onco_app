def normalize(drug_name: str) -> str:
    """Remove descriptions (anything after '–') and extra spaces."""
    return drug_name.split("–")[0].strip()


def check_drug_interactions(meds, lifestyle):
    """Check real cancer drug interactions and lifestyle effects."""

    alerts = []

    # Normalize meds for matching
    meds_clean = [normalize(m) for m in meds]

    # ❌ Negative / Dangerous Interactions
    negative_pairs = {
        ("Carboplatin", "Ifosfamide"): "Severe kidney toxicity (risk of renal damage)",
        ("Doxorubicin", "Trastuzumab"): "High risk of heart failure (cardiotoxicity)",
        ("Fluorouracil", "Leucovorin"): "Excessive toxicity when overdosed",
        ("Cyclophosphamide", "Doxorubicin"): "Bone marrow suppression risk",
        ("Etoposide", "Vincristine"): "Severe neurotoxicity and bone marrow suppression",
        ("Ifosfamide", "Cisplatin"): "Increased neurotoxicity and kidney damage",
        ("Vinblastine", "Bleomycin"): "Pulmonary toxicity (lung damage risk)"
    }

    # ✅ Positive / Synergistic Interactions
    positive_pairs = {
        ("Carboplatin", "Paclitaxel"): "Standard combo in ovarian & lung cancer (synergistic)",
        ("Doxorubicin", "Cyclophosphamide"): "Common breast cancer regimen (AC protocol)",
        ("Fluorouracil", "Leucovorin"): "Boosted efficacy in colorectal cancer",
        ("Etoposide", "Cisplatin"): "Synergistic in small-cell lung cancer",
        ("Vincristine", "Prednisone"): "Effective combination in leukemia protocols",
        ("Ifosfamide", "Etoposide"): "Enhanced tumor control in sarcoma therapy",
        ("Topotecan", "Cisplatin"): "Improved survival in cervical cancer"
    }

    # 🔍 Check negative interactions
    for (d1, d2), risk in negative_pairs.items():
        if d1 in meds_clean and d2 in meds_clean:
            alerts.append({
                "drug1": d1,
                "drug2": d2,
                "risk": risk,
                "type": "negative"
            })

    # 🔍 Check positive interactions
    for (d1, d2), benefit in positive_pairs.items():
        if d1 in meds_clean and d2 in meds_clean:
            alerts.append({
                "drug1": d1,
                "drug2": d2,
                "risk": benefit,
                "type": "positive"
            })

    # 🍷 Lifestyle effects
    if lifestyle.get("alcohol", 0) > 0.3 and "Methotrexate" in meds_clean:
        alerts.append({
            "drug1": "Methotrexate",
            "drug2": "Alcohol",
            "risk": "Liver toxicity risk increased significantly",
            "type": "negative"
        })
    if lifestyle.get("smoking", 0) > 0.3 and "Erlotinib" in meds_clean:
        alerts.append({
            "drug1": "Erlotinib",
            "drug2": "Smoking",
            "risk": "Smoking reduces Erlotinib effectiveness in lung cancer",
            "type": "negative"
        })

    return alerts
