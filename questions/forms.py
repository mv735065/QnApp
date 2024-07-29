from django import forms
from .models import Question, Answer, Comment

# forms.py
from django import forms
from .models import Question, Tag

class QuestionForm(forms.ModelForm):
    new_tags = forms.CharField(
        required=False, 
        max_length=500, 
        label='New Tags', 
        help_text='Enter new tags separated by commas.'
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Question
        fields = ['title', 'description', 'tags', 'created_at']
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})  # Customize input widget
        }

    def clean(self):
        cleaned_data = super().clean()
        new_tags = cleaned_data.get("new_tags")

        if new_tags:
            new_tags_list = [tag.strip() for tag in new_tags.split(',') if tag.strip()]
            existing_tags = Tag.objects.filter(name__in=new_tags_list)
            existing_tag_names = set(existing_tags.values_list('name', flat=True))
            new_tag_names = set(new_tags_list) - existing_tag_names

            # Create new tags
            for tag_name in new_tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                cleaned_data['tags'] = list(cleaned_data['tags']) + [tag]

        return cleaned_data



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class TagFilterForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
