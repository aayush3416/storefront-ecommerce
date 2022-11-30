from django import forms
from .models import Product, ReviewRating, Variation


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ('subject', 'review', 'rating')

    # def __init__(self, *args, **kwargs):
    #     super(ReviewForm, self).__init__(*args, **kwargs)
    #     self.fields['subject'].widget.attrs['class'] = 'form-control'
    #     self.fields['subject'].widget.attrs['placeholder'] = 'Enter subject'
    #     self.fields['subject'].widget.attrs['id'] = 'subject'
    #     self.fields['review'].widget.attrs['class'] = 'form-control'
    #     self.fields['review'].widget.attrs['placeholder'] = 'Enter review'
    #     self.fields['review'].widget.attrs['id'] = 'review'
    #     self.fields['rating'].widget.attrs['class'] = 'form-control'
    #     self.fields['rating'].widget.attrs['id'] = 'rating'