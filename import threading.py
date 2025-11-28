import threading

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
partial_sum1 = 0
partial_sum2 = 0

def sum_first_half():
    global partial_sum1
    partial_sum1 = sum(numbers[:len(numbers)//2])

def sum_second_half():
    global partial_sum2
    partial_sum2 = sum(numbers[len(numbers)//2:])

t1 = threading.Thread(target=sum_first_half)
t2 = threading.Thread(target=sum_second_half)

t1.start()
t2.start()

t1.join()
t2.join()

total = partial_sum1 + partial_sum2
print("Sum of first half:", partial_sum1)
print("Sum of second half:", partial_sum2)
print("Total sum:", total)