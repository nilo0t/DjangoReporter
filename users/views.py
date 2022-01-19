from django.shortcuts import render,get_object_or_404

from .models import user
from django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from django.http import  Http404

def user_list_view(request):
    queryset = user.objects.all()
    contex={
        "object_list": queryset
    }
    return render(request, "users/user_list.html", contex)

# DetailView

class userlistview(ListView):
    queryset = user.objects.all()
    template_name = "users/user_Detail.html"
    def get_context_data(self, *args, object_list=None, **kwargs):
        contex = super(userlistview,self).get_context_data(*args,**kwargs)
        print(contex)
        return contex

def user_Detail_view(request,*args, userid=None ,**kwargs):
    try:
        users = user.objects.get(id=userid)
    except user.DoesNotExist:
        raise Http404("User Not Found")
    except:
        print("what?")

    #users=get_object_or_404(user,id=userid)
    contex={
        "object": users
    }
    return render(request, "users/user_Detail.html", contex)



class userDetailview(DetailView):
    queryset = user.objects.all()
    template_name = "users/user_Detail.html"


    def get_context_data(self, *args, object_list=None, **kwargs):
       contex = super(userDetailview, self).get_context_data(*args, **kwargs)
       contex['abc']='this is my test data in contex'
       print(contex)
       return contex