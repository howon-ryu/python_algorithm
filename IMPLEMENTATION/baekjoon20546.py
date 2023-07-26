import copy

money_bnp = int(input())
bnp_cnt = 0
money_time = copy.deepcopy(money_bnp)
time_cnt = 0
stock_list = list(map(int,input().split()))



for i in stock_list:
    if(money_bnp>=i):
        bnp_cnt+=money_bnp//i
        money_bnp = money_bnp%i

up_cnt = 0
down_cnt = 0
for i in range(1,len(stock_list)):

    if(stock_list[i]>stock_list[i-1]):
        up_cnt+=1
        down_cnt=0
    elif(stock_list[i]<stock_list[i-1]):
        up_cnt = 0
        down_cnt += 1
    elif(stock_list[i]==stock_list[i-1]):
        up_cnt = 0
        down_cnt = 0

    if(up_cnt>=3):
        if(time_cnt!=0):
            money_time = time_cnt * stock_list[i]
            time_cnt = 0

    if(down_cnt>=3):

        time_cnt += money_time // stock_list[i]
        money_time = money_time % stock_list[i]






if((money_time+time_cnt*stock_list[-1])>(money_bnp+bnp_cnt*stock_list[-1])):
    print("TIMING")
elif((money_time+time_cnt*stock_list[-1])<(money_bnp+bnp_cnt*stock_list[-1])):
    print("BNP")
else:
    print("SAMESAME")