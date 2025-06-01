# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import pandas as pd
def output_folder():
    ruta = './files/output'
    if not os.path.exists(ruta):
        os.mkdir(ruta)
    return ruta
    
def read_file(file_path):
    headers = []
    with open(file_path,"r",encoding="utf-8") as file:
        headers = file.readlines()
    return headers

def create_dataset(path, target):
    columns = ['phrase', 'target']
    output_df = []
    for directory in os.listdir(path):
        if directory == target:
            path_directory = os.path.join(path, directory)
            for sentiment in os.listdir(path_directory):
                path_sentiment = os.path.join(path_directory, sentiment)
                for files in os.listdir(path_sentiment):
                    path_file = os.path.join(path_sentiment, files)
                    content_file = read_file(path_file)
                    content_file.append(sentiment)
                    output_df.append(content_file)
            df = pd.DataFrame(output_df, columns=columns)
            return df

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    # output_folder()

    path= '.\\files\\input'
    test_dataset= create_dataset(path, 'test')
    train_dataset = create_dataset(path, 'train')
    path_output_folder = output_folder()
    test_dataset.to_csv(os.path.join(path_output_folder, 'test_dataset.csv'))
    train_dataset.to_csv(os.path.join(path_output_folder, 'train_dataset.csv'))

# pregunta_01()