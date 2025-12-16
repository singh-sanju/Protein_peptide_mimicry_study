# Introduction

## Overview

This book documents a complete computational workflow investigating
molecular mimicry between ***Klebsiella pneumoniae***–derived peptides and
a human Annexin peptide (ANX) in binding to ***HLA-B27:05***, a Class-I MHC
associated with one autoimmune disease named ankylosing spondylitis.

The study evaluates peptide binding, structural stability, and post-molecular
dynamics behavior to identify potential microbial mimics.

<br>

## Background

Autoimmune diseases arise when the immune system mistakenly recognizes self-molecules as foreign, leading to chronic inflammation and tissue damage. A key component of adaptive immunity is the presentation of peptide antigens by major histocompatibility complex (MHC) molecules to T cells. The specificity and strength of peptide–MHC interactions play a critical role in determining immune tolerance versus activation.

Certain human leukocyte antigen (HLA) alleles are strongly associated with autoimmune disorders, suggesting that antigen presentation itself can influence disease susceptibility. Among these, HLA-B27 has been one of the most extensively studied due to its remarkably strong association with ***Ankylosing Spondylitis***.

<br>

## Molecular Mimicry and Autoimmunity

Molecular mimicry is a widely proposed mechanism in autoimmune pathogenesis, in which microbial peptides share structural or functional similarity with host-derived peptides. When such peptides are presented by the same HLA molecule, they may activate cross-reactive T cells that recognize both microbial and self antigens, ultimately breaking immune tolerance.

Rather than requiring high sequence identity, molecular mimicry often arises from similar physicochemical properties, conserved anchor residues, or shared conformational features within the peptide–MHC complex. As a result, structurally similar peptide–HLA complexes can elicit comparable T-cell responses even when sequence similarity is modest.

Several autoimmune diseases have been linked to microbial infections through this mechanism. In the context of ankylosing spondylitis, gut microbiota—particularly Klebsiella pneumoniae—have frequently been implicated. However, direct structural and dynamic comparisons between microbial and self peptide–HLA complexes remain limited. Computational pipelines integrating binding prediction, docking, and molecular dynamics simulations offer a systematic framework to investigate such mimicry at multiple levels.

<br>

## HLA-B27 and Ankylosing Spondylitis

Ankylosing spondylitis (AS) is a chronic inflammatory disease primarily affecting the axial skeleton, leading to pain, stiffness, and progressive spinal fusion. One of the most striking genetic associations in human immunology is between AS and the HLA-B27 allele, with over 90% of patients expressing this MHC class I molecule.

Multiple hypotheses have been proposed to explain the pathogenic role of HLA-B27, including aberrant peptide presentation, misfolding and endoplasmic reticulum stress, and altered immune signaling. Among these, the arthritogenic peptide hypothesis suggests that HLA-B27 presents peptides—either self-derived or microbial—that trigger autoreactive T-cell responses.

Klebsiella pneumoniae has been repeatedly associated with AS through epidemiological, serological, and immunological studies. It has been proposed that peptides derived from K. pneumoniae may mimic human peptides presented by HLA-B27, thereby contributing to disease initiation or progression. Understanding whether microbial peptides can bind HLA-B27 in a manner similar to self peptides, and whether such complexes exhibit comparable structural stability, is essential for evaluating this hypothesis.

<br>

## Study Objective

The goal of this work  is to investigate whether microbial peptides can 
structurally and energetically resemble human peptides and potentially trigger
autoimmune T-cell activation via molecular mimicry.

<br>

**This work helps to understand whether microbial peptides can:**

<br>

• Bind HLA-B27 in a similar way as human peptides.

• Form stable structural interactions.

• Exhibit comparable post-MD behavior

• It can also supports a potential molecular mimicry mechanism.

<br>

## Study Focuses on Learning

<br>

• Peptide generation and filtering

• HLA-B27 binding predictions

• Sequence similarity and mimicry search

• Peptide docking and molecular dynamics (MD)

• Trajectory analysis (RMSD, RMSF, SASA, PCA, MMGBSA




