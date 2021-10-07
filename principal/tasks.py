from .models import Aid
from datetime import timedelta, date


# Função que congela o socorro após 2 messes de sua criação. Passando de 2 meses e duas semanas ele executa a deleção do socorro automaticamente
def aid_checker(request):
    aid_list  = Aid.objects.all()
    for aid in aid_list:
        state = getattr(aid, 'state')
        aidDate = getattr(aid, 'creation_date')
        aidDate = int(date)
        deleteTime = timedelta(days=74)
        pauseTime = timedelta(days=60)

        if aidDate >= pauseTime:
            aid = aid.update(defaults={'state': 'C'})
            if state == "C" and aidDate >= deleteTime:
                aid = get_object_or_404(Aid, pk=aid.id)
                aid.delete()
                    
        elif aidDate < pauseTime:
            if state == "C":
                unfreeze = request.GET.get('descongelar')
                if unfreeze:
                    aid = aid.update(defaults={'state': 'A'})
                # messages.info(request, 'Socorro descongelado com sucesso')
    return redirect(f'/user/{request.user}/')
#     defaults = {'first_name': 'Bob'}
#     try:
#         obj = Person.objects.get(first_name='John', last_name='Lennon')
#     for key, value in defaults.items():
#         setattr(obj, key, value)
#     obj.save()
#     obj, created = Person.objects.update_or_create(
#     first_name='John', last_name='Lennon',
#     defaults={'first_name': 'Bob'},
# )
#     aid_list = Aid.objects.update_or_create(defaults={'state': 'C'})