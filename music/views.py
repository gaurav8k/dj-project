from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is music app homepage.. So, hello :)</h1>")
