> 📋 [Home Task](https://masterschool.notion.site/Home-work-Test-Plan-Test-Case-Design-212fc8ca6c014f7d9ca860ba5477f83e) &nbsp;|&nbsp; 🌐 [Open GroceryMate App](https://grocerymate.masterschool.com/)

---

<p align="center">
  <a href="https://grocerymate.masterschool.com/auth">
    <img src="https://github.com/user-attachments/assets/0461d1cd-3a18-4dda-b6a1-2781c17703b2" width="600"/>
  </a>
</p>

---

# 🧪 Test Case Design – MarketMate New Features

## 1. Product Rating System

### Test Design Techniques
  - Boundary Value Analysis (BVA)
  - Equivalence Partitioning (EP)
  - Use Case Testing
  - Error Guessing

### Test Cases
**1. Use Case Testing**
Test Case:
  - Verify that a user can submit a rating after purchasing a product
Input:
  - Logged-in user with completed purchase submits 4⭐ rating
Expected Outcome:
  - Rating is successfully saved and displayed
    
**2. Equivalence Partitioning**
Test Case: 
  - Verify rating submission for valid rating values (1–5)
Input:
  - Ratings = 1, 3, 5
Expected Outcome:
  - Ratings are accepted and displayed correctly

**3. Boundary Value Analysis**
Test Case: 
  - Verify rating outside valid range
Input:
  - Rating = 0 or 6
Expected Outcome:
  - Error message displayed, rating not accepted
    
**4. Use Case Testing**
Test Case: 
  - Verify user can edit an existing rating
Input:
  - Change rating from 3⭐ to 5⭐
Expected Outcome:
  - Rating is updated successfully
    
**5. Use Case Testing**
Test Case: 
  - Verify user can delete their rating
Input:
  - Delete submitted review
Expected Outcome:
  - Rating is removed from product page
    
**6. Equivalence Partitioning**
Test Case: 
  - Verify feedback text within valid length
Input:
  - Feedback = 100 characters
Expected Outcome:
  - Feedback is accepted and displayed
    
**7. Boundary Value Analysis**
Test Case: 
  - Verify feedback exceeding maximum length (500 chars)
Input:
  - Feedback = 501 characters
Expected Outcome:
  - Error message displayed

**8. Error Guessing**
Test Case: 
  - Submit rating without purchase
Input:
  - User without purchase attempts rating
Expected Outcome:
  - Rating is rejected

**9. Error Guessing**
Test Case: 
  - Submit empty rating and empty feedback
Input:
  - No rating, no text
Expected Outcome:
  - Error message displayed

2. Age Verification for Alcoholic Products
Test Design Techniques

Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing, Security Testing

Test Cases
Use Case Testing
Test Case: Verify modal appears when accessing alcoholic products
Input: Navigate to alcoholic category
Expected Outcome: Age verification modal is displayed
Boundary Value Analysis
Test Case: Verify access for user exactly 18 years old
Input: DOB = Today - 18 years
Expected Outcome: Access granted
Boundary Value Analysis
Test Case: Verify access for user just below 18
Input: DOB = Today - 18 years + 1 day
Expected Outcome: Access denied with error message
Equivalence Partitioning
Test Case: Verify access for valid adult users (>18)
Input: DOB = Today - 25 years
Expected Outcome: Access granted
Equivalence Partitioning
Test Case: Verify access for underage users (<18)
Input: DOB = Today - 16 years
Expected Outcome: Access denied
Error Guessing
Test Case: Submit empty input
Input: No DOB entered
Expected Outcome: Error message displayed
Error Guessing
Test Case: Enter invalid date format
Input: "32-13-2020"
Expected Outcome: Validation error
Security Testing
Test Case: Attempt to bypass modal
Input: Direct URL access or skip input
Expected Outcome: Access still restricted
Use Case Testing
Test Case: Verify session-based persistence
Input: Verify once, navigate away and return
Expected Outcome: Modal does not reappear during session
3. Shipping Cost Changes
Test Design Techniques

Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing, Error Guessing

Test Cases
Boundary Value Analysis
Test Case: Verify shipping cost at threshold (20€)
Input: Cart total = 20€
Expected Outcome: Shipping fee = 5€
Boundary Value Analysis
Test Case: Verify shipping cost just above threshold
Input: Cart total = 20.01€
Expected Outcome: Free shipping applied
Boundary Value Analysis
Test Case: Verify shipping cost just below threshold
Input: Cart total = 19.99€
Expected Outcome: Shipping fee = 5€
Equivalence Partitioning
Test Case: Verify free shipping for valid high-value orders
Input: Cart total = 50€
Expected Outcome: Shipping = 0€
Use Case Testing
Test Case: Verify dynamic update when adding products
Input: Increase cart from 15€ → 25€
Expected Outcome: Shipping changes from 5€ → 0€
Use Case Testing
Test Case: Verify dynamic update when removing products
Input: Decrease cart from 25€ → 15€
Expected Outcome: Shipping changes from 0€ → 5€
Error Guessing
Test Case: Apply discount affecting threshold
Input: Cart = 25€, apply discount → 18€
Expected Outcome: Shipping = 5€
Use Case Testing
Test Case: Verify message for free shipping threshold
Input: Cart total = 15€
Expected Outcome: Message shows "Add 5€ more for free shipping"
Error Guessing
Test Case: Empty cart scenario
Input: No products in cart
Expected Outcome: No shipping cost displayed
