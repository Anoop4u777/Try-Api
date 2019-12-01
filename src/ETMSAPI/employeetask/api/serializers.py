from rest_framework import serializers

from employeetask.models import EmployeeTask

class EmployeeTaskSerializers(serializers.ModelSerializer):
	user = serializers.CharField(source='user.username', read_only=True)
	date = serializers.DateField(format="%d-%m-%Y",)
	time = serializers.TimeField(format='%I:%M %p',)
	class Meta:
		model 	= EmployeeTask
		fields	= [
				'pk',
				'user',
				'task_id',
				'section',
				'task_details',
				'date',
				'time',	
				]
		read_only_fields = ['pk', 'user', 'date','time',]


	def validate_task_id(self, value):
		qs = EmployeeTask.objects.filter(task_id = value)
		if qs.exists():
			raise serializers.ValidationError('This task id already exists please enter a the latest task id')
		return value