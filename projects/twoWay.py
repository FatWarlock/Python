import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.stats as ss
import matplotlib.pyplot as plt

veri = pd.read_excel("C:/Users/fatih/Desktop/veri.xlsx")

model = ols("Dakika ~C(BardakTürü)+C(Masa)+(BardakTürü):C(Masa)",data=veri).fit()
hatalar = model.resid
print("""**********************************************""")
fig = sm.qqplot(hatalar,line="s")
plt.show()
print("""**********************************************""")
print(model.summary())
print("""**********************************************""")
anova = sm.stats.anova_lm(model,type=2)
print(anova)
print("""**********************************************""")
etkilerMasa =ss.multicomp.pairwise_tukeyhsd(endog=veri["Dakika"],groups=veri["Masa"])
print(etkilerMasa)

print("""**********************************************""")
etkilerBardak =ss.multicomp.pairwise_tukeyhsd(endog=veri["Dakika"],groups=veri["BardakTürü"])
print(etkilerBardak)

print("""**********************************************""")
etkiler  =ss.multicomp.pairwise_tukeyhsd(endog=veri["Dakika"],groups=veri["BardakTürü"]+" "+veri["Masa"])
print(etkiler)


print("""**********************************************""")

masalar=veri.groupby("Masa")["Dakika"].mean()
print(masalar)


print("""**********************************************""")

bardaklar=veri.groupby("BardakTürü")["Dakika"].mean()
print(bardaklar)


print("""**********************************************""")

bardaklarGenel =veri.groupby(["BardakTürü","Masa"]).mean()
print(bardaklarGenel)

print("""**********************************************""")

masalarGenel=veri.groupby(["Masa","BardakTürü"]).mean()
print(masalarGenel) 