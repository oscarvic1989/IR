'''
Created on Dec 3, 2016

@author: oscar
'''
import json
from collections import defaultdict
import math
import collections

print("Loading frequenceJsonObject...")
filestream1=open('Frequence.txt', "r")
frequenceJsonObject = json.loads(filestream1.read())
filestream1.close()
print("frequenceJsonObject load finish")

print("Loading IndexJsonObject...")
filestream1=open('AllIndex.txt', "r")
indexJsonObject = json.loads(filestream1.read())
filestream1.close()
print("IndexJsonObject load finish")

print("Loading LengthJsonObject...")
filestream1=open('Length.txt', "r")
LengthJsonObject = json.loads(filestream1.read())
filestream1.close()
print("LengthJsonObject load finish")

DYdictionary=defaultdict(list)

def calculateTf_Idf(term, doc):
    term1 = frequenceJsonObject[doc][term] / LengthJsonObject[doc] +1
    term2 = math.log10(1425/len(indexJsonObject[term]))+1
    total = term1 * term2
    if term2 <0 :
        print("term1 is "+str(term1)) 
        print("term2 is "+str(term2))
        print("total is "+str(total))
    return total
    
for a in indexJsonObject:
    for i in range(len(indexJsonObject[a])):
        tempWeight = calculateTf_Idf(a,indexJsonObject[a][i])
        DYdictionary[a].append([indexJsonObject[a][i],tempWeight]);

sorted_x = collections.OrderedDict(sorted(DYdictionary.items()))  
filestreamoutput=open("tf_idf.txt", "w")
finaltext=unicode(json.dumps(sorted_x, ensure_ascii=False)).encode('utf-8')
filestreamoutput.write(finaltext)
filestreamoutput.close()
DYdictionary.clear()