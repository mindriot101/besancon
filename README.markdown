Besançon parser
===============

[![Build Status](https://travis-ci.org/mindriot101/besancon.png?branch=master)](https://travis-ci.org/mindriot101/besancon)
[![Code Health](https://landscape.io/github/mindriot101/besancon/master/landscape.png)](https://landscape.io/github/mindriot101/besancon/master)

*Massive work in progress...*


For querying the Besançon model generation system

Usage
-----

``` python
from besancon import Besancon

b = Besancon(email="test@example.com")
b.limit_spectral_type("1.0", "9.5")
b.set_magnitude_limit("V", 10.0, 100.0)
b.add_colour_limit(0, "J-H", 0.3)
b.set_luminosity_clases(range(1, 8))
b.query(lat=20.3, long=51.2, area=64.0)
```


or

```python
from besancon import Besancon

b = Besancon.from_dict(...)

# or
b = Besancon.from_json(...)

```

## Notes

Input fields

* name: `longit`, field: longitude
* name: `latit`, field: latitude
* name: `soli`, field: solid angle
* name: `spectyp_min`, field: minimum spectral type
    * options: values 1-9
* name: `subspectyp_min`, field: minimum sub-spectral type
* name: `spectyp_max`, field: maximum spectral type
    * options: values 1-9
* name: `subspectyp_max`, field: maximum sub-spectral type
* name: `lumi[]`, field: luminosity classes
    * options: values 1-7
* name: `band0[2]`, field: U minimum magnitude
* name: `bandf[2]`, field: U maximum magnitude
* name: `band0[1]`, field: B minimum magnitude
* name: `bandf[1]`, field: B maximum magnitude
* name: `band0[0]`, field: V minimum magnitude
* name: `bandf[0]`, field: V maximum magnitude
* name: `band0[3]`, field: R minimum magnitude
* name: `bandf[3]`, field: R maximum magnitude
* name: `band0[4]`, field: I minimum magnitude
* name: `bandf[4]`, field: I maximum magnitude
* name: `band0[5]`, field: J minimum magnitude
* name: `bandf[5]`, field: J maximum magnitude
* name: `band0[6]`, field: H minimum magnitude
* name: `bandf[6]`, field: H maximum magnitude
* name: `band0[7]`, field: K minimum magnitude
* name: `bandf[7]`, field: K maximum magnitude
* name: `band0[8]`, field: L minimum magnitude
* name: `bandf[8]`, field: L maximum magnitude
* name: `colind[0]`, field: first colour
* name: `oo[9]`, field: first minimum colour
* name: `ff[9]`, field: first maximum colour
* name: `colind[1]`, field: second colour
* name: `oo[10]`, field: second minimum colour
* name: `ff[10]`, field: second maximum colour
* name: `colind[2]`, field: third colour
* name: `oo[11]`, field: third minimum colour
* name: `ff[11]`, field: third maximum colour
* name: `colind[3]`, field: fourth colour
* name: `oo[12]`, field: fourth minimum colour
* name: `ff[12]`, field: fourth maximum colour
* name: `email`, field: email
