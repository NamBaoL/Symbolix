# Symbolix

A golfing language inspired by APL.

**Status:** Still very unstable, more features are still in development.

**Demonstrations:**

```python
print("Hello World") # ==> "Hello World"
```

```python
sum(filter(lambda x: not(x % 3 or x % 5), array)) # ==> 100#((3%)(5%),\!)!(+)/
```

```python
[i for i in range(1, a + 1) if a % i == 0] # ==> x#(%!)!
```