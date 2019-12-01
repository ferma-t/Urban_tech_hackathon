# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.db.models import Q, Max, Count
from django.db.models import Q, Max, Count


@login_required(login_url='/accounts/login/')
def home(request):
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'index.html',
        {            
            'year': datetime.now().year,    
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'about.html',
        {            
            'year': datetime.now().year,    
        }
    )