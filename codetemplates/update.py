    def put(self, request, pk):
        obj = None
        try:
            obj = {tablename}.objects.get(pk=pk)
        except {tablename}.DoesNotExist:
            return JsonResponse({{"msg": "Id not exist"}}, status=404)
        obj_ser = {tablename}Serializer(instance=obj, data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return JsonResponse({{"msg": "Update success!"}}, status=200)
        else:
            return JsonResponse({{"msg": "Updata fail! Please check your body!"}}, status=404)
        res = {{"code": code, "msg": msg}}
        return Response(res)