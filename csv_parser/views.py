from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from csv_parser.reader import cacu_csv_reader1
from csv_parser.reader import cacu_csv_reader2


def test(request):
    return HttpResponse("Hello, World!")


@api_view(['POST'])
def file_test_1(request):
    if request.method == 'POST':
        if 'file' not in request.data:
            raise ParseError("Empty content")

        file = request.FILES['file']

        cacu_csv_reader1(file)

        return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def file_test_2(request):
    if request.method == 'POST':
        if 'file' not in request.data:
            raise ParseError("Empty content")

        file = request.FILES['file']

        response_data = cacu_csv_reader2(file)

        return JsonResponse(response_data)
        return Response(status=status.HTTP_201_CREATED)