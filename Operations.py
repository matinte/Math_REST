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

    def suma(self, v1, v2):
        # check list v1 not empty
        self.assertTrue(v1)
        # check list v2 not empty
        self.assertTrue(v2)
        # check lists have the same size
        self.assertEqual(len(v1), len(v2))
        # create new suma list
        v_suma = [None]*len(v1)
        # iterate over elements
        for i, val in enumerate(v1):
            e1 = v1[i]
            e2 = v2[i]
            # check elements are float type
            if not (isinstance(e1, float)) | (not isinstance(e2, float)):
                raise TypeError("Elements not of Float type: ", e1, " - ", e2)
            else: # then sum elements to result list
                v_suma[i] = e1 + e2;
        # return suma list
        return v_suma

    def resta(self, v1, v2):
        # check list v1 not empty
        self.assertTrue(v1)
        # check list v2 not empty
        self.assertTrue(v2)
        # check lists have the same size
        self.assertEqual(len(v1), len(v2))
        # create new resta list
        v_resta = [None]*len(v1)
        # iterate over elements
        for i, val in enumerate(v1):
            e1 = v1[i]
            e2 = v2[i]
            # check elements are float type
            if not (isinstance(e1, float)) | (not isinstance(e2, float)):
                raise TypeError("Elements not of Float type: ", e1, " - ", e2)
            else: # then resta elements to result list
                v_resta[i] = e1 - e2;
        # return suma list
        return v_resta

    def mult(self, v1, v2):
        # check list v1 not empty
        self.assertTrue(v1)
        # check list v2 not empty
        self.assertTrue(v2)
        # check lists have the same size
        self.assertEqual(len(v1), len(v2))
        # create new suma list
        v_mult = [None] * len(v1)
        # iterate over elements
        for i, val in enumerate(v1):
            e1 = v1[i]
            e2 = v2[i]
            # check elements are float type
            if not (isinstance(e1, float)) | (not isinstance(e2, float)):
                raise TypeError("Elements not of Float type: ", e1, " - ", e2)
            else:  # then mult elements to result list
                v_mult[i] = e1 * e2;
        # return mult list
        return v_mult

    def divis(self, v1, v2):
        # check list v1 not empty
        self.assertTrue(v1)
        # check list v2 not empty
        self.assertTrue(v2)
        # check lists have the same size
        self.assertEqual(len(v1), len(v2))
        # create new suma list
        v_divis = [None]*len(v1)
        # iterate over elements
        for i, val in enumerate(v1):
            e1 = v1[i]
            e2 = v2[i]
            # check elements are float type
            if not (isinstance(e1, float)) | (not isinstance(e2, float)):
                raise TypeError("Elements not of Float type: ", e1, " - ", e2)
            elif e2 == 0.0:
                raise TypeError("Cant divide when e2 equals to 0", e1, " - ", e2)
            else: # then divide elements to result list
                v_divis[i] = e1 / e2;
        # return mult list
        return v_divis