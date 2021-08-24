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

# get_data()

def post_data():
  data = {
    'name': 'Sanish',
    'roll': 36,
    'city':'Pokhara'
  }

  json_data = json.dumps(data)
  res = requests.post(url = URL, data = json_data)
  data = res.json()
  print(data)

# post_data()

def update_data():
  data = {
    'id':4,
    'name': 'Bishal Thapa',
    'roll': 14,
  }

  json_data = json.dumps(data)
  res = requests.put(url = URL, data = json_data)
  data = res.json()
  print(data)

# update_data()

def delete_data():
  data = {
    'id':2
  }

  json_data = json.dumps(data)
  res = requests.delete(url = URL, data = json_data)
  data = res.json()
  print(data)

delete_data()