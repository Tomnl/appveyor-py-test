# coding: utf-8
"""
Content
-----------------------------------------------------------------------------
This module exposes basic API of mzml2isa, either being called from command
line interface with arguments parsing via **run** function, or from another
Python program via the **full_parse** function which works the same.


About
-----------------------------------------------------------------------------
The mzml2isa parser was created by Tom Lawson (University of Birmingham, UK)
as part of a NERC funded placement at EBI Cambridge in June 2015. Python 3
port and small enhancements were carried out by Martin Larralde (ENS Cachan,
France) in June 2016 during an internship at the EBI Cambridge.

License
-----------------------------------------------------------------------------
GNU General Public License version 3.0 (GPLv3)
"""


import io
import os
import sys
import glob
import argparse
import textwrap
import warnings
import json
import tarfile
import zipfile

from multiprocessing import freeze_support
from multiprocessing.pool import Pool
from pronto import Ontology

try:
    import progressbar as pb
    PB_AVAILABLE = True
except ImportError:
    PB_AVAILABLE = False

MARKER = "#" if sys.version_info[0]==2 else "█"

import mzml2isa
import mzml2isa.isa as isa
import mzml2isa.mzml as mzml
from mzml2isa.versionutils import longest_substring


if __name__ == '__main__':
    freeze_support()
    dirname = os.path.dirname(os.path.realpath(__file__))
    _ms = Ontology(os.path.join(dirname, "psi-ms.obo"), False)
    _ims = Ontology(os.path.join(dirname, "imagingMS.obo"), False)
    _ims.terms.update(_ms.terms)
    mzml.mzMLmeta('C:\\DATA\\test\\Daph_P_WCX_1_LCMS-FC_Phenyl_neg_inj1.mzML')
