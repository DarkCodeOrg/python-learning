# this program depicts the use of dictionaries in python
import json #json library is imported for the use of the json.dumps feature for better printing of the dictionary 
mydict = {
        'car1'  : {
        "Brand" : "Audi",
        "Model" : "Q4",
        "year"  : 2016
        },

        'car2'  : {
        "Brand" : "Mercedes Benz",
        "Model" : "S-class",
        "year"  : 2014
        },

        'car3'  : {
        "Brand" : "Rolls Royce",
        "Model" : "Ghost",
        "year"  : 2020
        }               
}

print(json.dumps(mydict),indent = 2)