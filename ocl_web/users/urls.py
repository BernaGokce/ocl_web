# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

from users import views

__author__ = 'briandant'

urlpatterns = patterns('',
    # URL pattern for the UserListView
    url(r'^(?P<user>[a-zA-Z0-9\-\.]+)/sources/', include('apps.sources.urls')),
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w\-_]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
#    url(r'^$', OrganizationListView.as_view(), name='organization-list'),
    url(
        regex=r'^new/$',
        view=OrganizationCreateView.as_view(),
        name='org-new'
    ),
    url(
        # TODO:  Confirm the regex we'll use for users.
        # Using the one that came with django-cookiecutter, because presumably
        # those models match this regex.
        # Probably will need to change to match API: r'^(?P<username>[a-zA-Z0-9\-\.]+)/$',
        r'^(?P<username>[\w\-_]+)/$',
        OrganizationDetailView.as_view(),
        name='org-detail'
    ),
    url(
        regex=r'^(?P<username>[\w\-_]+)/sources/',
        include('apps.sources.urls')
    ),
    url(
        regex=r'^(?P<username>[a-zA-Z0-9\-\.]+)/collections/',
        include('apps.conceptcollections.urls')
    ),
)
