import sys

input_file_path = sys.argv[1]

read_input = open('./' + input_file_path, 'r')

input_lines = read_input.read().decode('utf-8').split('\n')

input_lines = filter(lambda x: x, input_lines)

read_input.close()

letters = [chr(i) for i in range(97, 123)]


def computeScore(line):
    letters_count = dict([(x, 0) for x in letters])
    line = line.lower()
    for char in line:
        if char in letters_count:
            letters_count[char] += 1
    letters_rank = sorted([(letters_count[x], x) for x in letters_count.keys()], reverse = True)
    total_score = 0
    for i in range(len(letters_rank)):
        total_score += letters_rank[i][0] * (26 - i)   
    return total_score

write_result = open('./Beautiful_String_Result.txt', 'w')

#print computeScore('Good luck in the Facebook Hacker Cup this year!')

for i in range(1, len(input_lines)):
    result = str(computeScore(input_lines[i]))
    if i == len(input_lines) - 1:
        write_result.write(('Case #' + str(i) + ': ' + result).encode('utf-8'))
    else:
        write_result.write(('Case #' + str(i) + ': ' + result + '\n').encode('utf-8'))
write_result.close()
    
