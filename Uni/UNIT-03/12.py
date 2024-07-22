class bank(object):#object is superclass for bank class also
    cash=1000000
    @classmethod
    def chk_cash(cls):
        print(cls.cash)
class andhrabank(bank):
    pass#inherite all method and object from superclass
class statebank(bank):
    cash=200000
    @classmethod
    def chk_cash(cls):
        print(cls.cash+bank.cash)

    """ 
            pass#this is multi line comment
    """
a=andhrabank()
a.chk_cash()
s=statebank()
s.chk_cash()