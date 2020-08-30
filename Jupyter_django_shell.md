# How to use the Django shell in Jupyter Notebook? 
- pip install django jupyter ipython django-extensions
- INSTALLED_APPS = [
    ...
    'django_extensions',
]
- DJANGO_ALLOW_ASYNC_UNSAFE=true && python manage.py shell_plus --notebook

** IMPORTANT! IPython added top-level async/await support, which is running the whole interpreter session inside of a default event loop and starting from Django 3.0 version running application from a thread where there is a running event loop, will cause a SynchronousOnlyOperation error. So, setting DJANGO_ALLOW_ASYNC_UNSAFE to true is mandatory in that case. More on this here. **
