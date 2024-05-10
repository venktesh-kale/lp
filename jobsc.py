
def schedule(arr,t):
    n = len(arr)

    #sort
    for i in range(n):
        for j in range(n-1-i):
            if arr[j][2]<arr[j+1][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


    result = [False]*t
    jobs = ['-1']*t
    sum  = 0

    for i in range(n):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if result[j] is False:
                result[j] = True
                jobs[j]=arr[i][0]
                sum = sum+arr[i][2]
                break

    print(jobs)
    print("profits is",sum)


job = [
    ('a',2,100),
    ('b',1,19),
    ('c',2,27),
    ('d',1,25),
    ('e',3,15)
]

schedule(job,3)


