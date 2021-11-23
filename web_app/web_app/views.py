from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from . import validator


def initial_page(request):
    return HttpResponse('''<a href='http://127.0.0.1:8000/albacorizer'>Albacorizer</a>
    <br><a href='parser'>Parser</a><br><a href='validator'>Validator</a>''')


def first_page(request):
    return HttpResponse("This page corresponds to Albacorizer.")


def second_page(request):
    return HttpResponse("This page corresponds to Parser.")


def third_page(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def code_validator(request):
    questions_json = request.POST.get('question_json')
    sections_json = request.POST.get('section_json')

    # Collecting the validator variables from index.html
    auto_answers = request.POST.get('auto_answers', 'off')
    duplicate_id = request.POST.get('duplicate_id', 'off')
    jumps = request.POST.get('jumps_check', 'off')
    inactive_q_group = request.POST.get('inactive_q_group', 'off')
    mandates_not_connected = request.POST.get('mandates_not_connected', 'off')
    print(auto_answers)

    issues = validator.current_question_data(questions_json, sections_json)
    issues_list = issues.split('\n')
    print(issues_list)
    len_of_elements = len(issues_list) - 1
    issues_list.pop(len_of_elements)
    params = {"issues_to_print": issues_list}
    return render(request, 'validator_result.html', params)
