from website.models import Information




def MYInformation(request):
    myinformations = Information.objects.all().first()
    
    return {'myinformations':myinformations}