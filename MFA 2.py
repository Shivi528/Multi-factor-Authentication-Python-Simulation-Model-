import random #used to generate random numbers
import matplotlib.pyplot as plt #library access used to create visualisations to help create the bar graph figure

# Default Settings for the simulation
numberoflogin_attempts = 500 #Number of simulated login attempts
passwordsuccessrate = 0.15 # Success rate for guessing password (15%) to help model the liklihood of a successful password guess by an attacker
otpsuccessrate = 0.1 #success of OPT if password is guessed but needs (MFA)

# Tracking successful login counter
login_withoutmfa = 0
login_withmfa = 0

#Tracking failed login counter
failed_withoutMFA = 0
failed_withMFA = 0

# Simulation loop to help measure login attempts
for attempt in range(numberoflogin_attempts):
    if random.random() < passwordsuccessrate:
        login_withoutmfa += 1
        if random.random() < otpsuccessrate:
            login_withmfa += 1
        else:
          failed_withMFA += 1
    else:
        failed_withoutMFA +=1
    

# Calculating success rates as percentages
success_rate_without_mfa = (login_withoutmfa / numberoflogin_attempts) * 100
success_rate_with_mfa = (login_withmfa / numberoflogin_attempts) * 100

# Visualisation of the bar chart to measure success rates with and without MFA
success_rates = [success_rate_without_mfa, success_rate_with_mfa] #comparison variables
labels = ['Without MFA', 'With MFA']
plt.bar(labels, success_rates, color=['red', 'blue'])
plt.title('Success Rate of Credential Stuffing Attacks With and Without MFA')
plt.ylabel('Success Rate (%)')
plt.ylim(0, max(success_rates) * 1.1)
plt.show()

# Print results of the success rate with and without MFA
print(f"Success rate without MFA: {success_rate_without_mfa:.2f}%")
print(f"Success rate with MFA: {success_rate_with_mfa:.2f}%")
print(f"Failed attempts without MFA: {failed_withoutMFA}")
print(f"Failed attempts with MFA: {failed_withMFA}")
