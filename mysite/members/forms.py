from django import forms

class MemberForm(forms.Form): 
    Id = forms.IntegerField(label="")
    Id.widget.attrs.update({"hidden": "hidden"})
    
    FirstName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))   
    FirstName.widget.attrs.update({"class": "form-control", "title" : "First Name"})

    LastName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))   
    LastName.widget.attrs.update({"class": "form-control", "title" : "Last Name"})   

    Email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'})) 
    Email.widget.attrs.update({"class": "form-control", "title" : "Email Address"})   
  
    Phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Phone (000-000-0000)'}))
    Phone.widget.attrs.update({"class": "form-control", "title" : "Phone Number"})   
    
    CHOICES = [
        (1, "Regular - Can't delete members"),
        (2, "Admin - Can delete members"),
    ]
    Role = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    
    
