from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import resp_serialize
from .forms import InputForm
from .utils import text_cleaner as tc
import regex as re

# Create your views here.

def home(request):
    context ={}
    context['form']= InputForm()
    return render(request, "index.html", context)

@api_view(['Post'])
def get_response(request, format=None):
    if request.method=='POST':
        try:
            inp=request.data['desc']
            inpt=tc.strip_accents(inp.lower())
            inpt=re.sub(r'\d+', '', inpt)
            inpt=tc.replace_words(inpt)
            inpt=tc.remove_punctuations(inpt)
            #inpt=tc.remove_stopwords(inpt)
            inpt=tc.lem(inpt)
            inpt=tc.strip_space(inpt)
            if len(inpt)>=20:
                predict=tc.get_pred(inpt)
                pred=[{"status":1,"desc":inp,"pred":predict}]
            else:
                pred=[{"status":0,"desc":inp,"pred":'Too short a description.'}]
            result=resp_serialize(pred, many=True).data
            return Response(result)
        except:
            pred=[{"status":0,"desc":"Null","pred":"Null"}]
            result=resp_serialize(pred, many=True).data
            return Response(result)
