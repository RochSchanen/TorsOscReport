
from math import pi

fh = open('./CalculatorOuput.txt', 'w')

def disp(s, x, u, n=''):
    fh.write(f'{s:4s} = {x:8.3f} {u:6s}')
    if n: fh.write(f'{n:30s}')
    fh.write('\n')

def sep(s=''): fh.write(f'\n{s}\n\n')

##############################################
eps0 = 8.854E-12  # F/m vacuum permitivity
k    = 2.618          # [N.m] torsion constant (spring constant)
##############################################

sep('----- Section 1')

##############################################
L    = 10E-3       # [m] Length
H    = 10E-3       # [m] Height
d    = 256E-6      # [m] gap
l    = 15E-3       # [m] centre of the electrodes
VS   = 600         # [V] static potential
V    = 7           # [V] AC drive
Q    = 980         # quality factor
f    = 141.8       # [Hz] frequency
VD   = VS          # [V] static detection voltage 
G    = 1E6         # [V/A] amplifier gain
##############################################

disp('eps0',eps0*1E12,'pF/m', 'vacuum permitivity')
disp('k', k, 'N.m', 'torsion contant')
disp('L', L*1E3, 'mm', 'Length')
disp('H', H*1E3, 'mm', 'Height')
disp('l', l*1E3, 'mm', 'centre of the electrodes')
disp('d', d*1E6, 'µm', 'gap')
disp('VS', VS,'V', 'static potential')
disp('VD', VD,'V', 'static detection potential')
disp('V', V, 'V', 'harmonic potential')
disp('Q', Q, '', 'quality factor')
disp('f', f, 'Hz', 'resonance frequency')
disp('G', G*1E-6,'V/µA', 'amplifier gain')

sep('-----')

# capacitance [F]
C = eps0 * L * H / d

disp('C', C*1E12, 'pF',' (1)')

# static force [N]
FS = 0.5*eps0*(L*H*VS**2) / d**2            
# static torque [N.m]
TS = FS*l
# static angular displacement [rad]
AS = TS/k
# static linear displacement
xS = 0.5*eps0*(L*H*VS**2)/d**2*l**2/k 

disp('FS', FS*1E3, 'mN',' (3)')
disp('TS', TS*1E6, 'µN.m',' (4)')
disp('AS', AS*180/pi*1E6, 'µDeg',' (5)')
disp('xS', xS*1E9, 'nm',' (8)')

# AC force
F = (eps0*L*H/d**2)*VS*V
# zero frequency response
x0 = (eps0*L*H/d**2)*VS*V*l**2/k
# response at resonance
x = Q*x0
# velocity
v = 2*pi*f*x

disp('F', F*1E6, 'µN','(11)')
disp('x0', x0*1E9, 'nm','(12)')
disp('x', x*1E6, 'µm','(22)')
disp('v', v*1E3, 'mm/s','(22)')

# current signal for 1mm/s
i = (eps0*L*H/d**2)*VD*1E-3
# voltage signal for 1mm/s
u = G*(eps0*L*H/d**2)*VD*1E-3

disp('i', i*1E9, 'nA','(27) for v = 1mm/s')
disp('u', u*1E3, 'mV','(28) for v = 1mm/s')

sep('----- Section 2')

##############################################
R = 40/2*1E-3  # [m] outer radius
r = 15/2*1E-3  # [m] inner radius
e = 6.0*pi/180 # [rad] overlap angle
N = 12         # number of radial electrodes
L = R-r        # [m] length
l = (R+r)/2    # [m] centre of the electrodes
##############################################

disp('R', R*1E3, 'mm', 'outer radius')
disp('r', r*1E3, 'mm', 'inner radius')
disp('e', e*180/pi, 'Deg', 'overlap angle')
disp('N', N, '', 'number of radial electrodes')
disp('L', L*1E3, 'mm', 'Length')
disp('l', l*1E3, 'mm', 'centre of the electrodes')

sep('-----')

# capacitance
C = eps0*N*l*L/d*e

disp('C', C*1E12, 'pF', '(30)')

# static torque [N.m]
TS = 0.5*eps0*N*l*L/d*VS**2
# static angular displacement [rad]
AS = TS/k
# static linear displacement
xS = AS*l

disp('TS', TS*1E6, 'µN.m','(32)')
disp('AS', AS*180/pi*1E6, 'µDeg','(33)')
disp('xS', xS*1E9, 'nm',' ')

# AC torque
T = (eps0*N*L*l/d)*VS*V
# zero frequency response
A0 = T/k
# zero frequency linear displacement
x0 = A0*l

disp('T0', T*1E6, 'µN.m','(34)')
disp('A0', A0*180/pi*1E6, 'µDeg','(35)')
disp('x0', x0*1E9, 'nm',' ')

# angular response at resonance
A = Q*A0
# linear displacement at resonance
x = Q*x0
# velocity
v = 2*pi*f*x

disp('A', A*180/pi*1E3, 'mDeg','(36)')
disp('x', x*1E6, 'µm',' ')
disp('v', v*1E3, 'mm/s','(37)')

# current signal for 1mm/s
i = (eps0*N*L*l/d)*VD*(1E-3/l)
# voltage signal for 1mm/s
u = G*i

disp('i', i*1E9, 'nA','(38) for v = 1mm/s')
disp('u', u*1E3, 'mV','     for v = 1mm/s')

fh.close()
