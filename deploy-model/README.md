# Despliegue del modelo en Vertex AI

**Nota:** Para obtener función de predicción verifique [get_predictions]()

Para el despliegue del modelo se utiliza el servicio de Google Cloud Platform Vertex AI que permite la creación de endpoints para obtener predicciones de modelos entrenados en pipelines del propio Vertex AI o de modelos personalizados importados.

Una manera de desplegar un modelo personalizado usando Vertex AI es usar los contenedores prediseñados. Con estos contenedores, se requiere cargar los archivos del modelo guardado (por ejemplo en TensorFlow) en un depósito de Google Cloud Storage, implementar el modelo y luego crear el punto de extremo para solicitar predicciones. Sin embargo, todas las versiones de YOLO se crearon y publicaron originalmente en Darknet, que tiene un formato de salida de modelo patentado. Esto significa que no puede simplemente entrenar su modelo en Darknet y usar los pesos entrenados directamente como modelo guardado de TensorFlow.

Para resolver lo anterior, se propone convertir los pesos del modelo optimo entrenado con Darknet al formato admitido por TensoFlow, dado que es la solución más practica y sencilla de implementar. También es posible crear una imagen de docker personalizada con darknet incluida, para realizar las predicciones sin tener que convertir el archivo de pesos generado originalmente.

## Preparación para convertir los pesos al formato TensorFlow SavedModel
Para convertir los mejores pesos de Darknet al formato TensorFlow SavedModel, usaremos el repositorio tensorflow-yolov4-lite de Việt Hùng. Se siguen los siguientes pasos:

1. Clonar la última versión del repositorio en su máquina local usando git clone https://github.com/hunglc007/tensorflow-yolov4-tflite.git.
2. Copiar el archivo .weights del modelo entrenado en el directorio /data.
3. Copiar el archivo .names que se creó para entrenar el modelo YOLOv4 personalizado en data/classes/.
4. Abrir core/config.py y cambiar el parámetro de configuración __C.YOLO.CLASSES  para que apunte al archivo .names personalizado.

## Adaptación de la entrada (input) para Vertex AI
El reto aquí radica en el hecho de que la entrada para la predicción en línea en Vertex AI necesita estar en un formato específico. Sin cambiar nada, el modelo acepta un array Numpy con la siguiente estructura [batch_size, input_size, input_size, channels]. Sin embargo, enviar imágenes como matrices Numpy a Vertex AI sería algo ineficiente. La solución propuesta, es codificar los datos binarios de la imagen como una cadena codificada en base64. 

Para esto se proponen las siguientes modificciones al archivo save_model.py:

1. Cambiar la variable input_layer para que acepte una cadena (codificada en base64) en lugar de una matriz Numpy.
2. Crear una función llamada jpeg_decode_fn() que decodifica la imagen a un tensor uint8, redimensiona la imagen para que coincida con el tamaño de entrada esperado y normaliza la imagen dividiéndola por 255.
3. Crear una función map_fn() que decodifica la cadena codificada en base64 a un tensor de tipo cadena y pasa la imagen a la función jpeg_decode_fn().
4. Pasar la imagen preprocesada al modelo en lugar de la entrada bruta.

## Adaptar la salida para Vertex AI
La salida en sí del modelo desplegado en Vertex AI es simplemente una matriz Numpy concatenada de forma [batch_size, number_of_detections, 4 + number_of_classes] (la última dimensión contiene las 4 coordenadas del cuadro delimitador + las puntuaciones de confianza para cada una de las clases disponibles). No es el formato más cómodo para trabajar, por eso se realiza el siguientes ajuste sobre el archivo save_model.py:

1. La estrucutra de la salida se reemplaza por un diccionario con tres claves, que representan las cajas delimitadoras, las clases identificadas y las puntuaciones de confianza.

Se carga el archivo save_model.py modificado.

Para convertir el modelo se ejecuta la siguiente sentencia:

tensorflow-yolov4-tflite % python save_model.py --weights data/yolov4-custom_best_1800.weights --output output/yolov4_1800 --input_size 416 --model yolov4


## Arquitectura del despliegue propuesto

![image](https://user-images.githubusercontent.com/87614301/210907400-c2d8bbdd-6bc4-4f3d-8dbd-b5c068aa1507.png)
