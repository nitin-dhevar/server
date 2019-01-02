from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import random
import csv
import django.core.serializers
import django.http
from django.utils import timezone
from datetime import datetime, timedelta
def demo(request):
    with open("sample_data.csv") as p :
        csvreader = csv.reader(p)

        # extracting field names through first row
        i = 0
        rows = []
        # extracting each data row one by one
        for row in csvreader:
            if i == 0 :
                pass
            else:
                rows.append(row)
                book = Book.objects.create(ISBN=row[0], Title=row[1], Author=row[2], Publisher=row[3], Image="http://placehold.it/120x120&text="+row[0])
                for m in range(0,5):
                    bookissue = Bookissue.objects.create(Book=book,ACCNO=int(row[0].replace('-',''))*1000 + m ,ED = timezone.now())
                    print(int(row[0].replace('-',''))*1000)
            i += 1

    print(rows)
    return HttpResponse("hello")

def apiFA(request):
    # books = Book.objects.all()
    # f = 0
    # for b in books:
    #     if f == 0:
    #         b.FA = 1
    #         b.save()
    #         f = 1
    #     else:
    #         f = 0
    books = Book.objects.filter(FA=1).values()
    b_list = list(books)  # important: convert the QuerySet to a list object
    #print(b_list)
    return JsonResponse(b_list, safe=False)

def apiBook(request,count):
    if count > 0 and count < 1001:
        pass
    else:
        count = 20
    books = Book.objects.all()[:count].values()
    b_list = list(books)  # important: convert the QuerySet to a list object
    #print(b_list)
    return JsonResponse(b_list, safe=False)

def apiBookIssue(request):
    email = request.POST["email"]
    accno = request.POST["accno"]

def getBook(request,isbn):
    book = Book.objects.filter(ISBN=isbn).first()
    #b_list = list(books)  # important: convert the QuerySet to a list object
    # print(b_list)
    s = django.core.serializers.serialize('json', [book])
    # s is a string with [] around it, so strip them off
    o = s.strip("[]").replace("\\","")
    return django.http.HttpResponse(o, content_type="application/json")
    #return JsonResponse(o, safe=False)
