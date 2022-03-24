from django.shortcuts import render
from django.views import generic
from .models import Post, CodeExp, CODE_TYPE


class BlogView(generic.ListView):
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = "blog"
        return context


class CodeExpView(generic.TemplateView):
    template_name = "code_exp.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['codexps'] = [(code_type[1], list(filter(lambda entry: entry.code_type == code_type[0],
                                                         CodeExp.objects.all().order_by('-order')))) for code_type in CODE_TYPE]
        context['menu'] = "experience"
        return context
