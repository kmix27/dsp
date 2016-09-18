[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)


InterpolateSample(df, 6.0)
mean 74278.7075312
std 93946.9299635
median 51226.4544789
skewness 4.94992024443
pearson skewness 0.736125801914
cdf[mean] 0.66000587956687196


InterpolateSample(df,7.0)
mean 124267.397222
std 559608.501374
median 51226.4544789
skewness 11.6036902675
pearson skewness 0.391564509277
cdf[mean] 0.8565630665207663

when the upper value is changed from 6 to 7 we see an increase in moment based skewness,  which makes sense as we are stretching and increasing the values on the upper end of the income distribution.  we can see that reflected in the percentiles at which the mean falls within the cdf, at 6, the mean falls at the 66th percentile,  at 7, the 85th percentile.  The pearson skewness drops, and significantly when going from 6 to 7,  this is due to how much that change effects the standard deviation,  increasing it by 5x.  We can conclude from this examination that the pearson skewness is not an effective summary statistic for this situation and we would be better served by calculating specifics from the data to provide context. 

see 6-1-Skewness.ipynb for code