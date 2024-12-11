from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    
    peoples=[
        {'name' : 'Chetan Yadav','age':22},
        {'name' : 'Deepesh Panwar','age':21},
        {'name' : 'Anand Chawda','age':20},
        {'name' : 'Hemu Keer','age':23},
        {'name' : 'Sourabh','age':17}
    ]
#     text="""
#   Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo esse sed distinctio amet accusantium consectetur mollitia voluptas unde eum voluptatibus quibusdam tenetur quis exercitationem, accusamus inventore delectus. Sapiente, facere dolor.

# """
    vegetables=[
        'Pumpkin','Tomato','Potatoe'


    ]




    return render(request, "home/index.html",context={'page':'Home','peoples':peoples,'vegetables':vegetables},)

def success_page(request):
    print("*" * 10 )
    return HttpResponse("<h1>Hey this is a success page</h1>")

def about(request):
   context={'page':'About'}
   return render(request, "home/about.html",context)



def contact(request):
  context={'page':'Contact'}
  return render(request, "home/contact.html",context)