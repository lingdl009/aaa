width = int(input('please enter width:'))
price_width = 10
item_width = width-price_width
head_format = '%-*s%*s'
format = '%-*s%*.2f'
print('='*width)
print(head_format % (item_width, 'Item',price_width,'Price'))
print('-'*width)
print(format %(item_width,'apple',price_width,0.4))
print(format %(item_width,'pears',price_width,0.5))
print(format %(item_width,'cantl',price_width,1.92))
print(format %(item_width,'dried apricots',price_width,8))
print('='*width)
aaaaa