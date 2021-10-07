from .models import Aid
from datetime import time, timedelta, date


def aid_checker():
    print("\n\n\nRODANDO AID_CHECKER\n\n\n")
    aid_list  = Aid.objects.all()
    for aid in aid_list:

        aid_date = aid.creation_date
        pause_time = timedelta(days=60)
        delete_time = timedelta(days=74)

        print("PT: ", pause_time, " | ", "DT: ", delete_time)

        if aid_date >= pause_time:
            aid.state = "C"
            aid = aid.save()
        
        if aid.state == "C" and aid_date >= delete_time:
            aid.delete()