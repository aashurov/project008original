from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class Index(LoginRequiredMixin, TemplateView):
    def get_template_names(self):
        if self.request.user.role == 'Manager':
            return ['index.html']
        else:
            return ['home.html']
