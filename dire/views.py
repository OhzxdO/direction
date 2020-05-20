from django.shortcuts import render
from django.http import HttpResponse
from dire.models import words
import getwords.getwords as g
from dire.models import classfications

# Create your views here.

def getwords(request):
    cl = classfications(classfication='考研必备单词')
    cl.save()
    for i in range(1,275):
        for j in range(19):
            try:
                word,sound,plain,example = g.getwords(13,i,j)
                data = words(word=word,sound=sound,plain=plain,example=example,classfication=cl)
                data.save()
            except:
                print('error')
        if i%10 == 0:
            print(i)
    return HttpResponse('ok')