# Introduction

## Overview 

This book documents a complete computational workflow investigating
molecular mimicry between ***Klebsiella pneumoniae***–derived peptides and
a human Annexin peptide (ANX) in binding to ***HLA-B27:05***, a Class-I MHC
associated with one autoimmune disease named ankylosing spondylitis.

The study evaluates peptide binding, structural stability, and some post-molecular
dynamics behavior to identify potential microbial mimics.


## Background

The human microbiome, comprising trillions of microorganisms, plays a crucial role in maintaining health and influencing the progression of disease @manasson_microbiome_2020 . Numerous studies on the relationship between the microbiome and certain diseases indicate that it plays a significant role in autoimmune disorders such as Ankylosing spondylitis (AS), which primarily affects the spine and sacroiliac joints @methe_framework_2012. These illnesses develop when the immune system misidentifies self-molecules as alien, resulting in tissue damage and persistent inflammation.

A key component of this adaptive immunity is the presentation of peptide antigens by major histocompatibility complex (MHC) molecules to T cells. Dysregulation of this process plays a central role in autoimmune diseases, including AS, which exhibits a strong association with specific MHC alleles, known as HLA @hazra_unraveling_2025. MHC represents a genomic region encoding antigen-presenting molecules, whereas human leukocyte antigen (HLA) refers specifically to the human MHC molecules that bind and present peptide antigens to T cells. These HLA alleles are strongly associated with autoimmune disorders, such as allele HLA-B27 is strongly linked to AS @zhu_ankylosing_2019, suggesting that antigen presentation itself can influence disease susceptibility.



## HLA-B27 and Ankylosing Spondylitis

Ankylosing spondylitis (AS) is a chronic inflammatory disease primarily affecting the axial skeleton, leading to pain, stiffness, and progressive spinal fusion. The HLA-B27 allele and AS have one of the most remarkable genetic correlations in human immunology; more than 90% of patients express this MHC class I molecule @furman_chronic_2019.

Research suggests that disease is caused by variations in HLA peptide-binding grooves that affect immune activation, peptide recognition, and binding stability. Beside it, the pathogenic role of HLA-B27 has been explained by a number of theories, including altered immune signalling, misfolding and endoplasmic reticulum stress, and aberrant peptide presentation. Among these, the arthritogenic peptide hypothesis postulates that HLA-B27 displays peptides that cause autoreactive T-cell reactions, whether they are microbial or self-derived. This is how the concept of molecular mimicry entered the picture of disease progression @abdel-magid_inhibition_2024.


## Molecular Mimicry and Autoimmunity

A common theory in autoimmune pathogenesis is molecular mimicry, in which microbial peptides share structural or functional similarity with host-derived peptides. When such peptides are presented by the same HLA molecule, they may activate cross-reactive T cells that recognize both microbial and self-antigens, ultimately breaking immune tolerance @verma_elucidating_2020.
Molecular mimicry frequently results from similar physicochemical characteristics, conserved anchor residues, or shared conformational features within the peptide–MHC complex rather than requiring high sequence identity. Therefore, even when sequence similarity is low, structurally similar peptide–HLA complexes can elicit similar T-cell responses @song_role_2022.

Klebsiella pneumoniae has been repeatedly associated with AS through epidemiological, serological, and immunological studies. It has been proposed that peptides derived from K. pneumoniae may mimic human peptides presented by HLA-B27, thereby contributing to disease initiation or progression @wang_gut_2022. However, direct structural and dynamic comparisons between microbial and self–peptide–HLA complexes remain limited. Therefore, understanding whether microbial peptides can bind HLA-B27-like self-peptides and whether such complexes exhibit comparable structural stability is essential for evaluating this hypothesis. Computational pipelines integrating binding prediction, docking, and molecular dynamics simulations presented in this study can offer a systematic framework to investigate such mimicry at computational levels. 


## Study Focuses on Learning


• Peptide generation and filtering

• HLA-B27 binding predictions

• Sequence similarity and mimicry search

• Peptide docking and molecular dynamics (MD)

• Trajectory analysis (RMSD, RMSF, SASA, PCA, MMGBSA



## Study Objective

An important immune molecule, the HLA-B27 protein is a transmembrane glycoprotein of about 362 amino acids with an antigen-binding groove (B pocket), between amino acids ~27-170 within α1/α2 domains @SCHITTENHELM20161867. This binding groove typically binds short peptides, approximately 9-12 amino acids in length, for presentation to T-cells. Because of this characteristic, HLA-B27 can bind specific microbial peptides that may structurally resemble self-peptides, allowing T-cell cross-reactivity and perhaps inducing autoimmune reactions by molecular mimicry or arthritogenic peptide binding @braun_fifty_2023,.

Thus, the purpose of this investigation is to determine whether microbial peptides may imitate human peptides both physically and energetically and perhaps cause autoimmune T-cell activation by molecular mimicry and the study can clarify whether microbial peptides may bind HLA-B27 similarly to human peptides, form persistent structural interactions, and support a possible molecular mimicry mechanism or not in some extent.






