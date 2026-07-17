from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from sections.models import Section, Content, Question
from sections.serializers.sections_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.content_serializers import ContentSerializer, ContentListSerializer
from sections.serializers.question_serializers import QuestionSerializer
from sections.permissions import IsModerator, IsSuperuser
from sections.paginators import SectionPaginator, ContentPaginator, QuestionPaginator


class SectionListApiView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionPaginator


class SectionCreateApiView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionRetrieveApiView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionUpdateApiView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionDestroyApiView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsSuperuser)


class ContentListApiView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = ContentPaginator


class ContentCreateApiView(CreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class ContentRetrieveApiView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)


class ContentUpdateApiView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class ContentDestroyApiView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsSuperuser)


class QuestionListApiView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = QuestionPaginator


class QuestionRetrieveApiView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        answers = [question.answer for question in Question.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1]
        answer = answer.title.strip().lower()
        member_answer = request.data.get('member_answer').strip().lower()
        is_correct = member_answer == answer
        return Response({'is_correct': is_correct})
