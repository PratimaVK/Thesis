import csv
from gensim.models import word2vec
import Levenshtein
from unicodedata import normalize
import w2vAida

def loadGoldData(dataset):
    with open(dataset, 'r') as file:
        lines = file.readlines()
        simGold = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            i += 1
            if line.startswith(":"):
                continue
            if line.startswith("\n"):
                i += 1
                continue
            splits = line.split(",")
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

def find_nsim():
    model=w2vAida.Word2Vec.load_word2vec_format(trainedModel, binary=True)

    with open(files_op, 'w') as csvs:
        for value in analogydataset:
            similarityRating = model.n_similarity_new([value[0], value[1]],[value[2],value[3]])
            #csvs.write(value[0]+' '+value[1]+' '+value[2]+' '+value[3]+' '+value[4]+' '+str(similarityRating)+'\n')
            csvs.write(value[0]+' '+value[1]+' '+value[2]+' '+value[3]+' '+value[4]+' '+str(similarityRating)+' '+value[5]+' '+value[6]+' '+value[7]+'\n')
    csvs.close()

if __name__ == '__main__':

    dataset="input_file"
    analogydataset = loadGoldData(dataset)
    trainedModel = "model.bin"
    files_op ="output_file"
    find_nsim()