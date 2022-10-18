from datetime import date
from .models import Lecture
from django.forms import ModelForm,DateInput,TimeInput,TextInput,IntegerField
from django.core.exceptions import ValidationError

# creating a lectureform class
class LectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"type": "time"}),
            'duration':TextInput(attrs={"type":"number","min":"1","max":"4"})
        }

    def clean_data(self):
        data = self.cleaned_data["date"]
        if data < date.today():
            raise ValidationError("Lectures can not be held in the past")
        return data   
