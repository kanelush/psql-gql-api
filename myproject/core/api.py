from ninja import NinjaAPI
from core.models import Category, Negocios, Contact, Competencia, Producto
from typing import List
from core.schema import NegocioSchema, NotFoundSchema, ContactSchema, CompetenciaSchema, ProductoSchema

api = NinjaAPI()

@api.get("/competencias", response=List[CompetenciaSchema])
def competencias(request):
    return Competencia.objects.all()

@api.get("/competencias/{competencia_id}", response={200:CompetenciaSchema, 404:NotFoundSchema})
def competencia(request, competencia_id: int):
    try:
        competencia = Competencia.objects.get(pk=competencia_id)
        return 200, competencia
    except Competencia.DoesNotExist as e:
        return 404, {"message": "Competencia no existe"}

@api.post("/contact", response={201: ContactSchema})
def create_contact(request, contact: ContactSchema):
    contact = Contact.objects.create(**contact.dict())
    return contact

@api.get("/contact", response=List[ContactSchema])

def negocios(request):
    return Contact.objects.all()


@api.get("/negocios", response=List[NegocioSchema])
def negocios(request):
    return Negocios.objects.all()

@api.get("/negocios/{negocio_id}", response={200: NegocioSchema, 404:NotFoundSchema})
def negocio(request, negocio_id: int):
    try:
        negocio = Negocios.objects.get(pk=negocio_id)
        return 200, negocio
    except Negocios.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}

@api.post("/negocios", response={201: NegocioSchema})
def create_negocio(request, negocio: NegocioSchema):
    negocio = Negocios.objects.create(**negocio.dict())
    return negocio

@api.put("/negocios/{negocio_id}", response={200: NegocioSchema, 404:NotFoundSchema})
def change_negocio(request, negocio_id: int, data: NegocioSchema):
    try:
        negocio = Negocios.objects.get(pk=negocio_id)
        for attribute, value in data.dict().items():
             setattr(negocio, attribute, value)
        negocio.save()
        return 200, negocio
    except Negocios.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}
         
@api.delete("/negocios/{negocio_id}", response={200:None, 404:NotFoundSchema})
def delete_negocio(request, negocio_id: int, data: NegocioSchema):
    try:
        negocio = Negocios.objects.get(pk=negocio_id)
        negocio.delete()
        return 200 
    except Negocios.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}

@api.get("/productos", response=List[ProductoSchema])
def productos(request):
    print(Producto.objects.filter(negocio_parent_id=2))
    return Producto.objects.all()

@api.get("/productos/sorted/{negocio_parent_id}", response=List[ProductoSchema])
def productosfilt(request, negocio_parent_id: int):
    try:
        producto = Producto.objects.filter(negocio_parent_id=negocio_parent_id)
        return 200, producto
    except Producto.DoesNotExist as e:
        return 404, {"message": "Producto no existe"}

@api.get("/productos/{producto_id}", response={200:ProductoSchema, 404:NotFoundSchema})
def producto(request, producto_id: int):
    try:
        producto = Producto.objects.get(pk=producto_id)
        return 200, producto
    except Producto.DoesNotExist as e:
        return 404, {"message": "Producto no existe"}
