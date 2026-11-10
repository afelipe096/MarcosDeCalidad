# DevSecOps: calidad y seguridad

## Fallo intencional del linter

El archivo linter_failure.py contiene dos defectos controlados para demostrar el bloqueo de la tubería:

- Espacios en blanco al final de una línea.
- Uso de una variable no definida.

El workflow .github/workflows/linter-failure.yml ejecuta Flake8. El job deploy depende de lint y solo se ejecuta cuando el linter termina correctamente. Con el archivo actual, el job de lint debe fallar y el despliegue debe quedar omitido.

## Escaneos de seguridad

El workflow .github/workflows/security.yml ejecuta:

- Bandit para revisar posibles problemas de seguridad en el código Python.
- pip-audit para revisar vulnerabilidades conocidas en dependencias declaradas.

El código de ejemplo está en src/app.py. El archivo requirements.txt está vacío porque el ejemplo no requiere paquetes externos.

## Ejecución en Google Colab

Ejecuta estas celdas en un notebook de Colab para obtener la salida real de los escaneos:

~~~python
!pip install -q bandit pip-audit
~~~

~~~python
!bandit -r src -ll
~~~

~~~python
!pip-audit -r devsecops/requirements.txt
~~~

La evidencia de aprobación debe corresponder a la salida real de las dos últimas celdas ejecutadas en Colab. Los resultados no se sustituyen por capturas simuladas.
