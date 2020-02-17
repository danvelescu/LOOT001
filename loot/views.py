from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

from .models import User

class Users(View):
    def get(self, request):
        user = User.objects.all()
        return render(request,"loot/user_list.html",
                      {"userlist":user})