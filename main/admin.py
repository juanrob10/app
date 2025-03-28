from django.contrib import admin
from .models import Student,Teacher,TakenQuiz,Answer,StudentAnswer,Quiz,Question


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Quiz)
admin.site.register(TakenQuiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(StudentAnswer)