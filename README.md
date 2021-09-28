# django-cementerio
Proyecto en Django para registro, búsqueda, y liquidación de deudas de sector Recaudaciones-Cementerio, Municipalidad de San José

Este módulo es de práctica y entrenamiento en el framework Django como también en Python.

## Problema
Es necesario contar con un sistema de gestión online, que permita registrar la actividad de la Oficina de cobros de Cementerio del Sector Recaudaciones.

La citada oficina realiza el cobro de derechos en concepto de Inhumacion y arrendamiento de parcelas y nichos en el cementerio local. Es necesario registrar, tanto, estos cobros como la información relacionada con ellos de manera ágil y que permita su búsqueda y referencia.

## Modelos de datos
### Pago: 
- Fecha del pago. 
- Datos del recibo de recaudación.
- Nombre del o los fallecidos alojados en la parcela o nicho. 
- Contribuyente a nombre de quien se realiza el recibo de recaudación. 
- Datos de la parcela o nicho.
- Fecha de vencimiento del pago realizado.
- Observación sobre el período o concepto abonado.
- Obsercacion anexa del pago (persona que abona es diferente a la que figura como contribuyente, etc.).

### Recibo:
- Número de Recibo.
- Contribuyente.
- Monto de tasa.
- Recargos si corresponden.

### Parcela o nicho:
- Número.
- Fila.
- Sector.
- Zona.

### Permiso Inhumacion (PDI):
- Fecha de gestión en el Registro Provincial de las Personas (RPP).
- Oficina del RPP donde se realizó la gestión.
- Departamento de ubicación de la oficina del RPP.
- Fecha presentación en oficina municipal.
- Fallecido.
- Dni Fallecido.
- Fecha fallecimiento.
- Persona que hace la presentación.
- Observaciones.
- Imágen del PDI.

### Contribuyente:
- Nombre.
- Dni.

### Fallecido:
- Nombre.
- Dni.

### Tasa:
- Zona.
- Periodicidad.
- Monto.
- Fecha desde cuando se aplica.
- Fecha hasta cuando se aplica.

### Usuario:
- Usuario.
- Nombre.
- Password.
- Nivel acceso.


## Funcionalidades necesarias
### Pagos:
- Cada pago debe poder registrarse a un solo contribuyente.
- En el campo FALLECIDO puede ser una o mas personas, que serían las ocupante de la parcela o nicho. Pero cada pago puede ser por una sola parcela o nicho.
- Los conceptos que se abonan son:
-- 
- Un pago puede ser por el período en curso, como tambien por períodos anteriores vencidos. (Ej. Actual 2021, o vencidos 2019, 2020.) En caso de ser por periodos anteriores vencidos la liquidacion de recargos se realiza por cada periodo independiente. No pudiendo aplicarse

- Se debe listar los registros de pago, ordenados por fecha de pago de manera descentende.
- El listado deberá tener paginación por razones de rendimiento.
- Debe generarse el formulario para la carga de registros de pago
- El listado principal debe contener un campo para busquedas mediante fallecido o contribuyente.
- El listado principal debe permitir una vista detallada donde se listen los demás pagos relacionados al fallecido o contribuyente.

