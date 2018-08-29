import requests
from PIL import Image, ImageFont, ImageDraw
from django.http import JsonResponse
from .models import AppModel, Result
from random import randint
import textwrap


def getdp(request):
    token = request.session['token']; id = request.session['id']
    url = 'https://graph.facebook.com/{}/picture/'.format(id)
    args = {'access_token':token,'width':300, 'height':300}
    result =requests.get(url,params=args,stream=True)
    if result.status_code == 200:
        return result.raw
    

def getname(request, name="name"):
    token = request.session['token']; id = request.session['id']
    url = 'https://graph.facebook.com/{}/'.format(id)
    args = {'access_token':token,'fields':name}
    result =requests.get(url,params=args)
    if result.status_code==200:
        print(result.json()[name])
        return result.json()[name]


def upload(data):
    url = "https://api.imgur.com/3/image"
    headers = {'Authorization': 'Client-ID e996a05c77b38b6'}
    response = requests.post(url, data=data, headers=headers)
    if response.status_code==200:
        return response.json()['data']['link']


def resultimg(request,pk):
    app = AppModel.objects.get(pk=pk)

    name = getname(request,name='first_name')
    with Image.open(getdp(request)) as dp, Image.open('background.png') as bg:
        bg.paste(dp,(20,20))

        text = app.placeholder.format(name=name)
        text = textwrap.fill(text,width=20)
        random = app.randoms.split(",")
        random = random[randint(0, len(random)-1)]
        random = textwrap.fill(random,width=12)

        font = ImageFont.truetype('anomali.otf',size=28, encoding='UTF-8')
        tw,th = font.getsize_multiline(text)

        bgd = ImageDraw.Draw(bg)
        bgd.multiline_text((350+(290-tw)/2,40), text, font=font, align='center')

        font = ImageFont.truetype('brush.otf', size=38, encoding='UTF-8')
        tw,th = font.getsize_multiline(random)

        bgd.multiline_text((350+(290-tw)/2, 130), random, font=font, align='center')

        bg.save('resultimage.png')
        bg.close();dp.close()

    with open("resultimage.png","rb") as f:
        r = upload(f)
    rpk= saveresult(name,r,pk)
    return JsonResponse({'link':r,'name':name,'resultpk':rpk})



def saveresult(name,url,pk):
    r = Result(name=name, imgurl=url,apppk=pk)
    r.save()
    return r.pk

