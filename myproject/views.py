from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return render(request, 'index.html')

def nitin(request):
    return HttpResponse("nitinbora")

def analyze(request):
    text1=request.POST.get('text','default')
    text2=request.POST.get('removepunc','off')
    s='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    k=""
    for i in text1:
        if(i not in s):
            k=k+i

    if(text2!='off'):
        params={'name':k,'pu':text2}
    else:
        params={'name':text1,'pu':text2}

    return render(request, 'analyze.html',params)


