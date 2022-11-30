from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=30)
    contact = forms.EmailField()

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=20)

class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    date = forms.DateField()
    content = forms.CharField()
    author = forms.CharField(max_length=30)
    category = forms.CharField(max_length=20)