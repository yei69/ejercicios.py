arr = [1, 2, 2, 5, 4, 6, 8, 8, 8, 8]

longest_seq_len = 1
longest_seq_num = arr[1]
current_seq_len = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        current_seq_len += 1
    else:
        if current_seq_len > longest_seq_len:
            longest_seq_len = current_seq_len
            longest_seq_num = arr[i-1]
        current_seq_len = 1

if current_seq_len > longest_seq_len:
    longest_seq_len = current_seq_len
    longest_seq_num = arr[-1]

print("Longest:", longest_seq_len)
print("Number:", longest_seq_num)