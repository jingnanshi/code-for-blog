import sympy as sp
from sympy.abc import x, y, z
from buchberger_alg import groebner 

def is_univariate(f):
    """Returns True if 'f' is univariate in its last variable. """
    for monom in f.monoms():
        if any(monom[:-1]):
            return False
    return True


def solve_poly_system(F, *gens):
    """ Solve a system of polynomials with Groebner basis"""

    G = groebner(F, *gens)
    breakpoint()
    
    return

if __name__ == "__main__":
    # polynomials to test
    F = [x**2 + y + z, x + y**2 + z, x + y + z**2]
    F = list(map(lambda x : sp.Poly(x), F))

    g_basis_sympy = sp.groebner(F, x, y, z, order="lex")
    print(f"Groebner's basis (SymPy): {g_basis_sympy}")

    A = list(sp.ordered([x**3*y, x**2, x]))
    B = list(sp.ordered([x, x**3*y, x**2]))
    solve_poly_system(F, x, y, z)


