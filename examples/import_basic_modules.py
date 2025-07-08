"""Check if we can import core modules"""

try:
    import math
    import random
    import datetime

    print("Módulos básicos importados correctamente.")
except ImportError as e:
    print(f"Error al importar módulos: {e}")
