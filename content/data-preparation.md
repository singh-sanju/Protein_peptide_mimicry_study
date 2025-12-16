# 1. Data Preparation

Computational studies of molecular mimicry require careful selection of both host and microbial proteins to ensure biological relevance. In this work, data preparation focused on selecting:

- A human self protein involved in immune regulation

- A microbial proteome from a gut bacterium implicated in autoimmune disease

This selection enables a systematic comparison of self and non-self peptides under identical computational conditions.

<br>

**a. Selection of Data Sources**

- ***Human Protein Source***

Annexins are a family of calcium-dependent phospholipid-binding proteins involved in membrane organization, intracellular trafficking, inflammation, and immune regulation. Several annexin family members have been linked to autoimmune and inflammatory disorders, either through dysregulated expression or the presence of autoantibodies.

therefor, Annexin (ANX) was selected as the representative human self protein in this study due to its reported association with autoimmune conditions. The full-length FASTA sequence of Annexin was obtained from UniProt and used for downstream peptide generation.

	FASTA file used:

		P07355_ANXA2_HUMAN_Annexin_A2.fasta

<br>

- ***Microbial Source***

*Klebsiella pneumoniae* has been widely implicated as a potential microbial trigger in ankylosing spondylitis, particularly in individuals carrying the HLA-B27 allele. Several studies have proposed that immune responses against K. pneumoniae antigens may cross-react with host peptides through molecular mimicry, contributing to chronic inflammation and autoimmunity.

Given its strong epidemiological and immunological association with HLA-B27–linked disease, the complete proteome of K. pneumoniae was selected as the microbial peptide source for this study. The proteome was downloaded from UniProt in FASTA format and used for peptide extraction and mimicry analysis.

	FASTA file used:

		uniprotkb_proteome_UP000000265_K_pneumoniae_strain_ATCC700721_MGH_78578.fasta

<br>

- **Rationale for Data Selection**

The combined selection of a self protein (ANX) with known immunological relevance and a microbial proteome (*K. pneumoniae*) strongly associated with HLA-B27–linked autoimmunity enables a systematic investigation of peptide-level molecular mimicry. This approach allows identification of microbial peptides that may bind HLA-B27 in a manner comparable to human peptides, potentially contributing to autoimmune cross-reactivity.

<br>

**b. Peptide Generation and Extraction**

Peptide identification was performed in two sequential steps:

- i. Peptide Slicing

- ii. Peptide Filtering and Similarity Screening

This two-step approach allows generation of a broad peptide pool.

The detailed explainantion of workflow used during extraction of peptide sequences from source protein and proteome is discussed under next section:




