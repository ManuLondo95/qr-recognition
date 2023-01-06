# Entrenamiento del modelo de identificación de objetos personalizado para códigos QR

Para consultar el proceso de entrenamiento ejecutado, explore el Notebook de [Google Colab](https://github.com/ManuLondo95/qr-recognition/blob/719eb8c71145b3e943b2ba07c204fa7bbab8f1fe/train-model/Entrenamiento_modelo_qr_recognition.ipynb)

## Modelos Evaluados:

Se seleccionan 4 modelos, correspondientes a la iteracion 1300, 1500, 1800 y 2100. Se utilizaran las siguientes métricas para comparar los modelos:

* **mAP (mean average precision):** El mAP compara el cuadro delimitador de verdad de campo con el cuadro detectado y devuelve una puntuación. Cuanto mayor sea la puntuación, más preciso será el modelo en sus detecciones.

* **IoU (Intersection over Union):** El IoU se calcula según dividiendo el área de intersección entre las 2 cajas (cuadro detectado y cuadro de verdad de campo) por el área de su unión. Cuanto mayor sea el IoU, mejor será la predicción.

* **Recall:** se calcula como la relación entre el número de muestras positivas clasificadas correctamente como positivas y el número total de muestras positivas.

1. Epoc: 1300

    **Performance during training and tes**
    
    Recall = 0.82  -  mAP = 0.6032 - IoU = 34.03%
   
    <img src="https://user-images.githubusercontent.com/87614301/210923708-53d55a75-25ab-4e32-9ae0-c36fda6e0fa0.png" width=50% height=50%>

2. Epoc: 1500

    **Performance during training and tes**
    
    Recall = 0.83  -  mAP = 0.7092 - IoU = 43.19 %
   
    <img src="https://user-images.githubusercontent.com/87614301/210923842-b37101f1-c41b-48d0-b43f-d5e0b8eddea4.png" width=50% height=50%>
    
 3. Epoc: 1800

    **Performance during training and tes**
    
    Recall = 0.78  -  mAP = 0.6597 - IoU = 48.99 %
   
    <img src="https://user-images.githubusercontent.com/87614301/210924023-57d73601-be6c-49b7-acb2-dbd03d7912aa.png" width=50% height=50%>
    
 4. Epoc: 1800

    **Performance during training and tes**
    
    Recall = 0.77  -  mAP = 0.6730 - IoU = 48.77 %
   
    <img src="https://user-images.githubusercontent.com/87614301/210924185-f28af5cd-fa6d-47cd-97dc-a62802122a49.png" width=50% height=50%>
    
## Modelo seleccionado

Teniendo en cuenta las métricas obtenidas, se seleccionan los pesos de la iteración 1800 ya que tienen la IoU métrica más alta y las demás son satisfactorias y de buen ajuste comparadas con las obtenidas por los pesos de otras iteraciones.

## Resultados con imagenes de prueba

<img src="https://user-images.githubusercontent.com/87614301/210927763-99f09fb7-a97c-4aba-a531-81f9f0d40a55.png" width=50% height=50%>

<img src="https://user-images.githubusercontent.com/87614301/210927817-bab5ba52-65f5-420a-88d8-b891acab137a.png" width=50% height=50%>




