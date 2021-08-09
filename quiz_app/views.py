from django.shortcuts import render
import requests
# from django.http import JsonResponse
from quiz_app.models import Add_Quiz 


def home(request):
    return render(request, 'home.html')

def select(request):
    select_topic = Add_Quiz.objects.all()
    context = {'select_topic': select_topic}
    return render(request, 'select.html', context)


# def api_question(request, id):
#     response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple').json()
#     questions = []

#     for raw_question in response.results:
#         question = {}
#         question['id'] = raw_question.id
#         question['question'] = raw_question.question
#         question['answer'] = raw_question.correct_answer
#         question['marks'] = raw_question.marks
#         options = []
#         options.append(raw_question.correct_answer)
#         options.append(raw_question.incorrect_answer[0])

#         if raw_question.incorrect_answer[1] != '':
#             options.append(raw_question.incorrect_answer[1])
        
#         if raw_question.incorrect_answer[2] != '':
#             options.append(raw_question.incorrect_answer[2])
        
#         question['options'] = options
         
#         questions.append(question)
        
#     return JsonResponse(questions , safe=False)

def play(request):
    response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple').json()
    # print(response)

    # for i in response.items(0):
    #     print(i)
        
    return render(request, 'play.html',{'response': response})

def rule(request):
    return render(request, 'rule.html')

def result(request):
    return render(request, 'result.html')
    
# def question_api(request):
#     response=request.get('https://opentdb.com/api.php?amount=10').json  ()
#     return render(request, 'home.html')

# def login(request):
#     return render(request, 'login.html')

