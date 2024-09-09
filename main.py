import random
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "NERF": "Empeorar las habilidades de algun objeto o personaje",
    "BUFF": "Meforar las habilidades de algun objeto o personaje",
    "CREEPY": "Algo aterrador o siniestro"
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(word, ":", meme_dict[word])
    else:
        new = random.choice(meme_dict.keys())
        print("Esa palabra esta mal escrita o no entra en este diccionario")
        print("Puedes poner por efemplo  ", new, ":", meme_dict[new])
