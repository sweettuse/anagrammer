from itertools import permutations

import click

__author__ = 'acushner'


@click.command()
@click.option('-n', '--num-letters', type=int, default=None, help='show only words of `n` length')
@click.option('-m', '--min-num-letters', default=3, help='show words >= `n` length')
@click.option('-f', '--full', count=True, help='use bigger dictionary (can be used up to twice)')
@click.option('-t', '--together', is_flag=True, help='words sorted together regardless of length', default=False)
@click.argument('word', nargs=1, required=True)
def do_the_anagram(num_letters, word, full, together, min_num_letters):
    fn = f'./words_{"sml"[min(full, 2)]}.txt'

    with open(fn) as f:
        words = {tuple(l.strip().lower()) for l in f}

    r = range(min_num_letters, len(word) + 1)
    if num_letters:
        r = range(num_letters, num_letters + 1)

    def p(*args):
        if not together:
            print(*args)

    res = set()
    for n in r:
        p('=================')
        p(n)
        curr = {w for w in permutations(word, n) if w in words}
        res.update(curr)
        p('\n'.join(sorted(''.join(w) for w in curr)))
        p(n)
        p('=================')
        p()

    if together:
        print('=================')
        p('\n'.join(sorted(''.join(w) for w in res)))
        print('=================')


def __main():
    do_the_anagram()


if __name__ == '__main__':
    __main()
