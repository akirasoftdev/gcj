import sys


def main():
    file = sys.argv[1]
    f = open(file)
    line = f.readline()
    num = int(line)
    for a in range(num):
        line = f.readline().rstrip('\n')
        num_row, num_col = line.split(' ')
        lines = []
        for b in range(int(num_row)):
            line = f.readline().rstrip('\n')
            lines.append(line)
        output_result(a, lines, int(num_row), int(num_col))
    f.close()


def output_result(case, in_rows):
    print('Case #%d:' % (case + 1))
    result = []
    cnt = 0

    for in_row in in_rows:
        out_row = create_row(in_row)
        if len(out_row) == 0:
            if len(result) == 0:
                cnt += 1
                continue
            result += [result[-1]]
        else:
            result += [out_row] * (cnt + 1)
            cnt = 0
    print_output(result)


def create_row(in_row):
    out_row = ''
    cnt = 0
    for in_char in list(in_row):
        if in_char == '?':
            if len(out_row) == 0:
                cnt += 1
                continue
            out_row += out_row[-1]
        else:
            out_row += (in_char * (cnt + 1))
            cnt = 0
    return out_row


def print_output(output):
    for line in output:
        print(line)

if __name__ == '__main__':
    main()