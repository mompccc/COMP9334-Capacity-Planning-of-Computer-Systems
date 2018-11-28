

class Server():
    def __init__(self, state='OFF', set_up=0, delay=0):
        self.state = state
        self.set_up = set_up
        self.busy_array = []
        self.delay = delay


def main_fun(arrival, service, m, setup, delay, end):
    m = m
    setup_time = setup
    delayedoff_time = delay
    arrival = arrival
    service = service
    end_time = end

    # initial----------------------------------------
    dispatcher = []
    servers = []
    count_marked = 0

    for i in range(m):
        servers.append(Server())

    print("Time={}, Dispatcher: {}".format(0, dispatcher))
    for i in range(len(servers)):
        print("Servers{}, {}, setup:{}, busy:{}, delay:{}".format(i+1, servers[i].state, servers[i].set_up, servers[i].busy_array,
                                                       servers[i].delay))

    # main-------------------------------------------

    off_count = m
    setup_count = 0
    delay_count = 0
    i = 0
    out_list = []
    for a in range(end_time*100):
        i += 0.01
        i = round(i, 2)
        if i in arrival and off_count != 0 and delay_count == 0:
            temp_index = arrival.index(i)
            dispatcher.append((i, service[temp_index], 'MARKED'))
            count_marked += 1
            for q in range(len(servers)):
                if servers[q].state == 'OFF':
                    temp_q = q
                    break
            servers[temp_q].state = 'SETUP'
            servers[temp_q].set_up = round(i + setup_time, 2)
            setup_count += 1
            off_count -= 1
            print("Time={}, Dispatcher: {}".format(i, dispatcher))
            for k in range(len(servers)):
                print("Servers{}, {}, setup:{}, busy:{}, delay:{}".format(k + 1, servers[k].state, servers[k].set_up,
                                                                     servers[k].busy_array,
                                                                     servers[k].delay))
        elif i in arrival and off_count != 0 and delay_count != 0:
            temp_index = arrival.index(i)
            max_delay = 0
            a = 0
            for j in range(len(servers)):
                if servers[j].state == 'DELAY':
                    if servers[j].delay > max_delay:
                        max_delay = servers[j].delay
                        a = j
            if max_delay > 0:
                servers[a].state = 'BUSY'
                servers[a].busy_array = [i, round(i + service[temp_index], 2)]
                servers[a].delay = 0
                delay_count -= 1
            print("Time={}, Dispatcher: {}".format(i, dispatcher))
            for k in range(len(servers)):
                print("Servers{}, {}, setup:{}, busy:{}, delay:{}".format(k + 1, servers[k].state, servers[k].set_up,
                                                                          servers[k].busy_array,
                                                                          servers[k].delay))
        elif i in arrival and off_count == 0 and delay_count == 0:
            temp_index = arrival.index(i)
            dispatcher.append((i, service[temp_index], 'UNMARKED'))
            print("Time={}, Dispatcher: {}".format(i, dispatcher))
            for k in range(len(servers)):
                print("Servers{}, {}, setup:{}, busy:{}, delay:{}".format(k + 1, servers[k].state, servers[k].set_up,
                                                                     servers[k].busy_array,
                                                                     servers[k].delay))
        for s in servers:
            if s.state == 'SETUP' and s.set_up == i:
                job = dispatcher.pop(0)
                start_time, last_time, mark = job[0], job[1], job[2]
                s.busy_array = [start_time, round(i + last_time, 2)]
                s.state = 'BUSY'
                s.set_up = 0
                setup_count -= 1
                if mark == 'MARKED':
                    count_marked -= 1
                if count_marked != setup_count:
                    if len(dispatcher) > count_marked:
                        job1 = dispatcher[count_marked]
                        start_time1, last_time1, mark1 = job1[0], job1[1], job1[2]
                        dispatcher[count_marked] = (start_time1, last_time1, 'MARKED')
                        count_marked += 1
                    else:
                        max_setup = 0
                        a = 0
                        for j in range(len(servers)):
                            if servers[j].state == 'SETUP':
                                if servers[j].set_up > max_setup:
                                    max_setup = servers[j].set_up
                                    a = j
                        servers[a].state = 'OFF'
                        servers[a].set_up = 0
                        setup_count -= 1
                        off_count += 1
                print("Time={}, Dispatcher: {}".format(i, dispatcher))
                for k in range(len(servers)):
                    print("Servers{}, {}, setup:{}, busy:{}, delay:{}".format(k + 1, servers[k].state, servers[k].set_up,
                                                                         servers[k].busy_array,
                                                                         servers[k].delay))
            elif s.state == 'BUSY' and s.busy_array[1] == i:
                out_list.append(s.busy_array)
                if dispatcher:
                    job = dispatcher.pop(0)
                    start_time, last_time, mark = job[0], job[1], job[2]
                    s.busy_array = [start_time, round(i + last_time, 2)]
                    if mark == 'MARKED':
                        count_marked -= 1
                    if count_marked != setup_count:
                        if len(dispatcher) > count_marked:
                            job1 = dispatcher[count_marked]
                            start_time1, last_time1, mark1 = job1[0], job1[1], job1[2]
                            dispatcher[count_marked] = (start_time1, last_time1, 'MARKED')
                            count_marked += 1
                        else:
                            max_setup = 0
                            a = 0
                            for j in range(len(servers)):
                                if servers[j].state == 'SETUP':
                                    if servers[j].set_up > max_setup:
                                        max_setup = servers[j].set_up
                                        a = j
                            servers[a].state = 'OFF'
                            servers[a].set_up = 0
                            off_count += 1
                            setup_count -= 1
                    print("Time={}, Dispatcher: {}".format(i, dispatcher))
                    for k in range(len(servers)):
                        print("Servers{}, {}, setup:{}, busy:{}, delay:{}".format(k + 1, servers[k].state, servers[k].set_up,
                                                                             servers[k].busy_array,
                                                                             servers[k].delay))
                else:
                    s.state = 'DELAY'
                    s.busy_array = []
                    s.delay = round(i + delayedoff_time, 2)
                    delay_count += 1
                    print("Time={}, Dispatcher: {}".format(i, dispatcher))
                    for k in range(len(servers)):
                        print("Servers{}, {}, setup:{}, busy:{}, delay:{}".format(k + 1, servers[k].state, servers[k].set_up,
                                                                             servers[k].busy_array,
                                                                             servers[k].delay))
            elif s.state == 'DELAY' and s.delay == i:
                delay_count -= 1
                if dispatcher:
                    job = dispatcher.pop(0)
                    start_time, last_time, mark = job[0], job[1], job[2]
                    s.busy_array = [start_time, round(i + last_time, 2)]
                    s.state = 'BUSY'
                    if mark == 'MARKED':
                        count_marked -= 1
                    if count_marked != setup_count:
                        if len(dispatcher) > count_marked:
                            job1 = dispatcher[count_marked]
                            start_time1, last_time1, mark1 = job1[0], job1[1], job1[2]
                            dispatcher[count_marked] = (start_time1, last_time1, 'MARKED')
                            count_marked += 1
                        else:
                            max_setup = 0
                            a = 0
                            for j in range(len(servers)):
                                if servers[j].state == 'SETUP':
                                    if servers[j].set_up > max_setup:
                                        max_setup = servers[j].set_up
                                        a = j
                            servers[a].state = 'OFF'
                            servers[a].set_up = 0
                            setup_count -= 1
                            off_count += 1
                    print("Time={}, Dispatcher: {}".format(i, dispatcher))
                    for k in range(len(servers)):
                        print(
                            "Servers{}, {}, setup:{}, busy:{}, delay:{}".format(k + 1, servers[k].state, servers[k].set_up,
                                                                                servers[k].busy_array,
                                                                                servers[k].delay))
                else:
                    s.state = 'OFF'
                    s.delay = 0
                    off_count += 1
                    print("Time={}, Dispatcher: {}".format(i, dispatcher))
                    for k in range(len(servers)):
                        print("Servers{}, {}, setup:{}, busy:{}, delay:{}".format(k + 1, servers[k].state, servers[k].set_up,
                                                                             servers[k].busy_array,
                                                                             servers[k].delay))

    response_time = []
    for x in out_list:
        response_time.append((x[1] - x[0]))
    for data in out_list:
        print(data)
    print("mean response time: ", sum(response_time)/len(response_time))
    return out_list, response_time
