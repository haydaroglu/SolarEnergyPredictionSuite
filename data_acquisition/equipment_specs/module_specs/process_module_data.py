# process_module_data.py

def pan_data_parser(pan_data):
    """Raw PAN data content'ını key-value çiftleri olarak ayırır."""
    data = {}
    for line in pan_data.split("\n"):
        parts = line.split("=")
        if len(parts) == 2:
            key, value = parts
            data[key.strip()] = value.strip()
    return data

def pan_to_pvlib(data):
    """Pan dosyasından gelen veriyi pvlib uyumlu yapısına dönüştürür."""
    pvlib_data = {
        'alpha_sc': float(data['muISC']) / 100,
        'I_L_ref': float(data['Isc']),
        'I_o_ref': None,
        'R_s': float(data['RSerie']),
        'R_sh_ref': float(data['RShunt']),
        'EgRef': 1.121,
        'cells_in_series': int(data['NCelS']),
        'V_oc_ref': float(data['Voc']),
    }
    return pvlib_data

def process_module_data(pan_data):
    """PAN verisini işleyip pvlib-compatible formatına dönüştürür."""
    data = pan_data_parser(pan_data)
    transformed_data = pan_to_pvlib(data)
    return transformed_data

