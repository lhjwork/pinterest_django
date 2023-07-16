from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name="accountapp"

# "127.0.0.1:8000/account/hello_world.html"
# 나중에는 저기 name으로 accountapp:hello_world.html 라는 식으로 간편하게 하는 함수가 있단다.
urlpatterns = [
    path('hello_world/', hello_world,  name='hello_world'),
    path('create/', AccountCreateView.as_view(),  name='create'),
]
