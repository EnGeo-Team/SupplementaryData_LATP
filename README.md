# SupplementaryData_LATP
This repository contains supplementary data for the manuscript "Disentangling the Coupled Origins of Li-Ion Transport in LATP through Hierarchical Modeling"

The repository contains the following files and folders:

* LATP_MD_finetuned: contains the MACE model finetuned for LATP MD simulations, including training data set, test data, bash input file for training and indices of the validation set
* LATP_grid_finetuned: contains the MACE model finetuned for LATP grid sampling, including training data set, test data, bash input file for training and indices of the validation set
* cif_files: contains cif files for all initial structures used in the study
* cp2k_grid_sampling.inp: an example cp2k input file used for grid sampling
* cp2k_geoOpt.inp: an example cp2k input file used for Geometry Optimization
* Equil_cp2k_MD.inp: an example cp2k input file used for MD equilibration
* grid_sampling_LAMMPS_MACE.in: an example LAMMPS-MACE input file used for grid sampling
* in.geoOpt_LAMMPS_MACE: an example LAMMPS-MACE input file used for Geometry Optimization
* MD_LAMMPS_MACE.in: an example LAMMPS-MACE input file used for MD simulations
* MSD_MDAnalysis.py: python script used to calculate MSD from MD trajectories
* Prod_cp2k_MD.inp: an example cp2k input file used for MD production (training data generation)


Software versions used:
RASPA version: 2.0.50
MACE version: 0.3.16
LAMMPS (10 Sep 2025) with Kokkos version 4.6.2 enabled
CP2K version: 2026.2
