from django import forms

from .models import Course

class CreatePersonCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('skills', 'no_skills',)
        exclude = ('position', 'price', 'featured', 'skill', 'title', 'slug', 'short_description',
                   'description', 'lessons', 'duration', 'pros_cons', 'preview', 'image')

        widgets = {
            'skills': forms.CheckboxSelectMultiple(attrs={'class': "checkboxes"}),
            'no_skills': forms.CheckboxInput(attrs={'class': "checkboxes", 'id': "id_no_skills"})
        }


class ChangePriceForm(forms.Form):
    price = forms.DecimalField(
        widget=forms.TextInput(),
        max_digits=20,
        decimal_places=2,
    )
    intensity_id = forms.CharField(
        widget=forms.TextInput(),
    )
    duration_id = forms.CharField(
        widget=forms.TextInput(),
    )
