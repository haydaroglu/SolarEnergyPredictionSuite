import matplotlib.pyplot as plt

def plot_voc(module_data, irrad):
    """Plots the open circuit voltage (Voc) for different cell temperatures using the module data and irradiance"""
    # Get the module data from the datasheet
    module_data = get_module_data()

    # Define a range of cell temperatures from 0 to 50 degrees with a step of 5 degrees
    temp_cell = range(0, 55, 5)

    # Calculate the Voc values for each cell temperature using the calculate_voc function
    voc = [calculate_voc(module_data, t, irrad) for t in temp_cell]

    # Plot the Voc values as a function of cell temperature
    plt.plot(temp_cell, voc)
    plt.xlabel("Cell temperature (C)")
    plt.ylabel("Open circuit voltage (V)")
    plt.title(f"Voc vs cell temperature for {module_data['Name']} at {irrad} W/m2 irradiance")
    plt.show()
