def netpay(basic):
    DA=basic*0.5
    HRA=basic*0.20
    PF=basic*0.11
    allowance=1420.125
    netpay=round(basic+HRA+DA-PF)-allowance
    return netpay
    
def gross(basic,netpay):
    
    ITAX=basic*15/100
    gross=netpay-ITAX
    return gross
