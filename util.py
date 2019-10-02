
def f_SS(SSin, SS, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, XH, XS):
    A = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*(SNH4+SNH3)/(0.2+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    B = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*0.2/(0.2+SNH4+SNH3)*SNO3/(0.2+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    D = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    E = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO2/(0.2+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    V = 0.3*exp(0.07*(t-20.0))*XS
    return q/v*(SSin - SS) + (-1.9*A -1.9*B -2.2*D -3.7*E +1.0*V)

def f_SI(SIin, SI):
    return q/v*(SIin - SI)

def f_SNH4(SHH4in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    A = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*(SNH4+SNH3)/(0.2+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    C = 0.2*exp(0.07*(t-20.0))*SO2/(0.2+SO2)*XH
    D = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    F = 0.1*exp(0.07*(t-20.0))*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*XH
    G = 0.8*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*(SNH4+SNH3)/(0.5+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN1
    H = 0.05*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*XN1
    J = 0.05*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*XN2
    K = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*(SNH4+SNH3)/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*Ie/500.0*exp(1.0-Ie/500.0)*XALG
    M = 0.1*exp(0.046*(t-20.0))*SO2/(0.2+SO2)*XALG
    N = 0.1*exp(0.046*(t-20.0))*XALG
    O = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XALG*XCON
    P = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XS*XCON
    Q = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XH*XCON
    R = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN1*XCON
    S = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN2*XCON
    TT = 0.05*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XCON
    U = 0.05*exp(0.08*(t-20.0))*XCON
    V = 0.3*exp(0.07*(t-20.0))*XS
    Z = 0.0001*(SNH4-SH*SNH3/KeqN)
    return q/v*(SNH4in-SNH4)+(-0.012*A +0.071*C +0.071*F -4.8*G +0.071*H +0.071*J -0.065*K +0.058*M +0.029*N +0.13*O +0.13*P +0.45*Q +0.45*R +0.45*S +0.058*TT +0.029*U +0.0*V -1.0*Z)

def f_SNH3(SNH3in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    Z = 0.0001*(SNH4-SH*SNH3/KeqN)
    return q/v*(SNH3in-SNH3)+(1.0*Z)

def f_SNO2(SNO2in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    D = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    E = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO2/(0.2+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    G = 0.8*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*(SNH4+SNH3)/(0.5+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN1
    I = 1.1*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*SNO2/(0.5+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN2
    return q/v*(SNO2in-SNO2)+(1.1*D-1.6*E+4.7*G-21.0*I)

def f_SNO3(SNO3in,  SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    B = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*0.2/(0.2+SNH4+SNH3)*SNO3/(0.2+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    D = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    F = 0.1*exp(0.07*(t-20.0))*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*XH
    I = 1.1*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*SNO2/(0.5+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN2
    LL = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*0.1/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*Ie/500.0*exp(1.0-Ie/500.0)*XALG
    return q/v*(SNO3in-SNO3)+(-0.012*B-1.1*D-0.27*F+21.0*I-0.065*LL)

def f_SHPO4(SHPO4in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    A = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*(SNH4+SNH3)/(0.2+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    B = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*0.2/(0.2+SNH4+SNH3)*SNO3/(0.2+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    C = 0.2*exp(0.07*(t-20.0))*SO2/(0.2+SO2)*XH
    D = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    E = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO2/(0.2+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    F = 0.1*exp(0.07*(t-20.0))*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*XH
    G = 0.8*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*(SNH4+SNH3)/(0.5+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN1
    H = 0.05*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*XN1
    I = 1.1*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*SNO2/(0.5+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN2
    J = 0.05*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*XN2
    K = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*(SNH4+SNH3)/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*Ie/500.0*exp(1.0-Ie/500.0)*XALG
    LL = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*0.1/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*Ie/500.0*exp(1.0-Ie/500.0)*XALG
    M = 0.1*exp(0.046*(t-20.0))*SO2/(0.2+SO2)*XALG
    N = 0.1*exp(0.046*(t-20.0))*XALG
    O = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XALG*XCON
    P = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XS*XCON
    Q = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XH*XCON
    R = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN1*XCON
    S = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN2*XCON
    TT = 0.05*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XCON
    U = 0.05*exp(0.08*(t-20.0))*XCON
    V = 0.3*exp(0.07*(t-20.0))*XS
    AA = 0.0001*(SH2PO4-SH*SHPO4/KeqP)
    return q/v*(SHPO4in-SHPO4)+(-0.0083*A-0.0083*B+0.017*C-0.0062*D+0.0021*E+0.017*F-0.019*G+0.017*H-0.019*I+0.017*J-0.011*K-0.011*LL+0.0086*M+0.0041*N+0.022*O+0.022*P+0.13*Q+0.13*R+0.13*S+0.0086*TT+0.0041*U+0.0*V+1.0*AA)

def f_SH2PO4(SH2PO4in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    AA = 0.0001*(SH2PO4-SH*SHPO4/KeqP)
    return q/v*(SH2PO4in-SH2PO4)+(-1.0*AA)

def f_SO2(SO2in,  SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    A = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*(SNH4+SNH3)/(0.2+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    B = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*0.2/(0.2+SNH4+SNH3)*SNO3/(0.2+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    C = 0.2*exp(0.07*(t-20.0))*SO2/(0.2+SO2)*XH
    G = 0.8*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*(SNH4+SNH3)/(0.5+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN1
    H = 0.05*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*XN1
    I = 1.1*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*SNO2/(0.5+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN2
    J = 0.05*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*XN2
    K = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*(SNH4+SNH3)/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)
    LL = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*0.1/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*Ie/50
    M = 0.1*exp(0.046*(t-20.0))*SO2/(0.2+SO2)*XALG
    N = 0.1*exp(0.046*(t-20.0))*XALG
    O = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XALG*XCON
    P = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XS*XCON
    Q = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XH*XCON
    R = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN1*XCON
    S = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN2*XCON
    TT = 0.05*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XCON
    U = 0.05*exp(0.08*(t-20.0))*XCON
    V = 0.3*exp(0.07*(t-20.0))*XS
    return q/v*(SO2in-SO2)+(-0.85*A-0.80*B-0.77*C-15.0*G-0.77*H-22.0*I-0.77*J+1.0*K+1.3*LL-0.60*M +0.20*N-0.15*O-4.8*P-3.8*Q-3.8*R-3.8*S-0.60*TT+0.20*U+0.0*V)+K2*(14.652-0.41022*t+0.007991*t*t-0.000077774*t*t*t-SO2)

def f_SCO2(SCO2in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    W = 0.001*(SCO2-SH*SHCO3/Keq1)
    return q/v*(SCO2in-SCO2)+(-1.0*W)

def f_SHCO3(SHCO3in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    A = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*(SNH4+SNH3)/(0.2+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    B = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*0.2/(0.2+SNH4+SNH3)*SNO3/(0.2+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    C = 0.2*exp(0.07*(t-20.0))*SO2/(0.2+SO2)*XH
    D = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    E = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO2/(0.2+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    F = 0.1*exp(0.07*(t-20.0))*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*XH
    G = 0.8*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*(SNH4+SNH3)/(0.5+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN1
    H = 0.05*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*XN1
    I = 1.1*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*SNO2/(0.5+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN2
    J = 0.05*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*XN2
    K = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*(SNH4+SNH3)/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)
    LL = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*0.1/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*Ie/50
    M = 0.1*exp(0.046*(t-20.0))*SO2/(0.2+SO2)*XALG
    N = 0.1*exp(0.046*(t-20.0))*XALG
    O = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XALG*XCON
    P = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XS*XCON
    Q = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XH*XCON
    R = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN1*XCON
    S = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN2*XCON
    TT = 0.05*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XCON
    U = 0.05*exp(0.08*(t-20.0))*XCON
    V = 0.3*exp(0.07*(t-20.0))*XS
    W = 0.001*(SCO2-SH*SHCO3/Keq1)
    X = 0.0001*(SHCO3-SH*SCO3/Keq2)
    return q/v*(SHCO3in-SHCO3)+(0.27*A+0.27*B+0.25*C+0.39*D+0.86*E+0.25*F-0.32*G+0.25*H-0.32*I+0.25*J-0.39*K-0.39*LL+0.26*M+0.0018*N+0.32*O+1.5*P+1.2*Q+1.2*R+1.2*S+0.26*TT+0.0018*U+0.0*V+1.0*W-1.0*X)

def f_SCO3(SCO3in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    X = 0.0001*(SHCO3-SH*SCO3/Keq2)
    AB = 0.00000002*(1.0-SCa*SCO3/12/40/Keqso)
    return q/v*(SCO3in-SCO3)+(1.0*X+0.30*AB)

def f_SH(SHin, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    A = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*(SNH4+SNH3)/(0.2+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    B = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*0.2/(0.2+SNH4+SNH3)*SNO3/(0.2+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    C = 0.2*exp(0.07*(t-20.0))*SO2/(0.2+SO2)*XH
    D = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    E = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO2/(0.2+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    F = 0.1*exp(0.07*(t-20.0))*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*XH
    G = 0.8*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*(SNH4+SNH3)/(0.5+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN1
    H = 0.05*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*XN1
    I = 1.1*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*SNO2/(0.5+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN2
    J = 0.05*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*XN2
    K = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*(SNH4+SNH3)/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)
    LL = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*0.1/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*Ie/50
    M = 0.1*exp(0.046*(t-20.0))*SO2/(0.2+SO2)*XALG
    N = 0.1*exp(0.046*(t-20.0))*XALG
    O = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XALG*XCON
    P = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XS*XCON
    Q = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XH*XCON
    R = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN1*XCON
    S = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN2*XCON
    TT = 0.05*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XCON
    U = 0.05*exp(0.08*(t-20.0))*XCON
    V = 0.3*exp(0.07*(t-20.0))*XS
    W = 0.001*(SCO2-SH*SHCO3/Keq1)
    X = 0.0001*(SHCO3-SH*SCO3/Keq2)
    Y = 0.0001*(1.0-SH*SOH/Keqw)
    Z = 0.0001*(SNH4-SH*SNH3/KeqN)
    AA = 0.0001*(SH2PO4-SH*SHPO4/KeqP)
    return q/v*(SHin-SH)+(0.023*A+0.021*B+0.017*C+0.032*D-0.045*E+0.0025*F+0.65*G+0.017*H-0.033*I+0.017*J-0.028*K-0.038*LL+0.018*M+0.0016*N+0.019*O+0.11*P+0.075*Q+0.075*R+0.075*S+0.018*TT+0.0016*U+0.0*V+0.083*W+0.083*X+1.0*Y+0.071*Z+0.032*AA)

def f_SOH(SOHin, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    Y = 0.0001*(1.0-SH*SOH/Keqw)
    return 

def f_SCa(SCain, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    AB = 0.00000002*(1.0-SCa*SCO3/12/40/Keqso)
    return q/v*(SOHin-SOH)+(1.0*Y)

def f_XH(XHin, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    A = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*(SNH4+SNH3)/(0.2+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    B = 2.0*exp(0.07*(t-20.0))*SS/(2.0+SS)*SO2/(0.2+SO2)*0.2/(0.2+SNH4+SNH3)*SNO3/(0.2+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    C = 0.2*exp(0.07*(t-20.0))*SO2/(0.2+SO2)*XH
    D = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    E = 1.6*exp(0.07*(t-20.0))*SS/(2.0+SS)*0.2/(0.2+SO2)*SNO2/(0.2+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XH
    F = 0.1*exp(0.07*(t-20.0))*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*XH
    Q = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XH*XCON
    return q/v*(XHin-XH)+(1.0*A+1.0*B-1.0*C+1.0*D+1.0*E-1.0*F-8.7*Q)+As/v*dt*(Ma*(vb-27216.0)*(vb-27216.0)*XHin0/(XHin0+XN1in0+XN2in0+XALGin0+XCONin0+XSin0a+XSin0b+XSin0c+XIin0a+XIin0b+XIin0c)-w*XH)

def f_XN1(XN1in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    G = 0.8*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*(SNH4+SNH3)/(0.5+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN1
    H = 0.05*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*XN1
    R = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN1*XCON
    return q/v*(XN1in-XN1)+(1.0*G-1.0*H-8.7*R)+As/v*dt*(Ma*(vb-27216.0)*(vb-27216.0)*XN1in0/(XHin0+XN1in0+XN2in0+XALGin0+XCONin0+XSin0a+XSin0b+XSin0c+XIin0a+XIin0b+XIin0c)-w*XN1)

def f_XN2(XH2in, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    I = 1.1*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*SNO2/(0.5+SNO2)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*XN2
    J = 0.05*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*XN2
    S = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN2*XCON
    return q/v*(XN2in-XN2)+(1.0*I-1.0*J-8.7*S)+As/v*dt*(Ma*(vb-27216.0)*(vb-27216.0)*XN2in0/(XHin0+XN1in0+XN2in0+XALGin0+XCONin0+XSin0a+XSin0b+XSin0c+XIin0a+XIin0b+XIin0c)-w*XN2)

def f_XALG(XALGin, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    K = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*(SNH4+SNH3)/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)
    LL = 2.0*exp(0.046*(t-20.0))*(SNH4+SNH3+SNO3)/(0.1+SNH4+SNH3+SNO3)*0.1/(0.1+SNH4+SNH3)*(SHPO4+SH2PO4)/(0.02+SHPO4+SH2PO4)*Ie/50
    M = 0.1*exp(0.046*(t-20.0))*SO2/(0.2+SO2)*XALG
    N = 0.1*exp(0.046*(t-20.0))*XALG
    O = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XALG*XCON
    return q/v*(XALGin-XALG)+(1.0*K+1.0*LL-1.0*M-1.0*N-5.0*O)+As/v*dt*(Ma*(vb-27216.0)*(vb-27216.0)*XALGin0/(XHin0+XN1in0+XN2in0+XALGin0+XCONin0+XSin0a+XSin0b+XSin0c+XIin0a+XIin0b+XIin0c)-w*XALG)

def f_XCON(XCONin, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    O = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XALG*XCON
    P = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XS*XCON
    Q = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XH*XCON
    R = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN1*XCON
    S = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN2*XCON
    TT = 0.05*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XCON
    U = 0.05*exp(0.08*(t-20.0))*XCON
    return q/v*(XCONin-XCON)+(1.0*O+1.0*P+1.0*Q+1.0*R+1.0*S-1.0*TT-1.0*U)+As/v*dt*(Ma*(vb-27216.0)*(vb-27216.0)*XCONin0/(XHin0+XN1in0+XN2in0+XALGin0+XCONin0+XSin0a+XSin0b+XSin0c+XIin0a+XIin0b+XIin0c)-w*XCON)

def f_XS(XSin, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    N = 0.1*exp(0.046*(t-20.0))*XALG
    O = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XALG*XCON
    P = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XS*XCON
    Q = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XH*XCON
    R = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN1*XCON
    S = 0.0002*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XN2*XCON
    U = 0.05*exp(0.08*(t-20.0))*XCON
    V = 0.3*exp(0.07*(t-20.0))*XS
    return q/v*(XSin-XS)+(0.95*N+3.8*O-5.8*P+3.8*Q+3.8*R+3.8*S+0.95*U-1.0*V)+As/v*dt*(Ma*(vb-27216.0)*(vb-27216.0)*(XSin0a+XSin0b+XSin0c)/(XHin0+XN1in0+XN2in0+XALGin0+XCONin0+XSin0a+XSin0b+XSin0c+XIin0a+XIin0b+XIin0c)-w*1000*XS)

def f_XI(XIin, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):
    C = 0.2*exp(0.07*(t-20.0))*SO2/(0.2+SO2)*XH
    F = 0.1*exp(0.07*(t-20.0))*0.2/(0.2+SO2)*SNO3/(0.5+SNO3)*XH
    H = 0.05*exp(0.098*(t-20.0))*SO2/(0.5+SO2)*XN1
    J = 0.05*exp(0.069*(t-20.0))*SO2/(0.5+SO2)*XN2
    M = 0.1*exp(0.046*(t-20.0))*SO2/(0.2+SO2)*XALG
    N = 0.1*exp(0.046*(t-20.0))*XALG
    TT = 0.05*exp(0.08*(t-20.0))*SO2/(0.5+SO2)*XCON
    U = 0.05*exp(0.08*(t-20.0))*XCON
    return q/v*(XIin-XI)+(0.23*C+0.23*F+0.23*H+0.23*J+0.40*M+0.25*N+0.40*TT+0.25*U)+As/v*dt*(Ma*(vb-27216.0)*(vb-27216.0)*(XIin0a+XIin0b+XIin0c)/(XHin0+XN1in0+XN2in0+XALGin0+XCONin0+XSin0a+XSin0b+XSin0c+XIin0a+XIin0b+XIin0c)-w*1000*XI)
# def f_XP(XPin, SS, SI, SNH4, SNH3, SNO2, SNO3, SHPO4, SH2PO4, SO2, SCO2, SHCO3, SCO3, SH, SOH, SCa, XH, XN1, XN2, XALG, XCON, XS, XP):

#     return  