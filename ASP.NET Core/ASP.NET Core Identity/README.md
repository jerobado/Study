# ASP.NET Core Identity
- is an API that supports user interface (UI) login functionality
- manages uers, passwords, profile data, roles, claims, token, email confirmation, and more

# Benefits
- users can create an account with the login information stored in Identiy or they can use an external login provide like _Facebook_, _Google_, _Microsoft Account_ and _Twitter_.

# Glossary

**Authentication**
- the process of creating users and letting them log in to your app
- the process of determining _who you are_

**Authorization**
- customizing the experience and controlloing what user's can do, based on the current logged-in user
- the process of determining _what you're allowed to do_

**claim**
- is a single piece of information about a principal
- it consists of a _claim type_ and a an optional _value_

**cookie**
- is a small piece of text that's sent back and fort between the browser and your app along with each request, consisting of a name and a value

**principal**
- is the current user, implemented as `ClaimsPrincipal` class
- it contains a collection of `Claims` that describe the user

**Two-factor authentication (2FA)**
- is where you require an extra piece of information to sign in, in addition to a password
- e.g., sending a code to a user's phone by SMS, or using a mobile app to generate a code
