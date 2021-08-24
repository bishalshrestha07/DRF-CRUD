import requests,json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
  data = {}
  if id is not None:
    data = {'id':id}
  #converting dict into json format
  json_data = json.dumps(data)
  
  res = requests.get(url= URL, data= json_data)#res is response that we get from api which will have json data and httpresponse type etc.
  print(res)
  data = res.json()
  print(data)

get_data()