from . import models

def get_logo(request):
    logo = models.AppSettings.objects.first()
    data = {
        'logo':logo.image_tag if logo else None,
    }
    return data