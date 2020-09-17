from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home2.html')


def analyze(request):
    # if any text is given in textarea then that text will be assigned to user_text or if it was empty then default will be the value of user_text
    user_text = request.POST.get('Text', 'default')

    # this will take the value of checkbox, if it is ticked then removepunc's value will be on else it will be off
    removepunc = request.POST.get('removepunc', 'off')
    allcaps = request.POST.get('allcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    removenum = request.POST.get('removenum', 'on')
    purpose = ''

    # check which checkbox is on
    if removepunc == 'on':
        result = ''
        Punctuations = '''`~!@#$%^&*()-_+{}[]:;"'<>?/.,'''
        for char in user_text:
            if char not in Punctuations:
                result += char
        param = {'purpose': 'Removing Punctuations', 'final_outcome': result}
        user_text = result
        purpose += 'Removing Punctuations,'
       

    if allcaps == 'on':
        result = ''
        result = user_text.upper()
        param = {'purpose': 'Capitalizing every character',
                 'final_outcome': result}
        user_text = result
        purpose += ' Capitalizing every character,'
       

    if newlineremove == 'on':
        result = ''
        for char in user_text:
            if char != '\n' and char != '\r':
                result += char
        param = {'purpose': 'Removing Newline', 'final_outcome': result}
        user_text = result
        purpose += ' Removing Newline,'
       
    
    
    if removenum == "on":
        result = ''
        number = '''0123456789'''
        for char in user_text:
            if char not in number:
                result += char
        param = {'purpose': 'Removing Numebrs', 'final_outcome': result}
        user_text = result
        purpose += ' Removing Numbers,'

    if extraspaceremove == 'on':
        result = ''
        for index, char in enumerate(user_text):
            if not (user_text[index] == ' ' and user_text[index + 1] == ' '):
                result += char
        param = {'purpose': 'Removing Unwanted Spaces',
                 'final_outcome': result}
        user_text = result
        purpose += ' Removing Unwanted Spaces,'
        

    if (removepunc != 'on' and allcaps != 'on' and newlineremove != 'on' and removenum != 'on' and extraspaceremove != 'on'):
        return render(request, 'empty.html')

    param = {'purpose': purpose, 'final_outcome': result}
    return render(request, 'analyze2.html', param)


def about(request):
    return render(request, 'about.html')
