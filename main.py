from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import TicketForm, SearchTicketForm

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})

def ticket_list(request, status='Open'):
    tickets = Ticket.objects.filter(status=status)
    return render(request, 'ticket_list.html', {'tickets': tickets, 'status': status})

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticket_detail.html', {'ticket': ticket, 'form': form})

def search_ticket(request):
    if request.method == 'POST':
        form = SearchTicketForm(request.POST)
        if form.is_valid():
            # Implement search logic based on form data
            # ...
    else:
        form = SearchTicketForm()
    return render(request, 'search_ticket.html', {'form': form})
