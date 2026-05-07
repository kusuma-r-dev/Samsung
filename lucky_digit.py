inp_n = int(input("Enter a number to find your lucky digit : "))
'''sum = 0
for i in inp_n :
    sum += i
final_sum = 0
for i in sum :
    final_sum += i
print(final_sum)'''
print(f'Number you inpupt is {inp_n}')
sum_of_digits = 0
while inp_n != 0 :
    rem = inp_n % 10
    inp_n //= 10
    sum_of_digits += rem
    if sum_of_digits > 9 and inp_n == 0 :
        inp_n = sum_of_digits
        sum_of_digits = 0

print("Your lucky digit is :",sum_of_digits)