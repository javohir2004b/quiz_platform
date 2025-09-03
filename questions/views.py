from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from questions.models import User, Question, Option, Result
from questions.serializer import RegisterSerializer, UserSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer,ResultSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(
  {
            "message":"User registered successfully",
            "user": UserSerializer(user).data
        },
        status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_detail(request,pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST','GET'])
def question_create_get(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions , many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        question_serializer = QuestionSerializer(data=request.data)
        if question_serializer.is_valid():
            question = question_serializer.save()
            options_data = request.data.get('options')
            if options_data:
                for option in options_data:
                    Option.objects.create(
                        question=question,
                        text=option['text'],
                        is_correct=option.get("is_correct", False)

                    )
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])
def question_rud(request, pk):
    question = get_object_or_404(Question,pk=pk)
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST', 'GET'])
def option_cr_view(request):
        if request.method == 'POST':
            serializer = OptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            options = Option.objects.all()
            serializer = OptionSerializer(options, many=True)
            return Response(serializer.data)



@api_view(['GET','DELETE','PUT'])
def option_rud(request,pk):
    option = get_object_or_404(Option , pk=pk)
    if request.method == 'GET':
        serializer = OptionSerializer(option)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OptionSerializer(option,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def check_answer(request):
    serializer = AnswerSerializer(data=request.data)
    if serializer.is_valid():
        question_id = serializer.validated_data['question_id']
        option_id = serializer.validated_data['option_id']

        try:
            option = Option.objects.get(id=option_id,question_id=question_id)
        except Option.DoesNotExist:
            return Response({"error":"bunday option yoq"},status=status.HTTP_400_BAD_REQUEST)

        user = request.user if request.user.is_authenticated else None

        result = Result.objects.create(
            user=user,
            question_id=question_id,
            selected_option_id=option_id,
            is_correct=option.is_correct
        )
        result_serializer = ResultSerializer(result)

        return Response(
            {
                "result":option.is_correct,
                "message":"To'gri javob" if option.is_correct else "Noto'g'ri javob",
                "detail":result_serializer.data
            }
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])
def result_rud(request,pk=None):
    if request.method == 'GET':
        if pk is not None:
            result = get_object_or_404(Result, pk=pk)
            serializer = ResultSerializer(result)
            return Response(serializer.data)
        else:
            results = Result.objects.all()
            serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        result = get_object_or_404(Result, pk=pk)
        serializer = ResultSerializer(result , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        result = get_object_or_404(Result, pk=pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def user_score(request, pk):
    user = get_object_or_404(User, pk=pk)
    results = Result.objects.filter(user=user, score=True)
    score = results.count()
    return Response({"user":user.username,  "score":score})