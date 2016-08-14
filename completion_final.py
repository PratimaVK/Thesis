import csv
from gensim.models import word2vec
import Levenshtein
from unicodedata import normalize
import w2vAida
from nltk.corpus import wordnet as wn

def loadGoldData(dataset):
    with open(dataset, 'r') as file:
        lines = file.readlines()
        simGold = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            i += 1
            if line.startswith("#"):
                continue
            if line.startswith("\n"):
                i += 1
                continue
            splits = line.split(" ")
            correctedsplits = [ ]
            correctedsplits.append(splits[0])
            correctedsplits.append(splits[1])
            correctedsplits.append(splits[2])
            correctedsplits.append(splits[3])
            correctedsplits.append(splits[4])
            correctedsplits.append(splits[5])
            correctedsplits.append(splits[6])
            correctedsplits.append(splits[7])
            correctedsplits.append(splits[8])
            correctedsplits.append(splits[9])
            simGold.append(correctedsplits)
        return simGold

def analogyCompletion_new():
   model=w2vAida.Word2Vec.load_word2vec_format(trainedModel, binary=True)
   count=0.0
   countlines=0.0
   analogy = loadGoldData(files_op)

   for value in analogy:
    #temp=model.most_similar(positive=[value[2], value[1]], negative=[value[0]],topn=1)
    #if(value[9]==word):
        PredictedResult=value[3]
        originalRating=value[4]
        if originalRating >= str(3.5):
            countlines+=1
        similarityvalue=value[5]
        similarityRating= value[6]
        print(PredictedResult,originalRating,similarityvalue,similarityRating)
        w1 = PredictedResult
        w2 = similarityvalue
        s1 = wn.synsets(w1)
        s2 = wn.synsets(w2)
        if not s2 or not s1:
            print(" W2V ")
            m1 = model.similarity_new(one=[PredictedResult],two=[similarityvalue])
            m2 = 0.0
        else:
            print(" WNet ")
            ss1 = s1[0]
            ss2 = s2[0]
            m2 = (ss1.wup_similarity(ss2, simulate_root=False))
            if m2==None:
                m2 = 0.0
                m1 = model.similarity_new(one=[PredictedResult],two=[similarityvalue])
            else:
                m1 = 0.0
        if m1!=0.0:
            print(m1)
            if (float(originalRating) >= 3.5 and float(similarityRating) >= 0.65 and float(m1) >=0.70):
                count+=1
        elif m2!=0.0:
            print(m2)
            if (float(originalRating) >= 3.5 and float(similarityRating) >= 0.65 and float(m2) >=0.70):
                count+=1

        percentage=count/countlines
        score = percentage*100
        print('  LINES  ',count,countlines)
        print('  Score  ',score)

if __name__ == '__main__':

    trainedModel = "model.bin"
    files_op ="output_file"
    analogyCompletion_new()