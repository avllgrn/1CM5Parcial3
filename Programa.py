import subprocess

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    n = int(input('Ingresa n '))

    s = 0
    i = 0
    while i<=n:
        print(f'i={i},\ts={s}')
        s = s+i
        i += 1

    print(f'\n\nSuma de [0, {n}] = {s}\n\n')


    p = 1
    i = 1
    while i<=n:
        print(f'i={i},\tp={p}')
        p = p*i
        i += 1

    print(f'\n\nProducto de [1, {n}] = {p}\n\n')
