# 5. Post-MD Analysis

# Post-MD Analysis

Post-MD analysis was performed to quantify structural stability, flexibility, compactness, solvent exposure, and interaction strength of peptide–HLA-B27 complexes. These analyses provide complementary insights into binding behavior beyond visual inspection.

All analysis steps were performed using GROMACS 2024 on the Supercomputer. The analyses were executed via custom shell scripts using the module GROMACS/2024r1-openmpi.

## Structural Stability and Flexibility

Root Mean Square Deviation (RMSD) was calculated to assess overall structural stability over time. Root Mean Square Fluctuation (RMSF) was used to examine residue-level flexibility and identify highly mobile regions within the complexes.

## Compactness and Solvent Exposure

The radius of gyration was calculated to evaluate the compactness of the complexes during simulation. Solvent Accessible Surface Area (SASA) was analyzed to assess changes in surface exposure and peptide burial within the HLA groove.

## Interaction Analysis

Hydrogen bond analysis was performed to evaluate peptide–HLA interaction persistence. Binding free energy was estimated using the MM-GBSA approach to compare relative binding strengths among the peptides.

:::{note}Note

Post-MD analysis scripts used for RMSD, RMSF, SASA and hydrogen bonds are available in the GitHub repository: /script/md/

:::
