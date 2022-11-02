import json
import pandas as pd
import pytest
import steps
from steps import schema_definition


@pytest.fixture(scope="module")
def setup():
    with open('../test_data/elastic_data.json', 'r') as f:
        data = json.loads(f.read())
        df = pd.json_normalize(data)
        products_df = pd.json_normalize(df["_source.products"])
        product_details0 = pd.json_normalize(products_df[0])
        product_details1 = pd.json_normalize(products_df[1])
        product_details1 = product_details1.reset_index(drop=True)
        products = pd.concat([product_details0, product_details1], axis=0)
        products = products.reindex()
        yield products


def test_validate_base_price_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["base_price"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_discount_percentage_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["discount_percentage"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_quantity_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["quantity"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_manufacturer_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["manufacturer"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_tax_amount_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["tax_amount"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_product_id_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["product_id"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_category_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["category"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_sku_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["sku"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_taxless_price_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["taxless_price"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_unit_discount_amount_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["unit_discount_amount"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_min_price_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["min_price"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_id_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["_id"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_discount_amount_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["discount_amount"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_created_on_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.product_schema_definitions(),
                                                   setup[["created_on"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_product_name_field(setup):
    assert steps.schema_definition.validate_fields(setup,
                                                   schema_definition.product_schema_definitions(),
                                                   setup[["product_name"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_price_field(setup):
    assert steps.schema_definition.validate_fields(setup,
                                                   schema_definition.product_schema_definitions(),
                                                   setup[["price"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_taxful_price_field(setup):
    assert steps.schema_definition.validate_fields(setup,
                                                   schema_definition.product_schema_definitions(),
                                                   setup[["taxful_price"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_base_unit_price_field(setup):
    assert steps.schema_definition.validate_fields(setup,
                                                   schema_definition.product_schema_definitions(),
                                                   setup[["base_unit_price"]]), \
        "Field validation failed, please check the csv file for more details."
