    def delete(self, request, pk):
        student = None
        try:
            student = {tablename}.objects.get(id=pk)
        except {tablename}.DoesNotExist:
            return JsonResponse({{"msg": "Id not exist"}}, status=404)
        student.delete()
        return JsonResponse({{"msg": "Delete success!"}}, status=200)