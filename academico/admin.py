from django.contrib import admin
from .models import Curso, Docente

# Register your models here.

@admin.register(Curso)                     #Primera forma de registrar los modelos
class CursoAdmin(admin.ModelAdmin):     
    list_display = ('id', 'datos', 'creditos')            #enlista los campos
    #search_fields = ('id', 'nombre', 'creditos')          #sirve para buscar
    #list_editable = ('creditos',)                         #sirve para editar directamente
    #list_display = ('nombre',)                            #selecciona uno como hipervinculo   

    def datos(self,obj):
        return obj.nombre.upper()
    
    datos.short_description = "MATERIAS"


#admin.site.register(Curso, CursoAdmin)    #Segunda forma de registrar los modelos

#admin.site.register(Curso)                #Tercera forma de registrar los modelos

admin.site.register(Docente)