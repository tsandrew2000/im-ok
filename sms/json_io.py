import json


def writeToJSONFile(filename, data):
    with open(filename, 'w+') as jf:
        jf.write(json.dumps(data, indent=4, sort_keys=True))


def readFromJSONFile(jsonfile, txtfile):
    doc = {}
    with open(txtfile, 'w') as tf:
        with open(jsonfile, 'r') as jf:
            for line in jf:
                doc = (json.load(line))


JSONFILE = "sms/contacts.json"
TXTFILE = "sms/contacts.txt"

data_out = {"Contacts": [{"Luis Gonzalez":
                          {"phone":
                           "+19393976360"
                           },
                          "Fernando Gonzalez":
                          {"phone":
                              "+17876675396"
                           }
                          }
                         ]
            }

writeToJSONFile(JSONFILE, data_out)
readFromJSONFile(JSONFILE, TXTFILE)
