# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Job, Company

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 4) # Show 4 jobs per page

    page = request.GET.get('page')

    try:
        job_pages = paginator.page(page)
    except PageNotAnInteger:
        job_pages = paginator.page(1)
    except EmptyPage:
        job_pages = paginator.page(paginator.num_pages)

    return render(request, 'jobs/job_list.html', { 'jobs': job_pages })

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', { 'job': job })
