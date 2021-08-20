from os import name, read
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils.dateparse import parse_date

import csv
from songs_api_prj.settings import BASE_DIR

# Models

from .models import (
     Album, Artista, Labels,
     Song, SongBandasSimilares, SongInstruments, SongLabels,
     Labels, Instrumentos, Genero,
     SubGenero, BandasSimilares
)



@api_view(['POST'])
def script_populate(request):

    with open(f'{BASE_DIR}/prueba_back_monoku_2021_datos.csv', 'r') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            fecha = row[0]
            id_externo = row[1]
            nombre = row[2]
            album, _ = Album.objects.get_or_create(name=row[3], banda=row[4])
            artista, _ = Artista.objects.get_or_create(name=row[5])
            duracion = row[6]
            genero, _ = Genero.objects.get_or_create(name=row[7])
            sub_genero, _ = SubGenero.objects.get_or_create(name=row[8])
            song, _ = Song.objects.get_or_create(fecha=fecha, id_externo=id_externo, nombre=nombre,
                                duracion=duracion, album=album, artista=artista, genero=genero,
                                sub_genero=sub_genero)
            bandas_similares = row[9]
            if bandas_similares:
                bandas_similares = bandas_similares.replace(' ', '')
                bandas_similares = bandas_similares.split(';')
                for banda in bandas_similares:
                    banda, _ = BandasSimilares.objects.get_or_create(name=banda)
                    SongBandasSimilares.objects.get_or_create(song=song, banda_similar=banda)
            labels = row[10]
            if labels:
                labels = labels.replace(' ', '')
                labels = labels.split(';')
                print(labels)
            instrumentos = row[11]
            if instrumentos:
                instrumentos = instrumentos.replace(' ', '')
                instrumentos = instrumentos.split(';')
                print(instrumentos)
            

    return Response({"data":"ok POST"}, status=status.HTTP_201_CREATED)

