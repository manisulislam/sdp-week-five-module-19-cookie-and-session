from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response=render(request, "home.html")
    # response.set_cookie("name","anis", max_age=20)
    response.set_cookie("name","anis", expires=datetime.utcnow()+timedelta(days=10) )
    return response

def get_cookie(request):
    name=request.COOKIES.get("name")
    return render(request, "get_cookie.html", {"name": name})


def del_cookie(request):
    response=render(request, "del_cookie.html")
    response.delete_cookie("name")
    return response


def set_session(request):
    data={
        "name":"anis",
        "age":23,
        "lang":"bd"
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request,"index.html")


def get_session(request):
    if "name" in request.session:
        name=request.session.get("name","Guest")
        age=request.session.get("age","Guest")
        request.session.modified=True
        return render(request,"get_session.html", {"name":name,"age":age})
    else:
        return HttpResponse("your session expire...please log in..")

def delete_session(request):
    request.session.flush()
    return render(request, "delete_session.html")