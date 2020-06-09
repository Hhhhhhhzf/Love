from django.shortcuts import render
# Create your views here.
from .models import Message
from .forms import MessageForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def messages_display(request):
    context = {}
    message_list = Message.objects.all()
    paginator = Paginator(message_list, 2)
    page = request.GET.get('page')
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)
    context['message'] = messages
    if request.method != 'POST':
        form = MessageForm()
        context['form'] = form
    return render(request, 'message_board/messages.html', context)


def new_message(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        message = form.save(commit=False)
        message.author = request.user
        message.save()
    return HttpResponseRedirect(reverse('message_board:messages_display'))
