from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from importlib_metadata.docs.conf import author
from mutagen.id3 import UFI
from oauthlib.uri_validate import authority

from .forms import UserCreationForm, Commentform, Photoform
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from .models import Post, Comment, PhotoCreate


# def LikeView(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('home', args=[str(pk)]))


# def LikeView(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     print(post)
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user.id)
#     else:
#         post.likes.add(request.user.id)
#     return HttpResponseRedirect(reverse('home'))


@csrf_exempt
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    result = {'status': 200, 'post_id': post.pk, 'count': post.likes.count()}
    try:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user.id)
            result['btn_type'] = 'remove'

        else:
            post.likes.add(request.user.id)
            result['btn_type'] = 'add'

    except Exception:
        result['status'] = 404
    return JsonResponse(result, safe=False)


@csrf_exempt
def subscribe_user(request):
    follows = get_object_or_404(PhotoCreate, id=request.POST.get('foll_id'))
    results = {'status': 200, 'foll_id': follows.pk, 'count': follows.follow.count()}
    try:
        if follows.follow.filter(id=request.user.id).exists():
            follows.follow.remove(request.user.id)
            results['btn_type'] = 'remove'

        else:
            follows.follow.add(request.user.id)
            results['btn_type'] = 'add'

    except Exception:
        results['status'] = 404
    return JsonResponse(results, safe=False)


# def subscribe_user(request, pk):
#     follows = get_object_or_404(Follow, id=request.POST.get('post_id'))
#     liked = False
#     if follows.follow.filter(id=request.user.id).exists():
#         follows.follow.remove(request.user.id)
#         liked = False
#     else:
#
#         follows.follow.add(request.user.id)
#         liked = True
#     return HttpResponseRedirect(reverse('home'))


class MyDetail(ListView):
    model = Post
    template_name = 'detail/my_project_id.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MyDetail, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author_id=self.kwargs.get('id'))
        context['users'] = User.objects.all()
        context['users1'] = User.objects.filter(username=self.request.user)
        context['follow'] = PhotoCreate.objects.filter(author_id=self.kwargs.get('id'))
        context['crate_photos1'] = PhotoCreate.objects.filter(author=self.kwargs.get('id'))
        return context

    # def get_queryset(self):
    #     return self.model.objects.filter(author_id=self.kwargs.get('id'))


class Search(ListView):
    template_name = 'detail/search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('posts'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['posts'] = self.request.GET.get('posts')
        return context


class HomeList(ListView):
    model = Post
    template_name = 'detail/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeList, self).get_context_data(**kwargs)
        context['photos1'] = PhotoCreate.objects.all()
        context['comments'] = Comment.objects.all()
        context['myuser'] = User.objects.filter(username=self.request.user)
        context['users'] = User.objects.all()
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = Commentform
    template_name = 'detail/comment.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)


class AvtorView(ListView):
    model = User
    template_name = 'detail/avtors.html'
    context_object_name = 'users'


class PhotoCreates(CreateView):
    model = PhotoCreate
    template_name = 'detail/photo_post.html'
    fields = 'photos', 'data_photo'

    def get_success_url(self):
        return reverse_lazy('my_project')

    def form_valid(self, forms):
        instance = forms.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(forms)


class PhotoUpdate(UpdateView):
    model = PhotoCreate
    template_name = 'detail/photoUpdate.html'
    fields = 'photos', 'data_photo',

    def get_success_url(self):
        return reverse_lazy('my_project')


class CreateList(CreateView):
    model = Post
    template_name = 'detail/create.html'
    fields = 'title', 'content',

    def get_success_url(self):
        return reverse_lazy('my_project')

    def form_valid(self, form):
        a = form.save(commit=False)
        a.author = self.request.user
        a.save()
        return super().form_valid(form)


class Myproject(ListView):
    model = Post
    template_name = 'detail/my_project.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Myproject, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user)
        context['users'] = User.objects.filter(username=self.request.user)
        context['users1'] = User.objects.all()
        context['photos'] = PhotoCreate.objects.filter(author=self.request.user)
        return context


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'detail/update.html'
    fields = 'title', 'content',

    def get_success_url(self):
        return reverse_lazy('my_project')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'detail/delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return True

    def get_success_url(self):
        return reverse_lazy('my_project')


class Register(View):
    template_name = 'registration/register.html'
    context_object_name = 'save'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


# class CommentView(CreateView):
#     model = Comment
#     template_name = 'detail/comment.html'
#     fields = 'body'
#
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     form.instance.post_id = self.kwargs['pk']
    #     return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('home')


class CommentView(CreateView):
    model = Comment
    template_name = 'detail/comment.html'
    fields = 'body',
    context_object_name = 'comments'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class Base(ListView):
    model = User
    template_name = 'detail/base.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Base, self).get_context_data(**kwargs)
        context['user'] = User.objects.name
        return context


class LogoutView(object):
    pass


