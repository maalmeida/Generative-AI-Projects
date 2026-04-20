def solve_polynomial(points_data, degree):
    """
    points_data: List of tuples (x, y, type) 
                 e.g., (-3, -2, 'min')
    degree: Integer degree (e.g., 7)
    """
    # 1. Define the independent variable
    x = var('x')
    
    # 2. Create a list of coefficients [a0, a1, a2, ..., an]
    # We use a list comprehension to ensure valid Python identifiers
    coeffs = [var('a%d' % i) for i in range(degree + 1)]
    
    # 3. Define the polynomial function f(x) and its derivative
    f = sum(c * x^i for i, c in enumerate(coeffs))
    df = diff(f, x)
    
    equations = []
    
    # 4. Build the system based on user constraints
    for (px, py, ptype) in points_data:
        # Every point must satisfy f(x) = y
        equations.append(f.substitute(x=px) == py)
        
        # Extrema must satisfy f'(x) = 0
        if ptype in ['min', 'max', 'extrema']:
            equations.append(df.substitute(x=px) == 0)
            
    # 5. Check for under-determined vs over-determined systems
    num_vars = degree + 1
    num_eqs = len(equations)
    
    if num_eqs > num_vars:
        print(f"Warning: Over-determined. {num_eqs} equations for {num_vars} variables.")
    elif num_eqs < num_vars:
        print(f"Note: Under-determined. You need {num_vars - num_eqs} more constraints.")

    # 6. Solve the system
    sol = solve(equations, coeffs)
    
    if not sol or len(sol) == 0:
        return "No solution found. Check if constraints are mathematically possible."
    
    # 7. Substitute the first solution found back into the polynomial
    # solve() returns a list of solutions; we take the first one [0]
    final_poly = f.substitute(sol[0])
    
    return final_poly.expand()

# --- Example Execution ---
# Points: (-3,-2) min, (-2,-1) max, (0,-3) point, (2,-5) min, (3,0) point
constraints = [
    (-4, 1, 'min'),
    (0, 0, 'point'),
    (3, 2, 'max'),
    (4, -2, 'min')
]

# Solving for a degree 7 polynomial
result = solve_polynomial(constraints, 6)

print("Resulting Polynomial:")
print(result)