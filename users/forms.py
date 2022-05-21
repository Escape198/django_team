from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User, Skills


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'surname', 'age', 'about','photo', 'languages', 'basic_skills', 'hobby', 'url')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput())


class UpdateUserBasicSkills(forms.ModelForm):
    basic_skills = forms.ModelMultipleChoiceField(
        queryset=Skills.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Skills',
        required=False,)

    class Meta:
        model = User
        fields = ('basic_skills',)


    def basic_skills(self, user, old_basic_skills, str_basic_skills):
        if str_basic_skills:
            old_basic_skills |= str_basic_skills
        user.basic_skills.clear()
        user.basic_skills.add(*old_basic_skills)
        return user


class UpdateBasicSkills(forms.Form):
    new_basic_skills = forms.CharField(
        max_length=100,
        label='Add your own skill',
        required=False,
        widget=forms.TextInput())

    def get_basic_skills(self):
        empty_check = self.cleaned_data['new_basic_skills']
        if empty_check:
            new_basic_skills = empty_check.split(', ')
            all_basic_skills = [basic_skill.name for basic_skill in Skills.objects.all()]

            no_repeat_basic_skills = [basic_skill for basic_skill in new_basic_skills if basic_skill not in all_basic_skills]
            repeat_basic_skills = [basic_skill for basic_skill in new_basic_skills if basic_skill in all_basic_skills]
            repeat_basic_skills_query = Skills.objects.filter(name__in=repeat_basic_skills)

            no_repeat_basic_skills_create_instance = Skills.objects.bulk_create([Skills(name=new_basic_skill) for new_basic_skill in no_repeat_basic_skills])
            no_repeat_basic_skills_query = Skills.objects.filter(name__in=[basic_skill.name for basic_skill in no_repeat_basic_skills_create_instance])
            return repeat_basic_skills_query | no_repeat_basic_skills_query
