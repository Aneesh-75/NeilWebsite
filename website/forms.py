from django import forms

from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["full_name", "email", "phone", "session_type", "preferred_date", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Your name",
                "autocomplete": "name",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "(optional)",
                "autocomplete": "tel",
            }),
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "message": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Who are the portraits for, and what would you love them to feel like?",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (css + " form-input").strip()
        self.fields["phone"].required = False
        self.fields["preferred_date"].required = False
