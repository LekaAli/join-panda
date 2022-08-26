from rest_framework import serializers

from csvapp.models import DataTable


class DataTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataTable
        fields = "__all__"

    def validate(self, validated_data):
        has_valid_fields = False
        print(validated_data)
        request = self.context.get("request")
        date = validated_data.get("date")
        country = validated_data.get("country")
        if "retrieve-rows" not in request.path:
            purchase_or_sale = validated_data.get("purchase_or_sale")
            currency = validated_data.get("currency")
            net = validated_data.get("net")
            vat = validated_data.get("vat")
            if not purchase_or_sale:
                raise serializers.ValidationError({"purchase_or_sale": "This is a required field."})
            if not currency:
                raise serializers.ValidationError({"currency": "This is a required field."})
            if not net:
                raise serializers.ValidationError({"net": "This is a required field."})
            if not vat:
                raise serializers.ValidationError({"vat": "This is a required field."})

        if not date:
            raise serializers.ValidationError({"date": "Invalid date format. Requires date format YYYY/MM/DD"})
        if not country:
            raise serializers.ValidationError({"country": "This is a required field."})

        if "retrieve-rows" in request.path:
            validated_data.update({"date__range": [validated_data["date"]] * 2})
            validated_data.pop("date")
        return validated_data
