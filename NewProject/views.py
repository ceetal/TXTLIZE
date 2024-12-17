from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   return render(request,'index.html')
def hello(request):
    return render(request,'hello.html')
    # return HttpResponse("<a href =https://www.google.com>Google</a>""<a href =https://www.facebook.com>Facebook</a>")
def analyze(request):
    djtext =(request.POST.get('text','default'))
    removepunc = (request.POST.get('removepunc','off'))
    uppercase = (request.POST.get('uppercase','off'))
    newlinespace = (request.POST.get('newlinespace','off'))
    extraspace = (request.POST.get('extraspace','off'))
    charactercount = (request.POST.get('charactercount','off'))
    # print(removepunc)
    # print(djtext)
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''  # Define punctuations to remove
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(uppercase=='on'):
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Upper Case','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if(newlinespace =='on'):
        analyzed = djtext.replace("\n", "").replace("\r", "") 
    #     analyzed=''
    #     for char in djtext:
    #         if char!='\n':
    #             analyzed = analyzed + char
        
        params = {'purpose': 'Remove New Line','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if(extraspace =='on'):
        analyzed = " ".join(djtext.split())
        params = {'purpose': 'Remove spaces','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if(charactercount =='on'):
        analyzed = len(djtext)
        params = {'purpose': 'Counting characters','analyzed_text':analyzed}
        djtext = analyzed
        
    if (removepunc!= 'on'and uppercase!='on' and newlinespace!='on' and extraspace!='on' and charactercount!='on'):
        return HttpResponse("Please select any operation to Perform")
    return render(request,'analyze.html',params)