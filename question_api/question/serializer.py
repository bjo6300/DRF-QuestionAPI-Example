from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    # 모델을 JSON 형태로 변환
    class Meta:
        model = Question # 모델 설정
        fields = ('id','title','content','created_at', 'updated_at') # json으로 만들어 줄 필드