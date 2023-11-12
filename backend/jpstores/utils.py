from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


def custom_paginate(self, data):
    page = self.paginate_queryset(data)

    if page is not None:
        serializers = self.get_serializer(page, many=True, read_only=True)
        return self.get_paginated_response(serializers.data)

    serializers = self.get_serializer(data, many=True, read_only=True)
    return Response(serializers.data, HTTP_200_OK)
