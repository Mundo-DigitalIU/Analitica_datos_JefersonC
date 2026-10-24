from datetime import datetime


class GeneradorResumenTXT:
    """Recibe los resultados de las otras dos clases y genera resumen.txt."""

    def __init__(self, url_csv, url_json, resultados_csv, resultados_json):
        self.url_csv = url_csv
        self.url_json = url_json
        self.res_csv = resultados_csv
        self.res_json = resultados_json

    def construir_texto(self):
        lineas = []
        lineas.append("RESUMEN DE EJECUCIÓN - EVIDENCIA DE APRENDIZAJE 2")
        lineas.append("=" * 60)
        lineas.append(f"Fecha de ejecución: {datetime.now():%Y-%m-%d %H:%M:%S}")

        lineas.append("\n1. URL DE ORIGEN")
        lineas.append(f"  CSV : {self.url_csv}")
        lineas.append(f"  JSON: {self.url_json}")

        lineas.append("\n2. DETALLE POR ARCHIVO")
        for r in (self.res_csv, self.res_json):
            lineas.append(f"\n--- {r['clase']} ---")
            lineas.append(f"Archivo importado: {r['archivo_importado']}")
            lineas.append(f"Registros importados: {r['registros_importados']}")
            lineas.append("Modificaciones realizadas:")
            for m in r["modificaciones"]:
                lineas.append(f"  - {m}")
            lineas.append(f"Archivo nuevo guardado: {r['archivo_guardado']}")
            lineas.append(f"Registros guardados: {r['registros_guardados']}")

        lineas.append("\n3. CLASES Y MÉTODOS UTILIZADOS")
        for r in (self.res_csv, self.res_json):
            lineas.append(f"  {r['clase']}: {', '.join(r['metodos_usados'])}")
        lineas.append("  GeneradorResumenTXT: construir_texto, generar_txt")

        total = self.res_csv["registros_importados"] + self.res_json["registros_importados"]
        lineas.append("\n4. REGISTROS PROCESADOS")
        lineas.append(f"  Total de registros importados (CSV + JSON): {total}")

        return "\n".join(lineas)

    def generar_txt(self, ruta="resumen.txt"):
        texto = self.construir_texto()
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
        return ruta