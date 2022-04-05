# 10. El aplicativo ha de estructurarse en dos partes. Por un lado un módulo que contenga una CLASE
# de Python donde se realicen las operaciones. Este módulo deberá ser instalable mediante PIP
# haciendo uso de la definición de un setup.py.


# 1. La aplicación debe tener 4 endpoints llamados: suma, resta, mult, divis.
# 2. Los 4 endpoints deben ser tipo POST.
# 3. Los 4 endpoints deben aceptar un JSON de la forma {‘v1’: [lista floats], ‘v2’: [lista floats]}.
# 4. El endpoint suma debe sumar element-wise las listas del JSON de entrada y devolver el
# resultado como respuesta HTTP.
# 5. El endpoint resta debe restar element-wise las listas del JSON de entrada y devolver el resultado
# como respuesta HTTP.
# 6. El endpoint mult, debe multiplicar element-wise las listas del JSON de entrada y devolver el
# resultad como respuesta HTTP.
# 7. El endpoint divis debe dividir element-wise las listas del JSON de entrada y devolver el resultado
# como respuesta HTTP.
# 8. Para cada operación se debe hacer la comprobación de que los valores y tipos de datos de
# entrada son adecuados (e.g. no entran ceros en la división) y si no son adecuados lanzar una
# Excepción.
# 9. El aplicativo REST no debe pararse porque los datos de entrada no sean adecuados. Debe
# capturar la excepción y devolver un código 500 de error HTTP.

import numpy as np


class Operations:

    def __init__(self):
        print("This is Constructor")

    def suma(v1, v2, self):
        self.assertEqual(len(v1), len(v2))
        # with self.assertRaises(TypeError):
        #     "Result different than expected"
        v_suma = [None]*len(v1)
        for i, val in enumerate(v1):
             e1 = v1[i];
             isinstance(e1, float)
             e2 = v2[i];
             v_suma[i] = e1 + e2;
        return v_suma
