# Marcos de Calidad

Actividad de Generación 4: arquitectura y DevSecOps para el Sistema de Nómina Colombiano.

## Arquitectura C4

### Nivel 1 – Diagrama de contexto

![Diagrama C4 Nivel 1 - Contexto](arquitectura/C1-contexto.png)

[Archivo fuente PlantUML](arquitectura/C1-contexto.puml)

### Nivel 2 – Diagrama de contenedores

![Diagrama C4 Nivel 2 - Contenedores](arquitectura/C2-contenedores.png)

[Archivo fuente PlantUML](arquitectura/C2-contenedores.puml)

### Decisión de arquitectura

[ADR-001 – Arquitectura basada en microservicios](arquitectura/ADR-001-microservicios.md)

## DevSecOps

- **Flake8:** validación de estilo y detección de errores en el archivo de prueba.
- **Bandit:** análisis estático del código Python.
- **pip-audit:** auditoría de dependencias.
- **GitHub Actions:** automatización de los análisis y exportación de diagramas PlantUML a PNG.

## Estructura

- `arquitectura/`: diagramas C4 y registro de decisión arquitectónica.
- `devsecops/`: archivo de prueba del linter y dependencias.
- `src/`: código Python de ejemplo.
- `.github/workflows/`: flujos automatizados de calidad, seguridad y generación de diagramas.
