from .models import Aid
from datetime import time, timedelta
from django.utils import timezone


# Para iniciar use: python manage.py qcluster

def aid_checker():
    print("\n\n\nRODANDO AID_CHECKER\n\n\n")
    aid_list  = Aid.objects.all()
    for aid in aid_list:

        pause_time = aid.creation_date + timedelta(days=60)
        delete_time = aid.creation_date + timedelta(days=74)

        print("Aid ID: ", aid.id, " | ","Today: ", timezone.now(), " | ", "PT: ", pause_time, " | ", "DT: ", delete_time)

        if timezone.now() >= pause_time and aid.state is not "C":
            aid.state = "C"
            aid.save()
        
        if aid.state == "C" and timezone.now() >= delete_time:
            aid.delete()