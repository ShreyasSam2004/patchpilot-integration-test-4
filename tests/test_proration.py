from decimal import Decimal

import pytest

from billing.proration import calculate_prorated_charge


def test_full_month_charge():
    assert calculate_prorated_charge(
        Decimal("30.00"), days_used=30, days_in_billing_period=30
    ) == Decimal("30.00")


def test_zero_days_costs_nothing():
    assert calculate_prorated_charge(
        Decimal("30.00"), days_used=0, days_in_billing_period=30
    ) == Decimal("0.00")


def test_rejects_days_beyond_period():
    with pytest.raises(ValueError, match="days used"):
        calculate_prorated_charge(
            Decimal("30.00"), days_used=31, days_in_billing_period=30
        )


def test_rejects_invalid_billing_period():
    with pytest.raises(ValueError, match="billing period"):
        calculate_prorated_charge(
            Decimal("30.00"), days_used=0, days_in_billing_period=0
        )
