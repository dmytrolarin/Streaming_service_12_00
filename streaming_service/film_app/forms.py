from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(max_length = 80, label = "Ваше ім'я:")
    email = forms.EmailField(label = "Ваш email:")
    message = forms.CharField(widget=forms.Textarea, label = "Ваш відгук:")