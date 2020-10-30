from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms


from .models import tareas

class tareasListado(generic.ListView): 
    model = tareas
 
class tareaDetalle(generic.DetailView): 
    model = tareas
 
class tareaCrear(SuccessMessageMixin, generic.CreateView): 
    model = tareas
    form = tareas
    fields = "__all__" 
    success_message = 'Tarea Creada Correctamente !'  
    
    def get_success_url(self):        
        return reverse('todo:leer')
 
class tareaActualizar(SuccessMessageMixin, generic.UpdateView): 
    model = tareas
    form = tareas
    fields = "__all__"  
    success_message = 'tarea Actualizado Correctamente !' 
     
    def get_success_url(self):               
        return reverse('todo:leer') 
 
class tareaEliminar(SuccessMessageMixin, generic.DeleteView): 
    model = tareas 
    form = tareas
    fields = "__all__"      
    
    def get_success_url(self): 
        success_message = 'Tarea Eliminada Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('todo:leer')