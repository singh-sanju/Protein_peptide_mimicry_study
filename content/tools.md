# Software and Computational Tools

The following open-source and academic software and computational tools[^1] were used at different stages of the workflow, including sequence analysis, structural modeling, molecular docking, molecular dynamics simulations, and post-simulation analysis.

All tools and software were downloaded[^2] and used as required at different stages of the study.


## Bioinformatics and Scripting

- **Python** (version 3.10 or higher)
- **Biopython**
- **NetMHCpan**

Python was used for scripting and automation tasks, including peptide generation, FASTA handling, and sequence-based analyses using the Biopython library.  
NetMHCpan was used to predict peptide binding affinities to HLA-B27:05.  
Sequence similarity analysis was performed using BLAST and pairwise alignment methods implemented through Bio.Align.

## Molecular Modeling and Docking

- **AlphaFold-Multimer** (via AlphaFold web server)
- **HADDOCK**
- **PyMOL**
- **VMD**

Structural modeling and docking of peptide–HLA complexes were performed using AlphaFold-Multimer and HADDOCK.  
Visualization of structural models and trajectories was carried out using PyMOL and VMD.

## Molecular Dynamics Simulation

- **AmberTools 23**
- **GROMACS 2024**

System preparation was carried out using AmberTools 23, including protonation state assignment and force-field parameterization.  
Molecular dynamics simulations, trajectory correction, and post-simulation analyses were performed using GROMACS 2024.

## Binding Free Energy Calculations

- **gmx_MMPBSA**

MM-GBSA binding free energy calculations were performed using this tool.

## Supporting Tools

- **GitHub** – version control and reproducibility @github,.
- **Jupyter Book** – documentation and presentation @jupyterbook,.


[^1]:All software used in this study is open-source or freely available for academic use.
[^2]:All available Download links for the used tools are available in the project GitHub repository (software.md)).
