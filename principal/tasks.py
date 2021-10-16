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

def freeze_checker():
    print("\n\n\nRODANDO FREEZE_CHECKER\n\n\n")
    aid_list  = Aid.objects.all()
    for aid in aid_list:
        print(f"\n {aid} : {aid.id} : {aid.title}")
        pause_time = aid.creation_date + timedelta(days=60)
        delete_time = aid.creation_date + timedelta(days=74)

        print("Aid ID: ", aid.id, " | ","Today: ", timezone.now(), " | ", "PT: ", pause_time, " | ", "DT: ", delete_time, end="")
        if type(aid) != type(None):
            print("Not None", end="")
            if timezone.now() >= pause_time and aid.state != "C":
                print("CONGELA")

                text_email = "ComuTech\n\n" \
                "Boa tarde, {aid.author.name}.\n" \
                "Esse é uma e-mail automático do sistema da ComuTech para te comunicar que seu socorro {aid.title} foi congelado após seus 2 meses de atividade, " \
                "caso deseje descongela-lo para que volte a aparecer para as pessoas, siga os seguintes passos:\n" \
                "1. Procure pelo seu socorro (você pode encontra-lo como um cartão no seu perfil (127.0.0.1:8000/user/{aid.author.id}) ou na página do mesmo em" \
                "127.0.0.1:8000/explorar/{aid.id})\n" \
                '2. Clique no botão "Opções" no canto inferior direito do cartão ou no superior direito da página\n' \
                '3. Selecione "Descongelar"\n\n' \
                "Em 2 semanas seu socorro será removido de nossos sistemas, por isso pedimos que caso queira que ele continue, siga as instruções" \
                "acima o quanto antes.\n\n\n" \
                "Agradecemos pelo sua atenção, abraços da equipe do ComuTech."
                
                html_email = \
                    f"""
                    <h1>ComuTech</h1>
                    <p>Boa tarde, {aid.author.name}.</p>
                    <p>Esse é um e-mail automático do sistema da ComuTech para te comunicar que seu socorro {aid.title} foi congelado após seus 2 meses de atividade, caso deseje descongela-lo para que volte a aparecer para as pessoas, siga os seguintes passos:</p>
                    <ol>
                    <li>Acesse seu socorro (você pode encontra-lo como um cartão no seu perfil (127.0.0.1:8000/user/{aid.author.id}) ou acessar a página do mesmo em 127.0.0.1:8000/explorar/{aid.id})</li>
                    <li>Clique no botão "Opções" no canto inferior direito do cartão ou no superior direito da página</li>
                    <li>Selecione "Descongelar"</li>
                    </ol>
                    <p>Em 2 semanas seu socorro será removido de nossos sistemas, por isso pedimos que caso queira que ele continue, siga as instruções acima o quanto antes.</p>
                    <p>Agradecemos pelo sua atenção, abraços da equipe do ComuTech.</p>
                    """
                send = send_mail(
                    subject= 'Aviso: Seu socorro foi congelado',
                    message=text_email,
                    html_message=html_email,
                    from_email= settings.EMAIL_HOST_USER,
                    recipient_list= [aid.author.email],
                )
                if send:
                    print(" | Sent")
                else:
                    print(" | Not Sent")
                aid.state = "C"
                aid.save()
            
            if aid.state == "C" and timezone.now() >= delete_time:
                print("\n\n\nDeletando\n\n\n")
                aid.delete()
    print("\nTERMINANDO AID_CHECKER\n")
    
def ending_checker():
    print("\n\n\nRODANDO ENDING_CHECKER\n\n\n")
    aid_list  = Aid.objects.all()
    for aid in aid_list:
        
        delete_time = aid.ending_date + timedelta(days=14)

        print("Aid ID: ", aid.id, " | ","Today: ", timezone.now(), " | ", "DT: ", delete_time)
        
        if aid.state == "F" and timezone.now() >= delete_time:
            aid.delete()
