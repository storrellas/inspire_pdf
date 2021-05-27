from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MedicalExpertPDFExportView(TemplateView):
    template_name = 'medical_expert_pdf_export.html'

    def get_context_data(self, **kwargs):
        context = super(MedicalExpertPDFExportView, self).get_context_data(**kwargs)
        # context['length_ranges'] = LengthRange.objects.all()
        # context['hull_types'] = Hull.objects.all()

        # institution__combined_name: "Asklepios Kliniken - Asklepios Klinik Altona, Abteilung für Neurologie"
        # institution__email: "info.altona@asklepios.com"
        # institution__location: "SRID=4326;POINT (9.902420399999999 53.5545532)"
        # institution__phone: "+49 40 1818811401"
        # position__name: "Head of"
        # career_stage: "Peak"
        # combined_name: "Joachim Röther"
        # cv: "https://www.asklepios.com/details/arztprofil~prId=3529~"
        # degree: "Prof. Dr."
        # email: "j.roether@asklepios.com"
        # focus_areas_reasearch_interests: "Forschungsschwerpunkte: mechanische Thrombektomie, Schlaganfall, Sekundärprävention, Thrombolyse. Wissenschaftliche Interessen: Bildgebende Methoden des Schlaganfalls, Epidemiologie des Schlaganfalls, Migräne, Vaskulitis, Zerebrovaskuläre Erkrankungen"
        # is_favorite_investigator: true
        # is_rising_star: false
        # number_co_authors: 123
        # number_co_authors_same_primary_affiliation: 0
        # number_linked_clinical_trials: 3
        # number_linked_clinical_trials_recruiting: 1
        # number_linked_events: 27
        # number_linked_events_position_chairperson: 11
        # number_linked_publications: 87
        # number_linked_publications_position_first_author: 11
        # oid: "think-me-000-345536"
        # phone: null
        # photo_url: "https://www.asklepios.com/.imaging/mte/asklepios/carouselTeaserItem_592/profiles/3529/photo/img_3529.jpg"
        # profile_last_updated_on: null
        # specialties: "Geriatric Medicine, Neurology"

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
            "number_linked_publications_position_first_author": 11,
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
        return context