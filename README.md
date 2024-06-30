# H4X

An easily embedable lisp like. Made for the hackclub langjam.

```
{fibonacci}
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

# TODO
 - Change the parsing/evaluation to and iterative function instead of a recursive one
 - Add dictionaries/hashmaps
 - Add more standard library (such as string manipulation)
