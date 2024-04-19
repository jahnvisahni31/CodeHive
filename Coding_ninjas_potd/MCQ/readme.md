### Question 1:
**Question:** N1, N2, N3, N4, and N5 are the natural numbers. What is the probability that the product of these numbers ends in an odd number that is not a multiple of 5? (Amdocs)

**Answer:**
- Product of 5 numbers to be odd, firstly, the last digit should not be even and the last digit should not be 5.
- Probability of any unit place = 1/10
- All the numbers should end with 1, 3, 7, and 9 i.e., 4 numbers.
- Probability of number P(N1) = 4/10.
- Probability of number P(N2) = 4/10.
- Probability of number P(N3) = 4/10.
- Probability of number P(N4) = 4/10.
- P(N1,N2,N3,N4, and N5) = P(N1)P(N2)P(N3)P(N4)P(N5) = (0.4)^5

### Question 2:
**Question:** What will be the output of the following code?
```python
s = "abcdef"
print(s[2:])
```
Answer: cdef

### Question 3:
**Question:** What is the output of the following code?
```java
public class Solution {
    public void display() {
        int x = 10;
    }

    public static void main(String args[]) {
        System.out.println(x);
    }
}
```
Answer:
Compile time error

### Question 4:
**Question:** An aeroplane covers a certain distance at a speed of 240 kmph in 5 hours. To cover the same distance in 1 and 2/3 hours, it must travel at a speed of

Answer:
Distance = (240 x 5) = 1200 km.
Speed = Distance/Time
Speed = 1200/(5/3) km/hr. [We can write 1 hours as 5/3 hours]
Required speed = (1200 x 3)/5 km/hr = 720 km/hr.

### Question 5:
**Question:** What will be the output of the following code?
```python
import collections

b = collections.Counter([2, 2, 3, 4, 4, 4])
b.most_common(1)
a = collections.Counter([2, 2, 3, 3, 3, 4])
b = collections.Counter([2, 2, 3, 4, 4])

a | b
```
Answer: Counter({2: 2, 3: 3, 4: 2})
