from django.shortcuts import render
from .models import Meme
import requests
from django.http import HttpResponse

# Create your views here.

def add_to_db():
    try:
        memes = requests.get('https://api.imgflip.com/get_memes')
    except:
        return 0

    if memes:
        memes = memes.json()
        memes = memes['data']['memes']
        for meme in memes:
            Meme.objects.create(id=meme['id'],name=meme['name'],
                                url=meme['url'],width=meme['width'],
                                height=meme['height'],box_count=meme['box_count'])
        return 1
    else:
        return 0

def main(response):
    memes = Meme.objects.all()

    flag = 1
    if not memes:
        flag = add_to_db()


    if flag:
        memes = Meme.objects.all()
        return render(response,'main/landing.html',{'memes':memes})
    else:
        return HttpResponse("<h1>Error Encountered</h1>")
