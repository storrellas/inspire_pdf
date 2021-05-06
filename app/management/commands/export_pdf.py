import io
# Django Imports
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.template.loader import render_to_string

# from ipyleaflet import Map, basemaps, basemap_to_tiles
import pdfkit


class Command(BaseCommand):
    help = 'Generates a PDF file based on template'


    def handle(self, *args, **options):
        print("Generating PDF file:")
        # m = Map(
        #       basemap=basemap_to_tiles(basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"),
        #       center=(52.204793, 360.121558),
        #       zoom=4
        # )
        # m.save('my_map.html', title='My Map')

        # img_data = m._to_png(5)
        # img = Image.open(io.BytesIO(img_data))
        # img.save('image.png')

        options = {
            'encoding': 'UTF-8',        
            'margin-left': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '20mm',
            'margin-top': '20mm'
        }

        html_str = render_to_string('index.html')
        pdfkit.from_string(html_str, 'out.pdf', options=options)

