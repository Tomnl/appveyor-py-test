import os
def multiparse(multi_in):
    print('Parsing file: {}'.format(multi_in[0]))
    parser = multi_in[1][multi_in[0].split(os.path.extsep)[-1]]
    ont = multi_in[2][multi_in[0].split(os.path.extsep)[-1]]
    ont =  multi_in[2]['mzML']
    print ont
    print "CHECK", multi_in[2]['mzML']['MS:1000525'].rchildren, "!!!!!!!!!!!!!!!!!!!!!"
    print "CHECK", ont['MS:1000525'].rchildren, "!!!!!!!!!!!!!!!!!!!!!"
    p = parser(multi_in[0], ont).meta_isa
    return p
