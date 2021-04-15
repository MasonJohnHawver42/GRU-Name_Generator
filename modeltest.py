import keras
import numpy as np
import json

model = keras.models.load_model("model/")

with open("model/config.json", "r") as read_file:
    data = json.load(read_file)

    char_to_index = data["cti"]
    index_to_char = dict( [ (v, k) for k, v in char_to_index.items()] )

    max_char = data["max_char"]
    char_dim = data["char_dim"]

def make_name(model):

    name = []
    x = np.zeros((1, max_char, char_dim))

    i = 0

    while i < max_char - 1:
        probs = np.array(model.predict(x)[0,i])
        probs = probs / np.sum(probs)
        id = np.random.choice(range(char_dim), p=probs)
        char = index_to_char[id]
        if char == '.':
            break

        name.append(char)
        x[0, i + 1, id] = 1
        i += 1

    print("".join(name))

while True:
    make_name(model)
