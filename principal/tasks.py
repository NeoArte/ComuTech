from .models import Aid
from datetime import time, timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

# Enviar email - testes

def email_send():
    enviou = send_mail(
    'Teste',
    'Mensagem de Teste',
    settings.EMAIL_HOST_USER,
    ['artemisaneo@protonmail.com'],
)
    if enviou:
        print('\n\n\nEnviado\n\n\n')
    else:
        print('\n\n\nNão enviou\n\n\n')


# Para iniciar use: python manage.py qcluster

def aid_checker():
    print("\n\n\nRODANDO AID_CHECKER\n\n\n")
    aid_list  = Aid.objects.all()
    for aid in aid_list:

        pause_time = aid.creation_date + timedelta(days=60)
        delete_time = aid.creation_date + timedelta(days=74)

        #print("Aid ID: ", aid.id, " | ","Today: ", timezone.now(), " | ", "PT: ", pause_time, " | ", "DT: ", delete_time, end="")
        print(f'\n\n{aid}:{aid.id}:{type(aid)}\n\n')
        if type(aid) != type(None):
            if timezone.now() >= pause_time and aid.state != "C":
                send = send_mail(
                    subject= 'Teste Nome',
                    message= f'Olá, {aid.author.name}!\n',
                    from_email= settings.EMAIL_HOST_USER,
                    recipient_list= [''],
                )
                if send:
                    print(" | Sent")
                else:
                    print(" | Not Sent")
                print(f'\n\n{aid}:{aid.id}:{type(aid)}\n\n')
                aid.state = "C"
                aid = aid.save()
            
            if aid.state == "C" and timezone.now() >= delete_time:
                print("\n\n\nDeletando\n\n\n")
                aid.delete()