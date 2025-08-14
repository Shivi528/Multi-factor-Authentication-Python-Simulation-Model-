Multi-factor authentication is a common security measure as it helps validate identity
of users before gaining access and is known to be one of the most trusted and reliable
way of protecting user account. Some examples of multi-factor authentication include
user phones or biometric verification (Joseph Williamson, 2021).

3.1.1 Implementation of MFA in Canva’s context
Implementation of multi-factor authentication ensures users complete additional
verification before logging in. In the case of credential stuffing, attackers are not able to
obtain access to usernames and passwords. Ultimately multi-factor authentication
prevents any form of unauthorised access unless the adversary has access to the
second authentication factor. This helps incredibly to reduce the success of a
credential-based attack (Joseph Williamson, 2021).

To illustrate the effectiveness of MFA in mitigating credential stuffing attacks, simulated
experimental data was conducted. The Python simulation model shows the behaviour
of user login behaviour based on two scenarios whether a user adds MFA and a user
without MFA. This simulation highlights the success rate of a credential attack as well
as the failed attempts in the case of an adversary trying to gain access to the database.

<img width="940" height="513" alt="image" src="https://github.com/user-attachments/assets/98eac464-86b0-4cbf-9d36-895cca3b795b" />

The simulation is designed to run 500 login attempts based on the parameters that are set:
•	Password(primarily) success rate: 15% likelihood of successful login attempt through username and password
•	OTP(MFA) success rate: 10% if MFA was implemented (additional level of security)

![Uploading image.png…]()
