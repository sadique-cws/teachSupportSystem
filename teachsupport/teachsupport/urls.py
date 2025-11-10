from django.contrib import admin
from django.urls import path
from tsm.views import *
from django.conf.urls.static import static
from django.conf import settings
from tsm.adminView import *
from tsm.userView import *


urlpatterns = [
    #public urls
    path('', index, name='index'),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),

    # admin urls
    path("admin/", dashbaord, name="admin_dashboard"),
    path("admin/manage_users/", manage_users, name="manage_users"),
    path("admin/manage_tickets/", manage_tickets, name="manage_tickets"),
    path("admin/reports/", reports, name="reports"),
    path("admin/settings/", adminSettings, name="settings"),
    path("admin/manage_agents/", manageAgents, name="manage_agents"),
    path("admin/close_ticket/<int:ticket_id>/", closeTicket, name="close_ticket"),

    # user urls
    path("user/dashboard/", userDashboard, name="user_dashboard"),
    path("user/raise_ticket/", raiseTicket, name="raise_ticket"),
    path("user/view_ticket/<int:ticket_id>/", viewTicket, name="view_ticket"),

    # superadmin url
    path('superadmin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)