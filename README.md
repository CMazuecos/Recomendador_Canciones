# Recomendador_Canciones
Este programa consistirá en que el programa recomendará al usuario dos canciones al usuario. Hay dos formas de recomendación, en primer lugar, en base a un artista y en segundo lugar, en base a un género. Posteriormente, al usuario se le pedirá un input a partir del cual el programa hará una búsqueda de canciones. De todas las canciones relacionadas a la búsqueda, se devolverá, la canción más popular relacionada con la búsqueda y, en caso de haber otras canciones, se cogerá una random.
### Archivos necesitados
- 'top_10.csv': archivo csv con todos los datos de las canciones.
- 'Recomendador_canciones.py': programa python que hace la recomendación.
### Outputs
- 2 canciones recomendadas con la búsqueda del usuario.
### Forma de ejecución
- Descargamos el archivo csv, el requirements.txt y el de python en una misma carpeta.
- Ejecutar en la terminal 'pip install requirements.txt'.
- Ejecutar 'Recomendador_canciones.py' y automáticamente se lee el csv con pandas. 
- Se pedirá el modo de ejecución y se introducirá 1 si se quiere que se recomiende en base a un artista o 2 en base a un género (en este caso se mostrarán los género posibles)
- Se pedirá al usuario que introduzca un input sobre el que se hará la búsqueda con regex (si con el input introducido no se encuentra nada, se irá eliminando el último carácter hasta que se encuentre un artista o género que contenga ese string).
- Una vez se encuentren resultados relacionados a ese input, se devolverá de todos los resultados posibles, el más popular y uno random.
Para más aclaraciones, código explicado en el texto.
