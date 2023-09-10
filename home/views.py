from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import default_storage
from home.models import submission
import os
from django.contrib import messages
import datetime
from datetime import date  
from django.http import JsonResponse
from home.serializer import SubmissionSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here


# class HackathonList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'index.html'

#     def get(self, request):
#         hackathons = submission.objects.all()
#         serializer = SubmissionSerializer(hackathons, many=True)
#         return Response({'posts': serializer.data})


# class MyModelCreateView(generics.CreateAPIView):
#     serializer_class = SubmissionSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# class HackathonList(APIView):

#     queryset = submission.objects.all()
#     serializer_class = SubmissionSerializer
# #     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self,request):
#         hackathons = submission.objects.all()
#         serializer = SubmissionSerializer(hackathons, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = SubmissionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, 
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, 
#                         status=status.HTTP_400_BAD_REQUEST)

def home(request):
     #to remember status of sorted order
     selected_option = request.session.get('selected_option')
     #fetching all data 
     hdata=submission.objects.all()
     return render(request, "index.html",{'posts':hdata,'selected_option': selected_option, 'active_link': "ALL"})


def favourite(request):
     selected_option = request.session.get('selected_option')
     hdata=submission.objects.all()
     hdata=submission.objects.all()
     n=len(hdata)
     hndata=[]
     for k in hdata:
          if k.flag==1:
               hndata.append(k)
     return render(request, "index.html",{'posts':hndata,'selected_option': selected_option,'active_link': "FAV"})



## search box and sorting 
def search(request):
    if request.method=='POST':
        selected_option = request.POST.get('order')
        request.session['selected_option'] = selected_option
        query = request.POST.get('search-query')
        order = request.POST.get('order')
        # process the search query
        if query == '':     
          results = submission.objects.all()
        else:
          results = submission.objects.filter(Title__icontains=query)

        
        if order == 'newest':
          print(order)
          results=results.order_by('-pub_date')
        elif order == 'oldest':
          print(order)
          results=results.order_by('pub_date')
        elif query=='':
          return redirect('/')
        return render(request, "index.html",{'posts':results,'selected_option': selected_option,'active_link': "ALL"})


###### ULPOADING NEW ENTRY
def upload(request):
     if request.method=="POST":
          title=request.POST['title']
          summary=request.POST['summary']
          description=request.POST['description']
          hackathonname=request.POST['hackathon-name']
          hackathonstartdate=request.POST['hackathon-start-date']
          hackathonenddate=request.POST['hackathon-end-date']
          githubrepo=request.POST['github-repo']
          otherlinks=request.POST['other-links']
          if len(request.FILES)!=0:
           #  Saving POST'ed file to storage
            file = request.FILES['image']
            hack=submission()
            hack.Title=title
            hack.Summary=summary
            hack.Description=description
            hack.Hackathon_name=hackathonname
            hack.Hackathon_startdate=hackathonstartdate
            hack.Hackathon_enddate=hackathonenddate
            hack.Github=githubrepo
            hack.Other=otherlinks
            hack.image=file
            hack.uploadtime=datetime.datetime.now()
            hack.flag=False
            hack.save()
            return redirect('/')
          else:
            print("error")
            messages.error(request, 'Upload valid image file')
            return render(request, "iform.html")
     return render(request, "iform.html")


###### MARK AS FAVOURITE
def markFavourite(request):
    # Get the product that user has wished for
    id = request.POST['id']
    status = request.POST['status']
    assignment = submission.objects.get(id=id)
    print(id)
    print(status)
    if status == "true":
        print("saving to true")
        assignment.flag = True
    else:
        print("saving to false")
        assignment.flag = False
    assignment.save()
    return HttpResponse('marked')

##### CARD PAGE
def card(request,id):
     hdata=submission.objects.get(id=id)
     return render(request, "card.html",{'posts': hdata})

###EDIT A FORM 
def editform(request,id):
     hack=submission.objects.get(id=id)
     if request.method=="POST":
          title=request.POST['title']
          summary=request.POST['summary']
          description=request.POST['description']
          hackathonname=request.POST['hackathon-name']
          hackathonstartdate=request.POST['hackathon-start-date']
          hackathonenddate=request.POST['hackathon-end-date']
          githubrepo=request.POST['github-repo']
          otherlinks=request.POST['other-links']
          if len(request.FILES)!=0:
           #  Saving POST'ed file to storage
            file = request.FILES['image']
            file_name = default_storage.save(file.name, file)
            #  Reading file from storage
            file = default_storage.open(file_name)
            file_url = str(os.getcwd()+str(default_storage.url(file_name)))
            print(file_url)
            hack.Title=title
            hack.Summary=summary
            hack.Description=description
            hack.Hackathon_name=hackathonname
            hack.Hackathon_startdate=hackathonstartdate
            hack.Hackathon_enddate=hackathonenddate
            hack.Github=githubrepo
            hack.Other=otherlinks
            hack.image=file
            hack.save()
            return redirect('/')
          else:
            print("error")
            messages.error(request, 'Upload valid image file')
            return redirect('editform/hack.id')
     return render(request, "editform.html",{'posts': hack})

##DELETE A FORM
def delete(request,id):
     hack=submission.objects.get(id=id)
     hack.delete()
     return redirect('/')