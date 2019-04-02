from django.shortcuts import render


def post_list(request):
    return render(request, 'block/post_list.html', {})
