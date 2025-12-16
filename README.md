HLA-B27 Molecular Mimicry Study — MD Simulation & Analysis
-----------------------------------

## 📘 Project Overview

This repository documents a complete computational workflow to identify Klebsiella pneumoniae–derived peptides that mimic a human Annexin peptide (ANX) in binding to HLA-B27:05, a Class-I MHC associated with autoimmune diseases such as Ankylosing Spondylitis.

The objective is to investigate whether microbial peptides can:

- Bind HLA-B27 in a similar way as human peptides.
- Form stable structural interactions.
- Exhibit comparable post-MD behavior.
- Supporting a potential molecular mimicry mechanism.
-------------------
I focused on learning:

- Peptide generation and filtering
- HLA-B27 binding predictions
- Sequence similarity and mimicry search
- Peptide docking and molecular dynamics (MD)
- Trajectory analysis (RMSD, RMSF, SASA, PCA, MMGBSA
--------------
🛠️## Overview of the Pipeline

- Generate peptides from human Annexin (anx) and full K. pneumoniae (kp)proteome
- HLA-B27 binding prediction using NetMHCpan
- Sequence similarity & mimic scoring
- Docking using AlphaFold-Multimer
- Structure optimization with AmberTools23 (tleap)
- Molecular Dynamics (MD) simulation in GROMACS 2024.
- Post-process trajectories (centering, frame skipping, fitting)
- Post-MD analysis: RMSD, RMSF, Rg, SASA, H-bonds, MM-GBSA
- Identification of strongest microbial mimic

-----------------

⚠️ **Note: ** The workflow was developed through trial and error, is not fully automated, and may not be fully reproducible. Scripts are shared to illustrate my learning process. This workflow includes:

------------

📘 ## Reproducibility Note

project was created for learning purposes. The scripts were developed through trial and error and are not fully automated, so the workflow may not be fully reproducible.The scripts are shared mainly to illustrate the approach and my learning process, not as a polished, production-ready workflow.

--------------

📌📑 ## Citation

If you use this repository, analysis pipeline, or scripts, please cite: Singh S. (2025). GitHub Repository for HLA-B27 molecular mimicry MD analysis. Link: https://github.com/singh-sanju/Protein_peptide_mimicry_study

--------------------

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

The contents in this repository are shared with a [CC BY 4.0 license](http://creativecommons.org/licenses/by/4.0/) unless otherwise noted. As this is work in progress, some reused content may not (yet) be listed here.

If you are using this template to create a new repository, specify your license in this section (we very strongly encourage CC BY 4.0!).

------------------------------

## Acknowledgements

I would like to thank my principal investigator, Dr. Nikolina Šoštarić (Bionanoscience Department, TU Delft, The Netherlands), for guidance and constructive feedback at various stages of this work.

Computational work, including molecular dynamics production runs and post-processing, was performed on the DelftBlue Supercomputer at TU Delft.

I further thank Dr. C. F. J. Pols, (Assistant Professor, Science & Engineering Education Department, TU Delft) for suggesting the use of Jupyter Notebook for presenting the material and for sharing a workshop template that supported the dissemination of this work.
