fruit_basket=[]
unique_fruits=[]
repeat_fruits=[]
for i in range(4):
    fruit=input('Enter fruits:')
    fruit_basket.append(fruit)
for fruit in fruit_basket:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)
    else:
      if fruit not in repeat_fruits:
        repeat_fruits.append(fruit)
print('Unique fruits:',unique_fruits)
print('Repeated fruits:',repeat_fruits)