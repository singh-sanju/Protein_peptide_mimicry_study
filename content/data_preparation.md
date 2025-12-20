## 1. Data Preparation

Computational studies of molecular mimicry require careful selection of both host and microbial proteins to ensure biological relevance. This chapter provides an overview of how raw biological data were selected and prepared for downstream computational analysis.  

### a. Selection of Data source

The data preparation workflow focused on selecting relevant protein sources followed by generation of peptide sequences. Two protein sources were considered in this study:

- A human protein representing a **self peptide**
- A microbial proteome representing **non-self (foreign) peptides**


**Human Protein Source (Self Peptides)**

Annexins are a family of calcium-dependent phospholipid-binding proteins involved in membrane organization, intracellular trafficking, inflammation, and immune regulation. Several members of the annexin family have been associated with autoimmune and inflammatory disorders through altered expression or immune recognition @li_annexin_2016.

Based on this immunological relevance, **Annexin (ANX)** was selected as the representative human self protein in this study.

		FASTA file used:

							P07355_ANXA2_HUMAN_Annexin_A2.fasta

**Microbial Protein Source (Non-Self Peptides)**

*Klebsiella pneumoniae* has been widely implicated as a potential microbial trigger in ankylosing spondylitis, particularly in individuals carrying the HLA-B27 allele. Several studies have proposed that immune responses against *K. pneumoniae* antigens may cross-react with host peptides through molecular mimicry, contributing to chronic inflammation and autoimmunity @puccetti_antibodies_2017.

Due to this reported association with HLA-B27–linked autoimmune disease, the complete proteome of *K. pneumoniae* was selected as the microbial peptide source.

		FASTA file used:
						uniprotkb_proteome_UP000000265_K_pneumoniae_strain_ATCC700721_MGH_78578.fasta



**Basis for Data Selection**

The combined selection of a human self protein (ANX) with immunological relevance and a microbial proteome (*K. pneumoniae*) strongly associated with HLA-B27–linked autoimmunity enables systematic investigation of peptide-level molecular mimicry. This approach allows identification of microbial peptides that may bind HLA-B27 in a manner comparable to human peptides, potentially contributing to autoimmune cross-reactivity.

:::{note}Note

- The full-length FASTA sequence of human Annexin and Klebsiella pneumoniae can be obtained from the UniProt database [UniProt](https://www.uniprot.org).

:::


### b. Peptide Generation and Extraction

Peptide identification was performed in two sequential steps:

- i. Peptide Slicing

- ii. Peptide Filtering and Similarity Screening

This two-step approach allows generation of a broad peptide pool.

The detailed explainantion of workflow used during extraction of peptide sequences from source protein and proteome is discussed under next section:

