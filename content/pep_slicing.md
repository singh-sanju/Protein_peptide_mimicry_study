#### i. Peptide Slicing

Peptides of length 9–12 amino acids were generated from both the selected human protein and the microbial proteome. These peptides were used as input for downstream binding prediction and molecular mimicry screening.
To balance biological relevance and broad coverage, two complementary peptide slicing strategies were applied:

- ***Rule-free peptide slicing***

- ***Anchor-rule-based peptide slicing***

The rule-free approach ensures broad exploration of the peptide space by generating all possible 9–12-mer peptides without applying any binding constraints. This allows potential mimicry candidates to be identified without bias. On the other hand, the anchor-rule-based approach applies known HLA-B27 anchor residue preferences to enrich for peptides with a higher likelihood of binding to the MHC groove.

Both strategies were applied consistently to human and microbial proteins, ensuring that all peptides were generated and evaluated under identical rules. This combined approach increases the robustness and credibility of downstream binding prediction and similarity analysis.

:::{hint} Hint

**Why 9–12 mers?**

HLA class-I molecules, including HLA-B27, preferentially bind short peptides presented in the antigen-binding groove.
Among these, 9-mer peptides are the most commonly observed binders, while 10–12-mer peptides are also accommodated with minor conformational flexibility.
Therefore, peptides of length 9–12 amino acids were selected to capture canonical binders while allowing limited variability @article, .


**What are anchor residues?**

Anchor residues are specific amino acids at defined positions within a peptide that enhance binding to the HLA groove by fitting into conserved binding pockets.
For HLA-B27, a positively charged residue (Arg or Lys) is typically preferred at position 2, and a hydrophobic or aromatic residue is favored at the C-terminal position (PΩ).
These anchor preferences increase the likelihood of stable peptide–MHC interactions @BARNEA2017642.

:::


##### Peptide Slicing Rules
**a. Rule-Free Peptide Slicing**

In this approach, peptides were generated using a simple sliding window method 
without applying any positional constraints. This strategy allows unbiased 
sampling of all possible 9–12 mer peptides from the protein sequences.
The goal of this method was to ensure that no potential mimicry candidate was
 missed during the initial screening.

<br>

**b. Anchor-Rule-Based Peptide Slicing**

In this approach, peptides were generated or sliced according to  known HLA-B27 anchor residue preferences rule. This method enriches for peptides that are more
likely to bind to HLA-B27 and anchor rules also helps focus the analysis on biologically plausible 
binders while reducing the total search space.

:::{note} Note

- All the peptide slicing processes were performed using custom Python scripts developed for this study.

- All the scripts used for peptide slicing are available in the projector repository under	*/scripts/pep_generation/*.
:::



