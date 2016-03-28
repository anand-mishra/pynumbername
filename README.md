Purpose
=======

Implement an iterative method to convert integers to number names.

[![Build Status](https://travis-ci.org/anand-mishra/pynumbername.svg?branch=master)](https://travis-ci.org/anand-mishra/pynumbername)

Installation
============

1. Using `pip`

    pip install numbername

2. Using source

    wget https://pypi.python.org/packages/source/n/numbername/numbername-0.0.6.tar.gz
    tar xvf numbername-0.0.6.tar.gz
    cd numbername-0.0.6
    python setup.py install

Usage
=====

Convert integers to number name

    from numbername import to_number_name
    print to_number_name(1123) 
    #ouputs: one thousand one hundred and twenty three

Convert integers to comma placed number

    from numbername import to_comma_placed
    print to_number_name(1123)
    #outputs: 1,123

Testing
=======

Python unit tests can be run as

    python -m unittest discover tests
    

TODO
====

1. convert floats as well to number names
2. convert number names to integers
