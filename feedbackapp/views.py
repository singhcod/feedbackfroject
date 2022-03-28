from django.shortcuts import render
from.models import FeedbackData


def feedback_view(request):
    if request.method == "POST":
       name1= request.POST.get('name')
       rating1 = request.POST.get('rating')
       feedback1 = request.POST.get('feedback')

       FeedbackData(
           name= name1,
           rating = rating1,
           feedback = feedback1
       ).save()

       feedbacks = FeedbackData.objects.all()
       return render(request, 'feedback.html', {'singh': feedbacks})



    else:
        feedbacks = FeedbackData.objects.all()
        return render(request,'feedback.html',{'singh':feedbacks})


