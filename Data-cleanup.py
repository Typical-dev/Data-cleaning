import csv
from os import access
import pandas as pd
df = pd.read_csv("Data-processing/final2.csv")
print(df.shape)
del df["hyperlink"]
print(df.shape)
df1 = df[["name", "light_years_from_earth","planet_mass","stellar_magnitude","discovery_date","planet_type", "planet_radius","orbital_radius","orbital_period","eccentricity","pl_hostname","pl_discmethod","pl_orbincl","pl_dens", "ra_str", "dec_str", "st_teff", "st_mass", "st_rad"]]
print(df1.head)
df1 = df1.rename({
    "pl_hostname":"solar_system_name","pl_discmethod":"planet_discovery_method","pl_orbincl":"planet_orbital_inclination","pl_dens":"planet_orbital_density", "ra_str":"right_ascension", "dec_str":"declination", "st_teff":"host_temperature", "st_mass":"host_mass", "st_rad":"host_radius"
},axis = "columns")
df1.to_csv("cleaned_data.csv")
