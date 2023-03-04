from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import CommentForm, ArticleForm
from django.contrib.auth.decorators import login_required


# class ArticleListView(ListView):
#     model = Article
#     template_name = 'articles/articles.html'


def article_list_view(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/articles.html', context)


# class ArticleDetailView(FormMixin, DetailView):
#     model = Article
#     template_name = 'articles/article_detail.html'
#     form_class = CommentForm
#
#     def get_success_url(self):
#         return reverse('article_detail', kwargs={'pk': self.object.pk})
#
#     def get_context_data(self, **kwargs):
#         context = super(ArticleDetailView, self).get_context_data(**kwargs)
#         context['form'] = CommentForm(initial={'article': self.object, 'author': self.request.user})
#         return context
#
#     def post(self, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             form.save()
#             return super(ArticleDetailView, self).form_valid(form)


def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.article = article
            obj.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    context = {'article': article, 'form': form}
    return render(request, 'articles/article_detail.html', context)


@login_required()
def article_create_view(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            post_body = form.cleaned_data['body']
            post_author = request.user
            obj = Article(title=post_title, body=post_body, author=post_author)
            obj.save()
            return HttpResponseRedirect('/articles/')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_create.html', {'form': form})


@login_required()
def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author:
        form = ArticleForm(request.POST or None, instance=article)
        if request.method == 'POST':
            form.save()
            return HttpResponseRedirect('/articles/' + str(pk))
        form = ArticleForm()
        context = {'article': article, 'form': form}
        return render(request, 'articles/article_update.html', context)
    else:
        return HttpResponseForbidden()


@login_required()
def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author:
        if request.method == 'POST':
            article.delete()
            return HttpResponseRedirect('/articles/')
        return render(request, 'articles/article_delete.html', {'article': article})
    else:
        return HttpResponseForbidden()

# class ArticleCreateView(LoginRequiredMixin, CreateView):
#     model = Article
#     template_name = 'articles/article_create.html'
#     fields = ['title', 'body']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#
# class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Article
#     success_url = reverse_lazy('article_list')
#     template_name = 'articles/article_update.html'
#     fields = ['title', 'body']
#
#     def test_func(self):
#         obj = self.get_object()  # my article
#         return obj.author == self.request.user
#


# class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Article
#     success_url = reverse_lazy('article_list')
#     template_name = 'articles/article_delete.html'
#
#     def test_func(self):
#         obj = self.get_object()  # my article
#         return obj.author == self.request.user
