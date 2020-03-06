
def run():
    counter = 0
    with open('numeros.txt') as f:
        for line in f:
            counter += line.count('3')
    
    print('3 se encuentra {} en el texto'.format(counter))

if __name__ == '__main__':
    run()