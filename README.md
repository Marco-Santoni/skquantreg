Scikit wrapper for quantreg
============================

Scikit wrapper for quantreg

Installation / Usage
----------------------------

To install use pip:

```
$ pip install skquantreg
```

Or clone the repo:

```
    $ git clone https://github.com/Marco-Santoni/skquantreg.git
    $ python setup.py install
```

Usage:

```
from skquantreg import QuantileRegressor
import numpy as np


X = np.random.rand(10,2)
y = np.random.rand(10)
X_test = np.random.rand(5,2)

model = QuantileRegressor(q=0.5)
model.fit(X, y)
model.predict(X_test)
```
