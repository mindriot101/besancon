#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# default query arguments (from astroquery)
keyword_defaults = {
    'rinf':0.000000,
    'rsup':50.000000,
    'dist_step_mode':0,
    'dlr': 0.000,
    'kleg':1,
    'longit': 10.62,
    'latit':-0.38,
    'soli':0.0003, # degrees. 0.00027777 = 1 arcsec
    'kleh':1,
    'eq1': 2000.0,
    'al0': 200.00,
    'alm': 200.00,
    'dl': 1.00,
    'ab0': 59.00,
    'abm': 59.00,
    'db': 1.00,
    'adif': 0.700,
    'ev':[""]*24,
    'di':[""]*24,
    'oo':[-7]+[-99]*12,
    'ff':[15]+[99]*12,
    'spectyp_min':1,
    'subspectyp_min': 0,
    'spectyp_max':9,
    'subspectyp_max': 5,
    'lumi':range(1,8),
    'sous_pop':range(1,11),
    'iband':8,
    'band0':[8]*9,
    'bandf':[25]*9,
    'colind':["J-H","H-K","J-K","V-K",],
    'nic': 4,
    'klea':1,
    'sc':[[0,0,0]]*9,
    'klee':0,
    'throughform':'ok',
    'kleb':3, # 3 = Catalogue Simulation, 1 = tables and differential counts
    'klec':1, # 1 = ubv, 15= cfhtls (photometric system)
    'cinem':0, # 0: no kinematics, 1: kinematics
    'outmod':"",
    'ff[15]': 500,
    'oo[15]': -500,
}

data = {
        'longit': 200,
        'latit': 30,
        'soli': 1,
        'spectyp_min': 2,
        'subspectyp_min': 5,
        'spectyp_max': 5,
        'subspectyp_max': 2,
        'email': 's.r.walker101@googlemail.com',
        }

payload = dict(keyword_defaults.items() + data.items())

# Flatten the arrays (from astroquery)
for _ in xrange(2):  # deal with nested lists
    for k,v in payload.items():
        if isinstance(v,list) or (isinstance(v,tuple) and len(v) > 1):
            if k in payload:
                del payload[k]
            for ii,x in enumerate(v):
                payload['%s[%i]' % (k,ii)] = x

base_url = 'http://model.obs-besancon.fr/modele_form.php'

# Query the database
# r = requests.post(base_url, data=data)

