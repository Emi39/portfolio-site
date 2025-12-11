from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 rounded bg-gray-100 dark:bg-gray-800 border-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 rounded bg-gray-100 dark:bg-gray-800 border-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'w-full p-3 rounded bg-gray-100 dark:bg-gray-800 border-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-3 rounded bg-gray-100 dark:bg-gray-800 border-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Your Message', 'rows': 5}),
        }
