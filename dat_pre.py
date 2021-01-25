import pandas as pd
from pprint import pprint

train_dat=pd.read_csv("dat\\train.tsv",sep="\t")
x=train_dat["SentenceId"]==1
y=train_dat["PhraseId"]==1
pprint (train_dat.values)