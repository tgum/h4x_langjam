# H4X

My project for the hackclub langjam. An easily embedable lisp like

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
