from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
  
def analyze(request):
            djtext=request.GET.get('text','default')
            removepunc=request.GET.get('removepunc','off')
            fullcaps=request.GET.get('fullcaps','off')
            newlineremover=request.GET.get('newlineremover','off')
            spaceremover=request.GET.get('spaceremover','off')
            charcount=request.GET.get('charcount','off')
            print(removepunc)
            # analyzed=djtext
            punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            if removepunc=="on":
                    analyzed=""
                    for char in djtext:
                        if char not in punctuations:
                             analyzed= analyzed +char
            elif(fullcaps=="on"):
                    analyzed=" "
                    for char in djtext:
                        analyzed=analyzed+ char.upper()

            elif(newlineremover=="on"):
                    analyzed=" "
                    
                    for char in djtext:
                        if char!='\n':
                            analyzed=analyzed+ char
            elif(spaceremover=="on"):
                    analyzed=" "
                    
                    for index,char in enumerate(djtext):
                        if djtext[index]==" " and djtext[index+1]==" ":
                            pass
                        else:        
                            analyzed=analyzed+ char
            elif(charcount=="on"):
                    analyzed=" "
                    count=0
                    for char in djtext:
                        count+=1

                    analyzed=analyzed+str(count)    
            
            else:
                analyzed=djtext
            params={'purpose':"remove punctuation",'analyzed_text':analyzed}
            return render(request,'analyze.html',params)
            