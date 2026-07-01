from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from rest_framework.fields import CharField, SerializerMethodField

from sections.models import Question, Section
from sections.serializers.sections_serializers import SectionSerializer

class QuestionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'section', 'question')

class QuestionSectionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())
    members_answer = CharField()

    class Meta: 
        model = Question
        fields = ('id', 'section', 'question', 'member_answer')

