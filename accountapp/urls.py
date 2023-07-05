from django.urls import path

from accountapp.views import hellow_world

app_name="accountapp"

# "127.0.0.1:8000/account/hellow_world"
# 나중에는 저기 name으로 accountapp:hellow_world 라는 식으로 간편하게 하는 함수가 있단다.


urlpatterns = [
    path('hellow_world/', hellow_world , name='hellow_world'),

]
