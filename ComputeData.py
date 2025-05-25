
def exportcommands(file, dico):
    OB, CB = r"{", r"}"
    _FH = open(file, 'w')
    for k in dico.keys():
        value, units = dico[k]
        nc = f"\\newcommand\\{k}{OB}\\si{OB}\\num{OB}{value}{CB}{units}{CB}{CB}"
        _FH.write(f"{nc}\n")
    _FH.close()


################################################################################

from scipy.constants import epsilon_0
V = 200


################################################################################

exportcommands("data.tex", {
    'epsilonzero'       : (f"{epsilon_0:.3E}",      f"\\farad\\per\\meter"),    
    'drivepotential'    : (f"{V}",                  f"\\volt")
    })
