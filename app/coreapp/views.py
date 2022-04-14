from django.shortcuts import render
from django.views import generic
from django.conf import settings
from os import listdir
from os.path import isfile, join
from .models import Post, CodeExp, CODE_TYPE, PROJECT_TYPE, Project, Music


def listMediaFiles(mediaPath, folder):
    media_path = join(settings.MEDIA_ROOT, mediaPath, folder)
    return [f for f in listdir(media_path) if isfile(join(media_path, f))]


class BlogView(generic.ListView):
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = "blog"
        return context


class BlogPost(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

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


class AboutView(generic.TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = "about"
        return context


class ProjectsView(generic.ListView):
    queryset = Project.objects.order_by('-order')
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #  List files in the preview folder
        for project in self.object_list:
            project.images = listMediaFiles('projects', project.previewFolder)

        context['types'] = PROJECT_TYPE
        context['menu'] = "projects"
        return context


class MusicView(generic.ListView):
    queryset = Music.objects.order_by('-order')
    template_name = "music.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #  List files in the preview folder
        for music in self.object_list:
            music.images = listMediaFiles('music', music.previewFolder)

        context['menu'] = "music"
        return context
