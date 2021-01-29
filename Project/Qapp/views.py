from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, User, Answer
from django.core.paginator import Paginator


def home(request):
    if request.GET:
        challenger = User()
        challenger.name = request.GET['name']           #<input txt > name="name"
        challenger.save()
        return redirect("quiz", challenger.pk)
    return render(request, "home.html")


def quiz(request,pk):
    user = get_object_or_404(User, pk=pk)
    aans=get_object_or_404(Answer)

    num = 1
    if request.POST:
        num = int(request.POST['quiz_id']) + 1          #quiz_id, answer,은 <input name>으로
        user.answer = ''.join([user.answer, request.POST['answer']])
        user.save()
        if request.POST['answer'] == aans.ans[num-2]:    #문제 index 0(1번답) ~
            user.result += 1
            user.save()

        if num > 4:     #4문제 기준-> 10문제:10으로 고치기
            return redirect("result", pk)
        
    quiz = get_object_or_404(Question, id=num)      #id값을 문제번호num로
    
    return render(request, "quiz.html", {'quiz':quiz})


def result(request,pk):
    user = get_object_or_404(User, pk=pk)
    if len(user.answer) == 4:           #4문제 기준!! ->10문제: 10으로 고치기
        while True:
            try:
                pass
                break
            except:
                return render(request, 'error.html')
    return render(request, "result.html", {"user":user})

