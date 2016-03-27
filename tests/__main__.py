# -*- coding: utf-8 -*-
"""main of the tests module

"""

#setup the proper path variables for discovery
from . import env
env.main()

#run the tests
from . import test_numbername
test_numbername.main()
