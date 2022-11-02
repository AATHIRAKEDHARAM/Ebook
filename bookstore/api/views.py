from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User





# Create your views here.
class UserRegister(APIView):
    

    def post(self,request):
        
        serializer=RegisterSerializer(data=request.data)
        
        data={}
        if serializer.is_valid():
            user = User.objects.create_user(username=request.data['username'],password=request.data['password'])
            user.save()

            serializer.save()
            data["message"]="registered"
            data["data"]=serializer.data
            print(serializer.data)
        else:
            data=serializer.errors
        return Response(data)





