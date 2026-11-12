"""Código de ejemplo utilizado por el workflow de análisis estático con Bandit."""


def estado_servicio():
    """Devuelve el estado básico del servicio de nómina."""
    return {"estado": "disponible"}


if __name__ == "__main__":
    print(estado_servicio())
