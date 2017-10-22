from django.views.generic import ListView, DetailView
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from jardam_kolu.contacts.models import Contact


class ContactsListView(ListView):
    queryset = Contact.objects.filter(active=True).prefetch_related('complex')
    model = Contact


class ContactsDetailView(DetailView):
    queryset = Contact.objects.all()
    model = Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id', 'email', 'phone_number',
            'additional_phones', 'additional_emails'
        )


class ContactContactsAPIView(APIView):
    serializer = ContactSerializer
    queryset = Contact.objects.filter(active=True)


class ContactsShowView(DetailView):
    queryset = Contact.objects.filter(active=True)
    model = Contact
    template_name = 'contacts/contacts_ajax.html'
