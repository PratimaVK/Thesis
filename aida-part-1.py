'''import os,mmap
f=os.open("file",os.O_RDWR)
m=mmap.mmap(f,0)
m[0:10]="Steve_Jobs"
#m[16:21]="Apple:Apple_Inc"
os.close(f)

text = "The cat sat on the mat"

text1 = text[:8] + "slept" + text[10:11] + "mop" +text[18:]
text2 = text1[:12] + "mop" + text1[14:]
print (text2)
s = r'Apple_Inc\u002e'
print s
Apple_Inc\u002e
print s.decode('unicode-escape')
Apple_Inc.
'''
import re

def filter(input,output):
    with open(input, 'r') as o:
        with open(output,'w') as m:

            lines = o.readlines()
            j = 0
            while j < len(lines):
                line = lines[j].strip()
                #l=line.replace(" ","_")
                l=re.sub(r'^((.*? .*?){2}) ', r'\1_',line)
                l1=re.sub(r'^((.*? .*?){2}) ', r'\1_',l)
                l2=re.sub(r'^((.*? .*?){2}) ', r'\1_',l1)
                l3=re.sub(r'^((.*? .*?){2}) ', r'\1_',l2)
                l4=re.sub(r'^((.*? .*?){2}) ', r'\1_',l3)
                l5=re.sub(r'^((.*? .*?){2}) ', r'\1_',l4)
                l6=re.sub(r'^((.*? .*?){2}) ', r'\1_',l5)
                l7=re.sub(r'^((.*? .*?){2}) ', r'\1_',l6)
                l8=re.sub(r'^((.*? .*?){2}) ', r'\1_',l7)
                l9=re.sub(r'^((.*? .*?){2}) ', r'\1_',l8)
                l0=re.sub(r'^((.*? .*?){2}) ', r'\1_',l9)
                #l6=l6.decode('unicode-escape')
                #l8 = u' '.join((l8)).encode('utf-8').strip()
                #print(l0)
                j += 1
                if l0.startswith("#"):
                    continue
                if l0.startswith("\n"):
                    j += 1
                    continue
                splits = l0.split(" ")
                m.write(l0+'\n')
            m.close()
        o.close()

if __name__ == '__main__':
    filter('input_file','output_file')

    