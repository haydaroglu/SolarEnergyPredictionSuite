#%%
import os
import pathlib
import pvlib
import pandas as pd
import matplotlib.pyplot as plt


def fetch_weather_data(location, start_date, end_date):
    """
    Belirli bir konum ve tarih aralığı için hava durumu verisi çekmek için kullanılır.

    Parameters:
    - location (str): Hava durumu verisinin alınacağı konum.
    - start_date (str): Başlangıç tarihi.
    - end_date (str): Bitiş tarihi.

    Returns:
    - pandas.DataFrame: Hava durumu verisi.
    """
    # Veri çekme işlemleri
    # Örnek olarak şu an boş bir DataFrame döndürelim.
    import pandas as pd
    return pd.DataFrame()

# %%

print(pvlib.__version__)

help(pvlib.iotools.read_tmy3)
# %%
DATA_DIR = pathlib.Path(pvlib.__file__).parent / 'data'
df_tmy, meta_dict = pvlib.iotools.read_tmy3(DATA_DIR / '723170TYA.CSV', coerce_year=1990)
meta_dict
# %%
df_tmy.head(4)
# %%
print("Number of rows:", len(df_tmy))
print("Number of columns:", len(df_tmy.columns))
# %%
df_tmy.iloc[0]
# %%
df_tmy.loc['1990-01-01 01:00:00-05:00'];

# %%
df_tmy.keys()
# %%
# GHI, DHI, DNI are irradiance measurements
# DryBulb is the "dry-bulb" (ambient) temperature
# Wspd is wind speed
df = df_tmy[['GHI', 'DHI', 'DNI', 'DryBulb', 'Wspd']]
# show the first 15 rows:
df.head(15)
# %%
first_week = df.head(24*7)  # Plotting 7 days, each one has 24 hours or entries
first_week[['GHI', 'DHI', 'DNI']].plot()
plt.ylabel('Irradiance [W/m$^2$]');
# %%
birthday = df.loc['1990-11-06':'1990-11-06']
plt.plot(birthday['DNI'], color='r') 
plt.plot(birthday['DHI'], color='g', marker='.') 
plt.plot(birthday['GHI'], color='b', marker='s') 
plt.ylabel('Irradiance [W/m$^2$]');
# %%
summer_week = df.loc['1990-06-01':'1990-06-08']
summer_week[['GHI', 'DHI', 'DNI']].plot()
plt.ylabel('Irradiance [W/m$^2$]');
# %%
first_week['DryBulb'].plot()
plt.ylabel('Ambient Temperature [°C]');
# %%
first_week['Wspd'].plot()
plt.ylabel('Wind Speed [m/s]');
# %%
# summing hourly irradiance (W/m^2) gives insolation (W h/m^2)
monthly_ghi = df['GHI'].resample('M').sum()
monthly_ghi.head(4)

# %%
monthly_ghi = monthly_ghi.tz_localize(None)  # don't need timezone for monthly data
monthly_ghi.plot.bar()
plt.ylabel('Monthly Global Horizontal Irradiance\n[W h/m$^2$]');
# %%
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # add a second y-axis
monthly_average_temp_wind = df[['DryBulb', 'Wspd']].resample('M').mean()
monthly_average_temp_wind['DryBulb'].plot(ax=ax1, c='tab:blue')
monthly_average_temp_wind['Wspd'].plot(ax=ax2, c='tab:orange')
ax1.set_ylabel(r'Ambient Temperature [$\degree$ C]')
ax2.set_ylabel(r'Wind Speed [m/s]')
ax1.legend(loc='lower left')
ax2.legend(loc='lower right');
# %%
try:
    daily_average_DNI = df[['']].resample('').mean()  # Add the column name, and resample by day. Month is 'M', day is..
    daily_average_DNI.plot()
except:
    print("You haven't finished this exercise correctly, try again!")
# %%
