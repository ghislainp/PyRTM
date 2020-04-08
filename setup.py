"""
    AtmosRT (c) 2020 Ghislain Picard (ghipicard@gmail.com)

    AtmosRT is based on PyRTM (c) 2012 Philip Schliehauf (uniphil@gmail.com) and
    the Queen's University Applied Sustainability Centre


    This project is hosted on github; for up-to-date code and contacts:
    https://github.com/ghislainp/atmosrt
 
    This file is part of AtmosRT.

    AtmosRT is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PyRTM and ARTM are distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with AtmosRT.  If not, see <http://www.gnu.org/licenses/>.
"""

import setuptools
from numpy.distutils.core import setup, Extension


lib = Extension(name='libsbdart',
                sources=[
                    "src/sbdart/main.pyf",
                    "src/sbdart/params.f",
                    "src/sbdart/disort.f",
                    "src/sbdart/disutil.f",
                    "src/sbdart/spectra.f",
                    "src/sbdart/tauaero.f",
                    "src/sbdart/atms.f",
                    "src/sbdart/taucloud.f",
                    "src/sbdart/taugas.f",
                    "src/sbdart/drt-python.f",
                ])


setup(
    name='AtmosRT',
    version='0.3',
    author='Ghislain Picard',
    author_email='ghipicard@gmail.com',
    license='license.txt',
    description='Numerical Computations for Atmospheric Radiative Transfer Modelling',
    long_description=open('README.md').read(),
    ext_modules=[lib],
    scripts=['src/sbdart/sbdart.py'],
    packages=['atmosrt', 'atmosrt.tools'],
    include_package_data=True,
    install_requires=['numpy', 'pandas'],
)
