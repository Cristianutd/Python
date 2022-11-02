import pytest
import pandas as pd
import steps
import json
from steps import schema_definition


@pytest.fixture(scope="module")
def setup():
    with open('../test_data/elastic_data.json', 'r') as f:
        data = json.loads(f.read())
        df = pd.json_normalize(data)
        yield df


def test_validate_category_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.category"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_currency_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.currency"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_firstname_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.customer_first_name"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_fullname_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.customer_full_name"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_customergender_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.customer_gender"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_customerid_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.customer_id"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_customerlastname_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.customer_last_name"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_customerphone_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.customer_phone"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_dayofweek_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.day_of_week"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_dayofweeknumber_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.day_of_week_i"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_email_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.email"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_manufacturer_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.manufacturer"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_orderdate_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.order_date"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_orderid_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.order_id"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_products_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.products"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_sku_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.sku"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_taxfultotalprice_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.taxful_total_price"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_taxlesstotalprice_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.taxless_total_price"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_totalquantity_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.total_quantity"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_totaluniqueproducts_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.total_unique_products"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_type_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.type"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_user_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.user"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_geoip_country_iso_code_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.geoip.country_iso_code"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_geoip_location_lon_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.geoip.location.lon"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_geoip_location_lat_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.geoip.location.lat"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_geoip_region_name_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.geoip.region_name"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_geoip_continent_name_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.geoip.continent_name"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_geoip_city_name_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.geoip.city_name"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_event_dataset(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.source_schema_definitions(),
                                                   setup[["_source.event.dataset"]]), \
        "Field validation failed, please check the csv file for more details."
