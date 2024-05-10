"""
    Noms: Daniel Arco, Izan Arnaiz.
    Data: 20/03/2024
    Grup: ASIXc1A
    Descripció:
    Módul per les diferents peticions a fer, ja sigui per teclat, peticions a un servidor o ChatGPT.
"""

import openai
import requests


def get_data__from_keyboard():
    dades = input("")
    return dades


def get_data_from_server():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'lp1kGetjUKQI2usjfvMWkQ==hsUk0gL8fH1zlEK4'})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return "Error:", response.status_code, response.text


def get_data_from_chatGPT(questio):
    openai.api_key = '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'
    ENGINE = "gpt-3.5-turbo"
    MAX_TOKENS = 2048
    print(f"Preguntando a dios....")
    completion = openai.ChatCompletion.create(
        model=ENGINE,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": questio}
        ],
        max_tokens=MAX_TOKENS
    )
    frase = completion.choices[0].message['content']
    return frase


# TODO al 3r lliurament
def get_data_from_file(file_name):
    """ Aquesta funció recull les dades des d'un arxiu
 Entrada: Una cadena de caràcters amb el nom del fitxer origen
       Retorna: una única cadena de caràcters"""
    dades = ""
