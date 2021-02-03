from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, PnuUser, Answer

def home(request):
    if request.GET:
        user = PnuUser()
        user.name = request.GET['name']           #<input txt > name="name"
        if request.GET['name'] == "":
            user.name = "익명"
        user.save()
        return redirect("quiz", user.pk)
    return render(request, "home.html")


def quiz(request,pk):
    user = get_object_or_404(PnuUser, pk=pk)
    aans=get_object_or_404(Answer)

    num = 1
    if request.POST:
        num = int(request.POST['quiz_id']) + 1          #quiz_id, answer,은 <input name>으로
        user.answer = user.answer + request.POST['answer']
        # user.save()     #해야지 전체 답안지(숫자리스트)가 나옴-지우면 틀린답은 안나옴..
        # 차피 밑에서 user.save를 해주기 때무네 없어도 됨 ㅎㅎ..
        if request.POST['answer'] == aans.ans[num-2]:    #문제 index 0(1번답) ~
            user.score += 1
            user.save()

        if num > 4:     #4문제 기준-> 10문제:10으로 고치기
            return redirect("result", pk)
        
    quiz = get_object_or_404(Question, id=num)      #id값을 문제번호num로
    
    return render(request, "quiz.html", {'quiz':quiz})


def result(request,pk):
    user = get_object_or_404(PnuUser, pk=pk)

    # 평균 점수 구하기
    all_user = PnuUser.objects.all()
    scorelst = []
    for i in all_user:
        each_score = i.score
        scorelst.append(each_score)
    average_score = round(sum(scorelst)/len(all_user))

    if len(user.answer) == 10:       #4문제 기준-> 10문제:10으로 고치기
        while True:
            try:
                pass
                break
            except:
                return render(request, 'error.html')
    return render(request, "result.html", {"user":user, 'average_score':average_score})

