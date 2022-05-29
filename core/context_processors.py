from .models import SiteSetting


def access_setting(request):
    setting = SiteSetting.objects.first()
    return {'setting': setting}
