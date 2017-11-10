# BBC

# Overview

# Restriction
* Total of Roast and Subset should match
* Can have any number of roast or subset
* No fraction

API
Request Type : GET
URL: http://<IP_ADDRESS>/?roast=2,2,2&subset=4,2

Query Parameters:
roast: Comma Seperated whole numbers of 
subset: Comma seperate subsets


Sample Response:

[
{
"Subset": {
"SUBSET 1": 2
},
"RoastCapacity": 2,
"RoastName": "ROAST 1"
},
{
"Subset": {
"SUBSET 2": 2
},
"RoastCapacity": 2,
"RoastName": "ROAST 2"
},
{
"Subset": {
"SUBSET 1": 2
},
"RoastCapacity": 2,
"RoastName": "ROAST 3"
}
]
