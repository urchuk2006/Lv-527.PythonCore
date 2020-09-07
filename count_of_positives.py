def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positive_count = 0
    negative_sum = 0
    for n in arr:
        if n > 0:
            positive_count += 1
        elif n < 0:
            negative_sum += n

    return [positive_count, negative_sum]
