import io, os
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


        path = os.path.dirname(__file__)



        context = {
            "oid": '123',
            "degree": "Prof. Dr.",
            "combined_name": "Joachim Röther",
            "photo_url": "https://www.asklepios.com/.imaging/mte/asklepios/carouselTeaserItem_592/profiles/3529/photo/img_3529.jpg",
            "specialties": "Geriatric Medicine, Neurology",
            "focus_areas_reasearch_interests": "Forschungsschwerpunkte: mechanische Thrombektomie, Schlaganfall, Sekundärprävention, Thrombolyse. Wissenschaftliche Interessen: Bildgebende Methoden des Schlaganfalls, Epidemiologie des Schlaganfalls, Migräne, Vaskulitis, Zerebrovaskuläre Erkrankungen",
            "affiliation": {
                "position__name": "Head of",
                "institution__combined_name": "Asklepios Kliniken - Asklepios Klinik Altona, Abteilung für Neurologie",
                "institution__phone": "+49 40 1818811401",
                "institution__email": "info.altona@asklepios.com",
                "institution__location": "SRID=4326;POINT (9.902420399999999 53.5545532)",
            },
            "career_stage": "Peak",
            "cv": "https://www.asklepios.com/details/arztprofil~prId=3529~",
            "email": "j.roether@asklepios.com",
            "phone": "123646",
            "number_linked_publications_first_author": 11,
            "number_linked_publications": 12,
            "number_co_authors_same_primary_affiliation": 12,
            "number_co_authors": 14,
            "number_linked_events_position_chairperson": 21,
            "number_linked_events": 11,
            "number_linked_clinical_trials_recruiting": 12,
            "number_linked_clinical_trials": 1,
            "profile_last_updated_on": None,
            "is_favorite_investigator": True,
            "is_rising_star": True,
            "cooperations_per_company": [
                {
                    "nature_of_payment": "1234",
                    "year": "2002",
                    "institution": "MyNewCompany",
                    "amount": "1233",
                    "currency": "EUR"
                },
                {
                    "nature_of_payment": "1234",
                    "year": "2002",
                    "institution": "MyNewCompany",
                    "amount": "1233",
                    "currency": "EUR"
                },
                {
                    "nature_of_payment": "1234",
                    "year": "2002",
                    "institution": "MyNewCompany",
                    "amount": "1233",
                    "currency": "EUR"
                }
            ],
        }
        options = {
            'encoding': 'UTF-8',        
            'margin-left': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '30mm',
            'margin-top': '30mm',
            "javascript-delay": 5000,   
            "header-html": f"file://{path}/footer.html"
        }
        html_str = render_to_string('medical_expert_pdf_export.html', context)

        config = pdfkit.configuration(wkhtmltopdf='/home/storrellas/workspace/inspire_pdf/wkhtmltopdf/usr/local/bin/wkhtmltopdf')
        pdfkit.from_string(html_str, 'out.pdf', options=options, configuration=config)

