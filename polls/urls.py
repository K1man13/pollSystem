from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("create/", views.create, name="create"),
    # path("edit/<int:question_id>/", views.edit, name="edit"),
    # path("delete/<int:question_id>/", views.delete, name="delete"),
]