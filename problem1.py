x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(x):
    result = list()
    for i in x:
        if isinstance(i,list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result

print(flatten_list(x))