#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Admin
#
# Created:     05.03.2013
# Copyright:   (c) Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import factors

def cancer_example():
    ##C = Variable('Cancer', ['yes', 'no'])
    ##T = Variable('Test', ['pos', 'neg'])
    ##
    ##F11 = Factor(name='C', cons=[C], CPDs=[0.0001, 0.9999])
    ##F12 = Factor(name='T|C', cons=[T], cond=[C], CPDs=[0.9, 0.1, 0.2, 0.8])
    ##F14 = (F12 - C) * F11
    ##F14.name='C,T'
    ##F15 = F14/(F12 - C)
    ##F15.name='C|T'
    ##print F15

    C = Factor(name='C', full="Cancer", values=["no", "yes"], CPD=[0.99, 0.01])
    T = Factor(name='T', full="Test", values=["pos", "neg"], cond=[C], CPD=[0.2, 0.8, 0.9, 0.1])
    print T
    print T.joint()
    print T.uncond()
    print T.query(query=[C], evidence=[T])
    print T.joint() / T.uncond()

def student_example():
    D = BinaryVariable("Difficulty")
    I = BinaryVariable("Intelligence")
    G = Variable("Grade", [1, 2, 3])
    S = BinaryVariable("SAT")
    L = BinaryVariable("Letter")

    F1 = Factor(name='D', var=[D], CPD=[0.6, 0.4])
    F2 = Factor(name='I', var=[I], CPD=[0.7, 0.3])
    F3 = Factor(name='G|I,D', var=[I, D, G], CPD=[ 0.3,  0.4,  0.3,
                                                    0.05, 0.25, 0.7,
                                                    0.9,  0.08, 0.02,
                                                    0.5,  0.3,  0.2])
    F4 = Factor(name='S|I', var=[I,S], CPD=[0.95, 0.05, 0.2, 0.8])
    F5 = Factor(name='L|G', var=[G,L], CPD=[0.1, 0.9, 0.4, 0.6, 0.99, 0.01])

    D = Factor(name='D', values=[0,1], CPD=[0.6, 0.4], full="Difficulty")
    I = Factor(name='I', values=[0,1], CPD=[0.7, 0.3], full="Intelligence")
    G = Factor(name='G|I,D', values=[1, 2, 3], cond=[D,I], CPD=[0.3,  0.4,  0.3,
                                                            0.05, 0.25, 0.7,
                                                            0.9,  0.08, 0.02,
                                                            0.5,  0.3,  0.2],
                                                            full="Grade")
    S = Factor(name='S|I', values=[0, 1], cond=[I], CPD=[0.95, 0.05, 0.2, 0.8], full="SAT")
    L = Factor(name='L|G', values=[0, 1], cond=[G], CPD=[0.1, 0.9, 0.4, 0.6, 0.99, 0.01], full="Letter")

    BN = Bayesian([D,I,S,G,L])
    #~ print G
    #~ print G.parents
    print G
    print str(G)
    print `G`

def bayesian_inference():
    A = Factor(name='A',
                values=[0, 1],
                CPD=[0.6, 0.4])
    B = Factor(name='B',
                values=[0, 1],
                CPD=[0.7, 0.3])
    C = Factor(name='C|A,B', full='C',
                values=[0, 1],
                cond=[A, B],
                CPD=[0.7, 0.3, 0.9, 0.1, 0.8, 0.2, 0.6, 0.4])
    print C.joint().marginal(B.var[-1]).reduce(var=C.var[-1], value=0).norm()

def exact_bayesian():
    A = Factor(name='A',
                values=[0, 1],
                CPD=[0.5, 0.5])
    B = Factor(name='B',
                values=[0, 1],
                CPD=[0.5, 0.5])
    C = Factor(name='C|A,B', full='C',
                values=[0, 1],
                cond=[A, B],
                CPD=[1, 0, 1, 0, 1, 0, 0, 1])
    print C.reduce(var=C.var[-1], value=0)

def main():
    exact_bayesian()
    pass

if __name__ == '__main__':
    main()