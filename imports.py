# some various useful generic imports, might slow you down if you're running this often
from datetime  import datetime, timedelta

import os, inspect, argparse, time, sys, socket

from pathlib import Path

import numpy as np
import scipy as sp
import xarray as xr
import pooch
import pandas as pd
import geopandas as gpd
import netCDF4
from netCDF4 import Dataset
from zipfile import ZipFile
import seaborn as sns

from multiprocessing import Pool as p

import os, inspect, argparse, time, sys, socket
import matplotlib as mpl
import matplotlib.pyplot as plt

# matplotlib doesn't like running headless...  off with its head
mpl.use('pdf');
mpl.interactive(False)
plt.ioff()                                  # turn off pyplot interactive mode 
os.environ['HDF5_USE_FILE_LOCKING']='FALSE' # just in case
os.environ['HDF5_MPI_OPT_TYPES']='TRUE'     # just in case

# Plotting Help
def adjust_lightness(color, amount=1.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])