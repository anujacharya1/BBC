# BBC

## Overview
This is the sample code that take roast and subset and give the result
=======

## APPROACH
* Understand the problem and clarify the requirements about the roast and subset and have a clear restriction in place
* Try to come up with the basic understanding of the problem and try to match with the similar problem solved in past "change machine problem" is one example
* It's a little bit varian of change machine problem; in which the the number of subset in each iterations changes as well along with the roast
* Try to think what kind of Algorithm is best suited, the best suited Algorithm for this kind of probem is recursion as after each recursion the same problem need to be solved again
* Come up with the Algorithm that is brute force i.e. think on white paper
* Test the approach of Algorthm with different use case and validate that the requirments would be meet
* Come up with the API specification
* Code the algorithm in Python using Flask as it's lightweight framework
* Deploy on heroku as it's easy to scale instances depending on the traffic and infuture can support multiple plugins for database
* Test and run different use case


## API

### Request Type : GET
### URL: https://bbc-flask-app.herokuapp.com/?roast=2,2,2&subset=4,2

### Query Parameters:

roast: Comma Seperated whole numbers value of roast

subset: Comma seperate subsets


### Sample Response:
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


## Restriction
* Total of Roast and Subset should match
* Can have any number of roast or subset
* No fraction

