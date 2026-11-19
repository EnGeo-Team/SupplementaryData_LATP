import numpy as np
import matplotlib.pyplot as plt
import re

import pathlib

import os
os.chdir(pathlib.Path(__file__).parent.resolve())

from ase.io.trajectory import Trajectory
from ase.io import read,write

import MDAnalysis as mda
from MDAnalysis.analysis.msd import EinsteinMSD
from MDAnalysis.transformations.nojump import NoJump

def main():
    items = os.listdir(".")

    filename_t = "trajectory_file_name.xyz"
    
    filename_s = "structure_file_name.cif"

    struc = read(filename_s)

    write("structure_file_name.xyz",struc,format="xyz")

    u = mda.Universe("structure_file_name.xyz",filename_t,dt=0.1)

    u.dimensions = struc.get_cell_lengths_and_angles()

    transformation = NoJump()
    u.trajectory.add_transformations(transformation)

    li_atoms = u.select_atoms("type LI")

    MSD = EinsteinMSD(u, select='type LI', msd_type='xyz', fft=True)
    MSD.run()

    msd =  MSD.results.timeseries
    
    lagtimes = MSD.results.delta_t_values

    MSD = EinsteinMSD(u, select='type LI', msd_type='x', fft=True)
    MSD.run()

    msd_x =  MSD.results.timeseries

    MSD = EinsteinMSD(u, select='type LI', msd_type='y', fft=True)
    MSD.run()

    msd_y =  MSD.results.timeseries

    MSD = EinsteinMSD(u, select='type LI', msd_type='z', fft=True)
    MSD.run()

    msd_z =  MSD.results.timeseries

    Nt = MSD.n_frames

    # write MSD to file
    data_print_msd = np.zeros((5,Nt))
    data_print_msd[0,:] = lagtimes
    data_print_msd[1,:] = msd
    data_print_msd[2,:] = msd_x
    data_print_msd[3,:] = msd_y
    data_print_msd[4,:] = msd_z
    fname = "MSD_raw_MDAnalysis_system_name.txt"
    np.savetxt(fname, data_print_msd.transpose(), fmt='%1.4e', delimiter=' ', header="tau [ps]   |   MSD_tot [A^2]  |   MSD_x [A^2]   |   MSD_y [A^2]   |   MSD_z [A^2]   |")

main()