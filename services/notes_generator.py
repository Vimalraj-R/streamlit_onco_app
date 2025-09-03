def generate_notes(patient):
    return f"""
    Patient {patient['name']} ({patient['age']} years old) diagnosed with {patient['condition']}.
    Medications: {', '.join(patient['meds'])}.
    Lifestyle risks: Smoking {patient['lifestyle']['smoking']*100:.0f}%, Alcohol {patient['lifestyle']['alcohol']*100:.0f}%.
    Genetic markers: {', '.join(patient['genes'])}.
    """
