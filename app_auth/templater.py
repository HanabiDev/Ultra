from numpy import mean, var

"""
La informacion biometrica del usuario viene en la forma:
[pulsacion_1, intervalo_1, pulsacion_2, intervalo_2,...,pulsacion_2n-1, intervalo2n-1]
donde n es la cantidad de caracteres de la cadena tecleada.

De esta informacion se obtiene la media para cada uno de los tiempos de pulsacion y el tiempo
entre pulsaciones, luego  se obtiene la varianza de cada uno de los tiempos. Finalmente los 
dos vectores se unen y se retornan como la plantilla biométrica a persistir en la BD
"""
def extract_biometric_data(template):

	means = []
	variances = []

	for index, val in template:
		mean = mean(template[:index])
		means.append(mean)

		variance = var(template[:index])
		variances.append(variance)

	return means.join(',') + variances.join(',')


"""
A partir de la plantilla biometrica almacenada en la base de datos se realiza la comparacion
con una plantilla a verificar, se utiliza la distancia euclidiana que genera un valor entre 0 y 1
representando el porcentaje de coincidencia entre los patrones, este resultado se convierte a escala de
0 a 100 para dar el resultado final
"""

from utils.extractor import extract_biometric_data
from scipy.spatial import distance

def match(test_template, original_data)
	test_data = extract_biometric_data(test_template)

	score = distance.euclidean(test_data, original_data)
	score = score * 100

	return score

