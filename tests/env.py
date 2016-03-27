# -*- coding: utf-8 -*-
"""setups environment variables for testing module to work.
"""

import sys
import os

def main():
    """Fix the system path variable for discovery of modules
    """

    # append module root directory to sys.path
    sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )
    # append module tests directory to sys.path
    sys.path.append(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

if __name__ == "__main__":
    main()
