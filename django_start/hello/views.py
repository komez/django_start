from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#view functionのことをコントローラーと呼ぶ場合もある
def hello(request):
    return HttpResponse('Hello Django')

#レンダリングの対象は辞書 ''key は str''
def index(request):
    params={'user':'米崎 亮太',
            'age':'23',
            }
    return render(request, 'hello/index.html', params)