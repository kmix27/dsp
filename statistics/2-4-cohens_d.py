import first
import nsfg
import thinkstats2
from math import sqrt

df = nsfg.ReadFemPreg()

def CohenEffectSize(group1, group2):
	# computes the effect size between two groups, expressed as
	# fraction of std deviation
	diffInMean = group1.mean() -group2.mean()
	variance1 = group1.var()
	variance2 = group2.var()
	n1, n2 = len(group1), len(group2)

	pooledVariance = (n1 * variance1 + n2 * variance2) / (n1 + n2)
	d = diffInMean / sqrt(pooledVariance)
	return d

def meanComparison(group1,group2):
	# computes the diffrence in pregnancy length between 
	# two groups expressed as fraction of the average pregnancy length
	meanPrgLngth = df.totalwgt_lb.mean()
	diffInMean = group1.mean() - group2.mean()
	meanToLngth = diffInMean/meanPrgLngth
	return meanToLngth


first = df[df['birthord'] == 1]
other = df[df['birthord'] > 1]

effectSizeWgt = CohenEffectSize(first.totalwgt_lb,other.totalwgt_lb)
meanWgt = df.totalwgt_lb.mean()
firstMeanWgt = first.totalwgt_lb.mean()
otherMeanwgt = other.totalwgt_lb.mean()
diffMeanWeight = meanComparison(first.totalwgt_lb,other.totalwgt_lb)
effectSizeLngth = CohenEffectSize(first.prglngth,other.prglngth)
wgtStd = (df.totalwgt_lb.std())
fracMeanDiff = diffMeanWeight / meanWgt

print('mean weight accross all pregnancies(lbs):', meanWgt)
print('firstborns mean wight(lbs):', firstMeanWgt)
print('non-firstborn mean weight(lbs):', otherMeanwgt)
print('diffrence in mean weight first to non first(lbs):',diffMeanWeight)
print('cohens d, first born to non firstborn(std deviations):', effectSizeWgt)