from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ApplicantForm
from django.core.serializers.json import DjangoJSONEncoder
import json

def handle_form(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)

        if 'save_draft' in request.POST:
            if form.is_valid():
                draft_data = {
                    'name': form.cleaned_data.get('name'),
                    'father_name': form.cleaned_data.get('father_name'),
                    'mother_name': form.cleaned_data.get('mother_name'),
                    'gender': form.cleaned_data.get('gender'),
                    'permanent_address': form.cleaned_data.get('permanent_address'),
                    'present_address': form.cleaned_data.get('present_address'),
                    'mobile_no': form.cleaned_data.get('mobile_no'),
                    'email': form.cleaned_data.get('email'),
                    'id_no': form.cleaned_data.get('id_no'),
                    'degree_name': form.cleaned_data.get('degree_name'),
                    'admission_session': form.cleaned_data.get('admission_session'),
                    'passing_year': form.cleaned_data.get('passing_year').isoformat() if form.cleaned_data.get('passing_year') else None,
                    'cgpa': form.cleaned_data.get('cgpa'),
                }
                json_data = json.dumps(draft_data, cls=DjangoJSONEncoder)
                request.session['draft_student_data'] = json_data
                return redirect('handle_form')

        elif 'submit' in request.POST:
            if form.is_valid():
                student = form.save(commit=False)
                student.save()
                return redirect('handle_form')
    else:
       draft_data = request.session.get('draft_student_data')
       if draft_data and isinstance(draft_data, dict):
            initial_data = {
                'name': draft_data.get('name'),
                'father_name': draft_data.get('father_name'),
                'mother_name': draft_data.get('mother_name'),
                'gender': draft_data.get('gender'),
                'permanent_address': draft_data.get('permanent_address'),
                'present_address': draft_data.get('present_address'),
                'mobile_no': draft_data.get('mobile_no'),
                'email': draft_data.get('email'),
                'id_no': draft_data.get('id_no'),
                'degree_name': draft_data.get('degree_name'),
                'admission_session': draft_data.get('admission_session'),
                'passing_year': draft_data.get('passing_year'),
                'cgpa': draft_data.get('cgpa'),
            }
            # Ensure 'passing_year' is a datetime object if it's present
            if 'passing_year' in initial_data and isinstance(initial_data['passing_year'], str):
                from datetime import datetime
                initial_data['passing_year'] = datetime.strptime(initial_data['passing_year'], '%Y-%m-%d').date()
       else:
            initial_data = {}

            form = ApplicantForm(initial=initial_data)

    return render(request, 'index.html', {'form': form})