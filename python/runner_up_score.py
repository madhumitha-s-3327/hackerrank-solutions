if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_score=sorted(list(set(arr)))
    print(unique_score[-2])
