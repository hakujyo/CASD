from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentViews(APIView):
    def get(self, request, pk):
        if pk:
            try:
                obj = Student.objects.get(id=pk)
                serializer = StudentSerializer(obj, many=False)
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return JsonResponse({"msg": "Id not exist"}, status=404)
        else:
            obj = Student.objects.all()
            serializer = StudentSerializer(obj, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


    def post(self, request):
        verify_data = StudentSerializer(data=request.data)
        if verify_data.is_valid():
            verify_data.save()
            return JsonResponse({"msg": "Create success!", "data": verify_data.data}, status=200)
        else:
            return JsonResponse(verify_data.errors)


    def put(self, request, pk):
        obj = None
        try:
            obj = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return JsonResponse({"msg": "Id not exist"}, status=404)
        obj_ser = StudentSerializer(instance=obj, data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return JsonResponse({"msg": "Update success!"}, status=200)
        else:
            return JsonResponse({"msg": "Updata fail! Please check your body!"}, status=404)
        res = {"code": code, "msg": msg}
        return Response(res)


    def delete(self, request, pk):
        student = None
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return JsonResponse({"msg": "Id not exist"}, status=404)
        student.delete()
        return JsonResponse({"msg": "Delete success!"}, status=200)