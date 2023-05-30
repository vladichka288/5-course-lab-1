from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import PhoneNumber
from .serializers import PhoneSerializer
from rest_framework.permissions import IsAuthenticated


class CreatePhoneDir(GenericAPIView):
    serializer_class = PhoneSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data
        if PhoneNumber.objects.filter(name=data.get('name')).exists():
            return Response('Contact already exist', status=409)
        new_phone_dir = PhoneNumber(book_owner=request.user, name=data.get('name'), phone_number1=data.get('phone_number1'), phone_number2=data.get('phone_number2'))
        new_phone_dir.save()
        response = new_phone_dir
        return Response(phone_to_json(response), status=201)


def phone_to_json(model):
    return {'book_owner': model.book_owner.id, 'name': model.name, 'phone_number1': model.phone_number1, 'phone_number2': model.phone_number2}


class GetPhoneList(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        phone_list = PhoneNumber.objects.filter(book_owner=request.user).order_by('name').values()
        return Response(phone_list, status=200)


class EditContact(GenericAPIView):
    serializer_class = PhoneSerializer
    permission_classes = (IsAuthenticated, )

    def put(self, request):
        data = request.data
        if not PhoneNumber.objects.filter(name=data.get('name')).exists():
            return Response('NotFound', status=404)
        contact = PhoneNumber.objects.get(name=data.get('name'))
        if 'name' in data.keys():
            contact.name = data.get('name')
        if 'phone_number1' in data.keys():
            contact.phone_number1 = data.get('phone_number1')
        if 'phone_number2' in data.keys():
            contact.phone_number2 = data.get('phone_number2')
        contact.save()
        return Response(phone_to_json(contact), status=200)


class DeleteContact(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, name):
        if not PhoneNumber.objects.filter(name=name).exists():
            return Response('NotFound', status=404)
        contact = PhoneNumber.objects.get(name=name)
        contact.delete()
        return Response(status=204)
