from django.shortcuts import render

# Create your views here.

def employeresumepage(request):
    context = { 'name' : 'Neha',
                'ph' : 9785461681,
                'email' :'neha@gmail.com',
                'objective':'Experienced software professional with a strong intrest in python development, seeking a python developer role to apply my programing skill and experience in developing practical,efficient',
                'experience': 'promiza it solutions',
                'role':'PHP DEVELOPER',
                'experience_details' : 'developed and maintained web applications using PHP,HTML,Javascripts, and MySQL',
                'skills':['PYTHON',
                         'Django',
                         'CSS',
                         'HTML',
                         'Javascript',
                         'PHP'],
                'qualification':'MCA',
               }
    return render(request,'resume.html',{'resume':context})
