
    # Windows Python38 Enviroment

    [출처] http://pythonstudy.xyz/Python/Django
    [참고] https://docs.djangoproject.com/ko/3.0/intro/

    ------------------------------------------------------------------------------------------------------

    # pip install virtualenv

    # python -m venv C:\dev\python-study\venv\

    # C:\dev\python-study\venv\Scripts\activate.bat

    # (venv) C:\dev\python-study\venv\Scripts\python -m pip install --upgrade pip

    # (venv) C:\dev\python-study\venv\Scripts\pip install django

    # (venv) C:\dev\python-study\  C:\dev\python-study\venv\Scripts\django-admin.exe startproject www

    # defalt port 8000
    (venv) C:\dev\python-study\www> C:\dev\python-study\venv\Scripts\python.exe .\manage.py runserver

    # external access && port 8080
    (venv) C:\dev\python-study\www> C:\dev\python-study\venv\Scripts\python.exe .\manage.py runserver 0.0.0.0:8080

    ------------------------------------------------------------------------------------------------------

    # Create Django App
        (venv) C:\dev\python-study\www\manage.py startapp home

        - Error
        ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
        C:\dev\python-study\venv\Scripts\activate.bat

        1) home/views.py file add

        from django.shortcuts import render
        from django.http import HttpResponse
        
        # Create your views here.
        def index(request):
        return HttpResponse("Hello, World!")

        2) settings.py file INSTALLED_APPS add home

        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'home',
        ]

        3) urls.py file add

        from home import views

        urlpatterns = [
            path('admin/', admin.site.urls),  # url(r'^admin/',admin.site.urls),
            path('home/', views.index),       # url(r'^$/',views.index),
        ]

    # View
      views.py

    # Template
     /home/templates/home/index.html     
     settings.py TEMPLATES 'BACKEND': 'django.template.backends.django.DjangoTemplates'

     --Django Template Language--
        
        - 템플릿 변수 {{  }} 

        <h4>
            Name : {{ name }}
            Type : {{ vip.key }}
        </h4>

        - 템플릿 태그 {%  %} 
        
        {% if count > 0 %}
            Data Count = {{ count }}
        {% else %}
            No Data
        {% endif %}
        
        {% for item in dataList %}
            <li>{{ item.name }}</li>
        {% endfor %}
        
        {% csrf_token %}

        - 템플릿 필터

        날짜 포맷 지정
        {{ createDate|date:"Y-m-d" }}
        
        소문자로 변경
        {{ lastName|lower }}

        - 코멘트 {#  #} {% comment %}  {% endcomment %}

        {# 1 라인 코멘트 #}
    
        {% comment %}  
        <div>
            <p>
                불필요한 블럭
            </p>
            <span></span>
        </div>
        {% endcomment %}

        - HTML Escape  {% autoescape on %}  {% endautoescape %}  {{ content|escape }}


    Template Extension (Template Inheritance)

    {% extends "base.html" %}
 
    {% block content %}
        <h1>{{message}}</h1>
    {% endblock content %}


    TEMPLATES = [
    {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [ os.path.join(BASE_DIR, 'templates') ],  # 추가
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]


    # Model
    models.py

    # DB Migration
    (venv) C:\dev\python-study\www\manage.py makemigrations

    (venv) C:\dev\python-study\www\manage.py migrate

    (venv) C:\dev\python-study\www\manage.py dbshell

    - Error
    CommandError: You appear not to have the 'sqlite3' program installed or on your path.    
    https://www.sqlite.org/download.html download PATH setting

    .tables <- 테이블 리스트 출력
    PRAGMA table_info(home_feedback); <- 테이블 컬럼 정보
    select * from home_feedback; <- 조회 

    settings.py 

    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # django.db.backends.postgresql
    # django.db.backends.mysql
    # django.db.backends.sqlite3
    # django.db.backends.oracle

    # Mysql
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'MyDB',
            'USER': 'user1',
            'PASSWORD': 'pwd',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

    python manage.py sqlmigrate home_feedback 0001
    
    # URL Mapping
      urls.py

    # Form
      forms.py

    # Static File
      settings.py

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

    STATIC_URL = '/static/'
    STATICFILES_DIRS = ( os.path.join('static'), )

    - Django App static
    home/static/home

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )


    {% load staticfiles %}

    <html lang="en">
    <head>
        <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
    </head>
    <body>
    </body>
    </html>

    - collectstatic

    STATIC_ROOT = '/var/www/myweb_static'

    C:\dev\python-study\www\manage.py collectstatic


    # createsuperuser
    
    C:\dev\python-study\www\manage.py createsuperuser

    admin.py add

        from django.contrib import admin

        from .models import Feedback

        # Register your models here.

        admin.site.register(Feedback)


    http://localhost:8000/admin

    
    

    # Django Debugging    

       (venv) C:\dev\python-study\venv\Scripts\pip install django-debug-toolbar

        - settings.py add

        DEBUG = True

        INTERNAL_IPS = ('127.0.0.1', '192.168.0.1',)

        DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}

        ALLOWED_HOSTS = []


        # Application definition

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'home',
            'feedback',
            'debug_toolbar',
        ]

        MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]

        - urls.py

        import debug_toolbar

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('home/', views.index),
            path('feedback/', include('feedback.urls')),
            path('__debug__/', include(debug_toolbar.urls)),
        ]

        (venv) C:\dev\python-study\www> C:\dev\python-study\venv\Scripts\python.exe .\manage.py runserver

    ------------------------------------------------------------------------------------------------------
    
    Django - Site Deployment (I)

    1. Python instll

        # yum install epel-release
        # yum install python34

        # su - alex
        $ pyvenv --without-pip venv1
        $
        $ . venv1/bin/activate
        (venv1)$ curl https://bootstrap.pypa.io/get-pip.py | python3.4   #pip 수동 설치
        (venv1)$ deactivate
        $

        $ . venv1/bin/activate
        (venv1)$ pip install -r requirements.txt

    2. Project copy

        # cd /var/www
        # chown -R alex:alex myweb

        $ . venv1/bin/activate
        (venv1) /var/www/myweb $ ./manage.py runserver

    3. WSGI (Web Server Gateway Interface)
        WSGI - uWSGI, Gunicorn , Apache/mod_wsgi 

        Gunicorn (Green Unicorn) 
        (venv1) $ pip install gunicorn
        
        (venv1) /var/www/myweb $ gunicorn myweb.wsgi
        (venv1) /var/www/myweb $ gunicorn myweb.wsgi --bind mydomain.com:80

    4. Nginx Install

        # yum install epel-release
        # yum install nginx

        # firewall-cmd --permanent --zone=public --add-service=http
        # firewall-cmd --permanent --zone=public --add-service=https
        # firewall-cmd --reload

        nginx.conf (/etc/nginx/nginx.conf)

        server {
            listen       80;
            server_name  mydomain.com;
            location / {
                proxy_pass http://localhost:8000/;
            }
            location /static {
                alias /var/www/myweb_static;
            }
        }

        # setsebool httpd_can_network_connect on -P

        # chcon -Rt httpd_sys_content_t /var/www

        settings.py
            STATIC_ROOT = '/var/www/myweb_static'

        (venv1) /var/www/myweb $ ./manage.py collectstatic

        # systemctl start nginx
        # systemctl enable nginx

        (venv1) /var/www/myweb $ gunicorn myweb.wsgi --bind localhost:8000

    5. WSGI 서비스 관리자

        - Gunicorn 실행 쉘 스크립트 작성
        start_myweb.sh 

        #!/bin/bash

        . /home/alex/venv1/bin/activate
        cd /var/www/myweb
        exec /home/alex/venv1/bin/gunicorn myweb.wsgi --bind localhost:8000

        - supervisor 설치
        # yum install supervisor
        # systemctl start supervisord

        - supervisor 설정
        vi /etc/supervisord.d/myweb.ini

        [program:myweb]
        command = /var/www/myweb/start_myweb.sh
        user = alex
        autostart = true
        autorestart = true
        stdout_logfile = /var/log/myweb.log
        redirect_stderr = true
        environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8

        # supervisorctl reread
        # supervisorctl update




    Django - Site Deployment (II)    

    1. Ubuntu에 Apache 서버 설치    

        # apt-get install apache2
        # apt-get install libapache2-mod-wsgi-py3

    2. Django 프로젝트 소스 복사        

        # cd /var/www
        # chown -R www-data:www-data myweb

    3. 파이썬 가상환경

        # apt-get install -y python3-venv

        # pyvenv venv

        # . venv/bin/activate
        (venv) pip install django

    4. Apache 서버 설정        

        "/etc/apache2/sites-available"에 있는 000-default.conf 파일을 복사해서 
        새로운 .conf 파일을 만들고 (예: myweb.conf) 아래와 같은 내용으로 편집한다 
        (서버명 및 파일경로 등을 환경에 맞게 변경).
        

        <VirtualHost *:80>
                ServerName myweb.com
                ServerAlias www.myweb.com
                ServerAdmin admin@myweb.com
                DocumentRoot /var/www/myweb

                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined

                Alias /static /var/www/myweb/static
                <Directory /var/www/myweb/static>
                        Require all granted
                </Directory>
                <Directory /var/www/myweb/cashcheck>
                        <Files wsgi.py>
                                Require all granted
                        </Files>
                </Directory>

                WSGIDaemonProcess myweb python-path=/var/www/myweb python-home=/var/www/myweb/venv
                WSGIProcessGroup myweb
                WSGIScriptAlias / /var/www/myweb/myweb/wsgi.py
        </VirtualHost>



        # a2ensite myweb.com      
        # service apache2 reload  (혹은 service apache2 restart)


    5. 추가 설정

        # cd /var/www/myweb
        # chmod 664 db.sqlite3

        settings.py
        ALLOWED_HOSTS = ['myweb.com', 'localhost', '127.0.0.1']
