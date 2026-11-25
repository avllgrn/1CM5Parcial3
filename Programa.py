import subprocess

if __name__ == '__main__':
    subprocess.run('cls', shell=True)

    n = int(input('¿De cuál número quieres la tabla? '))
    print('\n\n')

    i = 1
    while i<=10:
        print(f'{n} x {i}\t= {n*i}')
        i += 1
    print('\n\n')
