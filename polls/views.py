from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    context = {
        'latest_question_list': latest_question_list,
    }
    #template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context, request)) 我们不再需要导入 loader和 HttpResponse，而是从django.shortcuts导入了render等价于下面的render
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #try+except ===
    question = get_object_or_404(Question, pk=question_id)
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)