# DevSecOps: calidad y seguridad

## Fallo intencional del linter

El archivo linter_failure.py contiene dos defectos controlados:

- Espacios en blanco al final de una línea.
- Uso de una variable no definida.

El workflow .github/workflows/linter-failure.yml ejecuta Flake8. El job deploy depende de lint y solo se ejecuta cuando el linter termina correctamente. Con el archivo actual, el job lint debe fallar y el despliegue debe quedar omitido.

## Escaneos de seguridad

El workflow .github/workflows/security.yml ejecuta:

- Bandit para revisar posibles problemas de seguridad en el código Python.
- pip-audit para revisar vulnerabilidades conocidas en dependencias declaradas.

El código de ejemplo está en src/app.py. El archivo requirements.txt está vacío porque el ejemplo no requiere paquetes externos.

## Consulta de resultados

Los resultados se consultan en la pestaña Actions del repositorio. La ejecución de seguridad debe terminar correctamente y mostrar los pasos de Bandit y pip-audit aprobados. La ejecución del linter debe fallar de forma intencional para demostrar que el despliegue queda bloqueado.
