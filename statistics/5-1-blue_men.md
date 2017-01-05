[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Exercise 5.1  In the BRFSS (see Section 5.4), the distribution of
heights is roughly normal with parameters m = 178 cm and sd = 7.7 cm
for men, and m = 163 cm and sd = 7.3 cm for women. In order to join
Blue Man Group, you have to be male between 5ft10 and 6ft1. What
percentage of the U.S. male population is in this range? Hint: use
scipy.stats.norm.cdf

```python
import scipy.stats

# convert heights to cm
males5_10 = (5 * 12 + 10) * 2.54
males6_1 = (6 * 12 + 1) * 2.54

# calculate percentiles
lower = scipy.stats.norm.cdf(males5_10, loc=178, scale=7.7)
upper = scipy.stats.norm.cdf(males6_1, loc=178, scale=7.7)

# print out percent of males in Blue Man Group range
blueman = (upper - lower) * 100
print "The percentage of males between 5ft10in and 6ft1in is %.2f" % \
    blueman
```

Running the above, we get

```
The percentage of males between 5ft10in and 6ft1in is 34.27
```