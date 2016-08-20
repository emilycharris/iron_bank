# iron_bank
_This assignment was completed as part of my training at The Iron Yard._

###Objective:
_Create the start of a simulated banking portal._

###Description

_In a world where financial data is available by the click of a few buttons security is of incredible importance. Your task on this assignment is to create a simulated online banking portal that gives users a sense of security. After all, if you build a banking portal that isn't secure, nobody will use it._

**Learning Objectives**

After completing this part of the assignment, you should be able to:
- Utlize all User registration and authentication views we have covered in class so far.
- Create Class Based list and detail pages that are only visible to the currently logged in user.

**Requirements**
- A user that is not logged into your application should see nothing but the ability to login or create an account. Upon creating an account and/or logging in they should be greeted with their account details page. This will include the following:
 - A large display of the user's current bank account balance.
 - A list of transactions from the last 30 days.
 - The ability to click on the transactions to see a transaction detail.
 - The ability to create (through the admin page for part 1) a Transaction instance that is of type Debit or Credit.

**Transaction**

In financial processing a common way to store or resolve balances is to have the total just be a running total of all positive (deposit) transactions plus the negative (Debits) transactions. For example if I had a register that looks like:

\+ 100 (deposit)

\- 90 (withdraw/debit)

\+ 32 (deposit)

\-----

= 42 (balance)

You should not be storing the balance on any particular model - instead I would be calculating it on the fly and displaying kind of a naive version of it.

So a transaction should know how much it was processed for and if it was a deposit or a debit. Of course it should also know which bank account it belonged to.

Do not allow a user to perform a withdraw transaction if it would result in them having insufficient funds.

**Accounts**

When a user signs up for an account, they should have an account number that is unique to them. How you choose to handle the concept of an account number is up to you - but it could be anything from a separate model that is related to the user - all the way to the user's pk. It's up to you. This account number will be important for transferring funds. (do not fall into the trap of requiring an account number to be a long number just to seem official)

**Criteria**

If I am in any way able to breech another user's data as a logged in or not logged in user - you will be in trouble. ;)

**Transferring Funds**

For a user to transfer funds to another account they will require knowledge of the other bank account #. This will be assumed to have been shared outside of the application, so don't try to build anything that allows a user to search for another bank account - that would be BAD!!!! But given that two users have shared bank account numbers, one of those users should be able to transfer money from their own account into another users account. Do NOT allow a user to transfer funds if it would result in them having insufficient funds.

