# django-cementerio
Proyecto en Django para registro, búsqueda, y liquidación de deudas de sector Recaudaciones-Cementerio, Municipalidad de San José

Este módulo es de práctica y entrenamiento en el framework Django como también en Python.

La finalidad es desarrollar un módulo de gestión para administrar el registro de pagos de derechos en la oficina de cementerio del sector Recaudaciones de la Municipalidad de San José.

Toda la información se volcará a una DB Sql. A la cual se le cargarán datos reales para el desarrollo.

Funcionalidades--

Diseño DB SQL:

TABLA PAGOS
- id_registro: entero autoincremental.
- fecha_fallecimiento: fecha, null
- fecha_pago: fecha, not null
- recibo: entero, not null
- tasa: float, not null
- recargo: float, not null
- nombre_fallecido: varchar
- pagado_por: varchar
- tipo_parcela: varcahr, not null
- zona: varchar, not null
- observacion: varchar
- observacion2: varchar
- id_parcela: int, not null

- Se debe listar los registros de pago, ordenados por fecha de pago de manera descentende.
- El listado deberá tener paginación por razones de rendimiento.
- Debe generarse el formulario para la carga de registros de pago
- El listado principal debe contener un campo para busquedas mediante fallecido o contribuyente.
- El listado principal debe permitir una vista detallada donde se listen los demás pagos relacionados al fallecido o contribuyente.

