import requests

BASE = "http://127.0.0.1:5000/"

#data = [
#  {"likes": 150, "name": "Brim", "views": 50000},
#  {"likes": 10, "name": "Tim", "views": 100000},
#  {"likes": 1000, "name": "Hazel", "views": 500}
#]

response = requests.patch(BASE + "video/1", {"views":20})
print(response.json())

#for i in range(len(data)):
#  response = requests.put(BASE + "video/" + str(i), data[i])
#  print(response.json())
  
#input()

#response = requests.get(BASE + "video/0")
#print(response.json())