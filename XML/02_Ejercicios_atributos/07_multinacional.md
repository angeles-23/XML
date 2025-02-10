# Ejercicio: multinacional
Una multinacional que opera en bolsa necesita un formato de intercambio de datos para que sus programas intercambien información sobre los mercados de acciones.

En general todo archivo constará de un listado de cosas como se detalla a continuación

- En el listado aparecen siempre uno o varios futuros, despues una o varias divisas, despues uno o varios bonos y una o varias letras.

- Todos ellos tienen un atributo precio que es obligatorio

- Todos ellos tienen un elemento vacío que indica de donde es el producto anterior: «Madrid», «Nueva York», «Frankfurt» o «Tokio».

- Las divisas y los bonos tienen un atributo optativo que se usa para indicar si el producto ha sido estable en el pasado o no.

- Un futuro es un valor esperado que tendrá un cierto producto en el futuro. Se debe incluir este producto en forma de elemento. También puede aparecer un elemento mercado que indique el país de procedencia del producto.

- Todo bono tiene un elemento país_de_procedencia para saber a qué estado pertenece. Debe tener tres elementos extra llamados «valor_deseado», «valor_mínimo» y «valor_máximo» para saber los posibles precios.

- Las divisas tienen siempre un nombre pueden incluir uno o más tipos de cambio para otras monedas.

- Las letras tienen siempre un tipo de interés pagadero por un país emisor. El país emisor también debe existir y debe ser siempre de uno de los países cuyas capitales aparecen arriba (es decir «España», «EEUU», «Alemania» y «Japón»)