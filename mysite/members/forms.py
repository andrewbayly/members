from django import forms

class MemberForm(forms.Form): 
    Id = forms.IntegerField(label="")
    Id.widget.attrs.update({"hidden": "hidden"})
    
    FirstName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))   
    FirstName.widget.attrs.update({"class": "form-control"})

    LastName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))   
    LastName.widget.attrs.update({"class": "form-control"})   

    Email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'})) 
    Email.widget.attrs.update({"class": "form-control"})   
  
    Phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    Phone.widget.attrs.update({"class": "form-control"})   
    
    CHOICES = [
        (False, "Regular - Can't delete members"),
        (True, "Admin - Can delete members"),
    ]
    Admin = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    
    
