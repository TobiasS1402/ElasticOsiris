#POST request against hu.osiris-student.nl/student/osiris/student/cursussen/zoeken to export all courses from the Elastic back-end
#Made by Tobias
import json

f = open('input.json')
data = json.load(f)

studies = []
courses = []
dict = {}


for x in data['hits']['hits']:
    studies.append(x['_source']['coordinerend_onderdeel_oms'])
    courses.append(x['_source']['cursus_lange_naam'])

for key,value in zip(courses, studies):
    dict[key] = value

with open('result.json', 'w+') as write:
    json.dump(dict, write)

id = 0
templist = []
tempdict = {}

for key,value in dict.items():
    templist.append(value)
templist = list(dict.fromkeys(templist))

templist.clear

print(templist)
