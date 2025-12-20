## 2. Molecular Docking

Molecular docking was performed to model peptide–HLA-B27 complexes and
evaluate the binding orientation of selected human and microbial peptides
within the HLA groove.

Docking was carried out using **AlphaFold-Multimer** @jumper2021highly and HADDOCK @van2003haddock, via web server, which was used to
generate structural models of peptide–HLA-B27 complexes. For each selected
Annexin (ANX) peptide, all shortlisted *Klebsiella pneumoniae* (KP) peptides
were docked individually with HLA-B27.


### Output and Model Evaluation

After docking the AlphaFold-Multimer generated:

- Structural models in `.cif` format.

- Confidence scores in accompanying `.json` files.

<br>

The results of docking process were evaluated based on:

- Predicted docking confidence.

- Structural plausibility of the complex.

- Peptide orientation and positioning within the HLA-B27 binding groove  


### Selection of Peptides for MD Simulations

Based on docking confidence scores and visual inspection, three microbial peptides were selected against one human Annexin peptide.

The final peptide set consisted of four peptides:

**Human peptide**
- *IRSEFKRKY* (anx)

**Microbial peptides**
- *GRSDFKGDY* (KP1)  
- *GRSDFKGDYF* (KP2)  
- *SRSDRVAKY* (KP3)

{numref}`fig_dockedpep` shows the docked structural models of the four selected peptide–HLA-B27 complexes used for subsequent MD simulations.


```{figure} figures/docked_pep.png
:name: fig_dockedpep
:width: 85%
:align: center

Model of peptides generated on PyMol
```


These peptides showed stable and well-positioned docking poses within
the HLA groove and were selected for molecular dynamics simulations.

:::{note}Note

All peptide models were prepared using PyMol @pymol, for docking and visual inspection of docked Peptide–HLA complexes were also permormed and manually inspected in PyMOL to verify peptide placement, binding orientation, and overall structural plausibility within the HLA binding groove.

:::


