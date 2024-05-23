def maxProfit(self, prices: List[int]) -> int:
    Maxprofit=0
    L,R=0,1
    while(R<len(prices)):
        if(prices[L]<prices[R]):
            profit=prices[R]-prices[L]
            Maxprofit=max(Maxprofit,profit) 
        else:
            L=R
        R+=1
    return Maxprofit 
