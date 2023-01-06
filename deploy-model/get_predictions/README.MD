# Proceso de predicción

![image](https://user-images.githubusercontent.com/87614301/211117408-d84621e0-95b4-4077-af6a-52d418304854.png)

## ¿Cómo ejecutar la función de predicción?
1. Descargue la carpeta get_predictions
2. Almacene el token enviado para la autenticación con el endpoint de Vertex AI
3. Instale las librerias utilizadas en el proceso de predicción -- pip install -r requirements.txt (Se recomienda primero crear un ambiente virtual de python)
4. Invoque la función main.py en la terminal desde la carpeta get_predictions: 
    python3 main.py 'tokenid_path' 'image_path' 'result_path'
    
    **tokenid_path** path donde se almacena el token enviado para autenticación
    
    **imagen_path** path donde se almacena la imagen que quiere testear
    
    **result_path** path donde se almacena la imagen con las predicciones
    
## ¿Cómo decodificar códigos QR?
Se incluye un notebook que permite la decodficación de códigos QR (no se integra con la solución actual, es un recurso extra).
