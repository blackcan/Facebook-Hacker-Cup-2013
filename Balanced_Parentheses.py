
import sys

input_file_path = sys.argv[1]

read_input = open('./' + input_file_path, 'r')

input_lines = read_input.read().decode('utf-8').split('\n')

read_input.close()

num_of_lines = int(input_lines[0])

input_lines = input_lines[1:num_of_lines + 1]

#atoz = [chr(i) for i in range(97, 123)]


output_result = ''

for i in range(len(input_lines)):
    line = input_lines[i]
    #for char in atoz:
    #    line = line.replace(char, '')
    #line = line.replace(' ', '')
    line = line.replace(r'[^\:\(\)]', '')
    
    line = line.replace('(:)', '')
    line = line.replace(':(', '')
    line = line.replace(':)', '')
    while '()' in line:
        line = line.replace('()', '')

    if '(' in line or ')' in line:
        output_result += 'Case #' + str(i + 1) + ': NO\n'
    else:
        output_result += 'Case #' + str(i + 1) + ': YES\n'
        

write_result = open('./Balanced_Parentheses_Result.txt', 'w')
write_result.write(output_result.strip().encode('utf-8'))
write_result.close()
