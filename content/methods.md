# Methods

## Target Protein and Peptides

Target: HLA-B27:05

Reference structure: PDB ID 5txs

Peptides studied:

Human Annexin peptide

Top Klebsiella pneumoniae–derived peptides

## Peptide Generation

Peptide length: 9–12 mers

Sliding window approach

Anchor residue rules for HLA-B27

Tools: Biopython

Mention script purpose (not code)

## Binding Prediction (NetMHCpan)

Tool: NetMHCpan

Input: FASTA peptides

Output: binding affinity

Classification: Strong / Weak binders

Only binders carried forward

## Mimicry Scoring

Sequence similarity between human and microbial peptides

Scoring matrix: BLOSUM62

Selection of top mimics

Purpose: prioritize candidates

## Docking

Tool: AlphaFold-Multimer

Docking of peptide–HLA complexes

Output format: CIF + confidence files

Visual inspection in PyMOL

## Molecular Dynamics Simulation

Preparation: AmberTools (tleap)

Conversion to GROMACS

Water model: TIP3P

Ensemble: NVT → NPT → production

Duration: microsecond scale

Platform: DelftBlue supercomputer

## Post-MD Analysis

RMSD

RMSF

Radius of gyration

SASA

Hydrogen bonds

MM-GBSA binding energy

