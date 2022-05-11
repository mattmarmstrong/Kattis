import sys


operators = ['*', '+', '-', '//']


def fours(n):
    for i in operators:
        for j in operators:
            for k in operators:
                exp = '4 ' + i + ' 4 ' + j + ' 4 ' + k + ' 4'
                value = eval(exp)

                if value == n:
                    if '//' in exp:
                        exp.replace('//', '/')
                    return exp + ' = {}'.format(n)


m = int(sys.stdin.readline().strip())

for i in range(m):
    x = int(sys.stdin.readline().strip())
    result = fours(x)
    if result is None:
        print('no solution')
    else:
        print(result)

