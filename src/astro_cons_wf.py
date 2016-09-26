import sys

#from astropy import units as un
#import workflow
from workflow import Workflow, ICON_WARNING, ICON_INFO

def main(wf):
    ''' Astro-Constants
    Args:
        wf: Workflow object
    Return:
        exit status: int
    Raises:
        ImportError.
    '''

    try:
        from astropy import constants as co
    except ImportError:
        wf.add_item("Please install astropy first; v1.2.1 is recomanded.")
        #raise ImportError("Cannot import astropy!")

        # this dict will be calculated every time, maybe an optimized version
        # does better
    constants_dict = {
    "G":("Gravitational constant", co.G.cgs.value, co.G.cgs.unit.to_string(), \
        co.G.value, co.G.unit.to_string()),
    "L_bol0":("Luminosity for absolute bolometric magnitude 0", \
        co.L_bol0.cgs.value, co.L_bol0.cgs.unit.to_string(), \
        co.L_bol0.value, co.L_bol0.unit.to_string()),
    "L_sun":("Solar luminosity", \
        co.L_sun.cgs.value, co.L_sun.cgs.unit.to_string(), \
        co.L_sun.value, co.L_sun.unit.to_string()),
    "M_earth":("Earth mass", \
        co.M_earth.cgs.value, co.M_earth.cgs.unit.to_string(), \
        co.M_earth.value, co.M_earth.unit.to_string()),
    "M_jup":("Jupiter mass", \
        co.M_jup.cgs.value, co.M_jup.cgs.unit.to_string(), \
        co.M_jup.value, co.M_jup.unit.to_string()),
    "M_sun":("Solar mass", \
        co.M_sun.cgs.value, co.M_sun.cgs.unit.to_string(), \
        co.M_sun.value, co.M_sun.unit.to_string()),
    "N_A":("Avogadro's number", \
        co.N_A.cgs.value, co.N_A.cgs.unit.to_string(), \
        co.N_A.value, co.N_A.unit.to_string()),
    "R":("Gas constant", \
        co.R.cgs.value, co.R.cgs.unit.to_string(), \
        co.R.value, co.R.unit.to_string()),
    "R_earth":("Earth equatorial radius", \
        co.R_earth.cgs.value, co.R_earth.cgs.unit.to_string(), \
        co.R_earth.value, co.R_earth.unit.to_string()),
    "R_jup":("Jupiter equatorial radius", \
        co.R_jup.cgs.value, co.R_jup.cgs.unit.to_string(), \
        co.R_jup.value, co.R_jup.unit.to_string()),
    "R_sun":("Solar radius", \
        co.R_sun.cgs.value, co.R_sun.cgs.unit.to_string(), \
        co.R_sun.value, co.R_sun.unit.to_string()),
    "Ryd":("Rydberg constant", \
        co.Ryd.cgs.value, co.Ryd.cgs.unit.to_string(), \
        co.Ryd.value, co.Ryd.unit.to_string()),
    "a0":("Bohr radius", \
        co.a0.cgs.value, co.a0.cgs.unit.to_string(), \
        co.a0.value, co.a0.unit.to_string()),
    "alpha":("Fine-structure constant", \
        co.alpha.cgs.value, co.alpha.cgs.unit.to_string(), \
        co.alpha.value, co.alpha.unit.to_string()),
    "atmosphere":("Atomosphere", \
        co.atmosphere.cgs.value, co.atmosphere.cgs.unit.to_string(), \
        co.atmosphere.value, co.atmosphere.unit.to_string()),
    "au":("Astronomical Unit", \
        co.au.cgs.value, co.au.cgs.unit.to_string(), \
        co.au.value, co.au.unit.to_string()),
    "b_wien":("Wien wavelength displacement law constant", \
        co.b_wien.cgs.value, co.b_wien.cgs.unit.to_string(), \
        co.b_wien.value, co.b_wien.unit.to_string()),
    "c":("Speed of light in vacuum", \
        co.c.cgs.value, co.c.cgs.unit.to_string(), \
        co.c.value, co.c.unit.to_string()),
    "e":("Electron charge", \
        co.e.esu.value, co.e.esu.unit.to_string(), \
        co.e.value, co.e.unit.to_string()),
    "eps0":("Electric constant", \
        co.eps0.value, co.eps0.unit.to_string(), \
        co.eps0.value, co.eps0.unit.to_string()),
    "g0":("Standard acceleration of gravity", \
        co.g0.cgs.value, co.g0.cgs.unit.to_string(), \
        co.g0.value, co.g0.unit.to_string()),
    "h":("Planck constant", \
        co.h.cgs.value, co.h.cgs.unit.to_string(), \
        co.h.value, co.h.unit.to_string()),
    "hbar":("Reduced Planck constant", \
        co.hbar.cgs.value, co.hbar.cgs.unit.to_string(), \
        co.hbar.value, co.hbar.unit.to_string()),
    "k_B":("Boltzmann constant", \
        co.k_B.cgs.value, co.k_B.cgs.unit.to_string(), \
        co.k_B.value, co.k_B.unit.to_string()),
    "kpc":("Kiloparsec", \
        co.kpc.cgs.value, co.kpc.cgs.unit.to_string(), \
        co.kpc.value, co.kpc.unit.to_string()),
    "m_e":("Electron mass", \
        co.m_e.cgs.value, co.m_e.cgs.unit.to_string(), \
        co.m_e.value, co.m_e.unit.to_string()),
    "m_n":("Neutron mass", \
        co.m_n.cgs.value, co.m_n.cgs.unit.to_string(), \
        co.m_n.value, co.m_n.unit.to_string()),
    "m_p":("Proton mass", \
        co.m_p.cgs.value, co.m_p.cgs.unit.to_string(), \
        co.m_p.value, co.m_p.unit.to_string()),
    "mu0":("Magnetic constant", \
        co.mu0.value, co.mu0.unit.to_string(), \
        co.mu0.value, co.mu0.unit.to_string()),
    "muB":("Bohr magneton", \
        co.muB.value, co.muB.unit.to_string(), \
        co.muB.value, co.muB.unit.to_string()),
    "pc":("Parsec", \
        co.pc.cgs.value, co.pc.cgs.unit.to_string(), \
        co.pc.value, co.pc.unit.to_string()),
    "sigma_T":("Thomson scattering cross-section", \
        co.sigma_T.cgs.value, co.sigma_T.cgs.unit.to_string(), \
        co.sigma_T.value, co.sigma_T.unit.to_string()),
    "sigma_sb":("Stefan-Boltzmann constant", \
        co.sigma_sb.cgs.value, co.sigma_sb.cgs.unit.to_string(), \
        co.sigma_sb.value, co.sigma_sb.unit.to_string()),
    "u":("Atomic mass", \
        co.u.cgs.value, co.u.cgs.unit.to_string(), \
        co.u.value, co.u.unit.to_string()),
    }
