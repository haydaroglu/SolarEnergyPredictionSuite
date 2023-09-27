
#%%
import pvlib
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
DATA_DIR = pathlib.Path(pvlib.__file__).parent / 'data'
df_tmy, metadata = pvlib.iotools.read_tmy3(DATA_DIR / '723170TYA.CSV', coerce_year=1990)


# create pvlib Location object based on meta data
location = pvlib.location.Location(latitude=metadata['latitude'], longitude=metadata['longitude'])

# %%
print("We are looking at data from ", metadata['Name'], ",", metadata['State'])
# Note: TMY datasets are right-labeled hourly intervals, e.g. the
# 10AM to 11AM interval is labeled 11.  We should calculate solar position in
# the middle of the interval (10:30), so we subtract 30 minutes:
times = df_tmy.index - pd.Timedelta('30min')
solar_position = location.get_solarposition(times)
# but remember to shift the index back to line up with the TMY data:
solar_position.index += pd.Timedelta('30min')

solar_position.head()
# %%
df_poa = pvlib.irradiance.get_total_irradiance(
    surface_tilt=20,  # tilted 20 degrees from horizontal
    surface_azimuth=180,  # facing South
    dni=df_tmy['DNI'],
    ghi=df_tmy['GHI'],
    dhi=df_tmy['DHI'],
    solar_zenith=solar_position['apparent_zenith'],
    solar_azimuth=solar_position['azimuth'],
    model='isotropic')
# %%
df_poa.keys()

# %%
df = pd.DataFrame({
    'ghi': df_tmy['GHI'],
    'poa': df_poa['poa_global'],
})
df_monthly = df.resample('M').sum()
df_monthly.plot.bar()
plt.ylabel('Monthly Insolation [W h/m$^2$]');
# %%
