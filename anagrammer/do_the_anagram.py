from collections import defaultdict
from functools import reduce
from itertools import permutations, combinations

import click

__author__ = 'acushner'

CACHED_WORDS_SHELF = './.words_cache'


@click.command()
@click.option('-n', '--num-letters', type=int, default=None, help='show only words of `n` length')
@click.option('-m', '--min-num-letters', default=3, help='show words >= `n` length')
@click.option('-f', '--full', count=True, help='use bigger dictionary (can be used up to twice)')
@click.option('-t', '--together', is_flag=True, help='words sorted together regardless of length')
@click.argument('word', nargs=1, required=True)
def do_the_anagram(num_letters, word, full, together, min_num_letters):
    """calculate anagrams based on inputs"""
    word = word.lower()
    fn = f'./words_{"sml"[min(full, 2)]}.txt'

    r = range(min_num_letters, len(word) + 1)
    if num_letters:
        r = range(num_letters, num_letters + 1)

    def p(*args):
        if not together:
            print(*args)

    res = set()
    func = _do_the_anagram_big if len(word) > 9 else _do_the_anagram_small
    for n, curr in func(fn, word, r):
        p('=================')
        p(n)
        res.update(curr)
        p('\n'.join(sorted(''.join(w) for w in curr)))
        p(n)
        p('=================')
        p()

    if together:
        print('=================')
        print('\n'.join(sorted(''.join(w) for w in res)))
        print('=================')


def _do_the_anagram_big(fn, word, rng):
    """
    use combinations to find anagrams
    faster with bigger words
    """
    wbc = _get_words_by_counter(fn)
    for n in rng:
        words = (wbc.get(tuple(sorted(w)), set()) for w in combinations(word, n))
        yield n, reduce(set().union, words)


def _do_the_anagram_small(fn, word, rng):
    """
    use permutations to find anagrams
    faster with smaller words
    """
    with open(fn) as f:
        words = {tuple(l.strip().lower()) for l in f}

    for n in rng:
        yield n, {w for w in permutations(word, n) if w in words}


def _get_words_by_counter(fn):
    """convert file into data structure for use by combinations"""
    res = defaultdict(set)
    with open(fn) as f:
        for l in f:
            l = l.strip().lower()
            res[tuple(sorted(l))].add(l)
    return res


def __main():
    do_the_anagram()


if __name__ == '__main__':
    __main()
