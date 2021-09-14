# django-cementerio
Proyecto en Django para registro, búsqueda, y liquidación de deudas de sector Recaudaciones-Cementerio, Municipalidad de San José

Este módulo es de práctica y entrenamiento en el framework Django como también en Python.

Problema
Es necesario contar con un sistema de gestión online, que permita registrar la actividad de la Oficina de cobros de Cementerio del Sector Recaudaciones.

La citada oficina realiza el cobro de derechos en concepto de Inhumacion y arrendamiento de parcelas y nichos en el cementerio local. Es necesario registrar, tanto, estos cobros como la información relacionada con ellos de manera ágil y que permita su búsqueda y referencia.

Tambien es necesario procesar la información de los cobros, de manera de obtener fechas de vencimiento, liquidación de recargos en caso de mora en los pagos teniendo en cuenta las variaciones en los montos de las tasas y las fechas en las que entran en vigor, estado de deudas y futuros informes gerenciales.

Información relacionada con los cobros:
- Fallecimientos.
- Contribuyentes.
- Parcelas y nichos en el cementerio.
- Montos de las tasas proveniente de la ordenanza fiscal.

Toda la información se volcará a una DB Sql. A la cual se le cargarán datos reales para el desarrollo.

Funcionalidades--

Diseño DB SQL:

TABLA PAGOS
- id_registro: entero autoincremental
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

