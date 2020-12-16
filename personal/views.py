from django.shortcuts import render
from personal.models import Question

def home(request):
	questions = Question.objects.all()
	context = {
		"title": "StartGreat",
		"heder_title": "La productivité",
		"questions": questions,
	}
	print(request.headers)
	return render(request, 'personal/home.html', context)