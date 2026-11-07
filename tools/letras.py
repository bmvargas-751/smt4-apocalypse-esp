"""Letras españolas que no existen en Shift-JIS y el código que ocupa cada una.

Se usan los códigos del cirílico de Shift-JIS: la fuente del juego los trae y
el texto en inglés no los usa nunca. `fuente.py` redibuja esos glifos y
`mbm.py` escribe estos códigos al insertar el texto.
"""

ESPANOL = {
    "á": 0x8470, "é": 0x8471, "í": 0x8472, "ó": 0x8473, "ú": 0x8474, "ü": 0x8475, "ñ": 0x8476,
    "Á": 0x8440, "É": 0x8441, "Í": 0x8442, "Ó": 0x8443, "Ú": 0x8444, "Ü": 0x8445, "Ñ": 0x8446,
    "¿": 0x8477, "¡": 0x8478,
}

POR_CODIGO = {v: k for k, v in ESPANOL.items()}
