import pytest

@pytest.fixture
def sample_data():
    print("Preparing sample data...")
    return [100, 200, 300]

def test_total(sample_data):
    assert sum(sample_data) == 600

def test_max_value(sample_data):
    assert max(sample_data) == 300
