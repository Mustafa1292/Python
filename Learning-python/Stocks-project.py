# -*- coding: utf-8 -*-


data = []
with open("GOOG.csv", "r") as file:
    for line in file.readlines():
        temp = line.strip().split(",")
        if temp[0] == 'Date':
            continue
        data.append([temp[0], float(temp[2]), float(temp[3])])


best_buy = 0
best_sell = 1
value = 0
for buy in range(len(data)-1):
    for sell in range(buy+1,len(data)):
        gain = data[sell][1] - data[buy][2]
        if value < gain:
            value = gain
            best_buy = buy
            best_sell = sell


buy_message = "Buy on {0} at a price of {1:0.2f}"
sell_message = "Sell on {0} at a price of {1:0.2f}"


print("Profit per share: {0:0.2f}".format(value))
print(buy_message.format(data[best_buy][0], data[best_buy][2]))
print(sell_message.format(data[best_sell][0], data[best_sell][1]))

print("Ratio: {0:0.3f}".format(data[best_sell][1]/data[best_buy][2]))

        