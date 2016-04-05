from django.db import models

# Create your models here.

class Question(models.Model):
	question_text=models.CharField(max_length=50)
	pub_date=models.DateTimeField('date published')

	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
	question=models.ForeignKey(Question)
	choice_text=models.CharField(max_length=50)
	votes=models.IntegerField(default=0)
		
class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()


