from django.shortcuts import render
from django.http import HttpResponse
# from django.utils import timezone

api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiMDcwODQ1MjgtOWFkNy00NjViLWJjZGMtNmYxODZjMTQyZDYxIn0.XEivKJamIn8RH7-bWNdsSHGKMsnVYHVTS-jmPn4m1XM'

def index(request):

    return render(
        request,
        'index.html',
        # { },
    )

def change_photo(request):

    files = request.FILES
    print(files)

    photo = (files['image'])
    print('photo - ',photo)


    return HttpResponse('chto-to')
