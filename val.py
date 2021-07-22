import re


def validar(cadena):
    valid_precio = "[0-9]{0,}[.,]*[0-9]{1,2}$"
    valid_sap = "[58][0-9]{8}$"
    try:
        if re.match(valid_precio, cadena):
            return True
        elif re.match(valid_sap, cadena):
            return True
        else:
            return False
    except:
        return False
