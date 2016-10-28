import math

class Frecuencia:
    def __init__(self, datos):
        self.datos = datos
        self.longituid_datos = len(self.datos)
        self.dato_menor = datos[0]
        self.dato_mayor = datos[self.longituid_datos - 1]
        self.recorrido =self.dato_mayor - self.dato_menor
        self.intervalo = self.sturges(self.recorrido)
        self.ancho_intervalo = self.obtener_ancho_intervalo(self.recorrido, self.intervalo)
        self.tabla = []
        self.frecuencia_total = 0.0
        self.frecuencia_relativa_absoluta = 0.0

    def obtener_ancho_intervalo(self, recorrido, intervalo):
        result = recorrido / intervalo
        if not (result.is_integer()):
            self.dato_menor -= 0
            self.dato_mayor += 1
            self.recorrido = self.intervalo * round(result)
        return round(result)

    def sturges(self, recorrido):
        result = 1+(3.332 * math.log(recorrido,10))
        if math.trunc(result) % 2 == 0:
            return round(result)
        else:
            return math.trunc(result)

    def crear_tabla(self):
        intervalo_cerrado = self.intervalo -1
        rango_a = self.dato_menor
        for i in range(self.intervalo):
            rango_b = rango_a + intervalo_cerrado
            self.tabla.append({'intervalo':[rango_a, rango_b],
                               'f': self.buscar_por_intervalo(rango_a,rango_b),
                               'marca de clase': self.generar_marca_de_clase(rango_a, rango_b)})
            rango_a = rango_a + intervalo_cerrado + 1

        self.generar_frecuencia_total()
        self.generar_frecuencias_relativas()
        self.generar_frecuencia_absoluta()

    def generar_frecuencias_relativas(self):
        for i in self.tabla:
            i['frecuencia relativa'] = self.generar_frecuencia_relativa(i['f'])

    def generar_frecuencia_total(self):
        for i in self.tabla:
            self.frecuencia_total = self.frecuencia_total + i['f']

    def buscar_por_intervalo(self, rango_a, rango_b):
        cantidad = 0
        for i in self.datos:
            if ((i>=rango_a) and (i<=rango_b)):
                cantidad+=1
        return cantidad

    def generar_marca_de_clase(self,rango_a, rango_b):
        return (rango_a + rango_b)/2

    def generar_frecuencia_relativa(self, frecuencia_actual):
        return frecuencia_actual/self.frecuencia_total

    def generar_frecuencia_absoluta(self):
        for i in self.tabla:
            self.frecuencia_relativa_absoluta = self.frecuencia_relativa_absoluta + i['frecuencia relativa']
            i['frecuencia relativa acummulada'] = round(self.frecuencia_relativa_absoluta,3)

# data = [36, 30, 47, 60, 32, 35, 40, 50, 54, 35, 45, 52, 48, 58, 60, 38, 32, 35, 56, 48, 30, 55, 49, 39, 58, 50, 65, 35, 56, 47, 37, 56, 58, 50, 47, 58, 55, 39, 58, 45]
# data.sort()
# frecuencia = Frecuencia(data)
# frecuencia.crear_tabla()
#
# for i in frecuencia.tabla:
#     print(i)
