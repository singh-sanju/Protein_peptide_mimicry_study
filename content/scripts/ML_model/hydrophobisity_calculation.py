# Hydrophobicity calculator using Kyte-Doolittle scale (used for peptides or aa sequences)

# Kyte-Doolittle hydropathy index
kd_scale = {
    'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
    'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
    'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5,
    'K': -3.9, 'R': -4.5
}

# Example peptide sequences
peptides = {
    'H2': 'AKAQTDRENL',
    'H3': 'TNTQTYRESL',
    'H4': 'TNTQTYRESL',
    'M1': 'SRFEFKRVL',
    'M2': 'GRSDFKGDY',
    'M3': 'GRSDFKGDYF',
    'M4': 'SRSDRVAKY',
    'M5': 'NSRQTDREDE'
    }
# Function to calculate average hydrophobicity
def calculate_avg_hydrophobicity(sequence):
    values = [kd_scale.get(aa, 0) for aa in sequence]
    return sum(values) / len(values)

# Calculate and print
print("Peptide Hydrophobicity Scores (Kyte-Doolittle):\n")
for name, seq in peptides.items():
    avg_hydro = calculate_avg_hydrophobicity(seq)
    print(f"{name:8s} : {avg_hydro:.2f}")




