from django.shortcuts import render,redirect
from tsm.models import SupportTicket
def userDashboard(request):
    countTicket = {
        'openTicket': SupportTicket.objects.filter(status='Open', created_by=request.user).count(),
        "closedTicket": SupportTicket.objects.filter(status='Closed',created_by=request.user).count(),
    }
    return render(request, 'user/userdashboard.html', countTicket)

def raiseTicket(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        SupportTicket.objects.create(
            title=title,
            description=description,
            created_by=request.user,
            status='Open'
        )
        return redirect('user_dashboard')
    return render(request, 'user/raiseTicketForm.html')