import re
from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    if req.method == 'POST':
        
        print("POST Method called")
        
        data = req.POST
        text = data.get('text')

        
        
        if data.get('removePunc'):
            text = re.sub(r'[^\w\s]','', text)

        if data.get('case'):
            if data.get('case') == 'lower': text = text.lower()
            elif data.get('case') == 'upper': text = text.upper()
            else: pass
        
        if data.get('removeSpace'):
            text = text.replace(' ', '')

        text_data = {
            'word_count':len(text.split(' ')),
            'letter_count':len(text),
            'text':text
        }

        return render(req, "index.html", text_data)

    return render(req, "index.html")