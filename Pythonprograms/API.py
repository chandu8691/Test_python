import requests
import json
# r=requests.get("https://imgs.xkcd.com/comics/circuit_diagram.png")
# print(r)
# print(r.status_code)
# f=open("D:\Pythonprograms\sample.png","wb")
# f.write(r.content)
# print(r.content)
# f.close()



parm={"page":2,"count":4}
r=requests.get("http://httpbin.org/#/HTTP_Methods/get_get",params=parm)
print(r.status_code)
print(r.text,type(r.text))
json_data=json.loads(r.text) #convert text to dict format using loads
print(json_data)
# print(type(json_data))
# print(r.json(),type(r(json)))#covert the text to dict format with json()



