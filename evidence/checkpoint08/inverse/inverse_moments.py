#!/usr/bin/env python3
"""Exact deterministic inverse of limiting integer-Renyi entropy memory.

No Haar samples. Standard-library rational arithmetic handles every matrix,
inverse coefficient, and moment/Newton check. Optional quantum witnesses are
formed from rational cos(2*Cartan angle) values and hence are exactly physical.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json


def catalan(m):
    return comb(2*m, m)//(m+1)


def covariance_matrix(rank):
    return [[Q(k*comb(2*m, m-k)**2, (m-1)**2*catalan(m)**2)
             if k <= m else Q(0)
             for k in range(2, rank+1)] for m in range(2, rank+1)]


def invert_lower(a):
    n = len(a)
    b = [[Q(0) for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(row+1):
            b[row][col] = (Q(int(row == col))
                          - sum(a[row][j]*b[j][col] for j in range(row)))/a[row][row]
    return b


def matvec(a, x):
    return [sum(u*v for u, v in zip(row, x)) for row in a]


def moments(spectrum, rank):
    return [sum(x**m for x in spectrum) for m in range(1, rank+1)]


def newton_elementary(power_sums):
    e = [Q(1)]
    for j in range(1, len(power_sums)+1):
        e.append(sum((-1)**(k-1)*e[j-k]*power_sums[k-1]
                     for k in range(1, j+1))/j)
    return e


def polynomial_from_roots(roots):
    coeff = [Q(1)]
    for root in roots:
        out = [Q(0)]*(len(coeff)+1)
        for j, c in enumerate(coeff):
            out[j] += c
            out[j+1] -= root*c
        coeff = out
    return coeff


def cartan_spectrum(x, y, z):
    """x,y,z=cos(2*a),cos(2*b),cos(2*c) in [0,1]."""
    a, b, c = x*y, x*z, y*z
    return [Q(1+a+b+c, 4), Q(1-a-b+c, 4),
            Q(1-a+b-c, 4), Q(1+a-b-c, 4)]


def stringify(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): stringify(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [stringify(v) for v in x]
    return x


def main():
    rank = 12
    a = covariance_matrix(rank)
    b = invert_lower(a)
    variances = [sum(row) for row in a]
    assert variances == [Q(m, 4) for m in range(2, rank+1)]
    corr_inverse = [[v*variances[j] for j, v in enumerate(row)] for row in b]
    gain_c = [sum(abs(v) for v in row) for row in b]
    gain_corr = [sum(abs(v) for v in row) for row in corr_inverse]
    for i in range(rank-1):
        for j in range(rank-1):
            assert sum(a[i][k]*b[k][j] for k in range(rank-1)) == int(i == j)

    spectra = {
        'product': [Q(1), Q(0), Q(0), Q(0)],
        'rank2': [Q(3,4), Q(1,4), Q(0), Q(0)],
        'flat_rank4': [Q(1,4)]*4,
        'interior_cartan': cartan_spectrum(Q(1,5), Q(2,5), Q(3,5)),
        'rank12_general_probability': [Q(j,78) for j in range(1,13)],
    }
    witnesses = {}
    for name, spec in spectra.items():
        assert sum(spec) == 1 and min(spec) >= 0
        ps = moments(spec, rank)
        covs = matvec(a, ps[1:])
        assert matvec(b, covs) == ps[1:]
        e = newton_elementary(ps)
        padded = spec+[Q(0)]*(rank-len(spec))
        expected = polynomial_from_roots(padded)
        assert [(-1)**j*v for j,v in enumerate(e)] == expected
        witnesses[name] = {'spectrum': spec, 'moments_through_4': ps[:4],
                           'covariances_2_3_4': covs[:3],
                           'characteristic_polynomial': expected}

    # Each row's infinity-error amplification is attained by these independent
    # signed measurement errors. This does not assert physical realizability
    # of perturbed moments, which is unnecessary for a measurement-noise bound.
    noise=Q(1,10**6)
    adversarial_noise = []
    for row in corr_inverse[:3]:
        errors = [noise*(1 if z > 0 else -1 if z < 0 else 0) for z in row]
        error = sum(x*y for x,y in zip(row,errors))
        assert error == noise*sum(abs(x) for x in row)
        adversarial_noise.append(error)

    # Physical two-qubit family approaching flat spectrum. Cartan variables
    # (x,y,z)=(0,2*h,1) give eta=(1/4+h/2,1/4+h/2,1/4-h/2,1/4-h/2).
    # Here ||eta-flat||_2=h while F2-1/4=h^2, exactly.
    near_flat = []
    for h in [Q(1,10),Q(1,100),Q(1,1000)]:
        eta = cartan_spectrum(Q(0),2*h,Q(1))
        ps = moments(eta,4)
        assert ps[1]-Q(1,4) == h*h
        assert sum((v-Q(1,4))**2 for v in eta) == h*h
        near_flat.append({'h':h,'spectrum':eta,'F2_excess':ps[1]-Q(1,4)})

    report = {
        'definition': 'C_m=lim d^2 Cov(S_m(U psi),S_m(psi)); rho_m=4*C_m/m',
        'max_rank_checked':rank,
        'covariance_forward_matrix':a,
        'covariance_inverse_matrix':b,
        'correlation_inverse_matrix':corr_inverse,
        'variance_marginal':variances,
        'worst_case_absolute_noise_gain_covariances':gain_c,
        'worst_case_absolute_noise_gain_correlations':gain_corr,
        'correlation_error_1e_minus_6_gives_F2_F3_F4_errors':adversarial_noise,
        'exact_witnesses':witnesses,
        'physical_near_flat_root_sensitivity':near_flat,
        'checks':'All exact matrix, covariance, Newton, sharp noise, and physical near-flat checks passed.',
    }
    path = Path(__file__).with_name('inverse_results.json')
    path.write_text(json.dumps(stringify(report),indent=2)+'\n')
    print('m  covariance-noise gain  correlation-noise gain')
    for m,g,h in zip(range(2,rank+1),gain_c,gain_corr):
        print(m,str(g),str(h))
    print(report['checks'])
    print(path)


if __name__ == '__main__':
    main()
