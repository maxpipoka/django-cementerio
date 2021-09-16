# django-cementerio
Proyecto en Django para registro, búsqueda, y liquidación de deudas de sector Recaudaciones-Cementerio, Municipalidad de San José

Este módulo es de práctica y entrenamiento en el framework Django como también en Python.

## Problema
Es necesario contar con un sistema de gestión online, que permita registrar la actividad de la Oficina de cobros de Cementerio del Sector Recaudaciones.

La citada oficina realiza el cobro de derechos en concepto de Inhumacion y arrendamiento de parcelas y nichos en el cementerio local. Es necesario registrar, tanto, estos cobros como la información relacionada con ellos de manera ágil y que permita su búsqueda y referencia.

### Cada registro "Pago" debe contener los campos: 
- Fecha del pago. 
- Datos del recibo de recaudación.
- Nombre del o los fallecidos alojados en la parcela o nicho. 
- Contribuyente a nombre de quien se realiza el recibo de recaudación. 
- Datos de la parcela o nicho.
- Fecha de vencimiento del pago realizado.
- Un campo de texto para consignar el periodo o concepto abonado.
- Un campo de texto para consignar observaciones del pago.


### De cada recibo se debe registrar:
- Número de Recibo.
- Contribuyente.
- Monto de tasa.
- Recargos si corresponden.

### De cada parcela o nicho se debe registrar la siguiente informacion:
- 

Tambien es necesario procesar la información de los cobros, de manera de obtener fechas de vencimiento futuras, liquidación de recargos en caso de mora en los pagos teniendo en cuenta las variaciones en los montos de las tasas y las fechas en las que entran en vigor, estado de deudas y futuros informes gerenciales.

Información relacionada con los cobros:
- Fallecimientos.
- Contribuyentes.
- Parcelas y nichos en el cementerio.
- Montos de las tasas proveniente de la ordenanza fiscal.

Toda la información se volcará a una DB Sql. A la cual se le cargarán datos reales para el desarrollo.

Funcionalidades--

- Se debe listar los registros de pago, ordenados por fecha de pago de manera descentende.
- El listado deberá tener paginación por razones de rendimiento.
- Debe generarse el formulario para la carga de registros de pago
- El listado principal debe contener un campo para busquedas mediante fallecido o contribuyente.
- El listado principal debe permitir una vista detallada donde se listen los demás pagos relacionados al fallecido o contribuyente.

