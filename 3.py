# быстрая сортровка сложности O(nlogn)
# выполняется быстрее чем например bublesort где сложность O(n)2

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        q = random.choice(list)
        L = []
        M = []
        R = []
        for elem in list:
            if elem < q:
                l.append(elem) 
            elif elem > q: 
                r.append(elem) 
            else: 
                m.append(elem)
        return quick_sort(l) + m + quick_sort(r)


