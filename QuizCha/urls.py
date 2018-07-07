from django.urls import path
from QuizCha import views as Quiz


urlpatterns = [
   path('', Quiz.quiz),

   
]