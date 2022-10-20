# Lesson 31 JSON

import json

data = '''{
    "key1": "string val",
    "key2": {
        "sub_key1": 8
    },
    "key3": ["array", 2]
}'''
info = json.loads(data)
print(type(info)) # <class 'dict'>
print(info)
for k,v in info.items() :
    print(k,v)


data2 = '''[
    {
        "key1": "val1",
        "key2": 2
    },
    {
        "key1": "val2.1",
        "key2": 2 
    }
]'''
info2 = json.loads(data2)
print(type(info2)) # <class 'list'>
print(info2)
for obj in info2 :
    print(obj)