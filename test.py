import os,time,sys

def create_db():
    os.system('sqlite3 test.db < schema.sql')
    # get filenames under data
    data_files = os.listdir('data')
    for name in data_files:
        tbl_name = name.split('.')[0]
        os.popen(f'echo \".mode csv\n.separator |\n.import data/{name} {tbl_name}\n\" | sqlite3 test.db>/dev/null 2>&1')
        time.sleep(3)
        
def test(i):
    expected = open(f'outputs/{i}.out').read()
    out = os.popen(f'sqlite3 test.db < {i}.sql').read()
    if expected == out:
        print(f'Test {i} passed')
    else:
        print(f'Test {i} failed')
    time.sleep(3)
    

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'create':
        create_db()
    else:
        test(int(cmd))