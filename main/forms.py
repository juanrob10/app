from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Subject,Student,Teacher

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Nombre de usuario"
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Contraseña"
    )

class BaseSignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Nombre de usuario",
        help_text="Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.",
        widget=forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': '...'  # Clases Tailwind si necesito
        })
    )
    email = forms.EmailField(
        required=True,
        label="Correo electrónico"
    )
    first_name = forms.CharField(
        required=True,
        label="Nombre"
    )
    last_name = forms.CharField(
        required=True,
        label="Apellido"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class TeacherSignUpForm(BaseSignUpForm):
    department = forms.CharField(
        max_length=100,
        required=True,
        help_text="Ingrese su departamento académico",
        widget=forms.TextInput()  # Sin clases CSS para Tailwind
    )

    class Meta(BaseSignUpForm.Meta):
        fields = BaseSignUpForm.Meta.fields + ('department',)

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
            Teacher.objects.create(
                user=user,
                department=self.cleaned_data['department']
            )
        return user

class StudentSignUpForm(BaseSignUpForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True,
        help_text="Selecciona al menos un área de interés"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['interests'].label_from_instance = lambda obj: obj.name

    def clean_interests(self):
        interests = self.cleaned_data.get('interests')
        if not interests:
            raise forms.ValidationError("Debes seleccionar al menos un área de interés")
        return interests

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        
        if commit:
            user.save()
            student = Student.objects.create(user=user)
            student.interests.set(self.cleaned_data['interests'])
        
        return user