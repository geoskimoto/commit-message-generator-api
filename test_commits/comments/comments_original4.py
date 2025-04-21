import random

def gen():
    return [random.randint(50, 100) for _ in range(20)]

def proc(data):
    return sum(data) / len(data)

def high(data):
    return sorted(data)[-1]

def low(data):
    return sorted(data)[0]

def group(data):
    buckets = {'X': 0, 'Y': 0, 'Z': 0}
    for val in data:
        if val >= 85:
            buckets['X'] += 1
        elif val >= 70:
            buckets['Y'] += 1
        else:
            buckets['Z'] += 1
    return buckets

def out(data):
    print(f"p: {proc(data):.1f}")
    print(f"h: {high(data)}")
    print(f"l: {low(data)}")
    g = group(data)
    print("g:")
    for k, v in g.items():
        print(f" {k}: {v}")

def go():
    d = gen()
    out(d)

if __name__ == "__main__":
    go()
