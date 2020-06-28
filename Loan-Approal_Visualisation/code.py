# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)
#step1
loan_status=data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')
#step2
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar')
plt.xlabel('Property_Area');plt.ylabel('Loan_Status')
plt.xticks(rotation=45)
#step 3
education_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_loan.plot(kind='bar')
plt.xlabel('Education');plt.ylabel('Loan_Status')
plt.xticks(rotation=45)
#step4
graduate=data[data['Education'] == 'Graduate']
graduate.plot(kind="density",label="Graduate")
not_graduate=data[data['Education'] == 'Not Graduate']
not_graduate.plot(kind="density",label="Not Graduate")
#step5
fig,axs=plt.subplots(3,1)
a,b=data["ApplicantIncome"],data['LoanAmount']
axs[0].scatter(a,b)
axs[0].set_title("Applicant Income")
a,b=data['CoapplicantIncome'],data['LoanAmount']
axs[1].scatter(a,b)
axs[1].set_title("Coapplicant Income")
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
a,b=data['TotalIncome'],data['LoanAmount']
axs[2].scatter(a,b)
axs[2].set_title("Total Income")




