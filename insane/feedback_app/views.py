from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def submit_feedback(request):
    if request.method == 'POST':
        fullname =request.POST['fullname']
        subject = request.POST['subject']
        message = request.POST['message']
        add_feedback = Feedback(fullname=fullname, subject=subject, message=message)
        add_feedback.save()
        messages.success(request, "FeedBack submitted successfully")
        return redirect('/')
    return render(request, './feedback_app/submit_feedback.html')
    
 
def view_feedback(request):
    flist = Feedback.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(flist, 2)
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        feedbacks = paginator.page(1)
    except EmptyPage:
        feedbacks = paginator.page(paginator.num_pages)
    return render(request, './feedback_app/view_feedback.html', {'feedbacks': feedbacks})


 
 
 
 
 
 
 


