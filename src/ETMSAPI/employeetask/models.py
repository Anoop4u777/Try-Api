from django.conf import settings
from django.db import models

# Create your models here.
class EmployeeTask(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	task_id 		= models.IntegerField()
	section			= models.CharField(max_length = 50)
	task_details	= models.TextField(max_length = 50)
	date 			= models.DateField(auto_now_add = True, blank = True)
	time 			= models.TimeField(auto_now_add = True, blank = True)

	def __str__(self):
		return str(self.task_id)