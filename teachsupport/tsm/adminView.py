from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from tsm.models import SupportTicket,TicketComment,UserRole

def dashbaord(request):
    count = {
        "users" : User.objects.count(),
        "tickets" : SupportTicket.objects.count(),
        "replay" : TicketComment.objects.count(),
        "agents" : UserRole.objects.filter(role="staff").count(),
        "resloved_tickets": SupportTicket.objects.filter(status="closed").count(),
    }
    return render(request, 'admin/dashboard.html',{'count':count})

def manage_users(request):
    data = {
        "users" : User.objects.filter(is_superuser=False)
    }
    return render(request, 'admin/manageUsers.html',data)

def manage_tickets(request):
    data = {
        "tickets" : SupportTicket.objects.all()
    }
    return render(request, 'admin/manageTickets.html', data)

def reports(request):
    return render(request, 'admin/report.html')

def adminSettings(request):
    return render(request, 'admin/setting.html')

def manageAgents(request):
    return render(request, 'admin/manageAgents.html')

def closeTicket(request, ticket_id):
    ticket = SupportTicket.objects.get(id=ticket_id)
    ticket.status = 'Closed'
    ticket.save()
    return redirect('manage_tickets')