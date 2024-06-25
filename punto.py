''' 
Ejemplo de un modulo python. Contiene una variable llamada pi,
y una funcion para calcular el area de un circulo de radio r.
Tambien contiene una clase llamada Punto
@author: rzambrano
'''

import math 
pi = math.pi

def area_circulo(radio):
    '''
    Funcion que devuelve el area de un circulo de radio r
    '''
    return pi*radio**2

class Punto:
    '''
    Clase que instancie Puntos en dos dimensiones
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def formato(self):
        '''
        Devuelve el punto en formato (x, y)
        '''
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 +(p.y - self.y)**2)
        return d