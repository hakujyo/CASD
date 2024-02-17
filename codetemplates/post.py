    def post(self, request):
        verify_data = {tablename}Serializer(data=request.data)
        if verify_data.is_valid():
            verify_data.save()
            return JsonResponse({{"msg": "Create success!", "data": verify_data.data}}, status=200)
        else:
            return JsonResponse(verify_data.errors)