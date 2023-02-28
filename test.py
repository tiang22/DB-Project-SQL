import os,time,sys

def test_load():
    os.system('sqlite3 test.db < schema.sql')
    os.system('sqlite3 test.db < load.sql')
    data_files = os.listdir('data')
    data_files.sort()
    expected = open(f'outputs/0.out').read()
    out = ''
    for name in data_files:
        tbl_name = name.split('.')[0]
        out += os.popen(f'echo \"select * from {tbl_name};\" | sqlite3 test.db').read()
    if expected != out:
        print(f'Test 0 failed')
        return
    print(f'Test 0 passed')
        
def test(i):
    expected = open(f'outputs/{i}.out').read()
    out = os.popen(f'sqlite3 test.db < {i}.sql').read()
    if i == 2:
        out = os.popen(f'echo \"select L_TAX from lineitem WHERE L_DISCOUNT > 0.02;\" | sqlite3 test.db').read()
    if expected == out:
        print(f'Test {i} passed')
    else:
        print(f'Test {i} failed')
    time.sleep(3)
    

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'create':
        test_load()
    else:
        test(int(cmd))
