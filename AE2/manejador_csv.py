import csv
import os


class ManejadorCSV:
    """Importa, modifica y guarda archivos CSV con csv.reader y csv.writer."""

    def __init__(self, ruta_entrada):
        self.ruta_entrada = ruta_entrada
        self.encabezados = []
        self.filas = []
        self.ruta_salida = None
        self.cantidad_importada = 0
        self.cantidad_guardada = 0
        self.modificaciones = []
        self.metodos_usados = []

    def importar(self):
        with open(self.ruta_entrada, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)
            self.filas = list(lector)
        self.cantidad_importada = len(self.filas)
        self.metodos_usados.append("importar")
        return self.encabezados, self.filas

    def actualizar_valor(self, columna, valor_actual, valor_nuevo):
        indice = self.encabezados.index(columna)
        cambios = 0
        for fila in self.filas:
            if fila[indice] == valor_actual:
                fila[indice] = valor_nuevo
                cambios += 1
        self.modificaciones.append(
            f"Se actualizaron {cambios} registros: en la columna '{columna}' "
            f"se cambió '{valor_actual}' por '{valor_nuevo}'"
        )
        self.metodos_usados.append("actualizar_valor")
        return cambios

    def eliminar_registro(self, columna, valor):
        indice = self.encabezados.index(columna)
        antes = len(self.filas)
        self.filas = [fila for fila in self.filas if fila[indice] != valor]
        eliminados = antes - len(self.filas)
        self.modificaciones.append(
            f"Se eliminaron {eliminados} registros donde '{columna}' era '{valor}'"
        )
        self.metodos_usados.append("eliminar_registro")
        return eliminados

    def guardar(self, ruta_salida):
        carpeta = os.path.dirname(ruta_salida)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)
        with open(ruta_salida, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.filas)
        self.ruta_salida = ruta_salida
        self.cantidad_guardada = len(self.filas)
        self.metodos_usados.append("guardar")
        return ruta_salida

    def resultados(self):
        return {
            "clase": "ManejadorCSV",
            "archivo_importado": self.ruta_entrada,
            "archivo_guardado": self.ruta_salida,
            "registros_importados": self.cantidad_importada,
            "registros_guardados": self.cantidad_guardada,
            "modificaciones": self.modificaciones,
            "metodos_usados": self.metodos_usados,
        }