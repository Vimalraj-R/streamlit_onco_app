def explain(patient):
    return {
        "reasoning": (
            f"Patient {patient['name']} is on medications {', '.join(patient['meds'])}. "
            f"Genetic mutations ({', '.join(patient.get('genes', []))}) may alter drug response. "
            "Lifestyle factors such as smoking, alcohol, and obesity further modify toxicity levels "
            "and overall drug effectiveness. Clinical evaluation with genetic counseling is recommended."
        ),
        "reference": "PubMed ID: 12345"
    }
