from django.db import models


PRIORITY = [
	('H', 'High'),
	('M', 'Medium'),
	('L', 'Low'),
]

class Question(models.Model):
	"""docstring for Question"""

	title = models.CharField(max_length=70)
	question = models.TextField(max_length=5000)
	priority = models.CharField(max_length=3, choices=PRIORITY)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'The question'
		verbose_name_plural = "Poepole's questions"