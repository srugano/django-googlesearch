import django
version = django.get_version()

if version < 1.6:
    from django.conf.urls.defaults import patterns, url
    urlpatterns = patterns(
    '',

    url(
        r'^results/$', 
        'django.views.generic.simple.direct_to_template', 
        {'template': 'googlesearch/results.html'},
        name='googlesearch-results'
    ),

    url(
        r'^cref-cse\.xml/$', 
        'googlesearch.views.cref_cse', 
        {},
        name='googlesearch-cref-cse'
    ),
)
else:
    from django.conf.urls import patterns, url
    from django.views.generic import TemplateView

    urlpatterns = patterns(
    '',

    url(
        r'^results/$', TemplateView.as_view(template_name='googlesearch/results.html'), name="googlesearch-results"),
    ),

    url(
        r'^cref-cse\.xml/$', 
        'googlesearch.views.cref_cse', 
        {},
        name='googlesearch-cref-cse'
    ),
)
