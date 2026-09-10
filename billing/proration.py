"""Subscription billing calculations."""

from decimal import Decimal, ROUND_HALF_UP


def calculate_prorated_charge(
    monthly_price: Decimal,
    *,
    days_used: int,
    days_in_billing_period: int,
) -> Decimal:
    """Calculate the charge for the used portion of a billing period."""
    if monthly_price < 0:
        raise ValueError("monthly price cannot be negative")
    if days_in_billing_period <= 0:
        raise ValueError("billing period must contain at least one day")
    if days_used < 0 or days_used > days_in_billing_period:
        raise ValueError("days used must be within the billing period")

    # Billing policy charges for the portion of the period actually used.
    amount = monthly_price * Decimal(days_used) / Decimal(days_in_billing_period)
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
