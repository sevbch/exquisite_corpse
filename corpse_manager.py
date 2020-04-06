import pandas as pd
import numpy as np


class CorpseManager:
    def __init__(self, data_file):
        data = pd.read_csv(data_file)
        subject = data.subject.tolist()
        verb = data.verb.tolist()
        adverb = data.adverb.tolist()
        object = subject + data.object.tolist()
        self.vocabulary = {'subject': subject, 'verb': verb, 'adverb': adverb, 'object': object}
        self.clean_voc()

    def generate(self):
        r = np.random.rand()
        subject = self.get_random('subject')
        sentence = subject + \
                   " " + self.get_random('verb')
        if r < 0.25:
            sentence += " " + self.get_random('adverb')
        object = self.get_random('object')
        if object == subject:
            object = self.get_random('object')
        sentence += " " + object
        return sentence

    def get_random(self, voc_type):
        val = str(np.random.choice(self.vocabulary[voc_type]))
        while val == "nan":
            val = str(np.random.choice(self.vocabulary[voc_type]))
        return val

    def clean_voc(self):
        for l in self.vocabulary.values():
            assert isinstance(l, list)
            while 'nan' in l:
                l.remove('nan')
            check_duplicate = []
            for item in l:
                if item in check_duplicate:
                    l.remove(item)
                    continue
                check_duplicate.append(item)
                if str(item)[-1] == ' ':
                    item = str(item)[:-1]
