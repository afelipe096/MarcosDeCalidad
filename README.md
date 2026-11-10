# Marcos de Calidad

Actividad de Generación 4: arquitectura y DevSecOps para el Sistema de Nómina Colombiano.

## Arquitectura C4

### Nivel 1 – Diagrama de contexto

![Diagrama C4 Nivel 1 - Contexto](arquitectura/C1-contexto.png)

[Ver archivo fuente PlantUML](arquitectura/C1-contexto.puml)

### Nivel 2 – Diagrama de contenedores

![Diagrama C4 Nivel 2 - Contenedores](arquitectura/C2-contenedores.png)

[Ver archivo fuente PlantUML](arquitectura/C2-contenedores.puml)

### Decisión de arquitectura

[ADR-001 – Justificación de microservicios frente a monolito](arquitectura/ADR-001-microservicios.md)

Los diagramas PNG se generan automáticamente mediante el workflow de GitHub Actions cuando se modifican los archivos PlantUML. También se pueden generar manualmente desde la pestaña Actions ejecutando “Exportar diagramas C4 a PNG”.

## DevSecOps

- Caso controlado de fallo del linter: [linter_failure.py](devsecops/linter_failure.py).
- Pipeline que bloquea el despliegue cuando falla el linter: [linter-failure.yml](.github/workflows/linter-failure.yml).
- Pipeline de análisis de seguridad: [security.yml](.github/workflows/security.yml).
- Código analizado: [src/app.py](src/app.py).
- Notebook de Google Colab para ejecutar la prueba del linter y los escaneos: [escaneos_seguridad_colab.ipynb](devsecops/escaneos_seguridad_colab.ipynb).

## Evidencias

Las capturas de la ejecución real en Google Colab se almacenan en la carpeta [evidencias](evidencias/).
