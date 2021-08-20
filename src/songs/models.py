from django.db import models

"""Model for Albums"""
class Album(models.Model):
    name = models.CharField(max_length=150)
    banda = models.CharField(max_length=150)
    def __str__(self) -> str:
        return f'{self.name}'

"""Model for Artists"""
class Artista(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

"""Model for genre"""
class Genero(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

"""Model for sub-genre"""
class SubGenero(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

"""Model for bands"""
class BandasSimilares(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

"""Model for labels"""
class Labels(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

"""Model for Instruments"""
class Instrumentos(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

"""Model for songs"""
class Song(models.Model):
    fecha = models.DateField()
    id_externo = models.IntegerField()
    nombre = models.CharField(max_length=150)
    duracion = models.CharField(max_length=10)
    album = models.ForeignKey(Album, null=True ,related_name='album_songs', on_delete=models.SET_NULL)
    artista = models.ForeignKey(Artista, null=True, related_name='art_songs', on_delete=models.SET_NULL)
    genero = models.ForeignKey(Genero, null=True, on_delete=models.SET_NULL)
    sub_genero = models.ForeignKey(SubGenero, null=True, on_delete=models.SET_NULL)


    def __str__(self) -> str:
        return f'{self.nombre}'

"""Model to manage many-to-many relationship between Song and Labels"""
class SongLabels(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    label = models.ForeignKey(Labels, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.song} - {self.label}'

"""Model to manage many-to-many relationship between Song and Instruments"""
class SongInstruments(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrumentos, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.song} - {self.label}'