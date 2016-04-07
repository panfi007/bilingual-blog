from django import forms
from django.contrib import admin
from .models import Post, Profile
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    body_en = forms.CharField(widget=CKEditorWidget())
    body_es = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    form = PostAdminForm


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'user', 'date_of_birth', 'photo', 'description')
    list_filter = ('date_of_birth', 'occupation')
    search_fields = ('user', 'name', 'occupation')

admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)