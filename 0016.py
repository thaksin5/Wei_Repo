if __name__ == '__main__':
    num = int(input())
    ans = str(input())

    adrian_answer = 'ABC'
    bruno_answer = 'BABC'
    goran_answer = 'CCAABB'

    count=[0,0,0]

    for i in range(num):
        if(ans[i] == adrian_answer[i%3]):
            count[0]+=1
        if(ans[i] == bruno_answer[i%4]):
            count[1]+=1
        if(ans[i] == goran_answer[i%6]):
            count[2]+=1

    print(max(count))
    if max(count) == count[0]:
        print('Adrian')
    if max(count) == count[1]:
        print('Bruno')
    if max(count) == count[2]:
        print('Goran')
