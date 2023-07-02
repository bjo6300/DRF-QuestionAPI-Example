from django.db import models

# Create your models here.
from django.db import models

from question.models import Question

# Create your models here.
class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE) # onetomany 설정, 질문 삭제 시 답변도 삭제
    content = models.CharField(max_length=100) # 내용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title