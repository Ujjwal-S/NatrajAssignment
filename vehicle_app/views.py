from django.shortcuts import HttpResponse
from django.views import generic
from . models import Vehicle
from . forms import VehicleForm

class VehicleListView(generic.ListView):
    """ This CBV is responsible for displaying all the vehicles currently present in databse."""
    model = Vehicle


class VehicleDetailView(generic.DetailView):
    """ This CBV is responsible for handeling the details page of a particular instance of a vehicle."""

    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super(VehicleDetailView, self).get_context_data(**kwargs)
        context['vehicle_list'] = Vehicle.objects.all()
        return context


class VehicleCreateView(generic.CreateView):
    """ This CBV is responsible for handeling the creation of a particular instance of a vehicle."""

    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicle_app/vehicle_create.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(VehicleCreateView, self).get_context_data(**kwargs)
        context['vehicle_list'] = Vehicle.objects.all()
        return context


class VehicleUpdateView(generic.UpdateView):
    """ This CBV is responsible for updating the current information of a particular instance of a vehicle."""

    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicle_app/vehicle_update.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(VehicleUpdateView, self).get_context_data(**kwargs)
        context['vehicle_list'] = Vehicle.objects.all()
        return context


class VehicleDeleteView(generic.DeleteView):
    """ This CBV is responsible for deleting a particular instance of a vehicle."""

    def get(self, *args, **kwargs):
        return HttpResponse("For Security Reasons, this action is not allowed.")

    model = Vehicle
    success_url ="/"