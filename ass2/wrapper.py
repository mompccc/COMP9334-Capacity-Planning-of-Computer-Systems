import ass2
import random
import numpy
#import matplotlib.pyplot as py

# This file first read 'num_tests.txt' file to check cycle-index.
# All the input arguments should be recorded as file like 'mode_1.txt', 'arrival_1.txt'...
# You don't need to put arguments in command line, just run the program

def test(mrt_list):
    m = len(mrt_list)
    w = 500
    mt_smooth = []
    mt_smooth.append(mrt_list[0])
    for i in range(2, m-w):
        if i < w:
            temp1 = 0
            for j in range(1, i-1):
                temp1 += mrt_list[j]
            mt_smooth.append(temp1/(2*i -1))
        else:
            temp2 = 0
            for j in range(i-w, i+w):
                temp2 += mrt_list[j]
            mt_smooth.append(temp2/(2*w + 1))
    for d in mt_smooth:
        print(round(d, 3), end=" ")
    print()

seed = 0
random.seed(seed)
test_file = 'num_tests.txt'
with open(test_file, 'r') as file:
    test_num = int(file.read().strip())

'''for i in range(1, test_num + 1):
    mode_file = 'mode_{}.txt'.format(i)
    arrival_file = 'arrival_{}.txt'.format(i)
    service_file = 'service_{}.txt'.format(i)
    para_file = 'para_{}.txt'.format(i)
    with open(mode_file, 'r') as file:
        mode = file.read().strip()
    if mode == 'random':
        with open(para_file, 'r') as file:
            temp_list = [line.strip() for line in file]
        m = int(temp_list[0])
        setup_time = float(temp_list[1])
        delay_time = float(temp_list[2])
        end_time = int(temp_list[3])

        with open(arrival_file, 'r') as file:
            r = float(file.read().strip())
        q = r*0.9
        A = [random.expovariate(r) for x in range(int(end_time * q))]
        arrival = [round(A[0], 2)]
        for x in range(1, len(A)):
            arrival.append(round(arrival[x - 1] + A[x], 2))

        with open(service_file, 'r') as file:
            u = float(file.read().strip())
        B = [random.expovariate(u) for y in range(int(3 * end_time * q))]
        service = []
        for x in range(0, int(3 * end_time * q), 3):
            service.append(round(B[x] + B[x + 1] + B[x + 2], 2))

        out_list, response_time = ass2.main_fun(arrival, service, m, setup_time, delay_time, end_time)
        mrt_file = 'mrt_{}.txt'.format(i)
        departure_file = 'departure_{}.txt'.format(i)
        with open(departure_file, 'w') as file:
            for pair in out_list:
                file.writelines("%.3f\t%.3f\n" % (pair[0], pair[1]))
        final = []
        for j in range(int(0.05 * len(response_time)), len(response_time)):
            final.append(response_time[j])
        with open(mrt_file, 'w') as file:
            file.write("%.3f" % (sum(final) / len(final)))
        seed += 1
        random.seed(seed)

    elif mode == 'trace':
        with open(para_file, 'r') as file:
            temp_list = [line.strip() for line in file]
        m = int(temp_list[0])
        setup_time = float(temp_list[1])
        delay_time = float(temp_list[2])
        end_time = 1000

        with open(arrival_file, 'r') as file:
            arrival = [float(line.strip()) for line in file]

        with open(service_file, 'r') as file:
            service = [float(line.strip()) for line in file]

        out_list, response_time = ass2.main_fun(arrival, service, m, setup_time, delay_time, end_time)
        mrt_file = 'mrt_{}.txt'.format(i)
        departure_file = 'departure_{}.txt'.format(i)
        with open(departure_file, 'w') as file:
            for pair in out_list:
                file.writelines("%.3f\t%.3f\n" % (pair[0], pair[1]))
        final = []
        for j in range(int(0.05 * len(response_time)), len(response_time)):
            final.append(response_time[j])
        with open(mrt_file, 'w') as file:
            file.write("%.3f" % (sum(final)/len(final)))'''



with open('para_3.txt', 'r') as file:
    temp_list = [line.strip() for line in file]
m = int(temp_list[0])
setup_time = float(temp_list[1])
delay_time = float(temp_list[2])
end_time = 10000

with open('arrival_3.txt', 'r') as file:
    r = float(file.read().strip())
q = r*0.9
A = [random.expovariate(r) for x in range(int(end_time * q))]
arrival = [round(A[0], 2)]
for x in range(1, len(A)):
    arrival.append(round(arrival[x - 1] + A[x], 2))

with open('service_3.txt', 'r') as file:
    u = float(file.read().strip())

B = [random.expovariate(u) for y in range(int(3 * end_time * q))]
service = []
for x in range(0, int(3 * end_time * q), 3):
    service.append(round(B[x] + B[x + 1] + B[x + 2], 2))
print(arrival)

'''
new = []
c = 0
for i in range((int(max(A))+1)*10):
    temp = 0
    c += 0.1
    for data in A:
        if c < data < c+0.1:
            temp += 1
    new.append(temp)

for d in new:
    print(d, end=' ')
print()
c = 0
for d in new:
    c += 0.1
    print(round(c, 1), end=' ')'''


A = []
final = []
da = 0
count = 0
out_list, response_time = ass2.main_fun(arrival, service, m, setup_time, 0.1, end_time)

Y = []
for q in response_time:
    count += 1
    da += q
    Y.append(round(da/count, 3))
print(Y)
test(Y)
for i in range(int(0.05*len(response_time)), len(response_time)):
    final.append(response_time[i])
A.append((0.1, round(sum(final)/len(final), 3)))
print(A)

'''for i in range(1, 2):
    final = []
    out_list, response_time = ass2.main_fun(arrival, service, m, setup_time, i, end_time)
    for j in range(int(0.05 * len(response_time)), len(response_time)):
        final.append(response_time[j])
    A.append((i, round(sum(final)/len(final), 3)))
for fin in A:
    print(fin[0], fin[1])'''
