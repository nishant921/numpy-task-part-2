NumPy Broadcasting

What is Broadcasting?

Broadcasting is a NumPy mechanism that allows arithmetic operations to be performed between arrays of different shapes.

Instead of manually changing the shape of an array, NumPy automatically expands the smaller array conceptually so that the operation can be performed.

Broadcasting is commonly used with:

- Addition
- Subtraction
- Multiplication
- Division
- Comparison operations
- Mathematical operations

---

Why is Broadcasting Useful?

Suppose we have:

import numpy as np

a = np.array([1, 2, 3])
b = 10

print(a + b)

Output:

[11 12 13]

Normally, "a" contains three elements while "b" is only one value.

NumPy automatically applies "10" to every element:

[1, 2, 3]
+
[10, 10, 10]
----------------
[11, 12, 13]

This automatic behavior is called broadcasting.

---

Broadcasting Rules

NumPy compares the shapes of arrays from right to left.

Two dimensions are compatible when:

1. Both dimensions are equal.
2. One of the dimensions is "1".
3. One of the arrays does not have that dimension.

If the dimensions are incompatible, NumPy raises a "ValueError".

---

Example 1: Scalar and Array

import numpy as np

a = np.array([1, 2, 3])

print(a + 5)

Output:

[6 7 8]

The scalar "5" is broadcast to:

[5, 5, 5]

Therefore:

[1, 2, 3]
+
[5, 5, 5]
-------------
[6, 7, 8]

---

Example 2: Two Arrays with the Same Shape

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)

Output:

[11 22 33]

Both arrays have shape:

(3,)

Since their dimensions are equal, broadcasting is possible.

---

Example 3: 2D Array + 1D Array

Consider:

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print(a + b)

Shape of "a":

(2, 3)

Shape of "b":

(3,)

NumPy compares them from the right:

(2, 3)
(   3)
    ↑

The "3" matches the "3", so broadcasting is possible.

Conceptually, NumPy treats "b" as:

[10, 20, 30]
[10, 20, 30]

Therefore:

[1, 2, 3]   [10, 20, 30]
[4, 5, 6] + [10, 20, 30]

Output:

[[11 22 33]
 [14 25 36]]

---

Example 4: Broadcasting with a Column

Consider:

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [10],
    [20]
])

print(a + b)

Shapes:

a → (2, 3)
b → (2, 1)

Compare from right to left:

(2, 3)
(2, 1)
    ↑

The second dimension is "3" and "1".

Since one dimension is "1", broadcasting is possible.

Conceptually:

[1, 2, 3] + [10, 10, 10]
[4, 5, 6] + [20, 20, 20]

Output:

[[11 12 13]
 [24 25 26]]

---

Example 5: Broadcasting with (3, 1) and (1, 4)

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([
    [10, 20, 30, 40]
])

print(a + b)

Shapes:

a → (3, 1)
b → (1, 4)

Compare:

(3, 1)
(1, 4)

First:

1 and 4

One dimension is "1", so they are compatible.

Second:

3 and 1

Again, one dimension is "1".

Therefore, broadcasting is possible.

Result shape:

(3, 4)

Output:

[[11 21 31 41]
 [12 22 32 42]
 [13 23 33 43]]

---

Example 6: Broadcasting is NOT Possible

Consider:

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20])

print(a + b)

Shapes:

a → (2, 3)
b → (2,)

Compare from right to left:

(2, 3)
(   2)

We compare:

3 and 2

They are not equal, and neither is "1".

Therefore, broadcasting is not possible.

NumPy produces:

ValueError

---

How to Check Broadcasting

Always write the shapes next to each other.

For example:

A → (2, 3)
B → (3,)

Align them from the right:

A → (2, 3)
B → (   3)

Compare:

3 = 3  ✅

Therefore:

Broadcasting possible

---

Another Example

A → (2, 3, 4)
B →    (3, 4)

