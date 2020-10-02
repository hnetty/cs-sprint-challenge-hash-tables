def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    data = {}
    for i in range(len(weights)):
        data[weights[i]] = i
    for i in range(len(weights)):
        diff = limit-weights[i]
        if diff in data:
            return (max(i, data[diff]), min(i, data[diff]))

    return None
