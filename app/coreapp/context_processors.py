def add_variable_to_context(request):
    return {
        'navigation': [
            {
                'name': './posts',
                'url': ''
            },
            {
                'name': './projects',
                'url': ''
            },
            {
                'name': './code',
                'url': ''
            },
            {
                'name': './music',
                'url': ''
            },
            {
                'name': './about',
                'url': ''
            },
            {
                'name': './contact',
                'url': ''
            },
        ],
        'techstack': [
            {
                'name': 'Django',
                'icon': 'django.svg',
                'url': 'https://www.djangoproject.com'
            },
            {
                'name': 'Tailwindcss',
                'icon': 'tailwind-css.svg',
                'url': 'https://tailwindcss.com'
            },
            {
                'name': 'Summernote',
                'icon': 'summernote_icon.png',
                'url': 'https://summernote.org'
            },
            {
                'name': 'Gunicorn',
                'icon': 'gunicorn-icon.svg',
                'url': 'https://gunicorn.org'
            },
            {
                'name': 'Nginx',
                'icon': 'nginx-icon.svg',
                'url': 'https://www.nginx.com'
            },
            {
                'name': 'PostgreSQL',
                'icon': 'postgresql.svg',
                'url': 'https://www.postgresql.org/'
            },
            {
                'name': 'Alpine',
                'icon': 'alpine-linux-icon.svg',
                'url': 'https://alpinelinux.org'
            },
            {
                'name': 'Docker',
                'icon': 'docker-svgrepo-com.svg',
                'url': 'https://www.docker.com'
            },
            {
                'name': 'hosted on Ionos',
                'url': 'https://www.ionos.de'
            },
            {
                'name': 'checkout sourcecode',
                'icon': 'github.svg',
                'url': 'https://github.com/Rolleander/blog'
            }
        ]
    }
