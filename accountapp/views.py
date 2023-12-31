from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm

from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

# Create your views here.


class AccountCreateView(CreateView):
    model = User
    # 강의 에서는 UserCreationForm 사용
    form_class = BaseUserCreationForm
    # reverse와 reverse_lazy의 차이는 큰차이는 없으나 reverse의 경우 클래스에서 불러 올 수 없음 정도만 알자.
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
        model = User
        context_object_name = 'target_user'
        form_class = AccountUpdateForm
        success_url = reverse_lazy('accountapp:login')
        template_name = 'accountapp/update.html'

        # self는 여기 클래스 자체(AccountDeleteView)를 가리킨다.




@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


