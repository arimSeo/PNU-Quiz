from django.shortcuts import render
from .models import Question
from django.core.paginator import Paginator

lst = []
# answers = Question.objects.all()
# anslist = []

# for i in answers:
#     anslist.append(i.answer)

def home(request):
    lst.clear()
    return render(request, 'home.html')

def quiz(request):
    obj = Question.objects.all()
    count = Question.objects.all().count()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage, Invalidpage):
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz.html', {'obj' : obj, 'questions' : questions, 'count':count, 'lst':lst})

def result(request):
    answers = Question.objects.all()
    anslist = []
    for i in answers:
        anslist.append(i.answer)
        
    score = 0
    if len(lst)==len(anslist):
        for i in range(len(lst)):
            if lst[i]==anslist[i]:
                score += 1
    else:
        return render(request, 'error.html')
    return render(request, 'result.html', {'score':score, 'lst':lst, 'anslist':anslist})

def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)
