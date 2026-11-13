from analizador import contar_frecuencias

def test_frecuencias_basico():
    resultado = contar_frecuencias("mercado pueblo mercado")
    assert resultado["mercado"] == 2
    assert resultado["pueblo"] == 1

def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}

def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("Mercado mercado MERCADO")
    assert resultado["mercado"] == 3