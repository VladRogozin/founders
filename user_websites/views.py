from django.shortcuts import render, redirect
from .forms import UserWebsiteForm
from .models import UserWebsite
from django.contrib.auth.decorators import login_required

import os
from django.conf import settings

from django.core.exceptions import ValidationError

def is_valid_file(file, allowed_extensions):
    return file.name.lower().endswith(tuple(allowed_extensions))

@login_required
def upload_website(request):
    try:
        user_site = request.user.userwebsite
    except UserWebsite.DoesNotExist:
        user_site = UserWebsite(user=request.user)

    error = None

    if request.method == 'POST':
        uploaded_file = request.FILES.get('uploaded_file')

        if uploaded_file:
            filename = uploaded_file.name
            ext = filename.split('.')[-1].lower()

            if ext not in ['html', 'css', 'js']:
                error = "Можно загружать только файлы с расширением .html, .css или .js"
            else:
                # Удаляем старый файл
                if ext == 'html' and user_site.html_file:
                    user_site.html_file.delete(save=False)
                    user_site.html_file = uploaded_file

                elif ext == 'css' and user_site.css_file:
                    user_site.css_file.delete(save=False)
                    user_site.css_file = uploaded_file

                elif ext == 'js' and user_site.js_file:
                    user_site.js_file.delete(save=False)
                    user_site.js_file = uploaded_file

                else:
                    # Просто добавляем, если ранее не было
                    if ext == 'html':
                        user_site.html_file = uploaded_file
                    elif ext == 'css':
                        user_site.css_file = uploaded_file
                    elif ext == 'js':
                        user_site.js_file = uploaded_file

                user_site.save()
                return redirect('upload_website')

    return render(request, 'user_websites/upload.html', {'error': error})





from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required

@login_required
def view_website(request):
    try:
        website = request.user.userwebsite
    except UserWebsite.DoesNotExist:
        return HttpResponse("У вас пока нет загруженного сайта.")

    html_content = website.html_file.read().decode('utf-8')
    css_content = website.css_file.read().decode('utf-8')
    js_content = website.js_file.read().decode('utf-8')

    # Используем BeautifulSoup для модификации HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Вставляем CSS в <head>
    if soup.head is None:
        soup.head = soup.new_tag('head')
        soup.html.insert(0, soup.head)

    style_tag = soup.new_tag('style')
    style_tag.string = css_content
    soup.head.append(style_tag)

    # Вставляем JS в конец <body>
    if soup.body is None:
        soup.body = soup.new_tag('body')
        soup.html.append(soup.body)

    script_tag = soup.new_tag('script')
    script_tag.string = js_content
    soup.body.append(script_tag)

    # Возвращаем сгенерированный HTML как полноценный ответ
    return HttpResponse(str(soup), content_type='text/html')


