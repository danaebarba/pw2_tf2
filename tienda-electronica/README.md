# tienda-electronica

Utilize como ayuda los siguientes links:
https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/#put-route
https://www.youtube.com/watch?v=CXyFs5wWask&ab_channel=DanVega
https://www.youtube.com/watch?v=zsYIw6RXjfM&ab_channel=TechWithTim
https://graphql.org/learn/queries/


### Como compilar

Para correr la tienda electronica utilizo:
npm run dev
Para inicializar el server utilizo:
python app.py

Para utilizar rapidamente:
Nueva terminal:
cd "flask-vue-prj"
cd "server"
python app.py

Nueva terminal:
cd "flask-vue-prj"
cd "tienda-electronica"
npm run dev

Para ver el query utilice en navegador el siguiente link:
http://localhost:5001/graphql

Para hacer funcionar el test.py:
Primero hay que encender el servidor:
Nueva terminal:
cd "flask-vue-prj"
cd "server"
python app.py
En una nueva terminal correr el test con:
cd "flask-vue-prj"
cd "server"
python test.py

## Cosas diferentes de el anterior proyecto
Decidi cambiar el diseño por uno mas moderno y facil de utilizar.
El movimiento del stock funciona perfectamente, aun me faltan pruebas de la agregacion de productos ya que fue de mis ultimos arreglos y no tuve tiempo de mejorarlo al 100. 
Tambien hay un archivo llamado Alert.vue, y en electronics sale un warning por mencionarlo y no utilizarlo, tengo que hacerlo funcional, pero decidi enfocarme en otras cosas antes.
El ping.vue funciona para ver si la pagina compila.

# Fallos
Aun no funciona la logica de agregacion de un producto, se encuentra comentarizada en lo que logro resolverlo.
