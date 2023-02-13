from django.shortcuts import render

# Create your views here.

def application(request):
    if request.method == "POST":
        text = request.POST['text']
        text = text.split()
        # text = len(text)


        Vowels = 'aeiouAEIOU'
        Vowels = ''
        Consonants = ''
        Words = ''
        Characters = '' 

        for i in text:
            if i in Vowels:
                Vowels += 1 

            if i in Consonants:
                Consonants += 1

            if i in Words:
                Words += 1

            if i in Characters :
                Characters += 1
        

    return render(request, 'index.html')