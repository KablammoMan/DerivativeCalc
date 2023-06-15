def deriva(eff: int, x: bool, exp: int) -> str:
    "Returns the derivative of the argument parsed"
    if x:
        if exp-1 == 0:
            return str(eff*exp)
        elif exp-1 == 1:
            return str(eff*exp)+"x"
        else:
            return str(eff*exp)+"x^"+str(exp-1)
    else:
        return "0"

def derive(eq: str, rec: bool) -> str:
    "Returns the derivative equation of a function"
    eq = eq.replace(" ", "")
    eq = eq.replace("**", "^")
    newe = ""
    arg = ""
    for i in eq:
        if i != "+" and i != "-":
            arg += i
        else:
            sa = split_arg(arg)
            da = deriva(sa[0], sa[1], sa[2])
            if da != "0":
                newe += da + i
            arg = ""
    sa = split_arg(arg)
    da = deriva(sa[0], sa[1], sa[2])
    if da != "0":
        newe += da
    if newe[-1] == "+" or newe[-1] == "-":
        newe = newe[:-1]
    if not rec or not "^" in newe:
        return newe
    else:
        return derive(newe, rec)

def split_arg(arg: str) -> list:
    "Splits the provided argument into 'coefficient: int, x: bool, exponent: int'"
    eff_p = True
    s_eff = ""
    eff = 1
    s_exp = ""
    exp = 1
    x_p = False
    for j in arg:
        if eff_p == False and j != "^" and j != "x":
            s_exp += j
        elif eff_p == True and j != "x":
            s_eff += j
        elif j == "x":
            eff_p = False
            x_p = True
    if s_eff != "":
        eff = int(s_eff)
    if s_exp != "":
        exp = int(s_exp)
    ret = [eff, x_p, exp]
    return ret

inp = input("Enter eq: ").lower()
rec = ""
while not rec in ["y", "n"]:
    rec = input("Rec (y/N)? ").lower()
if rec == "y":
    print(derive(inp, True))
else:
    print(derive(inp, False))