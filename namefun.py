from csv import reader
import numpy as np

from keras.models import Sequential
from keras.layers import LSTM, Dense, GRU
from keras.callbacks import LambdaCallback\

from bpe import Encoder

def collectNames():
    fn = "/home/mason/Downloads/CollegeData-main/HugeCSV/MERGED2018_19_PP.csv"
    f = open("names.txt", "w+")

    with open(fn, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)

        name_i = header.index("INSTNM")
        aname_i = header.index("ALIAS")

        for row in csv_reader:
            name = row[name_i]
            f.write(name + "\n")

            for name in row[aname_i].split("|"):
                name = name.strip().lower()
                if name != "" and name != "null":
                    pass
                    #f.write(name + "\n")

    f.close()

def getNames():
    fn = "/home/mason/Downloads/CollegeData-main/src/names.txt"

    f = open(fn, "r")
    names = []

    for name in f.read().split("\n"):
        name = "".join([c for c in name if c.isalpha() or c == " "]).lower() + "."
        name = name.replace("  ", " ").replace("  ", " ")
        names.append(name)

    return names

# def makeEncoder(names, pairs, pct):
#     encoder = Encoder(pairs, pct_bpe=pct, required_tokens=[".", "-"])
#     encoder.fit(names)
#     encoder.save("model/bpe.json")
#
# def loadEncoder(fn):
#     encoder = Encoder.load(fn)
#     return encoder

collectNames()
names = getNames()
#
# makeEncoder(names, 200, 1)
# encoder = loadEncoder("model/bpe.json")

char_to_index = dict([ (v, i) for i, v in enumerate(list(set("".join(names))))])
index_to_char = dict( [ (v, k) for k, v in char_to_index.items()] )

max_char = min(len(max(names, key=len)), 75)
m = len(names)
char_dim = len(char_to_index)

con = { "cti" : char_to_index, "max_char" : max_char, "char_dim" : char_dim }

import json

with open("model/config.json", 'w') as fout:
    json.dump(con, fout, indent=4)


print(m, max_char, char_dim)

X = np.zeros((m, max_char, char_dim))
Y = np.zeros((m, max_char, char_dim))

for i, name in enumerate(names):
    for j, c in enumerate(name):
        if j < max_char:
            X[i, j, char_to_index[c]] = 1
            if j < len(name) - 1:
                Y[i, j, char_to_index[name[j + 1]]] = 1

model = Sequential()
model.add(GRU(128, input_shape=(max_char, char_dim), return_sequences=True))
model.add(Dense(char_dim, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')


def make_name(model):

    name = []
    x = np.zeros((1, max_char, char_dim))

    i = 0

    while i < max_char - 1:
        probs = list(model.predict(x)[0,i])
        probs = probs / np.sum(probs)
        id = np.random.choice(range(char_dim), p=probs)
        char = index_to_char[id]
        if char == '.':
            break

        name.append(char)
        x[0, i + 1, id] = 1
        i += 1

    print("".join(name))


def generate_name_loop(epoch, _):
    if epoch % 5 == 0:

        print('Names generated after epoch %d:' % epoch)

        for i in range(3):
            make_name(model)

        model.save('model/')
        print()

name_generator = LambdaCallback(on_epoch_end = generate_name_loop)

model.fit(X, Y, batch_size=64, epochs=30, callbacks=[name_generator], verbose=0)

model.save('model/')
