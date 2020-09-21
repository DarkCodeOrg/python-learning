# this program depicts the use of dictionaries in python

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