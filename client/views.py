from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import csv
# Create your views here.
# def demo(request):
#     with open("sample_data.csv") as p :
#         csvreader = csv.reader(p)
#
#         # extracting field names through first row
#         i = 0
#         rows = []
#         # extracting each data row one by one
#         for row in csvreader:
#             if i == 0 :
#                 pass
#             else:
#                 rows.append(row)
#                 book = Book.objects.create(ISBN=row[0], Title=row[1], Author=row[2], Publisher=row[3], Image="http://placehold.it/120x120&text="+row[0])
#             i += 1
#
#     print(rows)
#     return HttpResponse("hello")

def apiBook(request,count):
    if count > 0 and count < 1001:
        pass
    else:
        count = 20
    books = Book.objects.all()[:count].values()
    b_list = list(books)  # important: convert the QuerySet to a list object
    print(b_list)
    return JsonResponse(b_list, safe=False)
