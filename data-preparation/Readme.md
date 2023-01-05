# Preparación de los datos

Uno de los pasos más importantes para cualquier tarea de aprendizaje profundo es la preparación de los datos. En este caso las imágenes utilizadas para el entrenamiento fueron tomadas de [Kaggel](https://www.kaggle.com/datasets/hamidl/yoloqrlabeled?resource=download). 

Los datasets disponibles ya cuentan con las etiquetas de los códigos QR y el archivo classes.name  propio del formato YoloV4.

La muestras de datos utilizada está compuestas por 325 imágenes que fueron separadas en 2 dataset: 

1. **obj.zip :** imágenes y etiquetas para el entrenamiento del modelo YOLOv4 (80 %) 
2. **test.zip:** imágenes y etiquetas para la validación del modelo (20 %)

la estructura de la carpeta se describe a continuación:

Compuesta por 3 carpetas:
* **data:** se encuentran los objetos comprimidos de los conjuntos de entrenamiento y validación.

* **fuctions:** Se encuentran las funciones .py para generar los archivos .txt con las rutas de las imágenes de entrenamiento y validación, necesarios para el modelo yolov4-custom.

* **backup:** Ruta donde se almacenan los backups de los pesos del modelo yolov4-custom a medida que avanza el entrenamiento

y dos archivos auxiliares:

* **obj.data:** contiene la información del número de clases a identificar dentro de la imagen, la ruta donde se encuentra el archivo .txt con las imágenes de entrenamiento, la ruta donde se encuentra el archivo .txt con las imágenes de validación, la ruta donde se encuentra el archivo obj.names y la ruta donde se almacenara el backup.

* **obj.names:** archivo con nombres de objetos etiquetados en las imagenes de entrenamiento, cada uno en una nueva línea.

Esta estructura debe conservarse en Google Drive para correr el notebook de Google Colab creado para el entrenamiento del modelo.
