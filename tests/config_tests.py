from nose.tools import assert_equal
from wunderapi.config import Config


def setup():
    return Config(config_file="tests/resources/test_config")


def test_parse_config_with_correct_parms():
    pass


def test_parse_config_with_incorrect_parms():
    pass


def test_config_created_with_default_parms():
    config = setup()
    config.parse_config()
    assert_equal(config.api_key, 'API Key')
    assert_equal(config.location, 'Zipcode')
    assert_equal(config.date_format, 'date')
    assert_equal(config.units, 'english')
