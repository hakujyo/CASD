    def get(self, request, pk):
        if pk:
            try:
                obj = {tablename}.objects.get(id=pk)
                serializer = {tablename}Serializer(obj, many=False)
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            except {tablename}.DoesNotExist:
                return JsonResponse({{"msg": "Id not exist"}}, status=404)
        else:
            obj = {tablename}.objects.all()
            serializer = {tablename}Serializer(obj, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)