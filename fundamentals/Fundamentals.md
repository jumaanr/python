Asking question regarding Python. In python when I execute following ,  'python'  <  'Python'  ,returns TRUE . Why is that ?

In Python, string comparisons are performed based on lexicographic (dictionary) order. The comparison is done character by character from left to right, starting with the first character of each string. When comparing two strings, Python considers the ASCII values of the characters.

In ASCII, uppercase letters have lower values than lowercase letters. Therefore, when you compare the strings `'python'` and `'Python'`, Python compares the first characters `'p'` and `'P'`. Since the ASCII value of `'p'` is greater than the ASCII value of `'P'`, the string `'python'` is considered greater than `'Python'`.

Here's a comparison of the first characters of the two strings:

```
'p' (ASCII value: 112) > 'P' (ASCII value: 80)
```

As a result, `'python'` is considered greater than `'Python'`, and the expression `'python' < 'Python'` evaluates to `True`.

If you were to use lowercase letters for both strings, the comparison would be case-sensitive, and the result would be different:

```
'python' (ASCII: 112 121 116 104 111 110) < 'python' (ASCII: 112 121 116 104 111 110)
```

In this case, the strings are equal, and the expression `'python' < 'python'` would evaluate to `False`.