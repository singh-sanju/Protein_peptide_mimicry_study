## 4. Post-MD Trajectory Correction

After completion of the MD production run, several output files are generated, including:

- trajectory file (.xtc)
- structure file (.gro)
- energy file (.edr)
- log file (.log)

Among these, the .xtc trajectory stores the time-dependent atomic coordinates and is used for all downstream analyses.
However, raw trajectories often contain artifacts such as periodic boundary condition effects, system drift, and molecular fragmentation.
Therefore, trajectory correction is performed to remove these artifacts and obtain a physically continuous and centered trajectory.
The corrected .xtc file ensures reliable calculation of structural and dynamic properties during post-MD analysis.


### Trajectory Correction and Processing

In this study, trajectory correction was applied to ensure consistent structural alignment and meaningful comparison of molecular motions across simulation time. The trajectory files (.xtc) generated from production MD runs were processed to remove periodic boundary condition effects, recenter the protein–peptide complex, and eliminate overall translational and rotational motion.

All trajectory correction steps were performed using GROMACS 2024 on the supercomputing facility. The analyses were executed via custom shell scripts using the module GROMACS/2024r1-openmpi, ensuring reproducibility and consistent processing across all simulation systems.

The corrected trajectories were subsequently used for downstream structural and dynamic analyses, including RMSD, RMSF, hydrogen bond analysis, and conformational stability assessment


### Correction Procedure

Trajectory correction included in this work are as follows:

- Removal of periodic boundary effects
- Reconstruction of whole molecules
- Centering of the protein complex
- Rotational and translational fitting
- Frame skipping 

The trajectory correction process also helps to reduce data size while preserving essential dynamics.


:::{note}Note

- The scripts used for system preparation and MD execution are available in the GitHub repository: script/mdrun/.

- The scripts handle periodic boundary correction, trajectory centering, fitting, and frame reduction to prepare trajectories for post-MD analysis.

:::
