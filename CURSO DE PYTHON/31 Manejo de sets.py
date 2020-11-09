def run():
    s = set([1, 2, 3])
    t = set([3, 4, 5])

    print(s.union(t)) # [1, 2, 3, 4, 5]
    print(s.intersection(t)) # [3]
    print(s.difference(t)) # [1, 2]
    print(t.difference(s)) # [4, 5]

if __name__ == '__main__':
    run()