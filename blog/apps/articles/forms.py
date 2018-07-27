from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=200, min_length=5, required=True)


class ArticleAddForm(forms.Form):
    arttitle = forms.CharField(min_length=1, max_length=20, required=True)
    artdesc = forms.CharField(min_length=1, max_length=100, required=True)
    artimage = forms.FileField(required=True)
    artcontent = forms.CharField(min_length=5, required=True)
