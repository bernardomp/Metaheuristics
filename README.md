[![Build Status](https://travis-ci.org/bernardomp/Heuristic.svg?branch=master)](https://travis-ci.org/bernardomp/Heuristic)

python3 src/metaheuristic.py -h
usage: metaheuristic.py [-h] repeats input output algorithms [algorithms ...]

positional arguments:
  repeats     number of repeats for each algorithm
  input       filepath containing the input data
  output      filepath containing the output data
  algorithms  list of algorithms: ReducedVNS, BasicVNS or GeneralVNS

optional arguments:
  -h, --help  show this help message and exit

Example: python3 metaheuristic 30 input/inputs.txt ./ BasicVNS ReducedVNS

