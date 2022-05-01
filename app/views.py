from django.shortcuts import render,HttpResponse
import random
from utils.tencent.sms import send_sms_single
from django.conf import settings
# Create your views here.
def send_sms(request):
    #send message
    tpl = request.Get.get('tpl')
    settings.TENCENT_SMS_TPL.get(tpl)
    template_id = settings.TENCENT_SMS_TPL.get(tpl)
    if not template_id:
        return HttpResponse("Template not exsts")

    code=random.randrange(1000,9999)
    res = send_sms_single('151131289',template_id,[code, ])
    if res['resulr'] == 0:
        return HttpResponse("success")
    else:
        return HttpResponse("ERROR MESSGAE")