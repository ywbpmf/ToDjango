from django.shortcuts import render
import os
import datetime
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


class ArticleListView(ListView):
    # template_name 用于指定使用哪个模板进行渲染
    template_name = 'blog/article_index.html'

    # context_object_name 用于给上下文变量取名(在模板中使用该名字)
    context_object_name = 'article_list'

    # 页面类型，分类目录或标签列表等
    page_type = ''
    paginate_by = settings.PAGINATE_BY
    page_kwarg = 'page'

    def get_view_cache_key(self):
        return self.request.get['pages']


