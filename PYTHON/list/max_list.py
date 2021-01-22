l1=[6,5,33,2,11,3,22,4,66,100]

def max_list():
    print(l1)

    max=l1[0]

    for i in range(0,len(l1)):
        if(l1[i]>max):
            max=l1[i]
    
    print("maximum element in list is={} ".format(max))




max_list()



