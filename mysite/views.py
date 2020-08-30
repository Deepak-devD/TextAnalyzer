# I created this file
from django.http import HttpResponse
from django.shortcuts import render
# now creating a function and pass the argument request
def index(request):
    return render(request, 'index.html')
   # return HttpResponse('''<h1>hello</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">click the link below  </a> ''')
def News(request):
    return render(request, 'index2.html')
def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    full_Caps = request.POST.get('fullcaps', 'off')
    char_count = request.POST.get('charcount','off')
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)
    elif(full_Caps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Upper cased', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)
    elif (char_count == 'on'):
        analyzed = ""
        count=0
        for char in djtext:
            count+=1
        analyzed=count
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)
    else:
        return HttpResponse("Error")
