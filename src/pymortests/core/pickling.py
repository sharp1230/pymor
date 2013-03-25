from __future__ import absolute_import, division, print_function

import tempfile
import os

# import everything we might want to test so metaclass can register the types
from pymor import *
from pymor.core import *
from pymor.grids import *
from pymor.discreteoperators import *
from pymor.discretizations import *
from pymor.discretizers import *
from pymor.domaindescriptions import *
from pymor.domaindiscretizers import *
from pymor.functions import *
from pymor.reductors import *
from pymor.tools import *

from pymor.core.interfaces import (BasicInterface,)
from pymortests.base import (TestBase, runmodule, SubclassForImplemetorsOf)
from pymor import core


@SubclassForImplemetorsOf(BasicInterface)
class PickleMeInterface(TestBase):

    def testDump(self):
        try:
            obj = self.Type
        except (ValueError, TypeError) as e:
            self.logger.debug('Not testing {} because its init failed: {}'.format(self.Type, str(e)))
            return

        with tempfile.NamedTemporaryFile(mode='wb', delete=False) as dump_file:
            core.dump(obj, dump_file)
            dump_file.close()
            f = open(dump_file.name, 'rb')
            unpickled = core.load(f)
            self.assertTrue(obj.__class__ == unpickled.__class__)
            self.assertTrue(obj.__dict__ == unpickled.__dict__)
            os.unlink(dump_file.name)
        dump(obj, tempfile.TemporaryFile())

# this needs to go into every module that wants to use dynamically generated types, ie. testcases, below the test code
from pymor.core.dynamic import *

if __name__ == "__main__":
    runmodule(name='pymortests.core.pickling')
