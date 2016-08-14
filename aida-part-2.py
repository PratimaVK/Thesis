def comparison(out,input,aida):
   with open(out, 'w') as o:
    with open(aida, 'r') as a:
      lines = a.readlines()
      j = 0
      while j < len(lines):
            line = lines[j].strip()
            j += 1
            splits1 = line.split(" ")
            correctedsplits1 = [ ]
            correctedsplits1.append(splits1[0])
            correctedsplits1.append(splits1[1])
            correctedsplits1.append(splits1[2])

            c10=int(correctedsplits1[0])
            c11=int(correctedsplits1[1])
            c12=correctedsplits1[2]

            with open(input,'r') as i:
                l=i.read()
                #for k in enumerate(l):
                    #print(k)
                if(j < len(lines)):
                    line2 = lines[j].strip()
                    splits2 = line2.split(" ")
                    correctedsplits2 = [ ]
                    correctedsplits2.append(splits2[0])
                    correctedsplits2.append(splits2[1])
                    correctedsplits2.append(splits2[2])
                    c20=int(correctedsplits2[0])
                    c21=int(correctedsplits2[1])
                    c22=correctedsplits2[2]
                    #print(c12 + " " + l[c11:c20] + " " + l[c21:c10])
                    o.write(c12 + " " + l[c11:c20] + " " + l[c21:c10])
                    if(j==len(lines)-1):
                        o.write(c22 + ".")

            i.close()
    a.close()
   o.close()

if __name__ == '__main__':
    import sys
    print(sys.argv)
    comparison(sys.argv[0],sys.argv[1],sys.argv[2])
