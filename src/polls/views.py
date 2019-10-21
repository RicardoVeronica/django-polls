from .models import Choice, Question
from django.urls import reverse
from django.views import generic
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render


class IndexView(generic.ListView):
    """
    List the latest 5 questions for publication dates
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions
        """
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """
    Detail for one question
    """
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    """
    Show result of a question
    """
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    """
    Youre vote
    """
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results_url',
                                            args=(question_id,)))
