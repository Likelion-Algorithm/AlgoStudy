def solution(progresses, speeds):
    import math

    days_list = []
    days_dict = {}
    


    for i in range(len(progresses)):
        finish_day = math.ceil((100-progresses[i])/speeds[i])

        if len(days_list) == 0:
            days_list.append(finish_day)
            days_dict[finish_day] = 1
        else:
            if days_list[-1] < finish_day:
                days_list.append(finish_day)
                days_dict[finish_day] = 1
            else:
                days_dict[days_list[-1]] += 1
    
 
    return (list(days_dict.values()))



#통과링
