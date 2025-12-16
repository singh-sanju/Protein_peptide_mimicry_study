# 4. Post-MD Trajectory Correction

## Trajectory Correction and Processing

Raw MD trajectories often contain artifacts related to periodic boundary conditions, system translation, and rotation. These artifacts must be corrected before any quantitative analysis can be performed.

In this study, trajectory correction was applied to ensure consistent structural alignment and meaningful comparison of molecular motions across simulation time.

- All trajectory correction steps were performed using GROMACS 2024 on the Supercomputer. The analyses were executed via custom shell scripts using the module GROMACS/2024r1-openmpi.

## Correction Procedure

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

- The provided scripts are configured for the DelftBlue computing environment and may require adaptation for use on other systems or local installations of GROMACS.
:::
