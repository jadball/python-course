import json


def CreateJSON():
    data = {"Sub_ID": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "Name": ["Erik", "Daniel", "Michael", "Sven",
                     "Gary", "Carol", "Lisa", "Elisabeth"],
            "Salary": ["723.3", "515.2", "621", "731",
                       "844.15", "558", "642.8", "732.5"],
            "StartDate": ["1/1/2011", "7/23/2013", "12/15/2011",
                          "6/11/2013", "3/27/2011", "5/21/2012",
                          "7/30/2013", "6/17/2014"],
            "Department": ["IT", "Manegement", "IT", "HR",
                           "Finance", "IT", "Manegement", "IT"],
            "Sex": ["M", "M", "M",
                    "M", "M", "F", "F", "F"]}
    return data


def WriteJSONtoFile(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


def ReadJSONfromFile():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return data  # dictionary


data = CreateJSON()
WriteJSONtoFile(data)
data2 = ReadJSONfromFile()
print(data2)
