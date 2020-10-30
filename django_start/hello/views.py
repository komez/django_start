from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

# Create your views here.
#view functionのことをコントローラーと呼ぶ場合もある
def start(request):
    return HttpResponse('Hello Django')

#レンダリングの対象は辞書 ''key は str''
def index(request):
    params={
        'user':'米崎 亮太',
        'age':'23',
        'form': HelloForm(),
        'message': 'msg',
    }
    if request.method=='POST':
        params['message'] = '入力成功？'
        params['form'] = HelloForm(request.POST)

    return render(request, 'hello/index.html', params)


""" 
def form(request):
    msg = request.POST['msg']#request.POSTはフォームから値を取得する
    params = {
        'user':'米崎 亮太',
        'age':'23',#<input name='msg'
        'msg':msg,
    }
    return render(request, 'hello/index.html', params) """