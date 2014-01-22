from django import forms
from datetime import datetime
from vm.models import Wasco

# VOTE_RESPONSE_CHOICES = ('Yes','No','Undecided')
VOTER_RESPONSE_CHOICES = [(1, 'Yes'), (-1, 'No'), (0, 'Undecided')]
YARDSIGN_CHOICES = [(True, 'Yes'), (False, 'No')]

class VoteResponseForm(forms.ModelForm):
    voter_response = forms.ChoiceField(choices = VOTER_RESPONSE_CHOICES, widget=forms.RadioSelect())
    yardsign = forms.ChoiceField(choices=YARDSIGN_CHOICES, widget=forms.RadioSelect())
    time_response = forms.DateTimeField(widget = forms.HiddenInput(), required = False)

    class Meta:
        model = Wasco
        fields = ('voter_response', 'yardsign', 'time_response')
