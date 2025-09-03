from cmath import phase

from rest_framework import serializers
from questions.models import User, Question, Option, Result




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "phone", "email")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True , min_length=6)

    class Meta:
        model = User
        fields = ("username", "phone", "email","password")


    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            phone=validated_data["phone"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = [ "text","is_correct"]




class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"

    def create(self, validated_data):
        options = validated_data.pop("options")  # tashqi options_data ni ichida ishlatmaymiz
        question = Question.objects.create(**validated_data)
        for option_data in options:              # ichki nomni option_data deb o‘zgartirdik
            Option.objects.create(question=question, **option_data)
        return question

class AnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"
        read_only_fields = ("is_correct",)

