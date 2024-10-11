from website.models import Information
from website.Calculation_age import get_data


def MYInformation(request):
    myinformations = Information.objects.first()

    if myinformations is not None:
        year, month, day = get_data(myinformations.birthday.day, myinformations.birthday.month,
                                    myinformations.birthday.year)
        return {'myinformations': myinformations, "year": year, "month": month, "day": day}
    else:
        return {'myinformations': None, "year": None, "month": None, "day": None}
