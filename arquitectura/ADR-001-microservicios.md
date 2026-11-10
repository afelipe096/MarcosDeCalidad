# ADR-001: Selección de arquitectura basada en microservicios

- **Estado:** Aceptada para el diseño académico.
- **Fecha:** 10 de noviembre de 2026.
- **Sistema:** Sistema de Nómina Colombiano.

## Contexto

El sistema debe cubrir procesos relacionados, pero con responsabilidades distintas: administración de empleados y novedades, liquidación de nómina, cumplimiento de obligaciones colombianas, pagos y generación de reportes. Estos procesos manejan reglas de negocio diferentes y pueden cambiar en momentos distintos.

La liquidación depende de información laboral y de novedades. El cumplimiento requiere generar y transmitir información de nómina electrónica a la DIAN y preparar datos de aportes para el operador PILA. El proceso de pagos se comunica con entidades bancarias. Los reportes consultan información consolidada sin tener que ejecutar la liquidación.

## Decisión

Se adopta una arquitectura de microservicios. El sistema se divide por capacidades de negocio:

1. Servicio de identidad y acceso.
2. Servicio de empleados y novedades.
3. Servicio de liquidación.
4. Servicio de cumplimiento.
5. Servicio de pagos.
6. Servicio de reportes.

El portal web consume los servicios mediante un API Gateway. Los servicios intercambian eventos para procesos que no necesitan una respuesta inmediata. Cada servicio es responsable de sus datos y puede usar PostgreSQL como tecnología de persistencia. La mensajería se representa con RabbitMQ.

## Justificación frente a un monolito

| Criterio | Microservicios | Monolito |
|---|---|---|
| Cambios normativos | El servicio de cumplimiento puede actualizarse sin desplegar toda la aplicación. | Un cambio en una parte puede exigir probar y desplegar toda la aplicación. |
| Escalabilidad | Se puede ampliar el servicio de liquidación en periodos de alta carga sin escalar todos los módulos. | Normalmente se escala la aplicación completa. |
| Aislamiento de fallos | Un problema en reportes no tiene por qué detener la captura de novedades o la liquidación, si se diseñan tolerancia y reintentos. | Un fallo grave puede afectar el proceso completo. |
| Evolución | Los módulos pueden evolucionar de forma independiente y con contratos definidos. | La evolución está más acoplada al código y al ciclo de despliegue común. |
| Integraciones externas | DIAN, PILA y bancos quedan encapsulados en servicios con responsabilidades específicas. | Las integraciones comparten el despliegue y la estructura de la aplicación. |

La elección se justifica porque el dominio tiene procesos diferenciados y conexiones externas con ciclos de cambio propios. La separación permite mantener aisladas las integraciones y evolucionar el cálculo de nómina sin obligar a desplegar todos los módulos.

## Consecuencias y compromisos

- Se requiere monitoreo distribuido, trazabilidad y correlación de solicitudes.
- La comunicación entre servicios introduce latencia y posibles fallos de red.
- Deben definirse contratos de API y eventos versionados.
- Se necesita manejar consistencia eventual en procesos asíncronos.
- La operación es más compleja que la de un monolito y exige automatización de despliegues y pruebas.
- Para evitar transacciones distribuidas, cada servicio administra sus datos y se coordinan procesos mediante eventos y mecanismos de compensación cuando aplique.

## Alternativas consideradas

**Monolito modular:** sería más sencillo de desarrollar, probar y desplegar al inicio. Se descarta para este diseño porque la actividad solicita justificar microservicios y porque los procesos normativos, de liquidación e integración tienen necesidades de evolución diferenciadas.

**Microservicios:** seleccionada por la separación de capacidades, escalabilidad independiente y aislamiento de integraciones, aceptando el mayor costo operativo.

## Riesgos y medidas

- **Complejidad operativa:** automatizar compilación, pruebas, análisis de seguridad y despliegues.
- **Fallos de comunicación:** aplicar tiempos de espera, reintentos controlados e idempotencia.
- **Datos inconsistentes:** usar eventos con identificadores únicos, registro de estados y reconciliación.
- **Exposición de datos personales y salariales:** aplicar control de acceso por rol, cifrado en tránsito y reposo, auditoría y mínimo privilegio.

## Resultado esperado

Una plataforma organizada por capacidades de negocio, con servicios desplegables de forma independiente y controles de seguridad y calidad integrados en el proceso de entrega.
