from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from moviess.models import Movies


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'description', 'category', 'image', 'tags']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Поиск по названию, описанию или тегам...',
            'autocomplete': 'off'
        })
    )
    category = forms.ModelChoiceField(
        queryset=None,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from moviess.models import Category
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].empty_label = "Все категории"
