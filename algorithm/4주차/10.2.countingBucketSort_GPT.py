def counting_bucket_sort(arr, bucket_size=10):
    if len(arr) == 0:
        return arr

    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for num in arr:
        idx = (num - min_val) // bucket_size
        buckets[idx].append(num)

    # Sort each bucket using counting sort and concatenate
    def counting_sort(bucket):
        if not bucket:
            return []
        min_b, max_b = min(bucket), max(bucket)
        count = [0] * (max_b - min_b + 1)
        for num in bucket:
            count[num - min_b] += 1
        sorted_bucket = []
        for i, c in enumerate(count):
            sorted_bucket.extend([i + min_b] * c)
        return sorted_bucket

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(counting_sort(bucket))
    return sorted_arr

# Example usage:
if __name__ == "__main__":
    arr = [29, 25, 3, 49, 9, 37, 21, 43]
    print(counting_bucket_sort(arr))