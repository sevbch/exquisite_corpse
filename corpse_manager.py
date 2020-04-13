import pandas as pd
import numpy as np


class CorpseManager:
    def __init__(self, data_file):
        data = pd.read_csv(data_file)
        self.vocabulary = {}
        self.retrieve_voc(data)
        self.vocabulary['object'] += self.vocabulary['subject']

    def generate(self):
        subject = self.get_random('subject').capitalize()
        verb = self.get_random('verb')
        obj = self.get_random('object')
        while obj == subject:
            obj = self.get_random('object')
        sentence = [subject, verb, obj]
        r = np.random.rand()
        if r < 0.25:
            adverb = self.get_random('adverb')
            sentence.insert(2, adverb)
        return ' '.join(sentence) + '. #CadavreExquis'

    def get_random(self, voc_type):
        return str(np.random.choice(self.vocabulary[voc_type]))

    def retrieve_voc(self, data):
        for col_name in data.columns:
            voc = data[col_name].dropna().drop_duplicates().tolist()
            for i in range(len(voc)):
                voc[i] = str(voc[i]).strip()
                if len(voc[i]) == 0:
                    del voc[i]
                    continue
                voc[i] = voc[i][0].lower() + voc[i][1:]
            self.vocabulary[col_name] = voc
