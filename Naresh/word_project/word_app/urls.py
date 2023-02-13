

from django.urls import path
from . import views

urlpatterns = [
    path('',views.word,name='word list'),
    path('word_count',views.word_count,name='word_count'),
    path('vowel',views.vowel,name='vowel'),
    path('vowel_count',views.vowel_count,name='vowel_count page'),
    path('cons',views.cons,name='cons page'),
    path('cons_count',views.cons_count,name='cons_count page'),
    path('char',views.char,name='char page'),
    path('char_count',views.char_count,name='char_count page'),


]