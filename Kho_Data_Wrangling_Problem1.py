import pandas as pd
a={'Student': ['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
b={'Student': ['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
c={'Student': ['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
d={'Student': ['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
Math=pd.DataFrame(a,columns=['Student','Math'])
Elec=pd.DataFrame(b,columns=['Student','Electronics'])
Geas=pd.DataFrame(c,columns=['Student','GEAS'])
Esat=pd.DataFrame(d,columns=['Student','ESAT'])
merge1=pd.merge(Math, Elec,how='outer', on='Student')
merge2=pd.merge(Geas, Esat,how='outer', on='Student')
merge=pd.merge(merge1,merge2, how='outer',on='Student')
melted1 = pd.melt(merge, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
lastMelt = melted1.rename(columns = {'variable' : 'Subject', 'Value' : 'Grades'})