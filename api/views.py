from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .mixins import CSRFExempt
from .ml_models import result
from django.views.decorators.csrf import csrf_exempt
import json
#from django.conf import settings
from hatespeech import settings

# Create your views here.
class Index(CSRFExempt,View):
    def get(self,request,*args,**kwargs):
        text=self.request.GET.get("text")
        print(text)
        csv=getattr(settings, "csv1")
        #print("read csv")
        model=getattr(settings, "model1")
        res1=result.user_speech(text,model,csv)
        if res1==True:
            data={"message":True}
            return HttpResponse(json.dumps(data),content_type="application/json",status=200)
        else:
            data={"message":False}
            return HttpResponse(json.dumps(data),content_type="application/json",status=200)
