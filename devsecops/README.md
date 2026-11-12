# DevSecOps: calidad y seguridad

## Validación de calidad del código

Se incorporó el archivo `linter_failure.py` con dos defectos controlados para demostrar la detección de errores mediante análisis estático:

- Espacios en blanco al final de una línea.
- Uso de una variable no definida.

Se configuró el workflow `.github/workflows/linter-failure.yml` para ejecutar Flake8 con las reglas de estilo y nombres seleccionadas. El job `deploy` depende del resultado de `lint` y está condicionado a que la validación termine correctamente. Por eso, el caso de prueba está preparado para provocar el fallo del linter y bloquear el job de despliegue.

## Análisis de seguridad

Se configuró el workflow `.github/workflows/security.yml` con dos herramientas:

- **Bandit:** analiza el código Python ubicado en `src/` para identificar posibles problemas de seguridad.
- **pip-audit:** revisa las dependencias declaradas en `devsecops/requirements.txt` frente a vulnerabilidades conocidas.

Se agregó `src/app.py` como código de ejemplo. El archivo `requirements.txt` se encuentra vacío porque la aplicación de ejemplo no utiliza paquetes externos.

## Consulta de resultados

Los workflows se ejecutan en GitHub Actions. En la pestaña **Actions** se encuentran los estados, pasos y registros de cada ejecución. La evidencia de aprobación o fallo se toma del resultado real de esos workflows, no solamente de su configuración.
