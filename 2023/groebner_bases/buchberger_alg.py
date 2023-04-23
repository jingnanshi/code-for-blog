import copy
import itertools
import sympy as sp
from sympy.abc import x, y, z


def s_poly(f, g):
    """Calculate the S-polynomial for f and g"""
    lcm = sp.lcm(sp.LM(f), sp.LM(g))
    s = sp.expand(lcm * (f / sp.LT(f) - g / sp.LT(g)))
    return s


def buchberger(F):
    """Buchberger's Algorithm
    Note that this is slightly different from the pesudocode
    provided in Cox et. al. 2015.
    """
    G = copy.deepcopy(F)
    pqs = set(itertools.combinations(G, 2))
    while pqs:
        p, q = pqs.pop()
        s = s_poly(p, q)
        _, h = sp.reduced(s, G)
        if h != 0:
            for g in G:
                pqs.add((g, h))
            G.append(h)

    return G


def groebner(F, *gens):
    """Calculate a reduced Groebner basis for F.
    Use the default lex order.
    """
    # buchberger
    G = buchberger(F)

    # reduce
    G_reduced = []
    for i, g in enumerate(G):
        _, remainder = sp.reduced(g, G_reduced[:i] + G[i+1:])
        if remainder != 0:
            G_reduced.append(remainder)
 
    # sort
    # courtesy of SymPy buchberger implementation
    polys, opt = sp.parallel_poly_from_expr(G_reduced, *gens)
    ring = sp.polys.rings.PolyRing(gens, domain=polys[0].domain)
    polys = [ring.from_dict(poly.rep.to_dict()) for poly in polys if poly]
    G_reduced = sorted(polys, key=lambda f: f.LM, reverse=True)
    return sp.parallel_poly_from_expr([x.monic().as_expr() for x in G_reduced], *gens)[0]


if __name__ == "__main__":
    f1 = x**3 - 2 * x * y
    f2 = x**2 * y - 2 * y**2 + x
    G = [f1, f2]

    S = s_poly(f1, f2)
    print(f"S Poly: = {S}")

    a, r = sp.reduced(S, G)
    print(f"Remainder: {r}")

    g_basis_sympy = sp.groebner(G, x, y, z, order="lex")
    print(f"Groebner's basis (SymPy): {g_basis_sympy}")

    # test Buchberger
    g_basis = groebner(G, x, y, z)
    print(f"Groebner's basis: {g_basis}")

