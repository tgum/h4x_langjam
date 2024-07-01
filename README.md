# H4X

An easily embedable lisp like. Made for the hackclub langjam.

```
~ this is a comment
{
  this is a
  multiline
  comment
}

(print "hello world")

{ fibonacci }
(define fib
  (fn (n)
    (if (<= n 2)
      1
      ~ else
      (+
        (fib (- n 1))
        (fib (- n 2))
      )
    )
  )
)
(print fib 10) ~ <= 6765
```

# Requirements

This was tested with python 3.8 and 3.12. I don't think you need external libraries.


# How to use

To run a h4x file
```
python main.py [name of file.h4x]
```

There is an interactive repl
```
python repl.py
```

To use embed h4x in you own projects see [Docs/library.md](Docs/library.md)


# Bugs
this is very (probably) very buggy software idk if ill continue once langjam is over i think it would be cool
if you find bugs and stuff or have suggestions you can create an issue at the repo https://github.com/tgum/h4x_langjam/issues

# TODO
 - Change the parsing/evaluation to and iterative function instead of a recursive one
 - Add dictionaries/hashmaps
 - Add more standard library (such as string manipulation)
 - closures thats a very cool thing
