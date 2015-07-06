def nth_chandos_number(n):
    chando_list = []
    step = 1
    while len(chando_list) < n:
        temp_list = []
        chando_list.append(pow(5, step))
        last_item = chando_list[-1]
        for item in chando_list[:-1]:
            temp_list.append(item + last_item)
        if temp_list:
            chando_list.extend(temp_list)
        step += 1

    return chando_list[n - 1]
