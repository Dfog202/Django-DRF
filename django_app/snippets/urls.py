from django.conf.urls import url

from snippets import views

urlpatterns = [
    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<pk>\d+)/$', views.SnippetDetail.as_view()),
]
