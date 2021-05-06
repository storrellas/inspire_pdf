import io
from PIL import Image
# Django Imports
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.template.loader import render_to_string

# from ipyleaflet import Map, basemaps, basemap_to_tiles
import pdfkit


class Command(BaseCommand):
    help = 'Generates a PDF file based on template'


    def handle(self, *args, **options):
        print("-- Generating tokens --")
        # m = Map(
        #       basemap=basemap_to_tiles(basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"),
        #       center=(52.204793, 360.121558),
        #       zoom=4
        # )
        # m.save('my_map.html', title='My Map')

        # img_data = m._to_png(5)
        # img = Image.open(io.BytesIO(img_data))
        # img.save('image.png')
        html_str = render_to_string('index.html')
        pdfkit.from_string(html_str, 'out.pdf')

