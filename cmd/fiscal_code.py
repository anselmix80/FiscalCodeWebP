import sys
import assembly as fc

def fiscal_code(*args):
    cf = fc.assembly(*args)
    print(cf)
    return cf

parameters = [values for values in sys.argv[1:]]
fiscal_code(parameters)
