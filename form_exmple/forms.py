from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "field",
            }
        ),
        error_messages={
            "required": "This field is required",
            "invalid": "This field is invalid",
        },
    )

    email = forms.EmailField(required=True)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "placeholder": "message",
                "rows": 4,
            }
        )
    )

    def clean_name(self):
        #    cleaned_data = super().clean()
        name = self.cleaned_data.get("name")

        if len(name)<3:
            raise forms.ValidationError("Name must Be Greter than three Charater")
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')

        if name and email and name.lower() in email.lower():
            raise forms.ValidationError("Email should not contain your name")

        return cleaned_data
