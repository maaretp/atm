# Assignment

**An ATM allows a daily withdraw limit of $300**

You can’t ask the stakeholder any questions about the requirement, what tests would you run to understand the requirement better and test this functionality?

You can run the ATM by 'python3 atm_main.py'

One sample test is available to run with 'pytest test_my_atm.py'


Notes:
* Sizes of bills 10, 20, 50, 100
* Bills may run out of the ATM
* Available cash on the account
* This ATM or all ATMs withdraw limit
* Account withdrawal limit may be separate
* Rounding: 299.99 is not 300

# Clarify the Requirement Itself

What does “daily” mean?
* Calendar day (midnight–midnight)?
* 24-hour rolling window?
* Based on: ATM’s local time? Bank server time? Customer’s home branch time zone?
* What happens during daylight saving changes?
* What about leap days?
* What does “$300” mean?

Exactly $300 allowed?
* Is it cumulative per day?
* Is it per transaction or total across multiple transactions?
* Is the limit inclusive or exclusive?

# Boundary Value Testing

Classic boundary checks: + precision to 10, 1,.01 and .001 differences 
* $299 → should succeed
* $300 → should succeed?
* $301 → should fail
* $0 → valid?
* Negative amount → rejected?
* Very large amount → rejected
* $300 in one transaction vs. $100 + $100 + $100 vs. $200 + $100 + $1 (should fail on the last $1)

# Accumulation logic

Does the system correctly track multiple withdrawals?
* A transaction fails halfway?
* Cash is not dispensed?
* Network disconnect occurs after approval?
* Are reversed transactions correctly subtracted from the daily total?

# Accounts

* Is the limit per: Card? Account? Customer?
* Joint accounts: Do both cardholders share the $300?
* Multiple cards tied to same account: Can each withdraw $300?
* Business vs personal accounts: Different limits

Currency & Denominations
What if ATM dispenses only $20 bills?
Is $290 allowed?
Rounding issues?
What about foreign currency ATMs?
Is limit based on converted USD amount?
Exchange rate timing?

# Edge & Failure Scenarios

ATM offline mode:
How does it know daily total?
System restart during transaction?
Concurrent withdrawals at two ATMs?
Fraud hold placed mid-day?
Limit changed mid-day by bank?

# Security & Abuse Scenarios

Rapid repeated attempts to probe the limit
Attempt to withdraw just below the limit repeatedly
Race conditions (two ATMs at same time)
Manipulation of time (if client-side logic exists)

# Usability & Messaging

Clear error message when limit exceeded?
Does it show remaining daily amount?
Is message misleading (e.g., says insufficient funds instead of limit exceeded)?

# Audit & Compliance

Is limit enforcement logged?
Are attempts above limit logged?
Is it configurable?
Does it meet regulatory requirements?

# Non-Functional Considerations

Performance impact of limit checks
Reliability of tracking logic
Scalability across thousands of ATMs
Data consistency in distributed systems