Align:

A → (2, 3, 4)
B → (   3, 4)

Compare:

4 = 4  ✅
3 = 3  ✅

Therefore broadcasting is possible.

Result:

(2, 3, 4)

---

Example with Dimension 1

A → (2, 3, 4)
B → (   3, 1)

Align:

A → (2, 3, 4)
B → (   3, 1)

Compare:

4 vs 1 → ✅
3 vs 3 → ✅
2 vs nothing → ✅

Therefore broadcasting is possible.

Result shape:

(2, 3, 4)

---

Broadcasting Shape Cheat Sheet

Array A| Array B| Broadcasting
"(3,)"| "(3,)"| ✅
"(3,)"| "()"| ✅
"(2,3)"| "(3,)"| ✅
"(2,3)"| "(2,1)"| ✅
"(3,1)"| "(1,4)"| ✅
"(2,3,4)"| "(3,4)"| ✅
"(2,3,4)"| "(3,1)"| ✅
"(2,3)"| "(2,)"| ❌
"(3,4)"| "(2,4)"| ❌
"(2,3,4)"| "(2,3)"| ❌

---

Broadcasting in Multiplication

Broadcasting is not limited to addition.

import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print(a * b)

Output:

[[ 10  40  90]
 [ 40 100 180]]

Conceptually:

[1, 2, 3] × [10, 20, 30]
[4, 5, 6] × [10, 20, 30]

---

Broadcasting in Subtraction

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])

print(a - b)

Output:

[[ 9 18 27]
 [39 48 57]]

---

Broadcasting in Division

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([10, 10, 10])

print(a / b)

Output:

[[1. 2. 3.]
 [4. 5. 6.]]

---

Broadcasting and Memory

Broadcasting does not necessarily create a physically duplicated copy of the smaller array.

For example:

a + 10

NumPy conceptually treats "10" as if it were repeated for every element, but it can perform the operation efficiently without actually creating a large array of repeated values.

This is one reason broadcasting is both convenient and efficient.

---

Important Point

Broadcasting does not mean that NumPy can combine any two differently shaped arrays.

For example:

(2, 3)
(2,)

is not compatible.

But:

(2, 3)
(3,)

is compatible.

The important rule is:

«Compare dimensions from right to left. Each pair must either be equal, or one of them must be 1.»

---

Practice Questions

Question 1

What is the output?

import numpy as np

a = np.array([1, 2, 3])
print(a + 10)

---

Question 2

What is the output?

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print(a + b)

---

Question 3

Will broadcasting work?

A → (4, 3)
B → (3,)

Find the resulting shape.

---

Question 4

Will broadcasting work?

A → (4, 3)
B → (4,)

Explain why.

---

Question 5

Will broadcasting work?

A → (3, 1)
B → (1, 5)

If yes, find the result shape.

---

Question 6

Will broadcasting work?

A → (2, 3, 4)
B → (3, 4)

Find the result shape.

---

Question 7

Will broadcasting work?

A → (2, 3, 4)
B → (2, 3)

Explain your answer.

---

Question 8

Predict the output:

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([10, 20, 30, 40])

print(a + b)

---

Quick Revision

Broadcasting rules:

1. Compare shapes from RIGHT → LEFT.

2. Dimensions are compatible if:
   - They are equal, OR
   - One dimension is 1, OR
   - One dimension does not exist.

3. If any pair is incompatible:
   Broadcasting fails.

4. The resulting shape contains the larger
   dimension from each comparison.

Example:

(3, 1)
(1, 4)

Compare:

3 vs 1 → compatible
1 vs 4 → compatible

Result:

(3, 4)

Remember:

Equal dimensions → ✅
One dimension is 1 → ✅
Missing dimension → ✅
Different dimensions → ❌

One-line definition:

«Broadcasting is NumPy's ability to perform operations on arrays with different but compatible shapes by virtually expanding the smaller array.»
