# fetch_module_data.py

def read_pan_file(filepath):
    """Read the content of a given PAN file.

    Args:
        filepath (str): Path to the PAN file.

    Returns:
        str: Content of the PAN file.
    """
    with open(filepath, 'r') as file:
        content = file.read()
    return content
