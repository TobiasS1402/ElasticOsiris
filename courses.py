#POST request against hu.osiris-student.nl/student/osiris/student/cursussen/zoeken to export all courses from the Elastic back-end
#Made by Tobias
import json

'''
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

write.close()
f.close()
'''

insertsql = []
testdict = {}
count = 0

ddl = open('stutor.sql', 'w+')

f = open('result.json')
test = json.load(f)

templist = []
for key,value in test.items():
    templist.append(value)
templist = list(dict.fromkeys(templist))

for x in templist:
    count = count + 1
    testdict.update({count:x})
    ddl.write('INSERT INTO "Studies" ("_id", "name") VALUES')
    ddl.write("("+str(count) + ","+ f"'{x}'" +");\n")

templist.clear()
count = 0

for key,value in test.items():
    test1 = value
    test2 = key
    for key,value in testdict.items():
        if test1 == value:
            count = count + 1
            ddl.write('INSERT INTO "Courses" ("_id", "name", "studyId") VALUES ')
            ddl.write("("+str(count) + ","+ f"'{test2}'" + "," + str(key) + ");\n")

f.close()
ddl.close()