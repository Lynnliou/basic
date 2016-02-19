from django import forms
class add_event(forms.Form):
    event_date=forms.CharField(label='add_event',max_length=300)



