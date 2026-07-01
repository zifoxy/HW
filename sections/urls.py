from os import path as p

from django.urls import path
from rest_framework.routers import DefaultRouter

from sections.apps import SectionsConfig

from sections.views import SectionListApiView, SectionCreateApiView, SectionRetrieveApiView, SectionUpdateApiView, SectionDestroyApiView

app_name = SectionsConfig.name

router = DefaultRouter()

section = 'section/'
content = 'content/'
question = 'question/'
create = 'create/'
update = 'update/'
delete = 'delete/'
int_pk = '<int:pk>/'

urlpatterns = [
    # section urlpatterns
    path(p.join(section), SectionListApiView.as_view(), name='section_list'),
    path(p.join(section, create), SectionCreateApiView.as_view(), name='section_create'),
    path(p.join(section, int_pk), SectionRetrieveApiView.as_view(), name='section_detail'),
    path(p.join(section, int_pk, update), SectionUpdateApiView.as_view(), name='section_update'),
    path(p.join(section, int_pk, delete), SectionDestroyApiView.as_view(), name='section_delete'),

] + router.urls