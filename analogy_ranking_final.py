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
            simGold.append(correctedsplits)
        return simGold

def ranking():
   duplicatecount=0.0
   count=0.0
   countlines=0.0
   previouscheckvalue=0.0
   total=0.0
   analogydataset = loadGoldData(files_op)
   nextval = 0

   for value in analogydataset:
       #if(value[6]==word):
        similarityrating=value[5]
        countlines+=1
        originalRating=value[4]
        originalcheckvalue=value[0]
        if (originalRating >= '4.5' and similarityrating >= '0.70'):
                 count+=1
                 if(previouscheckvalue==originalcheckvalue):
                     count=duplicatecount

                 duplicatecount=count
                 previouscheckvalue=originalcheckvalue
        #print(originalcheckvalue)
        if nextval!=originalcheckvalue:
            #print(nextval,originalcheckvalue)
            total+=1
        nextval = originalcheckvalue

   print(count,total)

if __name__ == '__main__':

    #word = "Property_name"
    files_op ="input_file"
    ranking()