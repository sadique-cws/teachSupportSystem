from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from tsm.models import SupportTicket,TicketComment,UserRole
from tsm.forms import CommentTicketForm

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
        "tickets" : SupportTicket.objects.all().order_by("-status")
    }
    return render(request, 'admin/manageTickets.html', data)

def reports(request):
    return render(request, 'admin/report.html')

def adminSettings(request):
    return render(request, 'admin/setting.html')

def manageAgents(request):
    return render(request, 'admin/manageAgents.html')

def adminViewTicket(req,ticket_id):
    ticket = SupportTicket.objects.get(pk=ticket_id)
    replies = TicketComment.objects.filter(ticket=ticket_id)
    replayForm = CommentTicketForm(req.POST or None)

    if req.method == "POST":
        if replayForm.is_valid():
            data = replayForm.save(commit=False)
            data.author = req.user
            data.ticket = ticket
            data.save()
            #self assign if user replay then assign to this user
            if ticket.assigned_to == None:
                ticket.assigned_to = req.user
                if ticket.status == "open":
                    ticket.status = "in_progress" 
                ticket.save()
            return redirect(adminViewTicket,ticket_id)
    return render(req, "admin/viewTicket.html",{"ticket":ticket, "replies":replies,"form":replayForm})

def closeTicket(request, ticket_id):
    ticket = SupportTicket.objects.get(id=ticket_id)
    ticket.status = 'Closed'
    ticket.save()
    return redirect('manage_tickets')