[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Exercise 3.1 Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample. Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household. Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household. Plot the actual and biased distributions, and compute their means.

```python
import chap01soln
import thinkstats2
import thinkplot

fem = chap01soln.ReadFemResp()

# Construct the actual distribution
pmf_actual = thinkstats2.Pmf(fem.numkdhh, label='actual')
print "The mean of the actual distribution is %.3f.\n" % \
    pmf_actual.Mean()


# Compute the bias distribution
def biasPmf(pmf, label=''):
    """
    Returns the biased pmf
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf


pmf_bias = biasPmf(pmf_actual, label='biased')
print "The mean of the biased distribution is %.3f." % pmf_bias.Mean()

# Plot the distributions
thinkplot.PrePlot(2, cols=2)
thinkplot.Pmf(pmf_actual, label='Actual')
thinkplot.Config(xlabel="Number of Children", ylabel="Probability")

thinkplot.PrePlot(2)
thinkplot.SubPlot(2)
thinkplot.Pmf(pmf_bias, label="Biased")
thinkplot.Show(xlabel="Number of Children")
```

Running the above we get

```
The mean of the actual distribution is 1.024.

The mean of the biased distribution is 2.404.
```
![Q2pmf](img/Q2pmf.png)