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

def confirm_correct():
   count=0.0
   countlines=0.0
   analogydataset = loadGoldData(files_op)

   for value in analogydataset:
       #if(value[6]==word):
        similarityrating=value[5]
        originalRating=value[4]
        if (originalRating >= '4.0'):
            countlines+=1
            if similarityrating >= '0.65':
                count+=1
   print(count/countlines)

def confirm_wrong():
   count=0.0
   countlines=0.0
   analogydataset = loadGoldData(files_op)

   for value in analogydataset:
       #if(value[6]==word):
        similarityrating=value[5]
        originalRating=value[4]
        if (originalRating <= '2.0'):
            countlines+=1
            if similarityrating <= '0.20':
                count+=1
   print(count/countlines)

if __name__ == '__main__':

    files_op ="input_file"
    confirm_correct()
    confirm_wrong()