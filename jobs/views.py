# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Job, Company

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', { 'jobs': jobs })

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', { 'job': job })
