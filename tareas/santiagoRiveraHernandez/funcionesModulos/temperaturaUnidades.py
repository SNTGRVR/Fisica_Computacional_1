def CaK(C):
    """Esta función se encarga de convertir unidades de temperatura, de grados celsius a kelvin"""
    return C + 273.15
def CaF(C):
    """Esta función se encarga de convertir unidades de temperatura, de grados celsius a grados fahrenheit"""
    return (C*1.8) + 32
def CaR(C):
    """Esta función se encarga de convertir unidades de temperatura, de grados celsius a rankine"""
    return (C*1.8) + 491.67
def KaC(K):
    """Esta función se encarga de convertir unidades de temperatura, de kelvin a grados celsius"""
    return K - 273.15
def KaF(K):
    """Esta función se encarga de convertir unidades de temperatura, de kelvin a grados fahrenheit"""
    return (K - 273.15)*1.8 + 32
def KaR(K):
    """Esta función se encarga de convertir unidades de temperatura, de kelvin a rankine"""
    return K*1.8
def FaC(F):
    """Esta función se encarga de convertir unidades de temperatura, de grados fahrenheit a grados celsius"""
    return (F - 32)/1.8
def FaK(F):
    """Esta función se encarga de convertir unidades de temperatura, de grados fahrenheit a kelvin"""
    return (F - 32)*(5/9) + 273.15
def FaR(F):
    """Esta función se encarga de convertir unidades de temperatura, de grados fahrenheit a rankine"""
    return F + 459.67
def RaC(R):
    """Esta función se encarga de convertir unidades de temperatura, de rankine a grados celsius"""
    return (R - 491.67)*(5/9)
def RaK(R):
    """Esta función se encarga de convertir unidades de temperatura, de rankine a kelvin"""
    return R/1.8
def RaF(R):
    """Esta función se encarga de convertir unidades de temperatura, de rankine a grados fahrenheit"""
    return R - 459.67