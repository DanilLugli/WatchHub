from django.db.models import Count
from django.views.generic import TemplateView
from blog.models import Condition, Watch


# def manutenzione(request):
#    return HttpResponse("this site is under maintenance!")

class Home(TemplateView):
    template_name = 'home_extend.html'
    cond = Condition.objects.all()
    model = Watch



    def get_context_data(self, *args, **kwargs):
        cat_menu = Condition.objects.all()
        context = super(Home, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context


class Maintenance(TemplateView):
    template_name = 'Maintenance.html'
