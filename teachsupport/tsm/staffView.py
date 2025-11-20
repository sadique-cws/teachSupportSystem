from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from tsm.models import *
from django.db.models import Q
from .forms import CommentTicketForm

@login_required()
@role_required(allowed_roles={"staff"})
def staffDashboard(request):
    return render(request, 'staff/staffDashboard.html')


@login_required()
@role_required(allowed_roles={"staff"})
def staffmanageTicket(request):
    orQ = Q(assigned_to=request.user) | Q(status='open')
    tickets = SupportTicket.objects.filter(orQ).order_by("-status")
    return render(request, 'staff/staffmanageTicket.html', {'tickets': tickets})


@login_required()
@role_required(allowed_roles={"staff"})
def staffViewTicket(request, ticket_id):
    ticket = SupportTicket.objects.get(id=ticket_id)
    replies = TicketComment.objects.filter(ticket=ticket)
    form = CommentTicketForm(request.POST or None)
    if form.is_valid():
        comment = form.cleaned_data['comment']
        TicketComment.objects.create(
            ticket=ticket,
            comment=comment,
            author=request.user
        )
        ticket.status = 'in_progress'
        ticket.assigned_to = request.user
        ticket.save()
        return redirect('staffViewTicket', ticket_id=ticket_id)
    return render(request, 'staff/staffViewTicket.html', {'ticket': ticket, 'replies': replies, 'form': form})
