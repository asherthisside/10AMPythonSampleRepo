from django.shortcuts import render


def word(request):
    return render(request,'word.html')

def word_count(request):
   
    if request.method == 'POST':
        text = request.POST['text']
        word_list = text.split()
        list_length = len(word_list)

    return render(request,'word_count.html',{'list_length':list_length})
    

def vowel(request):
    return render(request,'vowel.html')

def vowel_count(request):
    if request.method == 'POST':
        text = request.POST['text']

        vowels = "AEIOUaeiou"
        count_vow = 0


        for i in text:
            if i in vowels:
                count_vow+=1
    return render(request,'vowel_count.html',{'count_vow':count_vow})



def cons(request):
    return render(request,'cons.html')


def cons_count(request):
    if request.method == 'POST':
        text = request.POST['text']

        vowels = "AEIOUaeiou"
        count_cons = 0


        for i in text:
            if i  not in vowels:
                count_cons+=1
    return render(request,'cons_count.html',{'count_cons':count_cons})




def char(request):
    return render(request,'char.html')


def char_count(request):
    if request.method == 'POST':
        text = request.POST['text']
        length = len(text)
            
    return render(request,'char_count.html',{'length':length})





