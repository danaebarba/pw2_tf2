¿Qué ventajas ofrece GraphQL sobre REST en este contexto?
En este ejercicio que realice, las ventajas que yo mas note fue especialmente la facilidad con la que se mueven los datos, antes de realizarlo completo, realice otra prueba unicamente con los datos en flask, y los datos no se cambiaban con tanta facilidad como al hacerlo con Graphql. Ademas de el guardado de datos, al yo cambiar un dato, se podia ver reflejado en la pantalla, pero al reiniciar estos datos se borraban, cosa que dejo de suceder al utilizar Graphql.

¿Cómo se definen los tipos y resolvers en una API con GraphQL?
Los tipos son los que te describen como es el dato que esta disponible, si estos se pueden modificar o consultar y como se relacionan, en este se define que datos se tendran en cuenta y su estructura.
Y los resolvers son funciones. Estos responden a las consultas o queries y a las mutaciones, estas resuelven cuando alguien pide algo a un API.

¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?
Para poder tener un buen control de los datos, estos datos pueden utilizarse en diferentes partes, por lo tanto tener el disponible solamente en el front hace que la desincronizacion pueda suceder. Se tiene una mejor consistencia de datos en este caso.

¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?
Que esta logica unicamente se encuentre en el backend, que el frontend pueda verla y preguntar por ella, pero cualquier tipo de cambio deba de pasar igualmente por el backend para ser aceptada. En este que se valide siempre antes de realizar algun movimiento, ya sea el id del producto y su stock.