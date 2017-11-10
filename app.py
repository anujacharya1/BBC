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
    
class Subset(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
          
class Roast(object):
     
    def __init__(self, name, initialValue, remainingValue):
            self.name = name
            self.initialValue = initialValue    
            self.remainingValue = remainingValue
            self.subset = {}
     
    def getName(self):
        return self.name 
     
    def getInitValue(self):
        return self.initialValue   
     
    def getRemainingValue(self):
        return self.remainingValue 
    
    def addToSubset(self, v):
        
        if self.subset.has_key(v.name):
                self.subset[v.name] += v.value
        else:
            self.subset[v.name] = v.value

            
@app.route('/')
def bbc():
    roast = request.args.get('roast')
    roastList = [int(x) for x in roast.split(",")]
    
    roastObjList = []
    for i,x in enumerate(roastList):
        roastObjList.append(Roast('ROAST '+str(i+1), x, x))
        
    subset = request.args.get('subset')
    subsetList =  [int(x) for x in subset.split(",")]
    
    subsetObjList = []
    for i,x in enumerate(subsetList):
        subsetObjList.append(Subset('SUBSET '+str(i+1), x))
        
    # sort decending
    subsetObjList.sort(key=lambda subsetObjList: subsetObjList.value, reverse=True)

    
    roastingTotal = sum(roastList)
    subsetListTotal = sum(subsetList)
    if(roastingTotal != subsetListTotal):
        return jsonify(result='Total Mismatch, Ensure that the roast total is matching subset total roast='+str(roastingTotal)+' subset='+str(subsetListTotal))    
          
    while(roastingTotal!=0):
        
        # sort roast in decending
        roastObjList.sort(key=lambda roastObjList: roastObjList.remainingValue, reverse=True)

        for i, roast in enumerate(roastObjList):
            newList = []
            # so
            for s in subsetObjList:
                if(roast.remainingValue >= s.value):
                    roast.remainingValue-=s.value
                    roastingTotal-=s.value
                    roast.addToSubset(s)
                    newList.append(s)
                    if roast.remainingValue == 0:
                        break
                else:
                    break
            
            # Update subset removing the processed one
            subsetObjList = [x for x in subsetObjList if x not in newList]
    
        if(roastingTotal!=0):
            # Deduct 1 lb from bag and try to find again, try with minimum bags each
            subsetObjList[0].value-=1
            subsetObjList.append(Subset(subsetObjList[0].name, 1))
            subsetObjList.sort(key=lambda subsetObjList: subsetObjList.value, reverse=True)
    
    jsonResult = list()
    for roast in roastObjList:
        jsonResult.append({'RoastName':roast.name,
                   'RoastCapacity':roast.initialValue,
                   'Subset':roast.subset})
        

    return Response(json.dumps(jsonResult),  mimetype='application/json')

    
if __name__ == '__main__':
    app.run()  