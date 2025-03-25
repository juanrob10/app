from django.contrib import admin
from .models import Student,Teacher,TakenQuiz,Answer,StudentAnswer


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(TakenQuiz)
admin.site.register(Answer)
admin.site.register(StudentAnswer)