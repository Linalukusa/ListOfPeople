from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View

from .models import People
from .forms import PostForm

import json as simplejson

class index(View):
    form = PostForm
    def post(self, request):
        posts = People.objects.all()
        form = self.form(self.request.GET)
        if form.is_valid():
            return People.objects.filter(name__icontains=form.cleaned_data['name'])
        response = {}

        if request.POST.get('action') == 'post':
            name = request.POST.get('name')
            response = {}
            response['name'] = name
            People.objects.create(
            name = name,
            )
            return HttpResponse(simplejson.dumps(response), content_type="application/json")
        return render(request, 'home/index.html', {'posts':posts})