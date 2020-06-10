from django.urls import path
from store import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail')
]
