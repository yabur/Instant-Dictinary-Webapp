import pandas as pd


class Definition:

    def __init__(self, term):
        self.term = term


    def get(self):
        df = pd.read_csv('data.csv')
        definitions = tuple(df.loc[df['word'] == self.term]['definition'])

        return definitions

d = Definition(term='moon')
print(d.get())

