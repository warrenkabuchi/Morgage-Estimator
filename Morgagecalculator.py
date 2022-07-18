def findPayment(loan,r,m):
    """Assumes : loan and r anre floats m an int 
    Returns the monthly payment for a morgage of size
    loan at a monthly roate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m-1))

class Mortgage (object):
    """"Abstract class for bulding diffrent kinds of morgages"""
    def __init__(self,loan,annRate,months):
        """Assumes:loan and annRate are floats, months an int 
        Creates a new mortgage of size loan, duration months 
        and annual rate annRate"""
        self.loan=loan
        self.rate =annRate/12
        self.months=months
        self.paid==[0.0]
        self.outstanding=[loan]
        self.payment=findPayment(loan, self.rate, months)
        self.legend=None #description of morgage
        
        def makePayment(self):
            """Make payment"""
            self.paid.append(self.payment)
            reduction =self.payment -self.outstanding[-1]*self.rate
            self.outstanding.append(self.outstanding[-1]-reduction)
            
        def getTotalPaid(self):
            """return the total amount paid so far"""
            return sum(self.paid)
        
        def __str__(self):
            return self.legend
    
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.init(self,loan,r,months)
        self.legend ='fixed, '+str(round(r*100,2))+'%'
class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months,pts):
        Mortgage.__init__(self,loan,r,months)
        self.pts=pts
        self.paid=[loan*(pts/100)]
        self.legend ='Fixed'+str(round(r*100,2))+'%,' +str(pts)+'points'
class TwoRate(Mortgage):
    def __init__(self,loan,r,teaserRate,teaserMonths):
        Mortgage.__init__(self.loan,teaserRate,teaserMonths)
        self.teaserMonths=teaserMonths
        self.teaserRate=teaserRate  
        self.nextRate=r/12
        self.legend=str(teaserRate*100) +'Months, then' +str(round(r*100,2))+'%'
        
def makePayment(self):
    if len(self.paid)==self.teaserMonths+1:
        self.rate=self.nextRate
        self.payment=findPayment(self.outstanding[-1],self.rate,self.months-self.teaserMonths)
    
    Mortgage.makePayment(self)
    
def compareMortgages(amt, years, fixedRate, pts, ptsRate,varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    for m in morts:
        print(m)
        print(' Total payments = $' + str(int(m.getTotalPaid())))


compareMortgages(amt=input("enter Amount"), years=input("Enter Years"), fixedRate=0.07,pts = 3.25, ptsRate=0.05, varRate1=0.045,varRate2=0.095, varMonths=48)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        