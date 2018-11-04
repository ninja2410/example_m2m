#recuerde que es necesario indicar que clases de nuestro modelo van a ser manejadas por la aplicación /admin.

from django.contrib import admin
from peliculas.models import Actor, ActorAdmin, Pelicula, PeliculaAdmin

#Registramos nuestras clases principales.
admin.site.register(Actor, ActorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)