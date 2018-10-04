from django.contrib import admin
from .models import Province, Municipality, Authority, Entity, UseCase, Allocation

admin.site.register(Province)
admin.site.register(Municipality)
admin.site.register(Authority)
admin.site.register(Entity)
admin.site.register(UseCase)
admin.site.register(Allocation)
