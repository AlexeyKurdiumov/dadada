french = set(map(int, input().split()))
swimmers = set(map(int, input().split()))
pianists = set(map(int, input().split()))
swimmers_and_pianists = swimmers & pianists
result_set = swimmers_and_pianists - french
result_sorted = sorted(list(result_set))
print(*result_sorted)
