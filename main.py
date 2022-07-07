import os
import glob
import time

if __name__ == '__main__':
    files = glob.glob("problem_*.py")
    files = sorted(files, key=lambda name: int(name.replace('.py', '').split('_')[1]))
    for i, file in enumerate(files, start=1):
        print(f'PROBLEM #{i}'.center(40, '='))
        start = time.time()
        os.system(f'python {file}')
        print("--- %s seconds ---" % (time.time() - start))
