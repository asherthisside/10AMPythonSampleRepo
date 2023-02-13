from django.shortcuts import render

def javed(request):
    return render(request,'mango.html')

def details(request):
    text = request.POST['text']
    word_list = text.split()
    list_length = len(word_list)

    vowels = "AEIOUaeiou"
    count_vow = 0
    count_cons = 0
    count_up = 0
    count_lower = 0
    count_sp = 0
    count_digit = 0
    count_char = 0

    for i in text:
        if i in vowels:
            count_vow+=1
        if i not in vowels:
            count_cons+=1
        if i.isupper():
            count_up+=1
        if i.lower():
            count_up+=1
        if i.isalnum():
            count_sp+=1


    context = {
        'list_length':list_length,
        'count_vow' :count_vow,
        'count_cons' : count_cons,
        'count_up': count_up,
        'count_lower' : count_lower,
        'count_sp' : count_sp,
        'count_digit': count_digit,
        'count_char': count_char,

    }

    return render(request,'result.html',context)
# 