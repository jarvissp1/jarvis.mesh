from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.models import TopicListing, Contact, Browse


# Create your view
def home(request):
    contacts = Contact.objects.first()
    browses = Browse.objects.all()

    return render(request, 'index.html', {'contacts': contacts, 'browses': browses})


def contact(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get('email')
        message = request.POST.get('message')
        full_message = f"{email} dan sizga quyidagi habar keldi:\n\n\n{message}"

        try:
            send_mail(
                f'{name} sizga habar yubordi.',
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return redirect('index')
        except Exception as e:
            print(f"Email yuborishda xato: {e}")
            return HttpResponse(f"xato yuz berdi :{e}")
    return render(request, 'contact.html', {'contacts': contacts})


def topics_listing(request):
    topics = TopicListing.objects.all()
    return render(request, 'topics-listing.html', {'topics': topics})


def topics_detail(request):
    return render(request, 'topics-detail.html')
