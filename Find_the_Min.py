import sys

input_file_path = sys.argv[1]

read_input = open('./' + input_file_path, 'r')

input_lines = read_input.read().decode('utf-8').split('\n')

read_input.close()

num_of_lines = int(input_lines[0])

input_lines = input_lines[1:num_of_lines * 2 + 1]

def findTheMin(parameters):
    n = parameters[0]
    k = parameters[1]
    a = parameters[2]
    b = parameters[3]
    c = parameters[4]
    r = parameters[5]
    last_value_show = {}
    prev_k_values = [a]
    if a <= k:
        last_value_show[a] = 0
    for i in range(1, k):
        new_value = (b * prev_k_values[i - 1] + c) % r
        prev_k_values.append(new_value)
        if new_value <= k:
            last_value_show[new_value] = i
    
    candidate_values = dict([(x, 0) for x in range(0, k + k)])
    for i in last_value_show.keys():
        del candidate_values[i]
    candidate_values = candidate_values.keys()
    candidate_values.sort()
    perfect_k_values = []
    candidate_from_k = []
    for i in range(k, k + k + 1):
        if candidate_from_k and candidate_from_k[0] < candidate_values[0]: 
            min_value = candidate_from_k.pop(0)
            last_value_show[min_value] = i
        else:
            min_value = candidate_values.pop(0)
            last_value_show[min_value] = i
        perfect_k_values.append(min_value)
        prev_k_values.append(min_value)
        if prev_k_values[i - k] <= k and i - last_value_show[prev_k_values[i - k]] >= k:
            candidate_from_k.append(prev_k_values[i - k])
        candidate_from_k.sort()
    return perfect_k_values[(n - k) % len(perfect_k_values) - 1]
 
output_result = ''
for i in range(0, len(input_lines), 2):
    parameters = input_lines[i].split() + input_lines[i + 1].split()
    parameters = [int(x) for x in parameters]
    min_value = findTheMin(parameters)
    output_result += 'Case #' + str((i + 1) / 2 + 1) + ': ' + str(min_value) + '\n'

write_result = open('./Find_the_Min_Result.txt', 'w')
write_result.write(output_result.strip().encode('utf-8'))
