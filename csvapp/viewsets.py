import csv
import io

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.utils import model_meta
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed

from django.contrib.auth import settings

from csvapp.models import DataTable
from csvapp.serializers import DataTableSerializer
from csvapp.utils import format_date, map_fieldnames, convert_currency


class DataTableViewSet(viewsets.ModelViewSet):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer

    @action(methods=["get"], detail=False, url_name="retrieve-rows", url_path="retrieve-rows")
    def retrieve_rows(self, request):
        data = request.query_params.dict()
        data["date"] = format_date(data.get("date"))
        serializer = self.serializer_class(data=data, context={"request": request})
        if serializer.is_valid() is True:
            data = serializer.validated_data
            queryset = self.get_queryset().filter(**data)
            return Response(self.serializer_class(queryset, many=True).data)
        return Response(serializer.errors)

    @action(methods=["post"], detail=False, url_name="process-file", url_path="process-file")
    def process_file(self, request):
        created_records = None
        uploaded_csv_file = self.request.FILES.get("uploaded_csv_file")
        if uploaded_csv_file:
            csv_data = uploaded_csv_file.read().decode("utf-8-sig")
            csv_data_rows = csv.DictReader(io.StringIO(csv_data))

            csv_data_row_instances = [
                DataTable(
                    **map_fieldnames(csv_row)
                ) for csv_row in csv_data_rows
            ]
            try:
                created_records = DataTable.objects.bulk_create(objs=csv_data_row_instances, batch_size=100)
            except serializers.ValidationError:
                raise serializers.ValidationError({"errors": "failed to load the csv data."})
        created_records = self.paginate_queryset(created_records)
        serializer = self.serializer_class(created_records, context={"request": request}, many=True)
        return self.get_parser_context(serializer.data)


