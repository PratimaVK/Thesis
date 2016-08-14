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
            if line.startswith(":"):
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
            simGold.append(correctedsplits)
            #print(correctedsplits)
        return simGold

def analogyCapture():
    model=w2vAida.Word2Vec.load_word2vec_format(trainedModel, binary=True)
    analogydataset = loadGoldData(dataset)

    with open(files_op, 'w') as csvs:
        for value in analogydataset:
            temp = model.most_similar_new(positive=[value[2], value[1]], negative=[value[0]],topn=1)
            for values in temp:
                if ':' in values[0]:
                    v = values[0]
                    v1 = v.split(':')
                    similarityvalue=v1[0]
                else:
                    similarityvalue=values[0]
                #csvs.write(value[0]+' '+value[1]+' '+value[2]+' '+value[3]+' ' +similarityvalue+' '+str(values[1])+'\n')
                csvs.write(value[0]+' '+value[1]+' '+value[2]+' '+value[3]+' '+value[4]+' '+similarityvalue+' '+str(values[1])+' '+value[5]+' '+value[6]+' '+value[7]+'\n')
    csvs.close()

if __name__ == '__main__':

    dataset="input_file"
    trainedModel = "model.bin"
    files_op ="output_file"
    analogyCapture()