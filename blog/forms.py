from django import forms


from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Comment"
        }
        error_messages = {
            "user_email": {
                "required": "Email is required",
                "invalid": "Enter a valid email address",
            },
            "user_name": {
                "required": "Name is required",
            },
            "text": {
                "required": "Please write a comment",
            },
        }
        