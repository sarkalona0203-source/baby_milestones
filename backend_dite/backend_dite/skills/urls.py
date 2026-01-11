from django.urls import path
from .views import SkillListView  # Импортируйте ваше представление

urlpatterns = [
    path('', SkillListView.as_view(), name='skills-list'),
]