"""Independent exact sparse-polynomial audit; Python standard library only.

No state sampling, imported project calculators, fitted constants, or CAS.
Starting point: the separately auditable global Haar-4 trace classification.
All rational identities are checked after their denominators are cleared.
"""
from pathlib import Path
from fractions import Fraction as F
import json


class P:
    # Variables: D,q,a,b. Every coefficient is exact rational.
    def __init__(self, obj):
        self.c = {k:F(v) for k,v in obj.items() if v} if isinstance(obj,dict) else ({(0,0,0,0):F(obj)} if obj else {})
    def __add__(self, rhs):
        rhs=rhs if isinstance(rhs,P) else P(rhs)
        out=self.c.copy()
        for k,v in rhs.c.items():out[k]=out.get(k,F(0))+v
        return P(out)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.c.items()})
    def __sub__(self,rhs):return self+-P(rhs) if not isinstance(rhs,P) else self+-rhs
    def __rsub__(self,lhs):return -self+lhs
    def __mul__(self,rhs):
        rhs=rhs if isinstance(rhs,P) else P(rhs)
        out={}
        for k,v in self.c.items():
            for l,w in rhs.c.items():
                key=tuple(x+y for x,y in zip(k,l))
                out[key]=out.get(key,F(0))+v*w
        return P(out)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        out=P(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,rhs):
        rhs=rhs if isinstance(rhs,P) else P(rhs)
        return self.c==rhs.c
    def at(self,**kwargs):
        inds={'D':0,'q':1,'a':2,'b':3};out=P(0)
        for powers,value in self.c.items():
            term=P(value)
            for name,j in inds.items():
                var=kwargs.get(name,P({tuple(int(i==j) for i in range(4)):1}))
                term=term*var**powers[j]
            out=out+term
        return out


D,q,a,b=[P({tuple(int(j==i) for j in range(4)):1}) for i in range(4)]
checks=[]
def check(name,lhs,rhs=0):
    assert lhs==rhs,name
    checks.append(name)

rawnum=4*D**3+16*D**2+2*D**2*(a+b)
check('global Haar4 centering',rawnum*(D+1)-4*D**2*(D+2)*(D+3),2*D**2*((D+1)*(a+b)-4))
B=(D-1)**2
Ns=(D+1)*(D*a+q**2*b)-4*D
Nc=(D+1)*(D*b+q**2*a)-4*D
R0num=(D+1)*(D+q**4)-4*D*q**2
H=(q**2+1)*D**2+(q**4+1-6*q**2)*D+q**2+q**4
E=q**2+1-q**2*(a+b) # ep=E/(q+1)^2
check('sum denominator',q**2*B+R0num,H)
check('difference denominator',q**2*B-R0num,(D+1)*(D-q**2)*(q**2-1))
check('sum numerator',q**2*(Ns+Nc),H-(D+1)*(D+q**2)*E)
check('difference numerator',Ns-Nc,(D+1)*(D-q**2)*(a-b))
check('positive denominator',H,(q**2+1)*(D-q**2)**2+(q**2-1)*(3*q**2-1)*(D-q**2)+2*q**2*(q**2-1)**2)
check('n1 coefficient reduction',(q+1)**2*(q**2+1)*(2*q**2)*(q-1)**2,(q**2+1)*H.at(D=q**2))
check('n1 difference variance zero',((D-q**2)*(q**2-1)).at(D=q**2))
result={
 'status':f'All {len(checks)} exact sparse-polynomial identities passed.',
 'checks':checks,
 'method':'Independent exact coefficient comparison after denominator clearing. No sampling.',
 'same_cut_correlation':'[(D+1)(D a+q^2 b)-4D]/(D-1)^2',
 'crossed_cut_correlation':'[(D+1)(D b+q^2 a)-4D]/(D-1)^2',
 'baseline_cut_correlation':'[(D+1)(D/q^2+q^2)-4D]/(D-1)^2',
 'plus_mode_variance':'4H/[q^2(D+1)^2(D+2)(D+3)]',
 'minus_mode_variance':'4(D-q^2)(q^2-1)/[q^2(D+1)(D+2)(D+3)]',
 'plus_increment_second_moment':'8(q+1)^2(D+q^2) ep/[q^2(D+1)(D+2)(D+3)]',
 'q1_excluded':True,
 'n1_difference_mode_undefined':True,
}
path=Path(__file__).with_name('two_cut_symbolic_audit.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
print(path)
