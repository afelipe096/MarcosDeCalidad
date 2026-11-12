# DevSecOps: calidad y seguridad

## Validación de calidad del código

El archivo `linter_failure.py` contiene dos errores controlados:

- Espacios en blanco al final de una línea.
- Uso de una variable no definida.

El workflow `.github/workflows/linter-failure.yml` ejecuta Flake8 con las reglas `E`, `W` y `F`. El job `deploy` depende del resultado del job `lint` y solo se ejecuta cuando la validación termina correctamente.

## Análisis de seguridad

El workflow `.github/workflows/security.yml` ejecuta:

- **Bandit:** análisis estático del código Python ubicado en `src/`.
- **pip-audit:** auditoría de las dependencias declaradas en `requirements.txt`.

## Automatización

Los workflows se ejecutan mediante GitHub Actions y pueden iniciarse manualmente o mediante los eventos de publicación configurados en cada archivo YAML.
