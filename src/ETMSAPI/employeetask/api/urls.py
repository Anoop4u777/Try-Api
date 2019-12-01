from django.conf.urls import url
from .views import (EmployeeTaskListCreateView, 
					EmployeeTaskRudView,
					EmployeeTasks,
					PandasView
					)


from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
urlpatterns = [
		url(r'^(?P<pk>\d+)/$', EmployeeTaskRudView.as_view(), name='detail'),
 		url(r'^$', EmployeeTaskListCreateView.as_view(), name='list'),
 		url(r'^json/$', EmployeeTasks.as_view(), name='emp-task-json'),  	#Renderer classes implimentation	
 		url(r'^excel/$', PandasView.as_view(), name='excel-render'),		#Creating excel file
 		]

