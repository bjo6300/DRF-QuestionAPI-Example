from rest_framework import serializers
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    # 모델을 JSON 형태로 변환
    class Meta:
        model = Answer # 모델 설정
        fields = ('__all__') # json으로 만들어 줄 필드