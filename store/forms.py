from crispy_forms import layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, ButtonHolder, Layout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from store.models import Comments


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required.')
    last_name = forms.CharField(max_length=30, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class CommentsForm(ModelForm):
    comment = forms.Textarea()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('comment', css_class='form-control'),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-secondary active')
            )
        )

    class Meta:
        model = Comments
        fields = ('comment',)
