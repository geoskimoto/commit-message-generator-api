def process_data(data):
    # Normalize the data by dividing each element by the maximum value
    normalized = [x / max(data) for x in data]
    # Filter values greater than 0.5
    filtered = [x for x in normalized if x > 0.5]
    # Return the average of the filtered values
    return sum(filtered) / len(filtered)
