'''
Created on Nov 8, 2017

@author: anujacharya
'''
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
import json

app = Flask(__name__)

'''
http://127.0.0.1:5000/?roast=30,20&subset=10,17,12,7,4
'''
    
class Roast(object):
     
    def __init__(self, name, initialValue, remainingValue):
            self.name = name
            self.initialValue = initialValue    
            self.remainingValue = remainingValue
            self.subset = list()
     
    def getName(self):
        return self.name 
     
    def getInitValue(self):
        return self.initialValue   
     
    def getRemainingValue(self):
        return self.remainingValue 
    
    def addToSubset(self, v):
        return self.subset.append(v) 

def process(roast, subset, result):
    
    roastResult = roast
    result[roastResult] = list()

    newlist = []
    for s in subset:
        if(roast >= s):
            roast-=s
            result[roastResult].append(s)
            if roast == 0:
                break
        else:
            newlist.append(s)
 
    subset = newlist
    return
            
@app.route('/')
def bbc():
    roast = request.args.get('roast')
    roastList = [int(x) for x in roast.split(",")]
    
    roastObjList = []
    for i,x in enumerate(roastList):
        roastObjList.append(Roast('ROAST '+str(i+1), x, x))
#     roastObjList.sort(key=lambda roastObjList: roastObjList.initialValue, reverse=True)

    print roastList
        
    subset = request.args.get('subset')
    subsetList =  [int(x) for x in subset.split(",")]
    subsetList.sort(reverse=True)
    print subsetList
    
    roastingLeft = sum(roast.remainingValue for roast in roastObjList)


    if(roastingLeft != sum(subsetList)):
        return jsonify(result='INPUT ERROR')    
    
#     while(totalRoasted!=0):
      
    while(roastingLeft!=0):
        
        roastObjList.sort(key=lambda roastObjList: roastObjList.remainingValue, reverse=True)

        for i, roast in enumerate(roastObjList):
            
#             roastTemp = roast.getInitValue()
#             result[roastTemp] = list()
        
            newList = []
            for s in subsetList:
                if(roast.remainingValue >= s):
                    roast.remainingValue-=s
                    roastingLeft-=s
                    roast.addToSubset(s)
                    newList.append(s)
                    if roast.remainingValue == 0:
                        break
                else:
                    break
            
            subsetList = [x for x in subsetList if x not in newList]
    
        if(roastingLeft!=0):
            # Create 1 lb bag
            newSubsetValue = subsetList[0]-1
            subsetList[0] = newSubsetValue;
            subsetList.append(1)
            subsetList.sort(reverse=True)

#     print 'new sublist'+str(subsetList)
#     print 'roast'+str(roastList)    
#     print 'totalRoasted'+str(roastingLeft)
    
#         process(roast, subsetList, result)
    
    jsonResult = list()
    for roast in roastObjList:
        jsonResult.append({'RoastName':roast.name,
                   'RoastCapacity':roast.initialValue,
                   'Subset':roast.subset})
        

    return Response(json.dumps(jsonResult),  mimetype='application/json')

    
if __name__ == '__main__':
    app.run()  