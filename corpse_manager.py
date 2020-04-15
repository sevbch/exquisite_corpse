import pandas as pd
import numpy as np
import pickle


class CorpseManager:
    def __init__(self, data_csv=None, data_pickle=None):
        if data_csv:
            data = pd.read_csv(data_csv)
            self.vocabulary = {}
            self.retrieve_voc(data)
            self.vocabulary['object'] += self.vocabulary['subject']
        elif data_pickle:
            with open(data_pickle, 'rb') as data:
                self.vocabulary = pickle.Unpickler(data).load()
        else:
            print('Error: please enter a data input.')

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

    def write_pickle(self, data_pickle):
        with open(data_pickle, 'wb') as data:
            pickle.Pickler(data).dump(self.vocabulary)

    def generate(self):
        subject = self.get_random('subject')
        verb = self.get_random('verb')
        obj = self.get_random('object')
        while obj == subject:
            obj = self.get_random('object')
        sentence = [subject[0].upper() + subject[1:], verb, obj]
        r = np.random.rand()
        if r < 0.25:
            adverb = self.get_random('adverb')
            sentence.insert(2, adverb)
        return ' '.join(sentence) + '. #CadavreExquis'

    def get_random(self, voc_type):
        return str(np.random.choice(self.vocabulary[voc_type]))


if __name__ == '__main__':
    file = "exquisite_data.csv"
    corpse = CorpseManager(data_csv=file)
    corpse.write_pickle('data_pickle')
