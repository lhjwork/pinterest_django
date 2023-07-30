from django.urls import path

from projectapp.views import ProjectCreateView

app_name= 'projectapp'

urlpatterns = [
    # path('create/', ProfileCreateView.as_view(), name='create'),
    # path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),


    path('create/',ProjectCreateView.as_view(), name='create'),

]