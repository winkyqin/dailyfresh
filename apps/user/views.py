from django.shortcuts import render

from django.views import View


class RegisterView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        print(request)
        render(request, "register.html")
