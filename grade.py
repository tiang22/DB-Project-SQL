import os,time,sys
import json

def test_load():
    os.system('make clean')
    os.system('sqlite3 test.db < schema.sql')
    os.system('sqlite3 test.db < load.sql')
    data_files = os.listdir('data')
    data_files.sort()
    expected = open(f'outputs/0.out').read()
    out = ''
    for name in data_files:
        tbl_name = name.split('.')[0]
        out += os.popen(f'echo "select * from {tbl_name};" | sqlite3 test.db').read()
    if expected != out:
        print('Test 0 failed')
        return 0
    print('Test 0 passed')
    return 1

def test(i):
    expected = open(f'outputs/{i}.out').read()
    out = os.popen(f'sqlite3 test.db < {i}.sql').read()
    if i == 2:
        if len(out) != 0:
            print(f'Test {i} failed')
            return 0
        out = os.popen(f'echo "select L_TAX from lineitem WHERE L_DISCOUNT > 0.02;" | sqlite3 test.db').read()
    if i in [1, 2, 3, 4, 5, 7]:
        expected = sorted(expected.splitlines())
        out = sorted(out.splitlines())
    if expected == out:
        print(f'Test {i} passed')
        return 1
    else:
        print(f'Test {i} failed')
        return 0

if __name__ == '__main__':
    if len(sys.argv) == 1:
        scores = {}
        if test_load():
            scores['Load'] = 2
            for i in range(1, 9):
                prob = 'Prob{}'.format(i)
                if test(i):
                    scores[prob] = 1
                else:
                    scores[prob] = 0
        else:
            scores['Load'] = 0
        print(json.dumps({'scores': scores}))
    else:
        cmd = sys.argv[1]
        if cmd == 'load':
            test_load()
        else:
            test(int(cmd))
