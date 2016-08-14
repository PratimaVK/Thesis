__author__ = 'PRAT'

import pandas as pd
import os
from nltk.corpus import stopwords
import nltk.data
import numpy as np  # Make sure that numpy is imported
import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                    level=logging.INFO)

sentences = word2vec.Text8Corpus('input_file')
model = word2vec.Word2Vec(sentences,size=200, workers=15,sg=1,negative=10,cbow_mean=0,hs=0,window=10,min_count=3,sample=1e-5,alpha=0.025,iter=2)
model.save_word2vec_format('output_file', binary=True)

