"""Deterministic evaluation of the fixed-support Haar entropy covariance law.

All covariances returned by this package are coefficients in the large-d
limit, in natural-log units. They are not finite-dimensional predictions
with an error estimate. Series sums use an explicit finite cutoff.
"""

from .core import (
    coefficients,
    covariance,
    correlation,
    operator_schmidt_probabilities,
    same_order_covariance,
    spatial_correlation_bound,
)

__all__ = [
    "coefficients", "covariance", "correlation",
    "operator_schmidt_probabilities", "same_order_covariance",
    "spatial_correlation_bound",
]
