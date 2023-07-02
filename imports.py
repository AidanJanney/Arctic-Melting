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