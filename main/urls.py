from django.urls import path
from .views import Home, PostCreation, PostDetail, PostEdit, PostLike, PostDelete, CommentDelete, CommentEdit, CommentLike, ProfileView, ProfileEditView, FollowView, FollowersView, FollowingView, ProfileSearchView, CreateClassroomView, ClassroomView, ClassroomsView

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('make_a_post/', PostCreation.as_view(), name='post_creation'),
    path('post/<int:pk>/detail', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', PostEdit.as_view(), name='post_edit'),
    path('post/<int:pk>/like', PostLike.as_view(), name='post_like'),
    path('post/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('comment/<int:pk>/delete', CommentDelete.as_view(), name='comment_delete'),
    path('post/<int:post_pk>/comment/<int:pk>/edit', CommentEdit.as_view(), name='comment_edit'),
    path('comment/<int:pk>/like', CommentLike.as_view(), name='comment_like'),
    path('profile/<int:pk>/view', ProfileView.as_view(), name='profile_view'),
    path('profile/<int:pk>/edit', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/<int:pk>/follow', FollowView.as_view(), name='follow'),
    path('profile/<int:pk>/followers', FollowersView.as_view(), name='followers'),
    path('profile/<int:pk>/following', FollowingView.as_view(), name='following'),
    path('search/', ProfileSearchView.as_view(), name='profile_search'),
    path('createclassroom/', CreateClassroomView.as_view(), name='classroom_create'),
    path('classroom/<int:pk>/view', ClassroomView.as_view(), name='classroom_view'),
    path('classroomsview', ClassroomsView.as_view(), name='classrooms_view'),
]