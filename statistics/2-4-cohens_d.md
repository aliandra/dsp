[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Exercise 2.4  Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?  

```python
import nsfg
from math import sqrt


def cohensD(group1, group2):
    '''
    Compares the standardised difference between two means.
    d = (mean(group1) - mean(group2)) / pooled standard deviation
    '''
    n1, n2 = len(group1), len(group2)
    var1, var2 = group1.var(), group2.var()
    pooled_var = ((n1 * var1) + (n2 * var2)) / (n1 + n2)
    pooled_sd = sqrt(pooled_var)
    d = (group1.mean() - group2.mean()) / pooled_sd
    return d


# read pregnancy data
preg = nsfg.ReadFemPreg()

# select pregnancies which resulted in live births
live = preg[preg.outcome == 1]

# partition live births into two groups, first babies and others
first = live[live.birthord == 1]
other = live[live.birthord != 1]

# calculate the mean total weight of first babies and other babies
print "The average weight for all babies is %.3f lbs," % \
    live.totalwgt_lb.mean()
print "with a standard deviation of %.3f lbs\n" % live.totalwgt_lb.std()
print "The average weight of first babies is %.3f lbs" % \
    first.totalwgt_lb.mean()
print "The average weight of other babies is %.3f lbs" % \
    other.totalwgt_lb.mean()
diff = first.totalwgt_lb.mean() - other.totalwgt_lb.mean()
print "The difference in mean weight is %.3f lbs\n" % diff

# calculate cohen's d
d = cohensD(first.totalwgt_lb, other.totalwgt_lb)
print "Cohen's d, the difference in means is %.3f standard deviations" \
    % d
```

Running the above we get:  

```
The average weight for all babies is 7.266 lbs,
with a standard deviation of 1.408 lbs

The average weight of first babies is 7.201 lbs
The average weight of other babies is 7.326 lbs
The difference in mean weight is -0.125 lbs

Cohen's d, the difference in means is -0.089 standard deviations
```

The difference in mean weight between first babies and other babies is approximately 0.125 lbs, which represents about 1.7% of the mean weight for all live births. This is not a large difference, and by calculating Cohen's D we see that the standard difference between means is only -0.089, with the mean weight for first babies slightly less than other babies. The calculated Cohen's D's for pregnancy length was also relatively small. The difference in mean pregnancy lengths was only 0.029 standard deviations apart, with the mean length of pregnancy slightly longer for first babies. 