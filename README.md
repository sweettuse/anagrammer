# anagrammer
simple anagram finder for american words

to run just do python3 do_the_anagram.py --help:

```
> python3 do_the_anagram.py --help
Usage: do_the_anagram.py [OPTIONS] WORD

Options:
  -n, --num-letters INTEGER      show only words of `n` length
  -m, --min-num-letters INTEGER  show words >= `n` length
  -f, --full                     use bigger dictionary (can be used up to
                                 twice)
  -t, --together                 words sorted together regardless of length
  --help                         Show this message and exit.
```

example
```
> python3 do_the_anagram.py -m6 american
=================
6
airman
airmen
anemia
anemic
arcane
caiman
camera
cinema
crimea
iceman
maniac
marina
marine
mincer
remain
6
=================

=================
7
america
anaemic
armenia
carmine
7
=================

=================
8
american
8
=================

```