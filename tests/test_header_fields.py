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


def test_validate_index_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.header_schema_definitions(),
                                                   setup[["_index"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_id_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.header_schema_definitions(),
                                                   setup[["_id"]]), \
        "Field validation failed, please check the csv file for more details."


def test_validate_score_field(setup):
    assert steps.schema_definition.validate_fields(setup, schema_definition.header_schema_definitions(),
                                                   setup[["_score"]]), \
        "Field validation failed, please check the csv file for more details."
