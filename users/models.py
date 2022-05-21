from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

import random


quote = ['Happiness can be found, even in the darkest of times, if one only remembers to turn on the light. — Albus Dumbledore',
        'What you fear most of all is — fear. Very wise.. — Professor Lupin',
        'The ones that love us never really leave us. And you can always find them in here.. — Sirius Black',
        'Mysterious thing, time. Powerful, and when meddled with, dangerous. — Albus Dumbledore',
        'When in doubt… I find retracing my steps to be a wise place to begin. — Albus Dumbledore',
        'Greatness inspires envy; envy engenders spite; spite spawns lies. — Tom Riddle',
        'People find it far easier to forgive others for being wrong than being right. — Albus Dumbledore',
        'Words are, in my not-so-humble opinion, our most inexhaustible source of magic. Capable of both inflicting injury, and remedying it. — Albus Dumbledore ',
        'Of course it is happening inside your head… but why on earth should that mean that it is not real? — Albus Dumbledore'
]


class Skills(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'skills'
        verbose_name = 'skill'


class Language(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'languages'
        verbose_name = 'language'



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    name = models.CharField(max_length=50, verbose_name='Name', default='Guest')
    surname = models.CharField(max_length=50, verbose_name='Surname', default=':)')
    age = models.IntegerField(default=18, verbose_name='Age')
    about = models.TextField(verbose_name='About me', default=random.choice(quote))
    languages = models.ManyToManyField(Language, blank=True, verbose_name='Languages')
    basic_skills = models.ManyToManyField(Skills, blank=True, verbose_name='Basic Skills')
    hobby = models.CharField(max_length=250, null=True, blank=True, verbose_name='Hobby')
    photo = models.ImageField('Photo', upload_to='users/photos', default='default.jpg')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    url = models.URLField(verbose_name='Link', default='https://hh.ru/applicant/resumes')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def full_name(self):
        return f'{self.name} {self.surname}'

    def all_basic_skills(self):
        basic_skills = [basic_skill.name for basic_skill in self.basic_skills.all()]
        return ' '.join(basic_skills)

    def all_languages(self):
        languages = [language.name for language in self.languages.all()]
        return ' '.join(languages)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
