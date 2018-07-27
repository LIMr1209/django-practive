from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(min_length=5, max_length=200, required=True)


class ArticleAddForm(forms.Form):
    arttitle = forms.CharField(min_length=1, required=True)
    artdesc = forms.CharField(min_length=1, required=True)
    artcontent = forms.CharField(min_length=1, required=True)
    artimage = forms.FileField(required=True)
