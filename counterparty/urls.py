from django.conf.urls import url

from counterparty import views

urlpatterns = [
    url(r'^$', views.CounterPartyListView.as_view(), name='list'),
    url(r'create/$', views.CreatePatternedCounterPartyView.as_view(), name='create'),
    url(r'pattern_matches/$', views.AliasPatternMatchesView.as_view(), name='pattern_matches'),
    url(r'add_pattern/$', views.AddPatternModalView.as_view(), name='add_pattern'),

    url(r'^(?P<pk>.+)/categorise/$', views.CategoriseModalView.as_view(), name='categorise'),
    url(r'^(?P<pk>.+)/$', views.CounterPartyDetailView.as_view(), name='detail'),
]
