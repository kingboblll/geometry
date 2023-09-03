def sqrt_sim(und_root):
    und_root = abs(int(und_root))
    rt_fc = []
    coef = 1
    if und_root < 0:
        return None
    elif und_root == 0:
        return 0
    else:
        for i in range(2, int(und_root**(0.5))+1):
            while und_root % (i**2) == 0:
                rt_fc.append(i)
                und_root /= i**2

        for ele in rt_fc:
            coef *= ele

        if coef == 1:
            sim_rad = "sqrt(" + str(und_root) + ")"

        else:
            sim_rad = str(coef) + '*sqrt(' + str(und_root) + ")"

        return sim_rad

def factor(a, b, c):
    if a == 0:
        return "This is not a quadratic equation"
    else:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            sol1 = complex(-b/(2*a), ((-discriminant)**0.5)/(2*a))
            sol2 = complex(-b/(2*a), -((-discriminant)**0.5)/(2*a))
            return "This equation has two complex solutions: " + str(sol1) + " and " + str(sol2)
        else:
            sol1 = -(-b + (discriminant)**0.5)/(2*a)
            sol2 = -(-b - (discriminant)**0.5)/(2*a)
            if discriminant == 0:
                return "This equation has one solution: " + str(round(-b/(2*a), 2))
            else:
                result = "This equation has two solutions: " + str(round(sol1, 2)) + " and " + str(round(sol2, 2))

                if isinstance(sol1, float): # Check if sol1 is a float
                    sim_sol1 = sqrt_sim(sol1**2) # Call sqrt_sim with sol1 as argument

                    if "*sqrt(1.0)" in sim_sol1:
                        sim_sol1 = sim_sol1.replace("*sqrt(1.0)", "")

                    if "sqrt(1)" in sim_sol1:
                        sim_sol1 = sim_sol1.replace("sqrt(1)", "1")

                    if sol1 < 0:
                        result += "\nSimplified radical sol1: -" + sim_sol1
                    else:
                        result += "\nSimplified radical sol1: " + sim_sol1


                if isinstance(sol2, float): # Check if sol2 is a float
                    sim_sol2 = sqrt_sim(sol2**2) # Call sqrt_sim with sol2 as argument

                    if "*sqrt(1.0)" in sim_sol2:
                        sim_sol2 = sim_sol2.replace("*sqrt(1.0)", "")

                    if "sqrt(1)" in sim_sol2:
                        sim_sol2 = sim_sol2.replace("sqrt(1)", "1")

                    if sol2 < 0:
                        result += "\nSimplified radical sol2: -" + sim_sol2
                    else:
                        result += "\nSimplified radical sol2: " + sim_sol2

                return result



"""
Example use:
print(factor(5, -25, -30))
"""
