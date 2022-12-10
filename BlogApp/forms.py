from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField()
    contact = forms.EmailField()

class CategoryForm(forms.Form):
    name = forms.CharField()

class PostForm(forms.Form):
    title = forms.CharField()
    date = forms.DateField(widget=forms.SelectDateWidget)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()
    category = forms.CharField()