from django.forms import ModelForm
from .models import Feedback
 
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['id', 'name','email','comment']


# views.py

# from django.shortcuts import render, redirect
# from .models import *
# from .forms import FeedbackForm
 
# def create(request):
#     if request.method=='POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/feedback/list')
#     else:
#         form = FeedbackForm()
 
#     return render(request, 'feedback.html', {'form': form})        


# def create(request):
#     form = FeedbackForm()
#     return render(request, 'feedback.html', {'form': form})