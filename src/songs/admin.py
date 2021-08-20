from django.contrib import admin

from .models import (
    Song, Labels, Instrumentos, BandasSimilares,
    SongInstruments, SongLabels,
    Artista, Album, Genero,
    SubGenero, SongBandasSimilares
)

# Register your models here.
admin.site.register(Song)
admin.site.register(Labels)
admin.site.register(Instrumentos)
admin.site.register(BandasSimilares)
admin.site.register(SongInstruments)
admin.site.register(SongBandasSimilares)
admin.site.register(SongLabels)
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(SubGenero)
