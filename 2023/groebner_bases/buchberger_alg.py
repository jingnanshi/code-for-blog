import copy
import itertools
import sympy as sp
from sympy.abc import x, y, z


def s_poly(f, g):
    """Calculate the S-polynomial for f and g"""
    lcm = sp.lcm(sp.LM(f), sp.LM(g))
    s = sp.expand(lcm * (f / sp.LT(f) - g / sp.LT(g)))
    return s


def buchberger(F, *gens, domain=sp.QQ):
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
    G = buchberger(F, *gens, domain=sp.QQ)

    # reduce
    G_reduced = []
    for i, g in enumerate(G):
        _, remainder = sp.reduced(g, G_reduced[:i] + G[i+1:])
        if remainder != 0:
            G_reduced.append(remainder)
 
    # sort
    # courtesy of SymPy buchberger implementation
    G_reduced = [sp.polys.polytools.poly_from_expr(x, domain=sp.QQ)[0] for x in G_reduced]
    ring = sp.ring(gens, domain=sp.QQ)[0]
    temp = [ring.from_dict(poly.rep.to_dict()) for poly in G_reduced if poly]
    breakpoint()
    G = sorted(temp, key=lambda f: ring.order(f.LM), reverse=True)

    breakpoint()
    
    return [x.monic() for x in G_reduced]


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

