import numpy as np
import pandas_schema
from pandas_schema import Column
from pandas_schema.validation import CustomElementValidation, InListValidation, CustomSeriesValidation
from steps.field_validators import check_integer, check_float, check_string, check_email, check_datetime, \
    check_only_string
from steps.utilities import output_details


def header_schema_definitions():
    int_validation = [CustomElementValidation(lambda i: check_integer(i), '--> is not integer')]
    str_validation = [CustomElementValidation(lambda i: check_string(i), '--> is not a string')]
    null_validation = [CustomElementValidation(lambda d: d is not np.nan, '--> field cannot be null')]

    schema = pandas_schema.Schema([
        Column('_index', str_validation + null_validation),
        Column('_id', str_validation + null_validation),
        Column('_score', int_validation + null_validation),
    ])

    return schema


def source_schema_definitions():
    int_validation = [CustomElementValidation(lambda i: check_integer(i), '--> is not integer')]
    float_validation = [CustomElementValidation(lambda i: check_float(i), '--> is not a valid amount')]
    str_validation = [CustomElementValidation(lambda i: check_string(i), '--> is not a string')]
    null_validation = [CustomElementValidation(lambda d: d is not np.nan, '--> field cannot be null')]
    email_validation = [CustomElementValidation(lambda s: check_email(s), "--> invalid email format")]
    datetime_validation = [CustomElementValidation(lambda s: check_datetime(s), "--> invalid datetime format")]
    only_strings_validation = [CustomElementValidation(lambda s: check_only_string(s),
                                                       "--> field contains numeric values and it is not allowed")]

    schema = pandas_schema.Schema([
        Column('_source.category', str_validation + null_validation),
        Column('_source.currency', str_validation + null_validation + [
            CustomSeriesValidation(lambda x: x.str.len() == 3, 'Length is not equal to 3 characters')]),
        Column('_source.customer_first_name', str_validation + null_validation + only_strings_validation),
        Column('_source.customer_full_name', str_validation + null_validation + only_strings_validation),
        Column('_source.customer_gender', [InListValidation(['MALE', 'FEMALE', 'OTHER'])]),
        Column('_source.customer_id', int_validation + null_validation),
        Column('_source.customer_last_name', str_validation + null_validation + only_strings_validation),
        Column('_source.customer_phone', str_validation + null_validation),
        Column('_source.day_of_week', str_validation + null_validation,
               [InListValidation(['Monday', 'Tuesday',
                                  'Wednesday', 'Thursday',
                                  'Friday', 'Saturday',
                                  'Sunday'])]),
        Column('_source.day_of_week_i', int_validation + null_validation,
               [InListValidation([1, 2, 3, 4, 5, 6, 7])]),
        Column('_source.email', str_validation + email_validation + null_validation),
        Column('_source.manufacturer', str_validation + null_validation),
        Column('_source.order_date', str_validation + datetime_validation + null_validation),
        Column('_source.order_id', int_validation + null_validation),
        Column('_source.products', str_validation + null_validation),
        Column('_source.sku', str_validation + null_validation),
        Column('_source.taxful_total_price', float_validation + null_validation),
        Column('_source.taxless_total_price', float_validation + null_validation),
        Column('_source.total_quantity', int_validation + null_validation),
        Column('_source.total_unique_products', int_validation + null_validation),
        Column('_source.type', str_validation + null_validation),
        Column('_source.user', str_validation + null_validation),
        Column('_source.geoip.country_iso_code', str_validation + null_validation + [
            CustomSeriesValidation(lambda x: x.str.len() == 2, 'Length is not equal to 2 characters')]),
        Column('_source.geoip.location.lon', float_validation + null_validation),
        Column('_source.geoip.location.lat', float_validation + null_validation),
        Column('_source.geoip.region_name', str_validation),
        Column('_source.geoip.continent_name', str_validation + null_validation + only_strings_validation),
        Column('_source.geoip.city_name', str_validation),
        Column('_source.event.dataset', str_validation + null_validation),
    ])

    return schema


def product_schema_definitions():
    float_validation = [CustomElementValidation(lambda i: check_float(i), "--> is not a valid amount")]
    str_validation = [CustomElementValidation(lambda i: check_string(i), "--> is not a string")]
    null_validation = [CustomElementValidation(lambda d: d is not np.nan, "--> field cannot be null")]
    datetime_validation = [CustomElementValidation(lambda s: check_datetime(s), "--> invalid datetime format")]

    schema = pandas_schema.Schema([
        Column('base_price', float_validation + null_validation),
        Column('discount_percentage', float_validation + null_validation),
        Column('quantity', float_validation + null_validation),
        Column('manufacturer', str_validation),
        Column('tax_amount', float_validation + null_validation),
        Column('product_id', float_validation + null_validation),
        Column('category', str_validation),
        Column('sku', str_validation),
        Column('taxless_price', float_validation + null_validation),
        Column('unit_discount_amount', float_validation + null_validation),
        Column('min_price', float_validation + null_validation),
        Column('_id', str_validation),
        Column('discount_amount', float_validation + null_validation),
        Column('created_on', datetime_validation),
        Column('product_name', str_validation),
        Column('price', float_validation + null_validation),
        Column('taxful_price', float_validation + null_validation),
        Column('base_unit_price', float_validation + null_validation)
    ])

    return schema


def validate_fields(df, schema, column):
    errors = schema.validate(df, column)
    if len(errors) == 0:
        return True
    else:
        output_details(errors)
        return False
