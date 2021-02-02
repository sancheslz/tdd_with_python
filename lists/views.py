from django.shortcuts import render


def home_page(request):
    # if request.method == 'POST':
    return render(request, 'lists/home.html', {
        'new_item_text': request.POST.get('item_text', '')
    })
    # return render(request, 'lists/home.html')
