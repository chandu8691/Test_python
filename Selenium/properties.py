# from pyjavaproperties import Properties
#
# p=Properties()
# p.load(open("C:\\Users\\kodiak\\PycharmProjects\\Test_python\\Selenium\\test.properties"))
# print(p['key'])

import json
with open("C:\\Users\\kodiak\\PycharmProjects\\Test_python\\Selenium\\abc.json")as f:
    data=json.load(f)
    print(data["details"])
