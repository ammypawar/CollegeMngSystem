from django.db import models


class Institute(models.Model):
	reg_no = models.IntegerField()
	uni_soc_name = models.CharField(max_length=100)
	institute_name = models.CharField(max_length=100)
	mobile = models.CharField(max_length=12)
	email = models.EmailField()
	address = models.TextField(default='')
	url = models.URLField(max_length=200, blank=True, help_text="e.g. http://www.something@example.com (optional)")

	def __unicode__(self):
		return self.institute_name