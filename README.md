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

Se documentó la propuesta de arquitectura mediante los diagramas C4 y el registro de decisión arquitectónica ADR-001. También se configuró un workflow de GitHub Actions para exportar los diagramas PlantUML a formato PNG y guardar los archivos generados en el repositorio.

## DevSecOps

- Se incorporó un caso controlado de fallo del linter en [linter_failure.py](devsecops/linter_failure.py), con espacios en blanco al final de una línea y una variable no definida.
- Se configuró [linter-failure.yml](.github/workflows/linter-failure.yml) para ejecutar Flake8 y condicionar el job de despliegue al resultado de la validación.
- Se configuró [security.yml](.github/workflows/security.yml) para ejecutar Bandit sobre el código Python y pip-audit sobre las dependencias declaradas.
- Se agregó [src/app.py](src/app.py) como código de ejemplo para el análisis estático de seguridad.

## Evidencias

Los workflows están configurados en GitHub Actions. Sus resultados y registros de ejecución se consultan en la pestaña Actions del repositorio. La configuración del pipeline no representa por sí sola una ejecución aprobada: los estados se verifican en los registros de cada ejecución.
