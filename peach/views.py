from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from peach.models import Item
from peach.serializers import ListItemSerializer


# class FirstAPIinmylife(APIView):
# def get(self, request):
# #     response={
# #         "message":"hello,comin over tonight?",
# #         "name":"your mom"
# #
# #     }
# #
# #     return Response(data=response,status=status.HTTP_200_OK)
# #   item = Item.objects.filter(name="cheesecake").first()
# array = ["pizza","abaali"]
# items=Item.objects.filter(name__in=array).values_list("id",flat=True)
# #   items = Item.objects.filter(price__lte=9).values_list("name", flat=True)
# return Response(data={"items": items}, status=status.HTTP_200_OK)
# example_name = "ecake"
# if Item.objects.filter(name=example_name).exists():
#     return Response(data={"key": Item.objects.filter(name=example_name).first().id}, status=status.HTTP_200_OK)
# else:
#     return Response(data={"message":"not found"},status=status.HTTP_404_NOT_FOUND)
# def post(self, request):
#
#     name=(request.data.get("name"))
#     price = float(request.data.get("price"))
#     try:
#         Item.objects.create(name=name, price= price)
#     except IntegrityError:
#         return Response(data={"error": f"name already exists...:{name}"},status=status.HTTP_406_NOT_ACCEPTABLE)
#     return Response(data={"message":"done"},status=status.HTTP_201_CREATED)
# try:
#     number = int(request.data.get("number"))
# except ValueError:
#     return Response(data={"ERROR": f"INVALID INPUT:{request.data.get('number')}"}, status=status.HTTP_400_BAD_REQUEST)
#
# return Response(data={"number":2*number},status=status.HTTP_200_OK)
# def get(self,request,**kwargs):
#
#     id = kwargs.get("id")
#     try:
#         selected_item = Item.objects.get(id=id)
#     except Item.DoesNotExist:
#         return Response(data={"message":f"not found:{id}"},status=status.HTTP_404_NOT_FOUND)
#
#     return Response(data={"name":selected_item.name,"price":selected_item.price},status=status.HTTP_200_OK)
# def put(self, request, **kwargs):
#     id = kwargs.get("id")
#     if Item.objects.filter(id=id).exists():
#
#         name = (request.data.get("name"))
#         price = float(request.data.get("price"))
#         Item.objects.filter(id=id).update(name=name, price=price)
#         return Response(data={"message": "done"}, status=status.HTTP_201_CREATED)
#
#     else:
#         return Response(data={"message": f"not found:{id}"}, status=status.HTTP_404_NOT_FOUND)
#
#
# def delete(self, request, **kwargs):
#     id = kwargs.get("id")
#     if Item.objects.filter(id=id).exists():
#         Item.objects.filter(id=id).delete()
#
#         return Response(data={"message": "done"}, status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response(data={"message": f"not found:{id}"}, status=status.HTTP_404_NOT_FOUND)


class ListItemView(APIView):
    def get(self, request, **kwargs):
        items=Item.objects.all()
        serializer= ListItemSerializer(items,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

