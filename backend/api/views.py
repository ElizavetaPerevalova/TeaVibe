from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('feedback')  # Перенаправляем на страницу с формой
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback.html', {'form': form})
