# Peptide Slicing

Peptides of length 9–12 amino acids were generated from both the human and 
microbial protein sequences. These peptides were used as input for downstream binding prediction and mimicry analysis.

Two different slicing strategies were applied to ensure both biological
relevance and broad coverage of potential candidates.>

<br>

:::{note} Note
**Scripts**

Peptide slicing was performed using custom Python scripts based on Biopython

Scripts are available in the GitHub repository under: /scripts
/pep_generation/
:::

<br>

**a. Rule-Free Peptide Slicing**

In this approach, peptides were generated using a simple sliding window method 
without applying any positional constraints. This strategy allows unbiased 
sampling of all possible 9–12 mer peptides from the protein sequences.

The goal of this method was to ensure that no potential mimicry candidate was
 missed during the initial screening.

<br>

**b. Anchor-Rule-Based Peptide Slicing**

In the second approach, known HLA-B27 anchor residue preferences were applied 
during peptide generation. This method enriches for peptides that are more
likely to bind to HLA-B27.

Applying anchor rules helps focus the analysis on biologically plausible 
binders while reducing the total search space.

<br>

:::{hint} Hint

**Why 9–12 mers?**

HLA class-I molecules, including HLA-B27, preferentially bind peptides of 9–12 amino acids.
Among these, 9-mers are the most commonly observed binders.


**What are anchor residues?**

Anchor residues are specific amino acids at defined positions within a peptide
that enhance binding to the HLA groove. For HLA-B27, positively charged residues
at position 2 and hydrophobic or aromatic residues at the C-terminal position are commonly preferred.
:::

<br>


