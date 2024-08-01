# Symbolix

A stack-based golfing language inspired by APL.

**Status:** Still very unstable, many features and functions are still in development.

**Demonstrations:**

```python
print("Hello World") # ==> "Hello World"
```

```python
sum(filter(lambda x: not (x % 3 or x % 5)), array)) # ==> 100#((3%)(5%),\!)!(+)/
```

```python
[i for i in range(1, a + 1) if a % i == 0] # ==> x#(%!)!
```

# Features

To run Symbolix, download Python first and then clone this repository:
```
git clone https://github.com/NamBaoL/Symbolix.git
```

To run in interactive mode, just run ```terminal.py``` and start entering in the commands. You can try the examples above!

# Documentation

Check out the wiki for documentation, as well as tutorials, and more details about the elements of Symbolix.