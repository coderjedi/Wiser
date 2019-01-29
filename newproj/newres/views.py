from django.shortcuts import render
from newres import forms
from django.views.generic import View,ListView
# Create your views here.

def user_data_form(request):
    form1=forms.Userform()
    if request.method=='POST':
        form1=forms.Userform(request.POST)
        if form_is_valid():
            form1.save(commit=True)
            return name_of_view_to_redirect_to(request)
    return render(request,'newres/userformpage.html',{'form':form1})

class PreassesmentoneView(generic.ListView):
    template_name = 'questions/block1.html'
    context_object_name = 'Question_list_1'

    def get_queryset(self):
        return Question.objects.filter(question_id=1)

class PreassesmenttwoView(generic.ListView):
    template_name = 'questions/block2.html'
    context_object_name = 'Question_list_2'

    def get_queryset(self):
        return Question.objects.filter(question_id=2)

class PreassesmentthreeView(generic.ListView):
    template_name = 'questions/block3.html'
    context_object_name = 'Question_list_3'

    def get_queryset(self):
        return Question.objects.filter(question_id=3)

class PreassesmentfourView(generic.ListView):
    template_name = 'questions/block4.html'
    context_object_name = 'Question_list_4'

    def get_queryset(self):
        return Question.objects.filter(question_id=4)
