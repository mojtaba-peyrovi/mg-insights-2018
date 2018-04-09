import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sales=pd.read_excel("C:\\Users\\mojiway\\Desktop\\reports to new MD\\sales2016.xlsx")
#print(sales)
#plt.figure(figsize=(20,20))
#sns.countplot(x='nationality',data=sales,hue='status')
#sns.set_context('poster')
fp = sales.pivot_table(index='month',columns='year',values='revenueTHB',aggfunc=np.sum)
plt.figure(figsize=(20,20))
monthlySale = sns.heatmap(fp,cmap='YlGn',linecolor='white',linewidth=1,annot=True,fmt='g')
monthlySale.set_title('MONTHLY REVENUE PER INSURER(THB)')
#fp2 = sales.pivot_table(index='Insurer',columns='year',values='revenueTHB',aggfunc=np.sum)
#salesInsurer = sns.heatmap(fp2,cmap='YlGn',linecolor='white',linewidth=1,annot=True,fmt='g')
#salesInsurer.set_title('MONTHLY SALES PER INSURER(THB)')
#df = pd.read_excel("C:\\Users\\mojiway\\Desktop\\reports to new MD\\visits-Jan-Feb-Mar-2018.xlsx")
#fp3 = df.pivot_table(index='day',columns='month',values='Page Views',aggfunc=np.sum,fill_value=0)
#fp3.columns = [
 # 'January',
 # 'February',
 # 'March'
#]
#plt.figure(figsize=(20,20))
#visits = sns.heatmap(fp3,cmap='YlGn',linecolor='white',linewidth=1,annot=True,fmt='g')
#visits.set_title("Visits per day")
#website=pd.read_excel("C:\\Users\\mojiway\\Desktop\\reports to new MD\\visit-revenue-Jan-Feb-Mar-2018.xlsx",sheetname='website-view-lead-sale')
#print(website)
#sns.jointplot(x='website leads',y='website sale',data=website,kind='kde')
#plt.figure(figsize=(80,30))
#sns.set_style("whitegrid")
#g = sns.lmplot(x='website leads',y='website sale',data=website,palette="hot")
plt.show()
