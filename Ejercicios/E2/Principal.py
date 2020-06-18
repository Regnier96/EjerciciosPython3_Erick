from Modulos import ListaOrdenada
from pymongo import MongoClient
cliente = MongoClient()

# Ordenamiento de una lista por medio del metodo de la burbuja
numeros = [5, 8, 6, 7, 10, 111, 0, 88, 9]
print(ListaOrdenada.ordenarLista(numeros))
