from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from Bot.forms import IndexForm, ConsentForm, SurveyForm
from Bot.Main.InputRecogniser import InputRec
from Bot.models import Sessions, Questionnaire
import json

class index(TemplateView):
    template_name = 'Bot/index.html'

    def get(self, request):
        form = IndexForm()
        return render(request, self.template_name, {'form': form,})
    
    def post(self, request):
        form = IndexForm(request.POST)
        
        if form.is_valid():
            text = form.cleaned_data['post']
            form = IndexForm()
            content = []
            uinput = text
            test = request.session._session_key
            request.session.set_expiry(0)
            print(test)
            if not Sessions.objects.filter(SessionKey=test).exists():
                s = Sessions(SessionKey=test)
                s.save()
            t = Sessions.objects.get(SessionKey=test)
            jsonDec = json.decoder.JSONDecoder()
            if t.StatementPath == "":
               pass
            else:
               content = jsonDec.decode(t.StatementPath)
            content.append("User: " + uinput)
            t.StatementPath = json.dumps(content)
            t.save()
            output = InputRec(uinput, test)
            t = Sessions.objects.get(SessionKey=test)
            content = jsonDec.decode(t.StatementPath)
            content.append("Chatbot: " + str(output))
            t.StatementPath = json.dumps(content)
            t.save()
            chatlog = jsonDec.decode(t.StatementPath)
        args = {'form': form, 'text': output, 'Input': chatlog}
        return render(request, self.template_name, args)


class Consent(TemplateView):
    template_name = 'Bot/Consent.html'

    def get(self, request):
        form = ConsentForm()
        test = request.session._session_key
        request.session.set_expiry(0)
        print(test)
        return render(request, self.template_name, {'form': form})

class Intro(TemplateView):
    template_name = 'Bot/Intro.html'

    def get(self, request):
        
        return render(request, self.template_name)

class QuestionnaireView(TemplateView):
    template_name = 'Bot/Questionnaire.html'

    def get(self, request):
        form = SurveyForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SurveyForm(request.POST)
        if form.is_valid():
            test = request.session._session_key
            request.session.set_expiry(0)
            print(test)
            if not Questionnaire.objects.filter(SessionKey=test).exists():
                s = Questionnaire(SessionKey=test)
                s.save()
            t = Questionnaire.objects.get(SessionKey=test)
            t.Question1 = form.cleaned_data['Question1']
            t.Question2 = form.cleaned_data['Question2']
            t.Question3 = form.cleaned_data['Question3']
            t.Question4 = form.cleaned_data['Question4']
            t.Question5 = form.cleaned_data['Question5']
            t.Question6 = form.cleaned_data['Question6']
            t.Question7 = form.cleaned_data['Question7']
            t.Question8 = form.cleaned_data['Question8']
            t.save()
        
        return render(request, self.template_name, {'form': form})