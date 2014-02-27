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
b.add_magnitude_limit("V", 10.0, 100.0)
b.add_colour_limit("J-H", 0.3)
b.query(lat=20.3, long=51.2, area=64.0)
```


or

```python
from besancon import Besancon

b = Besancon.from_dict(...)

# or
b = Besancon.from_json(...)

```
