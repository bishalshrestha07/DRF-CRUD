from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer


def student_api(request):
  if request.method == 'GET':
    # storing the json data from third party request to json_data
    json_data = request.body
    stream = io.BytesIO(json_data)
    #converting json into python dictionary
    pythondata = JSONParser().parse(stream)
    # put id= id if there is id if not then id=None
    id = pythondata.get('id',None)
    
    if id is not None:
      # fetching the student object with id
      stu = Student.objects.get(id=id)
      # convert complex student(object) instance to the python native data type i.e. python dictionary
      serialized_data = StudentSerializer(stu)
      #converting python dictionary to json
      json_data = JSONRenderer().render(serialized_data.data)
      return HttpResponse(json_data,content_type='application/json')
    
    stu = Student.objects.all()
    serialized_data = StudentSerializer(stu,many=True)
    json_data = JSONRenderer().render(serialized_data.data)
    return HttpResponse(json_data,content_type='application/json')