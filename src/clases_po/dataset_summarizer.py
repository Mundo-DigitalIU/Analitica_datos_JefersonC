import pandas as pd


class DatasetSummarizer:
    """Recibe un DataFrame y genera un resumen de su contenido en un .txt."""

    def __init__(self, df: pd.DataFrame, nombre="dataset"):
        self.df = df
        self.nombre = nombre

    def generar_resumen(self) -> str:
        lineas = []
        lineas.append(f"RESUMEN DE: {self.nombre}")
        lineas.append("=" * 50)

        filas, columnas = self.df.shape
        lineas.append(f"Filas: {filas}")
        lineas.append(f"Columnas: {columnas}")

        lineas.append("\nColumnas y tipos de datos:")
        for col, tipo in self.df.dtypes.items():
            lineas.append(f"  - {col}: {tipo}")

        lineas.append("\nValores nulos por columna:")
        for col, nulos in self.df.isnull().sum().items():
            lineas.append(f"  - {col}: {nulos}")

        lineas.append("\nEstadísticas descriptivas:")
        lineas.append(self.df.describe(include="all").to_string())

        return "\n".join(lineas)

    def guardar_txt(self, ruta="resumen.txt"):
        resumen = self.generar_resumen()
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(resumen)
        return ruta