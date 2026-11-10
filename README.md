# Marcos de Calidad

Actividad de Generación 4: arquitectura y DevSecOps para el Sistema de Nómina Colombiano.

## Entregables

### Arquitectura
- Diagrama C4 Nivel 1: contexto del sistema.
- Diagrama C4 Nivel 2: contenedores del sistema.
- ADR-001: justificación de la arquitectura de microservicios frente a un monolito.
- Exportación PNG de los diagramas mediante el workflow de PlantUML.

### DevSecOps
- Caso controlado de fallo del linter.
- Pipeline que bloquea el despliegue cuando falla el linter.
- Pipeline de análisis de seguridad con Bandit y pip-audit.

## Estructura

- arquitectura/: diagramas PlantUML y decisión de arquitectura.
- devsecops/: caso de fallo del linter, dependencias e instrucciones de escaneo.
- src/: código de ejemplo analizado por las herramientas de seguridad.
- .github/workflows/: automatizaciones de calidad, seguridad y exportación de diagramas.
- evidencias/: capturas y soportes de ejecución.

## Diagramas

Los archivos PlantUML se encuentran en arquitectura/. El workflow diagrams.yml genera los archivos PNG y los publica como artefacto descargable de la ejecución de GitHub Actions.
