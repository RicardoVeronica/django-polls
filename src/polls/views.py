from django.shortcuts import HttpResponse


def index(request):
    """
    Show simple hello world message in browser
    """
    return HttpResponse("Hello world")


def detail(request, question_id):
    """
    Detail for one question
    """
    return HttpResponse(f"You're looking at question {question_id}")


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
