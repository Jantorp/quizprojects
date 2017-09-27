#Rätt URL:s med rätt vyer. Alltså visa rätt sida när URL har ett visst värde.

from django.urls import path
from quiz import views

urlpatterns = [
	path("",views.startpage, name="start_page"),
	path("quiz/<int:quiz_number>/",views.quiz, name="quiz_page"),
	path("quiz/<int:quiz_number>/question/<int:question_number>/", views.question, name="question_page"),
	path("quiz/<int:quiz_number>/completed/", views.completed, name="completed_page"),
]

