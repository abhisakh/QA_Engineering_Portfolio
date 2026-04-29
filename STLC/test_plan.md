> 📋 [Home Task](https://masterschool.notion.site/Home-work-Test-Plan-Test-Case-Design-212fc8ca6c014f7d9ca860ba5477f83e) &nbsp;|&nbsp; 🌐 [Open MarketMate App](https://grocerymate.masterschool.com/)

---

<p align="center">
  <a href="https://grocerymate.masterschool.com/auth">
    <img src="https://github.com/user-attachments/assets/0461d1cd-3a18-4dda-b6a1-2781c17703b2" width="600"/>
  </a>
</p>

---

# Test Plan for Webshop New Features

---

## 1. Analyze the Product

### Objective
The objective of this webshop is to provide users with a seamless online shopping experience, including product browsing, purchasing, and interaction features.
The new features aim to: <br>
  - Enhance user engagement (Product Rating System) <br>
  - Ensure legal compliance (Age Verification for alcoholic products) <br>
  - Improve pricing transparency (Shipping Cost logic) <br>

### User Base
The system is intended for: <br>
  - General online shoppers <br>
  - Registered users purchasing products <br>
  - Users aged 18+ (for alcoholic products)  <br>
  - Returning users interacting with reviews and cart features  <br>

### Hardware and Software Specifications
**Hardware Requirements:**  <br>
  - Devices: Desktop, laptop, tablet, smartphone <br>
  - Minimum: 4GB RAM, modern processor  <br>

**Software Requirements:**
  - Operating Systems: Windows, macOS, Android, iOS  <br>
  - Browsers: Chrome, Firefox, Safari, Edge  <br>
  - Dependencies:  <br>
    - Payment gateway integration  <br>
    - Session management system  <br>
    - Backend APIs for products, ratings, and checkout  <br>

### Product Functionality
The webshop allows users to:
  - Register and log in
  - Browse and search products
  - Add products to favorites and basket
  - Complete checkout (billing, shipping, payment)
  - Rate and review products
  - Access restricted products based on age
  - View dynamic shipping costs

## 2. Design the Test Strategy

### Scope of Testing

**In Scope:**
  - Product Rating System
  - Age Verification for Alcoholic Products
  - Shipping Cost Calculation
  - Regression testing of:
    - Cart functionality
    - Checkout flow

**Out of Scope:**
  - Internal database validation not visible via UI
  - Third-party payment gateway internal logic
  - External integrations not impacted by new features
    
### Types of Testing
  - Functional Testing – Core feature validation
  - Regression Testing – Ensure no existing functionality breaks
  - Boundary Value Testing – Age limits, price thresholds
  - Usability Testing – Modal behavior, rating UI
  - Security Testing – Age verification bypass, session handling
  - Exploratory Testing – выявление unexpected issues

### Risks and Issues
  - Age verification bypass (legal risk) => Mitigation: Strong validation + negative testing
  - Incorrect shipping calculation (financial impact) => Mitigation: Boundary and dynamic cart testing
  - Unmoderated user content (reputation risk) => Mitigation: Future moderation recommendation
  - Session-based logic failures => Mitigation: Session expiration and persistence testing

### Test Logistics
  - Test Manager – Oversees planning and execution
  - QA Engineer(s) – Functional, regression, exploratory testing
  - Developer(s) – Bug fixing and support
  - End Users – UAT validation
    
## 3. Define Test Objectives

### Objectives

**Functionality:**
  - Verify all new features behave according to requirements
  - Data Validation:
    - Ensure correct handling of:
      - Age input
      - Ratings
      - Price calculations
  - User Experience:
    - Validate usability of:
      - Rating system
      - Age verification modal
      - Shipping feedback messages
  - Security:
    - Prevent:
      - Age restriction bypass
      - Invalid input acceptance
        
**Expected Outcomes**
  - Ratings are correctly created, edited, and displayed
  - Age-restricted content is properly controlled
  - Shipping cost updates accurately based on cart value
  - No critical defects in core purchase flow
    
## 4. Define Test Criteria
### Entry Criteria
  - Requirements document finalized
  - Test environment available
  - Test data prepared
  - 
### Suspension Criteria
  - Critical defects blocking:
    - Checkout
    - Product access
  - Test environment unavailable
    
### Exit Criteria
  - ≥ 95% test cases executed
  - ≥ 90% pass rate
  - No Critical (Severity 1) defects open
  - No High (Severity 2) defects impacting:
    - Checkout
    - Age verification
  - All major bugs retested and closed
  - UAT sign-off completed
    
## 5. Resource Planning
### Human Resources:
  - QA Engineers
  - Developers
  - Test Manager
  - UAT participants

### Hardware:
  - Desktop and mobile devices

### Software:
  - Browsers (Chrome, Firefox, Safari, Edge)
  - Test management tools (e.g., Jira, TestRail)

### Test Data:
  - User accounts (underage, adult)
  - Products (alcoholic & non-alcoholic)
  - Cart scenarios (below/above 20€)
    
## 6. Plan Test Environment
### Environments:
  - DEV – Development testing
  - TEST – QA validation
  - ACC/UAT – User acceptance
  - PROD – Live environment

### Setup Requirements:
  - Stable backend APIs
  - Session management enabled
  - Test accounts and seeded data
    
## 7. Schedule and Estimation
| Activity | Start Date | End Date | Environment | Responsible | Effort |
| --- | --- | --- | --- | --- | --- |
| Test Planning | 01/05/2026 |	03/05/2026 | All |	Test Manager | 16h |
| Test Case Design	| 04/05/2026 |	08/05/2026 |	TEST |	QA Team |	32h |
| Functional Testing |	09/05/2026 |	15/05/2026 |	TEST |	QA Team |	48h |
| Regression Testing |	16/05/2026 |	18/05/2026 |	TEST |	QA Team |	24h |
| Security Testing |	19/05/2026 |	20/05/2026 |	TEST |	QA Team	| 16h |
| UAT	21/05/2026 |	25/05/2026 |	ACC |	Users |	24h |
| Final Fix & Retest |	26/05/2026 |	28/05/2026 |	TEST |	QA + Dev |	24h |
| Release |	30/05/2026 |	30/05/2026 |	PROD |	DevOps |	8h |

## 8. Test Deliverables
The following deliverables will be produced:
  - Test Plan Document
  - Test Cases & Test Scenarios
  - Test Data Sets
  - Bug/Defect Reports
  - Test Execution Reports
  - Regression Test Suite
  - UAT Sign-off Document
