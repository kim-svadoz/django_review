from django.shortcuts import render, redirect
from .models import Musician
from .forms import MusicianForm

# Create your views here.
def index(request):
    # .all()로 조회하면 querySet형태
    # querySet은 list처럼 사용가능
    musicians = Musician.objects.all()
    context = {
        'musicians' : musicians
    }
    return render(request, 'musicians/index.html', context)

def create(request):
    if request.method == "POST":
        # 사용자의 요청 정보를 담아준다.
        form = MusicianForm(request.POST)
        # forms를 상속받았기 때문에 사용가능
        if form.is_valid():
            # Musician가 models에게 받은 메서드
            # ModelForm을 정의 할 때
            # class Meta :
            # model = Musiciain을 담아줬따
            musician = form.save()
            # app_name : path_name
            return redirect('musicians:index')
    else:
        # MusicianForm 불러오기
        # form은 MusicianForm의 인스턴스
        # MusicianForm이 가진 정보를 가짐.
        # MusicianForm은 Musician의 정보
        # template에서 보여줄 tag들
        form = MusicianForm
        print(form)
    context = {
        'form' : form
    }
    return render(request, 'musicians/create.html', context)

# 함수정의 함수이름(사용자요청정보, url에 작성한 변수명)
def detail(request, musician_pk):
    # Model.objects.get(pk=변수명)
    musician = Musician.objects.get(pk=musician_pk)
    context = {
        'musician' : musician
    }
    return render(request, 'musicians/detail.html', context)

def update(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    if request.method=="POST":
        form = MusicianForm(request.POST, instance = musician)
        if form.is_valid():
            musician = form.save()
            return redirect('musicians:index')
    else:
        form = MusicianForm(instance = musician)
    context = {
        'form' : form
    }
    return render(request, 'musicians/create.html', context)

def delete(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    musician.delete()
    return redirect('musicians:index')