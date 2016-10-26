import math
from itertools import groupby

class TendenciaCentralNoAgrupada:
    def __init__(self, datos):
        self.datos = datos
        self.datos.sort()
        self.longitud = len(self.datos)

    def media(self):
        m = 0
        for k in self.datos:
            m = m + k
        return m/self.longitud

    def mediana(self):
        media = int(self.longitud/2)
        if self.longitud % 2 == 0:
            return (self.datos[media - 1] + self.datos[media]) / 2
        else:
            return self.datos[media]

    def cuartil(self):
        cuartiles = []
        if(self.longitud % 2 != 0):
            self.__ncil_impar(cuartiles, 4)
        else:
            self.__ncil_par(cuartiles, 4)

        return cuartiles

    def decil(self):
        deciles = []
        if (self.longitud % 2 != 0):
            self.__ncil_impar(deciles, 10)
        else:
            self.__ncil_par(deciles, 10)

        return deciles

    def percentil(self):
        percentil = []
        if (self.longitud % 2 != 0):
            self.__ncil_impar(percentil, 100)
        else:
            self.__ncil_par(percentil, 100)

        return percentil

    def moda(self):
        m = [len(list(group)) for key, group in groupby(self.datos)]
        data = []
        for i in m:
            if i > 1:
                data.append(i)
        return data

    def media_geometrica(self):
        g = 1
        for k in self.datos:
            g = g * k
        return math.pow(g,1/self.longitud)

    def media_armonica(self):
        armonica = 0
        for k in self.datos:
            armonica = armonica + (1/k)

        return (self.longitud/armonica)

    """Metodos privados"""

    def __ncil_par(self, nciles, cantidad):
        for i in range(cantidad-1):
            k = math.trunc((i * self.longitud) / cantidad) - 1
            nciles.append((self.datos[k] + self.datos[k + 1]) / 2)

    def __ncil_impar(self, nciles, cantidad):
        for i in range(cantidad-1):
            k = math.trunc((i * self.longitud) / cantidad) - 1
            nciles.append(self.datos[k])


class TendenciaCentralAgrupada:
    def __init__(self, intervalos, frecuencia, amplitud):
        self.intervalos = intervalos
        self.frecuencia = frecuencia
        self.total = 0
        self.amplitud = amplitud
        self.frecuencia_acumulada = []
        self.marca_de_clase = []
        self.y = []
        self.yf = []
        self.y2 = []
        self.y2f = []

        self.__obtener_total()
        self.__obtener_marcas_de_clases()
        self.__obtener_frecuencia_acumulada()
        self.__obtener_y()
        self.__obtener_yf()
        self.__obtener_y2()

    def media(self):
        total = 0
        i = 0
        while i < len(self.intervalos):
            total = total + (self.frecuencia[i] * self.marca_de_clase[i])
            i += 1
        return round(total/self.total,2)

    def mediana(self):
        n = self.total/2
        position = self.__buscar_medio(n)
        limite_inferior = self.intervalos[position][0]
        mediana = round(limite_inferior + ((n-self.frecuencia_acumulada[position-1])*self.amplitud)/(self.frecuencia[position]),3)
        return mediana

    def moda(self):
        mayor = self.__buscar_tendencia()
        posicion = self.frecuencia.index(mayor)
        limite_inferior = self.intervalos[posicion][0]
        parte_a = self.frecuencia[posicion] - self.frecuencia[posicion-1]
        parte_b = parte_a + (self.frecuencia[posicion] - self.frecuencia[posicion+1])
        moda =  round(limite_inferior + ((parte_a/parte_b)*self.amplitud),3)
        return moda

    """Metodos privados"""

    def __buscar_medio(self, medium):
        posicion = 1
        for k in self.frecuencia_acumulada:
            if medium <= k:
                break
            posicion += 1
        return posicion - 1

    def __buscar_tendencia(self):
        mayor = self.frecuencia[0]
        for k in self.frecuencia:
            if k > mayor:
                mayor = k
        return mayor

    def __obtener_total(self):
        for k in self.frecuencia:
            self.total = self.total + k

    def __obtener_frecuencia_acumulada(self):
        total = 0
        for k in range(len(self.frecuencia)):
            total = total + self.frecuencia[k]
            self.frecuencia_acumulada.append(total)

    def __obtener_marcas_de_clases(self):
        for k in self.intervalos:
            self.marca_de_clase.append((k[0]+k[1])/2)

    def __obtener_y(self):
        for k in self.intervalos:
            self.y.append((k[0] + k[1])/2)

    def __obtener_yf(self):
        i = 0
        for k in self.y:
            self.yf.append(float(self.y[i])*k)
            i += 1

    def __obtener_y2(self):
        for k in self.y:
            self.y2.append(k*k)

    def __obtener_y2f(self):
        i = 0
        for k in self.y2:
            self.y2f.append(k * float(self.y[i]))
            i += 1


t = TendenciaCentralNoAgrupada([2, 3, 4, 4, 5, 5, 5, 6, 6])
#v = TendenciaCentralNoAgrupada([7, 8, 9, 10, 11, 12])
#c = TendenciaCentralNoAgrupada([2, 5, 3, 6, 7, 4, 9])
print(t.media())
print(t.mediana())
print(t.media_geometrica())
print(t.media_armonica())
print(t.moda())

#print(v.mediana())
#print(c.datos)
#print(c.cuartil())

"""cpar = TendenciaCentralNoAgrupada([2, 5, 3, 4, 6, 7, 1, 9])
print(cpar.datos)
print(cpar.cuartil())
print(cpar.decil())
print(cpar.percentil())
"""

"""k = TendenciaCentralAgrupada([[2,8],[8,14],[14,20],[20,26],[26,32]],
                             [8,12,22,18,10], 6)
print(k.intervalos)
print(k.frecuencia)
print(k.frecuencia_acumulada)
print(k.marca_de_clase)
#print(k.media())
#print(k.mediana())
#print(k.moda())
print(k.y)
print(k.yf)
print(k.y2)"""