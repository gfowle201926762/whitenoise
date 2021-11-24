from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Post, Comment, UserProfile, Classroom
from .forms import PostForm, CommentForm, UserProfileForm, ClassroomForm

class Home(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        posts = Post.objects.filter(Q(author__profile__followers__in=[request.user.id]) | Q(author__in=[request.user.id])).order_by('-created_on').distinct()
        
        context = {
            'posts' : posts,
        }
        return render(request, 'main/home.html', context)

    def post(self, request, *args, **kwargs):
        pass


class PostCreation(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        context = {
            'form' : form,
        }
        print(request.path)
        return render(request, 'main/post_creation.html', context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('home')
        else:
            context = {
                'form' : form
            }
            return render(request, 'main/post_creation.html', context)


class PostDetail(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        context = {
            'post' : post,
            'form' : form,
        }
        return render(request, 'main/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.post = post
            obj.save()
            return redirect('post_detail', pk)

        else:
            context = {
                'post' : post,
                'form' : form
            }
            return render(request, 'main/post_detail.html', context)

class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'main/post_creation.html'
    success_url = '/home/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        liked = False
        for like in post.likes.all():
            if like == request.user:
                liked = True

        if liked == False:
            post.likes.add(request.user)

        if liked == True:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class PostDelete(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        post.delete()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

"""
class CommentEdit(View):
    def get(self, request, post_pk, comment_pk, *args, **kwargs):
        comment = Comment.objects.get(pk=comment_pk)
        post = comment.post
        form = CommentForm()
        context = {
            'post' : post,
            'form' : form
        }
        return render(request, 'main/post_detail.html', context)
"""

class CommentEdit(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main/post_detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=pk)
        context['post'] = post
        return context


class CommentDelete(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
        


class CommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        liked = False
        for like in comment.likes.all():
            if like == request.user:
                liked = True

        if liked == False:
            comment.likes.add(request.user)

        if liked == True:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        if profile.followers.all().filter(id=request.user.id).exists() == False:
            is_following = False
        else:
            is_following = True

        context = {
            'user' : user,
            'profile' : profile,
            'posts' : posts,
            'is_following' : is_following
        }

        return render(request, 'main/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'main/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile_view', kwargs={'pk' : pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

class FollowView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        followed_profile = UserProfile.objects.get(pk=pk)

        if followed_profile.user != request.user:

            if followed_profile.followers.all().filter(id=request.user.id).exists() == False:

                followed_profile.followers.add(request.user)
                follower_profile = request.user.profile
                follower_profile.following.add(followed_profile.user)

            else:
                followed_profile.followers.remove(request.user)
                follower_profile = request.user.profile
                follower_profile.following.remove(followed_profile.user)

            #return redirect('profile_view', pk)

            next = request.POST.get('next', '/')
            query = request.POST.get('query')
            if query:
                connector = "?query="
                url = next + connector + query
            else:
                url = next

            return HttpResponseRedirect(url, pk)



class FollowersView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        followers = profile.followers.all
        context = {
            'profile': profile,
            'followers': followers
        }
        return render(request, 'main/followers.html', context)

class FollowingView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        following = profile.following.all
        context = {
            'profile': profile,
            'following': following
        }
        return render(request, 'main/following.html', context)

class ProfileSearchView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')

        profile_list = UserProfile.objects.filter(
            Q(name__icontains=query)
        )

        context = {
            'profile_list': profile_list
        }
        return render(request, 'main/profile_search.html', context)

class CreateClassroomView(View):
    def get(self, request, *args, **kwargs):
        form = ClassroomForm()
        profile = UserProfile.objects.get(pk=request.user.profile.pk)
        context = {
            'form': form,
            'profile' : profile,
        }
        return render(request, 'main/classroom_create.html', context)

    def post(self, request, *args, **kwargs):
        form = ClassroomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            form.save()
            pk = room.pk
            return redirect('classroom_view', pk)
        else:
            context = {
                'form': form
            }
            return render(request, 'main/classroom_create.html', context)

class ClassroomView(View):
    def get(self, request, pk, *args, **kwargs):
        room = Classroom.objects.get(pk=pk)
        context = {
            'room': room
        }
        return render(request, 'main/classroom_view.html', context)

class ClassroomsView(View):
    def get(self, request, *args, **kwargs):
        teacher_rooms = request.user.teacher.all
        student_rooms = request.user.student.all
        context = {
            'teacher_rooms': teacher_rooms,
            'student_rooms': student_rooms
        }
        return render(request, 'main/classrooms_view.html', context)