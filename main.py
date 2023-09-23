# main.py

from data_acquisition.equipment_specs.module_specs.fetch_module_data import read_pan_file
from data_acquisition.equipment_specs.module_specs.process_module_data import process_module_data

# .pan dosyasını oku

pan_data = read_pan_file("C:\\Users\\Pratikus\\Documents\\GitHub\\SolarEnergyPredictionSuite\\data_acquisition\\equipment_specs\\module_specs\\ALFA_370.PAN")


# Veriyi pvlib uyumlu bir formata dönüştür
pvlib_data = process_module_data(pan_data)

# Test için çıktıyı göster
print(pvlib_data)

