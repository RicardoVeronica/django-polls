from .models import Question
from django.shortcuts import HttpResponse, render, get_object_or_404


def index(request):
    """
    List the latest 5 questions for publication dates
    """
    template = 'polls/index.html'
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, template, context)


def detail(request, question_id):
    """
    Detail for one question
    """
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """
    Show result of a question
    """
    return HttpResponse(
        f"You're looking at the results of question {question_id}"
    )


def vote(request, question_id):
    """
    Youre vote
    """
    return HttpResponse(f"You're voting on question {question_id}")
