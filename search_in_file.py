#-*- coding: utf-8 -*-

def run():
    word = 'Beatriz'
    counter = 0
    with open('aleph.txt') as f:
        for line in f :
            counter += line.count(word)

    print('{} se encontro {} veces en el texto'.format(word, counter))

if __name__ == '__main__':
    run()
