from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from . import names

class HomePage(TemplateView):
    template_name = "homepage.html"
    def get_context_data(self, **kwargs):
        context = {
            'name': names.name,
            'user_image': names.user_image,
            'notifications_number': names.notifications_number
        }
        return context


