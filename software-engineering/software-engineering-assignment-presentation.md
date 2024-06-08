
# Building a Payment Processor - Software Requirements Specification (SRS)
drafted and submitted by Akash Shanmugaraj, 22z255
for 19Z405 - Software Engineering


## 1. Preface 
    
A Payment Processor is almost being used by the entire population, especially right after the boom of the e-commerce industry. Online Shopping giants like Amazon and Flipkart, being the major shareholders in the E-Commerce industry paved the road for the future of Payment Processors. In the more recents years, not only the Consumer Market, but also the Banking Sector in general has witnessed a ginormous increase in the amount of Contact-Less Payments or Unified Payments Interface (UPI). 

But a Payment Processor is not only limited to UPI payments. In general a payment processor includes all forms of payment like Credit and Debit Cards, Net Banking, Digital wallets, Buy now, pay later, etc.
    
Some applications that are currently being used as payment processors are Stripe, Paytm, Razor Pay, Juspay. All of them have an pricing model that works on a Percentage Service fee per transaction.
    
Early mode of Digital Payments were acutally made using the Credit Cards, after which came Electronic Fund Transfer. Later, during the early 2000s, after the development of Secure Sockets Layer, we had Bank Transfer. In the last decade we witnessed applications that were made for Peer-to-Peer Transactions like Paytm, Google Pay etc. 
Further into the future we witness payments on the blockchain becoming more and more common. 
    

## 2. Glossary
    
Payment Gateway: A service which allows users to make payments via a variety of payment methods

Payment Service Provider (PSP): Service that makes sure that the money is transferred from the remitter's bank account to the beneficiary's bank account

Issuer Bank: The bank associated with the remitter

Accquiring Bank: The bank associated with the beneficiary

Card Association: Intermediaries between the consumer and merchant, like Visa, MasterCard, RuPay, etc that provide secure and standardized infrastructure.

Payment Card Industry data Security Standard (PCI DSS): Globally accepted security standard used to prevent credit card frauds.

3D Secure: Secure protocol defined by Visa and used by other processrs. consists of three domains

ISO-8583: Electronic Fund Transfer (EFT) switch messaging format for payment processing

## 3. User requirements definition

### Functional Requirements
Here are some functional requirements that might define the payment processor:
1. Support for a variety of payment methods (Debit and Credit cards, Netbanking, Digital Wallets, etc)
2. Support for handling international currencies 
3. Support for application developers to extend their exisiting platform with given payment processor for accepting payment
4. Online dashboard for Businesses and Store Owners to monitor the sales, volume of transactions and different / preferred payment methods used by his/her customers
5. Support for different types of payment models
### Non-Functional Requirements
Here are some non-functional requirements that one might expect for using a payment processor
1. Ease of use, being able to quickly navigate into preffered payment system
2. Extremely Low / Zero payment failure rate
3. Payment being quickly reverted back (credited back) to the remitter's bank account in case of failure
4. Secure transaction platform and portal to ensure that the remitter's personal information does not get into bad actor's hands.
5. High Consistency and High Availability

## 4. System architecture

The proposed application requries certain functions:
1. Collecting payment information from the user interface.
2. Validating and encrypting payment information (following PCI DSS compliance).
3. Converting payment information to a standard format (e.g., ISO 8583).
4. Communicating with the payment processor using APIs.
5. Managing communication with different entities (banks, card associations).
6. Handling payment confirmations and responses.
7. Potentially integrating with fraud detection services.

## 5. System requirements specification

This section details the functional and non-functional requirements of the payment processor system, along with the system architecture that provides the foundation for meeting these requirements.

**Functional Requirements:**

* **Support for Various Payment Methods:**
    * The system shall support a variety of payment methods including debit cards, credit cards, net banking, digital wallets (e.g., Apple Pay, Google Pay), and other popular payment options based on market research.
    * The system shall be adaptable to integrate future payment methods as they emerge.
* **International Currency Handling:**
    * The system shall support processing transactions in multiple currencies.
    * The system shall display currency options and conversion rates clearly to users during the checkout process.
* **Application Developer Integration:**
    * The system shall provide well-documented APIs (Application Programming Interfaces) to allow developers to easily integrate the payment processor with their existing platforms.
    * APIs shall offer functionalities for initiating payments, capturing transaction details, and receiving payment confirmations.
