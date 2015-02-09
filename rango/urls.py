from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^like_category/$', views.like_category, name='like_category'),
    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
    url(r'^auto_add_page/$', views.auto_add_page, name='auto_add_page'),
    url(r'^goto/$', views.track_url, name='goto'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^setting_page/$', views.setting_page, name='setting_page'),
    url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', kwargs={'template_name': 'password_reset_form.html'}, name='password-reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', kwargs={'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$','django.contrib.auth.views.password_reset_confirm',kwargs={'template_name': 'password_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', kwargs={'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),

    )

