from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from organization import models as organmodels
from company import models as compmodels
from . import models
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, FormView


@method_decorator(csrf_exempt, name='dispatch')
class AddQuote(LoginRequiredMixin, FormView):
    model = models.QuoteItem
    template_name = 'sellProcess/add-quote.html'
    extra_context = {
        # ol : object list
        'organizations_ol': organmodels.Organization.objects.all(),
        'products_ol': compmodels.CompanyProduct.objects.all(),
    }
    fields = (
        'organization',
    )
