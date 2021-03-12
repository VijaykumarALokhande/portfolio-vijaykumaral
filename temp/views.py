from django.shortcuts import render, get_object_or_404
from .models import Tempo
def fn(request):
    b_objs = Tempo.objects
    return render(request, 'temp/krab.html', {"b_objs":b_objs})

def fnspacific(request, blog_id):
    spcf_b_objs = get_object_or_404(Tempo, pk=blog_id)
    return render(request, 'temp/spf.html', {"pacific":spcf_b_objs})
