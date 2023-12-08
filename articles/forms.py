from django import forms

# Article creating form rendered in write.html
class Article_Form(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Title", "class": "form-control"}
        ),
    
    )
    content = forms.CharField(
         widget=forms.TextInput(
            attrs={"placeholder": "Content", "class": "form-control"}
        ),
    )
    
    file = forms.FileField( 
        required=False,
        widget=forms.FileInput(
            attrs={"class": "form-control"}
        ),)

    tags = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Tags note: Seperate with comma(\",\")", "class": "form-control"}
        ),
    )

