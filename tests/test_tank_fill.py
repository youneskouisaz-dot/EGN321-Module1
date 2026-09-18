import pytest

from src.tank_fill import calculate_tank_volume


def test_r101_known_correct_case():
    result = calculate_tank_volume(10, 6, 8)
    assert result == pytest.approx(374.026, rel=1e-6)


def test_r102_known_correct_case():
    result = calculate_tank_volume(10, 6, 10.5)
    assert result == pytest.approx(490.909125, rel=1e-6)


def test_r108_regression_case():
    result = calculate_tank_volume(10, 6, 25.0)
    assert result == pytest.approx(935.065, rel=1e-6)


def test_negative_length_rejected():
    with pytest.raises(ValueError):
        calculate_tank_volume(-10, 6, 8)


def test_zero_depth_rejected():
    with pytest.raises(ValueError):
        calculate_tank_volume(10, 6, 0)
