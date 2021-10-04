from django import template
from principal.models import Aid

register = template.Library()

@register.simple_tag
def get_thumbnail(pk):
    
    # get_thumbnail vai fazer uso de uma backwards relationship (ao invés de irmos de AidPhotos para Aid, faremos Aid para AidPhotos)
    # então dado um objeto com pk=pk (parametro), usamos images (Manager, é o que conecta o lado 1 de uma relação 1 para N) e pegamos todos os
    # elementos.
    img = Aid.objects.get(pk=pk).photos.all()
    if not img.exists():
        return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZO25RX0Me_oYwuXa2hPcgah-3t07WXVWXWJGVGYuI0cp4BMW1QXj0KQGHDyzR5TFy8Ys&usqp=CAU"
    img = img.first().image
    return "/media/" + img.name

