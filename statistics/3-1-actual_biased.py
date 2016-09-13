import chap01soln
import thinkstats2
import thinkplot
resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp['numkdhh'],label='actual pmf')


def BiasedPmf(pmf, label=''):
	"""
	returns new pmf object whose result is the distribution that would be seen if the 
	values were oversampled in proportion to their values.  Input is a pmf object with an optional
	label for visualization purposes.

	args:
		pmf - Pmf object
		label - string descripiton of bias introduced
	Returns:
		Pmf object
	"""
	new_pmf = pmf.Copy(label=label)
	for x, p in pmf.Items():
		new_pmf.Mult(x, x)
	new_pmf.Normalize()
	return new_pmf

# creat biased pmf from child respondant perspective
biasedPmf = BiasPmf(pmf,label='biased pmf from child respondant perspective')

# creat step function visualization of actual v. biased distributions
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biasedPmf])
thinkplot.Show(xlabel ='num of children',
                ylabel = 'probability')

actualMean = pmf.Mean()
biasedMean = biasedPmf.Mean()

print('Actual mean child frequency:', actualMean)
print('Biased mean child frequency:', biasedMean)
