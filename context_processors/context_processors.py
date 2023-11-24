from website.models import Information
from website.Calculation_age import get_data



def MYInformation(request):
    myinformations = Information.objects.all().first()
    year,month,day = get_data(myinformations.birthday.day,myinformations.birthday.month,myinformations.birthday.year)
    return {'myinformations':myinformations,"year":year} #"month":month,"day":day