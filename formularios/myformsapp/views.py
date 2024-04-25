from django.shortcuts import render, redirect

from .forms import MyCustomForm  # Importa tu formulario personalizado

def inicio(request):
    # Aquí puedes agregar lógica adicional si es necesario
    return render(request, 'myformsapp/inicio.html')  # Renderiza la plantilla de inicio


def nueva_pagina(request):
    form = MyCustomForm()

    if request.method == 'POST':
        form = MyCustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_confirmacion')  # Redirección a la página de confirmación

    return render(request, 'myformsapp/nueva_pagina.html', {'form': form})

def pagina_confirmacion(request):
    return render(request, 'myformsapp/pagina_confirmacion.html' )