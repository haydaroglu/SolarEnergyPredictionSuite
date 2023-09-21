import pvlib

def calculate_voc(module_data, temp_cell, irrad):
    """Returns the open circuit voltage (Voc) for a given module data, cell temperature and irradiance using the single diode model and the SAPM"""
    # Create a PVSystem object using the module data
    panel = pvlib.pvsystem.PVSystem(
        module_parameters=module_data,
        temperature_model_parameters=pvlib.temperature.TEMPERATURE_MODEL_PARAMETERS["sapm"]["open_rack_glass_glass"],
    )
    # Call the sapm_voc method to calculate Voc
    voc = panel.sapm_voc(temp_cell, irrad)
    return voc
