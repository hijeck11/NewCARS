from django.shortcuts import render, get_object_or_404
from .models import Autohaus, AutoOptions

def autohaus_list(request):
    autos = Autohaus.objects.all()
    return render(request, 'autohaus_list.html', {'autos': autos})

def auto_detail(request, auto_id):
    auto = get_object_or_404(Autohaus, pk=auto_id)
    return render(request, 'auto_detail.html', {'auto': auto})

def order_options(request, auto_id):
    auto = get_object_or_404(Autohaus, id=auto_id)
    options = AutoOptions.objects.all()

    if request.method == 'POST':
        selected_options = request.POST.getlist('options')
        selected_options_objects = AutoOptions.objects.filter(id__in=selected_options)
        total_price = auto.price + sum(option.option_price for option in selected_options_objects)
    else:
        total_price = auto.price

    return render(request, 'order_options.html',
                  {'auto': auto, 'options': options, 'total_price': total_price})

def submit_order(request, auto_id):
    if request.method == 'POST':
        auto = get_object_or_404(Autohaus, id=auto_id)
        selected_options = request.POST.getlist('options')
        # Добавьте логику для обработки выбранных опций и оформления заказа
        # Например, создание объекта Order и связывание с выбранными опциями
        # После успешного оформления заказа перенаправьте пользователя на страницу "спасибо" или другую подходящую
        return redirect('thank_you_page')
    # В случае GET-запроса можно реализовать обработку и отображение формы выбора опций
    # Это может потребоваться в зависимости от ваших потребностей
    return redirect('order_options', auto_id=auto_id)