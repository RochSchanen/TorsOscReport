
dico = {}

from scipy.constants import epsilon_0
dico['epsilonzero'] = f"{epsilon_0:.3E}", f"\\Farad\\per\\meter"    

V = 200 # [V]
dico['drivepotential'] = f"{V}", "\\volt"









############################################################################
OB, CB = r"{", r"}"
_FH = open("data.tex", 'w')
for k in dico.keys():
    value, units = dico[k]
    nc = f"\\newcommand\\{k}{OB}\\si{OB}\\num{OB}{value}{CB}{units}{CB}{CB}"
    _FH.write(f"{nc}\n")
_FH.close()
