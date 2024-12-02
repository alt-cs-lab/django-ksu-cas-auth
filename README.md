sets up auth using ksu cas server for django projects

usage guide:
include the package in pyproject.toml if using poetry
```
[tool.poetry.dependencies]
django-ksu-cas-auth = {git = "https://github.com/alt-cs-lab/django-ksu-cas-auth"}
```
include the package in requirements.txt if not using poetry
```
git+https://github.com/alt-cs-lab/django-ksu-cas-auth
```

in your project's urls.py add the package urls
```
urlpatterns = [
  path('accounts/', include('django_ksu_cas_auth.urls')),
]
```
in this case, accounts/login and accounts/logout are the login and logout paths.

in your project's settings.py, add the following
```
INSTALLED_APPS = [
  'django_ksu_cas_auth',
  'django_cas_ng',
]

AUTHENTICATION_BACKENDS = [
    'django_cas_ng.backends.CASBackend',
]

CAS_SERVER_URL = 'https://signin.k-state.edu/WebISO/'
CAS_LOGOUT_COMPLETELY = True
CAS_REDIRECT_URL = '/authed/' if environ.get('CODESPACES') is None else 'https://' + environ.get('CODESPACE_NAME') + '-8000.' + environ.get('GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN') + '/authed/'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'

```
CAS_REDIRECT_URL is where users will be redirected after logging in. in this case its /authed, and we also handle codespaces url forwarding with the if.


