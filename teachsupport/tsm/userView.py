from django.shortcuts import render,redirect
from tsm.models import SupportTicket,TicketAttachment
def userDashboard(request):
    countTicket = {
        'openTicket': SupportTicket.objects.filter(status='open', created_by=request.user).count(),
        "closedTicket": SupportTicket.objects.filter(status='closed',created_by=request.user).count(),
        "myTickets": SupportTicket.objects.filter(created_by=request.user)
    }
    return render(request, 'user/userdashboard.html', countTicket)

def raiseTicket(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Create the support ticket
        newTicket = SupportTicket.objects.create(
            title=title,
            description=description,
            created_by=request.user,
            status='open'
        )

        if 'attachments' in request.FILES:
            attachments = request.FILES.getlist('attachments')
            for file in attachments:
                TicketAttachment.objects.create(file=file,ticket=newTicket,uploaded_by=request.user)
            
        

        

        return redirect('user_dashboard')
    return render(request, 'user/raiseTicketForm.html')



def viewTicket(request, ticket_id):
    ticket = SupportTicket.objects.get(id=ticket_id, created_by=request.user)
    attachments = TicketAttachment.objects.filter(ticket=ticket)
    context = {
        'ticket': ticket,
        'attachments': attachments
    }
    return render(request, 'user/ticketView.html', context) 