from django.views.generic import TemplateView


from productos.models import PlatformUser

class Login(TemplateView):
    model = PlatformUser
    template_name = "productos/login.html"
    context_object_name = "location"
    
    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['location'] = {'here':"Login"}
        return context