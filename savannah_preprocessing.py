import numpy as np
import xarray as xr
from functools import partial

# Define function to spatial subset data and resample to a time-mean
def preprocess(ds,freq,lonrange,latrange):
     return ds.sel(lon=slice(*lonrange),lat=slice(*latrange)).resample(time=freq).mean()
function = partial(preprocess,freq,lonrange=lonrange,latrange=latrange)

# Load in monthly-mean spatial subsets for all variables as a single dataset
files = np.sort(glob.glob('/path/to/files/hourly_*_2000-2010.nc'))
freq,lonrange,latrange = 'M',(100,150),(20,30)
ds = xr.open_mfdataset(files,preprocess=function)  

# Break up the dataset and save the datasets by year
years,datasets = zip(*ds.groupby('time.year'))
paths = [f'monthly_subset_T_Q_{year}.nc' for year in years]
xr.save_mfdataset(datasets,paths)
