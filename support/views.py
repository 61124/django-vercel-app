from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import SupportForm
from .models import SupportTicket

def submit_ticket(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            ticket = form.save()

            # Send email notification to the admin
            send_mail(
                f'New Support Ticket: {ticket.subject}',
                f'Ticket ID: {ticket.id}\nName: {ticket.name}\nEmail: {ticket.email}\nMessage: {ticket.message}',
                'your_email@gmail.com',
                ['admin_email@gmail.com'],
            )
            return render(request, 'support/success.html')
    else:
        form = SupportForm()
    return render(request, 'support/submit_ticket.html', {'form': form})
