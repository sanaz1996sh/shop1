from django import forms
w_message=forms.widgets.Textarea(attrs={"class":"textarea textarea-bordered h-24"})
w1=forms.widgets.TextInput(attrs={"class":"input input-bordered w-full"})
class fcontact(forms.Form):
    name=forms.CharField(max_length=50,label=" نام و نام خانوادگی",help_text="نام و نام خانوادگی باید حداقل 6 کاراکتر داشته باشد",
                         widget=w1)
    subject=forms.CharField(max_length=50,label="موضوع",widget=w1)
    email=forms.EmailField(max_length=50,label="ایمیل",help_text="ایمیل باید معتبر باشد",widget=w1)
    message= forms.CharField(max_length=3000,label="پیام",widget=w_message)
    

    def clean_name(self):
        n=self.cleaned_data["name"]
        if len(n)<6:
            raise forms.ValidationError("نام و نام خانوادگی باید حداقل 6 کاراکتر داشته باشد")
        return n
