from django.db import models

# Create your models here.
class WorkDetail(models.Model):
	TYPES = (
		('Frontend','Forntend'),
		('Backend','Backend'),
		('Database','Database'),
		('FullStack','FullStack'),
		)
	project = models.CharField(max_length=120)
	project_type = models.CharField(max_length = 40, choices=TYPES)
	duration = models.IntegerField()
	is_complete = models.BooleanField(default = False)


	def __str__(self):
		return self.project

