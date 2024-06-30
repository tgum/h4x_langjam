# Standard library reference

## Control flow

### if

syntax:
```
(if (= 5 6)
    (print "condition is true")
    ~ else
    (print "condition is false")
)
```
The last argument is optional.

### for

syntax 1:
```
(for i (amount)
    body
)
```
syntax 2:
```
(for i (start end)
    body
)
```
syntax 3:
```
(for i (start end increment)
    body
)
```