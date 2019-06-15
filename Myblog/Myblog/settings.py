"""
Django settings for Myblog project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
# -*- coding: UTF-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'XXX'

# SECURITY WARNING: don't run with debug turned on in production!
#测试环境
DEBUG =  True
#线上关闭，'django.contrib.staticfiles'失效，不再有报错新信息
#DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'django.contrib.staticfiles',

     # django-allauth必须安装的app
    'django.contrib.auth',
    'django.contrib.sites', 
    'allauth',
    'allauth.account',   
    'allauth.socialaccount',
    # 第三方账号相关的
    'allauth.socialaccount.providers.weixin', 
    'allauth.socialaccount.providers.github',
    # Django模板语言样式库
    'widget_tweaks',
    # 网站地图应用
    'django.contrib.sitemaps',
    #admin编辑器
    "mdeditor",
    #allauth用户个人资料扩展新建APP
    'Myaccount',
    # 博客应用
    'Storm',  
    # 评论应用
    'Comment',  

]

 # django-allauth相关设置
AUTHENTICATION_BACKENDS = (
      # django admin所使用的用户登录与django-allauth无关 
      'django.contrib.auth.backends.ModelBackend',
      # allauth 身份验证 
      'allauth.account.auth_backends.AuthenticationBackend',
)

#使用django.contrib.sites需要设置
SITE_ID = 1
#当用户登录时，既可以使用用户名也可以使用email，
ACCOUNT_AUTHENTICATION_METHOD = 'username_email' 
#要求用户注册时必须填写email
ACCOUNT_EMAIL_REQUIRED = True  
#注册成功后，会发送一封验证邮件，用户必须验证邮箱后，才能登陆
ACCOUNT_EMAIL_VERIFICATION ="optional"
# 邮箱确认邮件的截止日期(天数)
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3 
# 更改为True，用户一旦确认他们的电子邮件地址，就会自动登录
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True
#登录或注册后自动跳转到/accounts/profile/
LOGIN_REDIRECT_URL = '/accounts/profile/'

#allauth 在注册用户时，会给用户填写的邮箱发送一封激活邮件
# smtp 服务器
EMAIL_HOST = 'smtp.qq.com'
# 默认端口25，请求超时可尝试465
EMAIL_PORT = 465
#帐号xx
EMAIL_HOST_USER = 'xxx@qq.com'
# 授权码（注意不是密码）
EMAIL_HOST_PASSWORD = 'xxx'
# 是否使用了SSL 或者TLS
# EMAIL_USE_TLS = True  
EMAIL_USE_SSL = True
#发送人
EMAIL_FROM = 'xxx@qq.com' 
# 默认显示的发送人，（邮箱地址必须与发送人一致），不设置的话django默认使用的webmaster@localhost
DEFAULT_FROM_EMAIL = 'EOSONES博客 <374542101@qq.com>'

#__________________________________________________________________________________________________

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #提交form表单CSRF验证
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Middleware.auth.CountMiddleware',
]

ROOT_URLCONF = 'Myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates",],
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

WSGI_APPLICATION = 'Myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
import sys
# 添加 apps 目录
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Myblog',
        'USER': 'root', 
        'PASSWORD': 'xxx',
        'HOST':'localhost',
        'PORT':'3306',

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#设置中文
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'  #设置为中国时区

USE_I18N = True

USE_L10N = True

USE_TZ = False


#________________________________________在模板中要读取到预先配置文件夹及Url_________________________________________

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# 静态文件收集
STATIC_URL = '/static/'
#当执行python manage.py collectstatic时, 收集的静态文件放在该目录下.
#django会将STATICFILES_DIRS下的所有文件以及admin所需要用到的js,css,image文件全都放到STATIC_ROOT目录下.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'STATIC'),
)

# 媒体文件专属参数设置（需要加url识别才能访问）
MEDIA_URL = "/media/"   # 媒体文件别名(相对路径) 和 绝对路径
#存放上传的文件
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)

# 如果使用自定义用户model user，为了让 Django 能够识别自定义的用户模型，必须在此处添加app.自定义表名
AUTH_USER_MODEL = 'Myaccount.User'

#一个网站最基本的SEO就是设置TDK
# 网站描述
SITE_DESCRIPTION = "EOSONES的个人网站，记录生活的瞬间，分享学习的心得"
# 网站关键词
SITE_KEYWORDS = "EOSONES,网络,IT,技术,博客,Python"
# 网站页面
SITE_END_TITLE = "EOSONES的个人博客"


