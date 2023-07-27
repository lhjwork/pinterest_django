from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from articleapp.models import Article
from commentapp.form import CommentCreationForm
from commentapp.models import Comment


# Create your views here.


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    def form_valid(self, form):

        temp_comment = form.save(commit=False)
        # create.html 에서 hidden 으로 넘긴 값이 여기로 넘어감
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})