from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from main.models import Author, Quote, Articles, Tag



class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'born_date', 'born_location', 'description']



class QuoteForm(forms.ModelForm):
    new_author = forms.CharField(required=False, label='New Author')
    new_tags = forms.CharField(required=False, label='New Tags', help_text='Comma-separated list of new tags')

    class Meta:
        model = Quote
        fields = ['text', 'author', 'tags', 'new_tags']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Quote text'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select or add author'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Select or add tags'
            }),
        }

    def save(self, commit=True):
        new_author = self.cleaned_data.get('new_author')
        if new_author:
            author, created = Author.objects.get_or_create(name=new_author)
            self.instance.author = author

        if commit:
            self.instance.save()


        new_tags = self.cleaned_data.get('new_tags')
        tags = []
        if new_tags:
            tag_names = [tag.strip() for tag in new_tags.split(',')]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                tags.append(tag)
    
        instance = super().save(commit=commit)
    
        if tags:
            instance.tags.set(tags)
    
        return instance



class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name_author', 'title', 'full_text', 'date']

    widgets = {
        "name_author": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Author name'
        }),
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Article title'
        }),
        "date": DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Date and time'
        }),
        "full_text": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Article text'
        }),
    }



