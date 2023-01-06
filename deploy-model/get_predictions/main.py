# Instalación de librerias
#pip install -r requerimientos.txt
#pip install --upgrade google-api-python-client

# Importacion de librerias
import cv2
import base64
import argparse
import numpy as np
from PIL import Image
from random import randint
from google.cloud import aiplatform
from predict_custom_trained_model_sample import predict_custom_trained_model_sample

project_id ="1008294310504"
endpoint_id="5012950587960983552"
location="us-central1"

# Definicion de funciones
def read_image(image_path):
    '''
        Funcion que recibe el path de la imagen y devuelve
        una cadena de textp codificada en base64
    '''
    image_bytes = ''
    instances = { "image_bytes": ""}
    with open(image_path, "rb") as image_file:
        image_bytes = base64.urlsafe_b64encode(image_file.read()).decode()
        instances["image_bytes"]=image_bytes
    
    return instances

def get_result(image_path, result_path, predictions):
    '''
        Funcion que recibe las predicciones y las ubica en la imagen
        la imagen modificada se almacena en la ruta ingresada
    '''
    name_image = image_path.split('/')[-1]
    for p in predictions:
        polygons = dict(p)['tf.identity']
        polygons_true = [x for x in polygons if not np.all(np.array(x)) == 0]
        image = cv2.imread(image_path)
    # Draw boxes
    colors = {}
    for box in polygons_true:
        index = polygons_true.index(box)
        if index not in colors:
            colors[index] = [randint(0, 255), randint(0, 255), randint(0, 255)]
        y1, x1, y2, x2 = map(float, box)
        cv2.rectangle(image, (int(round(x1*416)), int(round(y1*416))), (int(round(x2*416)), int(round(y2*416))), color=colors[index], thickness=2)
    cv2.imwrite(f'{result_path}/result_{name_image}', image)


# Definicion del main #
#---------------------#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("tokenid_path", help = "Introduzca la ruta donde se almacena el archivo .json con la clave de acceso", type = str)
    parser.add_argument("image_path", help = "Introduzca la ruta donde se almacena la imagen que quiere probar", type = str)
    parser.add_argument("result_path", help = "Introduzca la ruta donde se almacenan los resultados", type = str)
    args = parser.parse_args()
    
    try:
        print("======= Identificador de códigos QR ======")
        print("======= Lectura de la imagen ======")
        instance = read_image(image_path=args.image_path)
        print("======= Enviando predicción de prediccón ======")
        try:
            predictions = predict_custom_trained_model_sample(project_id,endpoint_id,instance,location="us-central1", 
            api_endpoint = "us-central1-aiplatform.googleapis.com", tokenid=args.tokenid_path)
            print("======= Nueva predicción ======")
        except:
            print("====== No se identifican códigos QR en la imagen =======")
        get_result(image_path=args.image_path, result_path=args.result_path, predictions=predictions)
        print(f"====== Resultados almacenados en: {args.result_path} =======")
    except:
        print("No es posible obtener predicciones")
