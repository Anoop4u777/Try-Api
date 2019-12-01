from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q


from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_pandas.renderers import PandasExcelRenderer

from rest_pandas import PandasView

from employeetask.models import EmployeeTask
from .serializers import EmployeeTaskSerializers



class EmployeeTaskRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = EmployeeTaskSerializers

	def get_queryset(self):
		return EmployeeTask.objects.filter(user = self.request.user)


class EmployeeTaskListCreateView(mixins.CreateModelMixin, generics.ListAPIView): # Create, List, Search
	lookup_field 		= 'pk'
	serializer_class 	= EmployeeTaskSerializers
	
	def get_queryset(self):
		query 		= EmployeeTask.objects.filter(user = self.request.user)
		search_obj 	= self.request.GET.get('q')
		if search_obj is not None:
			query 	= query.filter(Q(task_id = search_obj)|
								Q(section__iexact = search_obj)
								).distinct()
		return query

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
	
	def perform_create(self, serializer):
		serializer.save(user = self.request.user)


class EmployeeTasks(APIView): #simply created to check renderer_classes
	renderer_classes = [JSONRenderer]
	def get(self, request):
		query = EmployeeTask.objects.filter(user = self.request.user)
		serializer = EmployeeTaskSerializers(query, many = True)
		return Response(serializer.data)


class PandasView(PandasView):
    queryset = EmployeeTask.objects.all()
    serializer_class = EmployeeTaskSerializers
    renderer_classes = [PandasExcelRenderer]


    def filter_queryset(self, qs): 
    	qs = EmployeeTask.objects.filter(user = self.request.user)
        return qs


    def transform_dataframe(self, dataframe):
        return dataframe
    
    
    def get_pandas_filename(self, request, format):
        return None