* **Business Dashboard:**
    * The system shall provide a secure online dashboard for businesses and store owners.
    * The dashboard shall display real-time and historical sales data, transaction volume, and preferred payment methods used by customers.
    * The dashboard shall offer reporting tools for generating detailed sales reports.
* **Support for Payment Models:**
    * The system shall support various payment models including one-time payments, recurring payments (subscriptions), and buy now, pay later options. 

**Non-Functional Requirements:**

* **Ease of Use:**
    * The user interface for both customers and businesses shall be intuitive and user-friendly.
    * The payment process shall be streamlined with minimal steps for a smooth user experience.
* **Payment Failure Rate:**
    * The system shall strive for an extremely low payment failure rate, aiming for a target below 0.1%.
    * The system shall implement robust error handling and retry mechanisms to minimize failures.
* **Payment Reversal:**
    * In case of transaction failures, the system shall automatically initiate a reversal process, crediting the refunded amount back to the customer's account within 24 hours.
    * The system shall provide clear communication to users about the reversal process and timelines.
* **Security:**
    * The system shall comply with industry-standard security protocols like PCI DSS to ensure the protection of sensitive user data (payment information, personal details).
    * The system shall implement secure communication channels (HTTPS) for all data transmission.
    * The system shall employ robust access controls and user authentication mechanisms to prevent unauthorized access.
* **High Consistency and Availability:**
    * The system shall maintain high consistency of data, ensuring accuracy and integrity of transaction records.
    * The system shall strive for high availability, minimizing downtime and ensuring service accessibility for users. 

**System Architecture:**

A high-level system architecture diagram (refer to Section 6) will be included to illustrate the distribution of functionalities across different system components and how they interact to achieve the defined requirements. This diagram will depict the following components:

* User Interface (UI): Provides user interaction points for customers and businesses.
* Payment Gateway Application: Handles core payment processing functionalities, interacting with other components securely.
* Payment Processor: Authorizes and settles payments, communicating with issuing and acquiring banks.
* External Systems: Issuing banks, acquiring banks, and potentially card associations for routing and network rules.
* Data Storage: Securely stores transaction data, user information (if allowed), and other relevant details.
 

## 6. System models 

This section represents interaction between various components of the system.

Here’s a simplified breakdown of the process:

1. User enters their card details on the seller’s website or on a payment gateway’s UI (if the seller’s website is not PCI DSS compliant).
2. The card details are sent securely (over SSL) to the merchant’s application.
3. The merchant’s application securely transmits the details to the payment gateway.
4. The payment gateway converts the message format into ISO 8583 standard.
5. The message is then sent to the payment processor.
6. The payment processor communicates with the issuing bank to verify the card details and authorize the payment.
7. Once authorized, the payment processor sends a confirmation message back to the payment gateway.
8. The payment gateway sends a confirmation message to the merchant’s application.
9. The merchant’s application then displays a confirmation message to the user.

## 7. System evolution 

This section represents the part of the system where a developer can anticipate changes.

1. Support for New Payment Methods with Modular Design and Pluggable Payment Processors 

2. Securing the platform against evolving Security Threats through frequent Security Updates and Regular Security Audits

## 8. Appendices 
    
This section involves a separate description for hardware configuration, database descriptions and so on.

**Hardware Configuration:**

Servers: Minimum 4 cores, 3.0 GHz, 16 GB or more RAM, 1 TB of Solid State Drive storage
Network infrastructure: atleast 1 GBPS of internet with 

**Database Descriptions:**

We can use a relational database with a supporting Entity Relationship Diagram. The database system must be partitioned for the current date and also for all payment methods (seperate payment for Card, Netbanking, etc)


## 9. Index 

Term | Page Number
------- | --------
Accquiring Bank | 1
Application Developer Integration | 2
Business Dashboard | 3
Card Association | 1
Currency Handling | 1
Data Storage | 3
Ease of Use | 3
Electronic Fund Transfer (EFT) | 1
High Availability | 2
High Consistency | 2
International Currency Handling | 1
ISO-8583 | 1
Issuing Bank | 3
Online Dashboard | 2
Payment Failure Rate | 3
Payment Gateway Application | 3
Payment Model | 2
Payment Processor | 1
Payment Reversal | 3
PCI DSS | 2
Secure Sockets Layer (SSL) | 4
3D Secure | 1