#    revers_dic={}
#    for ii in constants_dict.keys():
#        revers_dic[constants_dict[ii][0]] = ii
#        revers_dic[constants_dict[ii][0].lower()] = ii
        # for revers searching

#    revers_dic[""]
    if not len(wf.args):
        return 1
    else:
        query = wf.args[0]
        for ii in constants_dict.keys():
            description = constants_dict[ii][0]
#            if (ii.find(query)>-1 or ii.lower().find(query)>-1):
            if (ii.find(query)>-1 or ii.lower().find(query)>-1 or \
                description.find(query)>-1 or description.lower().find(query)>-1):
#                result_tmp=constants_dict[ii][0]+' '+str(constants_dict[ii][1])+' '+constants_dict[ii][2]
                result_tmp=ii+' '+str(constants_dict[ii][1])+' '+constants_dict[ii][2]
                wf.add_item(result_tmp,
                            constants_dict[ii][0],
                            valid=True,
                            copytext=str(constants_dict[ii][1]),
                            arg=str(constants_dict[ii][1]),
                            icon='icon.jpg')

#    try:
#        result=constants_dict[query][0]+' '+str(constants_dict[query][1])+' '+constants_dict[query][2]
#        wf.add_item(result,
#                    valid=True,
#                    copytext=str(constants_dict[query][1]),
#                    arg=str(constants_dict[query][1]),
#                    icon='icon.jpg')
#    except KeyError:
#        wf.add_item('Constant name cannot be resolved!',
#                     valid=False,
#                     icon=ICON_WARNING)

    wf.send_feedback()
   # print constants_dict["G"]

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
    #if (sys.argv[1]=='c'):
    #    print co.c.value
