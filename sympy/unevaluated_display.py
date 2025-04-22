# unevaluated_display.py  -- put this on PYTHONPATH or %run it in a notebook
from sympy import Pow, S
from sympy.printing.latex import latex
from IPython.display import display, Math

__all__ = ["show_unevaluated"]

def show_unevaluated(base, exp, *, evaluate=False, **latex_kwargs):
    """
    Display (base)**(exp) without rewriting fractional exponents as roots.

    Parameters
    ----------
    base, exp : str | int | Rational | Expr
        Anything SymPy's S() can convert.
    evaluate : bool, optional (default=False)
        Forwarded to Pow(..., evaluate=evaluate).
    **latex_kwargs :
        Extra keyword arguments passed straight to sympy.printing.latex.latex().
        `root_notation` is forced to False unless you explicitly override it.
    """
    # ensure we preserve 1/10, 1/20, etc. as Rational objects
    base = S(base)
    exp  = S(exp)

    expr = Pow(base, exp, evaluate=evaluate)

    # user can still override if they *want* root notation
    if "root_notation" not in latex_kwargs:
        latex_kwargs["root_notation"] = False

    tex = latex(expr, **latex_kwargs)
    display(Math(tex))
    return expr            # return SymPy object in case caller needs it
