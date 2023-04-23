import sympy as sp
from sympy.abc import x, y, z
from buchberger_alg import groebner 

def is_univariate(f):
    """Returns True if 'f' is univariate in its last variable. """
    for monom in f.monoms():
        if any(monom[:-1]):
            return False
    return True

def subs_root(f, gen, zero):
    """ Substitute in a solution for a generator """
    p = f.as_expr({gen: zero})

    if f.degree(gen) >= 2:
        p = p.expand(deep=False)

    return p

def solve_poly_system_recursive(F, gens, entry=False):
    """ Recursive helper function 
    Based on SymPy solve_generic
    SymPy License: https://github.com/sympy/sympy/blob/master/LICENSE
    """
    basis = groebner(F, *gens)

    if len(basis) == 1 and basis[0].is_ground:
        if not entry:
            return []
        else:
            return None

    if len(basis) < len(gens):
        raise ValueError("Potentially infinite solutions.")

    univar = [x for x in basis if is_univariate(x)]

    if len(univar) == 1:
        f = univar.pop()
    else:
        raise ValueError("Potentially infinite solutions.")

    # find solutions for the univariate element
    gens = f.gens
    gen = gens[-1]

    zeros = list(sp.roots(f.ltrim(gen)).keys())

    if not zeros:
        # no solution
        return []
    
    # single variable
    if len(basis) == 1:
        return [(zero,) for zero in zeros]

    # recursively solve for the rest of the basis 
    solutions = []
    for zero in zeros:
        new_system = []
        new_gens = gens[:-1]

        # back substitution of solution
        for b in basis[:-1]:
            eq = subs_root(b, gen, zero)

            if eq is not sp.core.S.Zero:
                new_system.append(eq)

        new_system = sp.parallel_poly_from_expr(new_system, *new_gens)[0]
        for solution in solve_poly_system_recursive(new_system, new_gens):
            solutions.append(solution + (zero,))

    return solutions


def solve_poly_system(F, *gens):
    """ Solve a system of polynomials with Groebner basis
    Based on SymPy solve_generic
    SymPy License: https://github.com/sympy/sympy/blob/master/LICENSE
    """
    result = solve_poly_system_recursive(F, gens, entry=True)
    return sorted(result , key=sp.default_sort_key)

if __name__ == "__main__":
    # polynomials to test
    F = [x**2 + y + z, x + y**2 + z, x + y + z**2]
    F = list(map(lambda x : sp.Poly(x), F))

    g_basis_sympy = sp.groebner(F, x, y, z, order="lex")
    print(f"Groebner's basis (SymPy): {g_basis_sympy}")

    solution = solve_poly_system(F, x, y, z)
    print(f"Poly Sols: {solution}")

    solution_sympy = sp.solve_poly_system(F, x, y, z)
    print(f"Poly Sols (SymPy): {solution_sympy}")


