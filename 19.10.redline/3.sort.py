import sys
from collections import Counter
def main():
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return
        
    n = int(input_data[0].strip())
    votes = (line.strip() for line in input_data[1:n+1] if line.strip())
    
    counter = Counter(votes)
    
    for movie, count in counter.most_common():
        print(f"{movie} {count}")


if __name__ == '__main__':
    main()
