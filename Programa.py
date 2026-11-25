import subprocess

def f(x):
    return 5*x**2 - 3*x + 8

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    ini = float(input('Dame ini '))
    fin = float(input('Dame fin '))
    inc = float(input('Dame inc '))
    print('\n\n')
    
    if inc>0:
        print(f'x\t| f(x) = 5x^2 -3x + 8\n')
        x = ini
        while x<=fin:
            print(f'{x}\t| {f(x)}')
            x += inc
