from __future__ import unicode_literals

import os

from datetime import datetime

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

FILEUPLOADPATH = os.path.join(settings.MEDIA_ROOT, settings.MEDIA_URL)
	
def user_directory_path(instance, filename):
	#import pdb;pdb.set_trace()
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	#return 'user_{0}/{1}'.format(instance.user.id, filename) 
	return 'user_{0}/{1}'.format('admin', filename) 

class Rule(models.Model):
	rulename = models.CharField("rulename", max_length=30, unique=True)
	datafile = models.FileField(max_length=10000)
	filelocation = models.CharField("filelocation", max_length=255, default=True)
	created = models.DateTimeField(auto_now_add=True)
	#scheduler = models.ForeignKey('RuleScheduler', related_name='rules', on_delete=models.CASCADE, null=False, blank=False)
	#schedulertime = models.TimeField('schedulertime', default=datetime.now)
	hours = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])
	minutes = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(60)])
        schedulertype = models.CharField("schedulertype", max_length=20)
	

	class Meta:
		db_table = 'rules'


#class RuleScheduler(models.Model):
#	schedulertime = models.DateTimeField('schedulertime', default=datetime.now)
#        schedulertype = models.CharField("schedulertype", max_length=20)
#
#	class Meta:
#		db_table = 'rulescheduler'


class RuleExecutionSummary(models.Model):
	rulename = models.CharField("rulename", max_length=30) 
	ruleid = models.PositiveIntegerField("ruleid")
	starttime = models.DateTimeField("starttime", default=datetime.now)
	stoptime = models.DateTimeField("stoptime", default=datetime.now)
	status = models.CharField("status", max_length=20)
	filelocation = models.CharField("filelocation", max_length=255)
	error_message = models.CharField("error_message", max_length=255)
	
	class Meta:
		db_table = "ruleexecutionsummary"
