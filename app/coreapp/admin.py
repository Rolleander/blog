from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, CodeExp

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

class CodeExpAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_type', 'order')
    list_filter = ("code_type",)
    search_fields = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(CodeExp, CodeExpAdmin)
