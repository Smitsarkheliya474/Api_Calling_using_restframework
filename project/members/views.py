'''from members.models import Employee
from members.serializers import EmplSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmpList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        r1 = Employee.objects.all()
        serializer = EmplSerializers(r1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmplSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class EmpDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        r1 = self.get_object(pk)
        serializer = EmplSerializers(r1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        r1 = self.get_object(pk)
        serializer = EmplSerializers(r1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
         
from members.models import Employee
from members.serializers import EmplSerializers
from rest_framework import mixins
from rest_framework import generics

class EmpList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmplSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmpDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmplSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)       
'''from members.models import Employee
from members.serializers import EmplSerializers
from rest_framework import generics


class EmpList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmplSerializers
    
class EmpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmplSerializers'''