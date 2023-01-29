import tensorflow_hub as hub

module_url = "https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/1"
#module_url = "https://tfhub.dev/tensorflow/bert_en_uncased_L-24_H-1024_A-16/1"

import pandas as pd

train = pd.read_csv("data/letters.csv")
test = pd.read_csv("data/letters.csv")#TODO

bert_layer = hub.KerasLayer(module_url, trainable=True)

train.head(3)