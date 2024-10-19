#بازی اعداد که عدد بین1-9انتخاب میکنیم حاصلش با بازی میشه8
frist_number= int(input("pless your number between 1 -9:"))
number=frist_number
number*=2
number+=8
number+=frist_number
number-=2
number/=3
number-=frist_number
number*=4
print(number)