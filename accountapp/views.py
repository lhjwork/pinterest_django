from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        # account app 내부에 있는 hello_world로 제 접속하라 -> def hello_world를 말하는 거 같음
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:

        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list' : hello_world_list })


class AccountCreateView(CreateView):
    model = User
    # 강의 에서는 UserCreationForm 사용
    form_class = BaseUserCreationForm
    # reverse와 reverse_lazy의 차이는 큰차이는 없으나 reverse의 경우 클래스에서 불러 올 수 없음 정도만 알자.
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

