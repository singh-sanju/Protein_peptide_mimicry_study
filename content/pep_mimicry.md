# Peptide Filtering and Similarity Screening

The large peptide pool generated from slicing was filtered to identify biologically relevant molecular mimicry candidates. The filtering strategy focused on three key criteria:

- Predicted binding to HLA-B27  
- Sequence similarity to the human Annexin (ANX) peptide  
- Potential functional relevance  


## HLA-B27 Binding Prediction

All generated peptides from both human and microbial sources were screened
for HLA-B27 binding using NetMHCpan.

Based on predicted binding affinity, peptides were classified as:
- Strong binders (SB)
- Weak binders (WB)

Only top strong binders were retained for further analysis based on binding scores. Approximately ten strong-binding ANX peptides and ninety strong-binding microbial peptides were selected at this stage.

## Mimicry Scoring

Sequence similarity between human ANX peptides and microbial peptides was evaluated using a two-step approach.

First, BLAST-based sequence comparison was used for an initial inspection of similarity between human and microbial peptides. This step provided a broad overview of potential overlaps and helped guide further analysis.

Subsequently, pairwise sequence alignment was performed using Biopython (Bio.Align) with the BLOSUM62 scoring matrix. This step was used for systematic and quantitative similarity scoring between ANX-derived peptides and *Klebsiella pneumoniae* peptides.

The pairwise alignment scores were used to identify microbial peptides sharing conserved residues and sequence patterns with the human reference peptide, and these candidates were carried forward for binding prediction and structural analysis.


## Selection of Top Mimicry Candidates

To prioritize candidates for structural modeling, all 28 peptides (3 anx and 25 kp) obtained from previous scoring were ranked based on a combination of:
- Predicted HLA-B27 binding strength  
- Sequence similarity to ANX peptides  

For each 3 ANX peptide, the top 5 microbial mimicry candidates were extracted by using python script and they were further used for docking and molecular dynamics simulations processes.

:::{note} Note:

All the peptides filtering and similarity screening processes were performed using custom Python scripts.

all the scripts are available in the repository under: scripts/pep_generation/
:::

