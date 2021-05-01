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

        if str(data.get('replace_this')):
            if str(data.get('replace_with_this')):
                text = text.replace(str(data.get('replace_this')), str(data.get('replace_with_this')))
            else:
                pass

        if data.get('removeSpace'):
            text = text.replace(' ', '')
            
        if data.get('case'):
            if data.get('case') == 'lower': text = text.lower()
            elif data.get('case') == 'upper': text = text.upper()
            else: pass
    

        text_data = {
            'word_count':len(text.split(' ')),
            'letter_count':len(text),
            'text':text
        }

        return render(req, "index.html", text_data)

    return render(req, "index.html")