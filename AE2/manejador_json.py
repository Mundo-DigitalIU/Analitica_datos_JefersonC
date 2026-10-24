import json
import os


class ManejadorJSON:
    """Importa, modifica y guarda archivos JSON con json.load y json.dump."""

    def __init__(self, ruta_entrada):
        self.ruta_entrada = ruta_entrada
        self.registros = []
        self.ruta_salida = None
        self.cantidad_importada = 0
        self.cantidad_guardada = 0
        self.modificaciones = []
        self.metodos_usados = []

    def importar(self):
        with open(self.ruta_entrada, "r", encoding="utf-8") as archivo:
            self.registros = json.load(archivo)
        self.cantidad_importada = len(self.registros)
        self.metodos_usados.append("importar")
        return self.registros

    def actualizar_valor(self, indice, campo, valor_nuevo):
        valor_anterior = self.registros[indice].get(campo)
        self.registros[indice][campo] = valor_nuevo
        self.modificaciones.append(
            f"Se actualizó el registro {indice}: campo '{campo}' "
            f"de '{valor_anterior}' a '{valor_nuevo}'"
        )
        self.metodos_usados.append("actualizar_valor")

    def agregar_registro(self, nuevo_registro):
        self.registros.append(nuevo_registro)
        self.modificaciones.append("Se agregó 1 registro nuevo al final de la lista")
        self.metodos_usados.append("agregar_registro")

    def guardar(self, ruta_salida):
        carpeta = os.path.dirname(ruta_salida)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)
        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            json.dump(self.registros, archivo, indent=4, ensure_ascii=False)
        self.ruta_salida = ruta_salida
        self.cantidad_guardada = len(self.registros)
        self.metodos_usados.append("guardar")
        return ruta_salida

    def resultados(self):
        return {
            "clase": "ManejadorJSON",
            "archivo_importado": self.ruta_entrada,
            "archivo_guardado": self.ruta_salida,
            "registros_importados": self.cantidad_importada,
            "registros_guardados": self.cantidad_guardada,
            "modificaciones": self.modificaciones,
            "metodos_usados": self.metodos_usados,
        }