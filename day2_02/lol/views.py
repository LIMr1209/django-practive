from django.shortcuts import render


# Create your views here.
def lol_index(request):
    return render(request, 'lol_index.html')


def hero(request):
    print(request.GET)
    name = request.GET.get("name", '')
    # type = request.GET.get('type', '')
    type = request.GET.getlist('type')
    return render(request, 'hero.html', {
        "name": name,
        'type': type,
    })
