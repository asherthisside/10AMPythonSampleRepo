from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def result(request):
    name=request.GET['username'] 
    ls=len(name)
    word=len(name.split())
    val=['a','e','i','o','u']
    val_count = 0
    consonatcount = 0
    for i in name:
        if i.isalpha():
            if i in val or i.lower() in val:
                val_count+=1
            else:
                consonatcount+=1
    data={'name':name,'ls':ls,'word':word,'val_count':val_count,
          'consonatcount':consonatcount
        }
    return render(request,'result.html',data)


