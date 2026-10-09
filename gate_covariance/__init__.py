"""Deterministic evaluation of the fixed-support Haar entropy covariance law.

All covariances returned by this package are coefficients in the large-d
limit, in natural-log units. They are not finite-dimensional predictions
with an error estimate. Series sums use an explicit finite cutoff with exact marginal normalization.
Tail helpers evaluate analytical series bounds in floating point; they are
not outward-rounded certificates and do not enclose other numerical errors.
"""

from .core import (
    coefficients,
    marginal_variance,
    same_state_covariance,
    marginal_tail,
    covariance_tail_bound,
    correlation_tail_bound,
    covariance,
    correlation,
    operator_schmidt_probabilities,
    same_order_covariance,
    spatial_correlation_bound,
)

__all__ = [
    "coefficients", "covariance", "correlation",
    "marginal_variance", "same_state_covariance", "marginal_tail",
    "covariance_tail_bound", "correlation_tail_bound",
    "operator_schmidt_probabilities", "same_order_covariance",
    "spatial_correlation_bound",
]
