class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        "Takes input list of stocks and output max profit"
        Maxprofit=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                print(i,j,profit,Maxprofit)
                if(profit>Maxprofit):
                    Maxprofit=profit
        return Maxprofit
#output time limit exceed time complexity n2 need to improve
