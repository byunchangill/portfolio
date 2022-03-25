inputs = 9001 + 14000+ 29996+89262+10000+95700+100000+100000+60000+26000+30000+15000+12027+200000+40000+14500+264447 + 6447+30000+16232+32801+40000+20000+60910+100000+210000

print('초반자금',inputs)

outputs = 26693 + 216500 + 546268 + 49025 + 53132 + 400000 + 15401 + 200000 + 10000 + 164550

print('초반 출금',outputs)

profit = outputs - inputs 

print('첫분기 이득',profit)

inputs2 = 40000 + 45000 + 10000 + 40000 + 50000 + 20000 + 40000 + 35000 + 15000 + 7000 + 80000
print('시즌2 입금',inputs2)

outputs2 = 50000
print('시즌2 출금',outputs2)

now_mine = inputs2 - outputs2

print('현재 있어야하는돈',now_mine)

# 지금까지 입금한돈 
all_inputs = inputs + inputs2
print('지금까지 입금한 돈:',all_inputs)

# 지금까지 출금한돈
all_outputs = outputs + outputs2
print('지금까지 출금한 돈:',all_outputs)