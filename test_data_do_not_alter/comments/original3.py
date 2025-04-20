def process_data(data):
    normalized = [x / max(data) for x in data]
    filtered = [x for x in normalized if x > 0.5]
    return sum(filtered) / len(filtered)
