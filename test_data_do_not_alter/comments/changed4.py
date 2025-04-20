import random

# Generate a list of 20 random integers between 50 and 100
def gen():
    return [random.randint(50, 100) for _ in range(20)]

# Calculate the average of the data
def proc(data):
    return sum(data) / len(data)

# Find the highest value in the dataset
def high(data):
    return sorted(data)[-1]

# Find the lowest value in the dataset
def low(data):
    return sorted(data)[0]

# Group the data into three categories:
# 'X' for scores 85 and above,
# 'Y' for scores between 70 and 84,
# 'Z' for scores below 70
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

# Print summary statistics and category distribution
def out(data):
    print(f"p: {proc(data):.1f}")       # average
    print(f"h: {high(data)}")           # highest
    print(f"l: {low(data)}")            # lowest
    g = group(data)
    print("g:")                         # group counts
    for k, v in g.items():
        print(f" {k}: {v}")

# Main function to generate data and show output
def go():
    d = gen()
    out(d)

if __name__ == "__main__":
    go()
