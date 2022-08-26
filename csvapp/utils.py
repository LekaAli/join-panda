import coreapi.exceptions
from django.contrib.auth import settings
from datetime import datetime
from coreapi import Client


def format_date(date):
    if date:
        try:
            year, month, day = date.split("/")
            if len(year) == 4 and len(month) in [1, 2] and len(day) in [1, 2]:
                date = datetime.strptime(date, settings.OLD_DATE_INPUT_FORMATS).strftime(settings.DATE_INPUT_FORMATS)
            else:
                raise ValueError("")
        except ValueError:
            return None
    return date


def map_fieldnames(row):
    field_mapping = {
        "Date": "date",
        "Purchase/Sale": "purchase_or_sale",
        "Country": "country",
        "Currency": "currency",
        "Net": "net",
        "VAT": "vat",
    }
    row = {db_name: format_date(row[csv_name]) if db_name == 'date' else row[csv_name] for csv_name, db_name in field_mapping.items()}
    return row


def convert_currency(data_row):
    time_frame = data_row["date"]
    currency = data_row["currency"]
    external_service_url = f"{settings.CENTRAL_BANK_EXR_SERVICE_URL}/D.{currency}.EUR.SP00.A?startPeriod={time_frame}&endPeriod={time_frame}&format=jsondata"
    client = Client()
    try:
        response = client.get(external_service_url)
        data_row
    except coreapi.exceptions.ErrorMessage:
        pass
    return data_row
