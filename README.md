Python Radiative Transfer Modelling Wrappers
============================================

Get spectral or integrated broadband irradiance outputs from SMARTS and SBdart
conveniently, in Python 3.


Prerequisites
-------------

 * Python 3.6.
 * SBdart and SMARTS 2.9.5 must be compiled and installed on your system
   `$PATH` as `sbdart` and `smarts295` respectively.
 * Numpy and Pandas are required.


Installation
------------

    $ pip install git+https://github.com/ghislainp/PyRTM

Be careful, the package on PyPi is old and only support Python 2. Don't use "pip install rtm".

Tutorial
--------

To run SBdart or SMARTS, create a model object with a default settings, adjust the setting and call the spectrum or irradiance methods to obtain a Pandas DataFrame with the simultion results:

```python
import rtm

model = rtm.SMARTS(rtm.settings.pollution['moderate'])

model['time'] = datetime.datetime(2020, 2, 11, 12, 0)
model['latitude'] = 45
model['longitude'] = 3

spec = model.spectrum()

```

Documentation
-------------

Check the Appropedia page: http://www.appropedia.org/PyRTM

Acknowledgment
---------------

The initial repository (Python 2 version) is: https://github.com/Queens-Applied-Sustainability/PyRTM