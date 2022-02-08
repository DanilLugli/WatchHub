from django import forms

from blog.models import Watch, Maison, Condition
from django.contrib.auth.models import User

choices = Condition.objects.all().values_list('condition','condition')

choice_list = []
for item in choices:
    choice_list.append(item)


class WatchCreate(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('maison', 'model', 'movement', 'condition', 'owner', 'reference', 'price', 'photo', )
        widgets = {
            'cond' : forms.Select(choices = choice_list, attrs={'class':'form-control'}),
        }


class MaisonForm(forms.ModelForm):
    class Meta:
        model = Maison
        fields = ('maison',)
        labels = {
            'maison': 'Maison Name',
        }
