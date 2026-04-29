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
Test Case:<br>
  - Verify that a user can submit a rating after purchasing a product<br>
Input:<br>
  - Logged-in user with completed purchase submits 4⭐ rating<br>
Expected Outcome:<br>
  - Rating is successfully saved and displayed<br>
    
**2. Equivalence Partitioning**
Test Case:<br> 
  - Verify rating submission for valid rating values (1–5)<br>
Input:<br>
  - Ratings = 1, 3, 5 <br>
Expected Outcome:<br>
  - Ratings are accepted and displayed correctly<br>

**3. Boundary Value Analysis**
Test Case: <br>
  - Verify rating outside valid range<br>
Input:<br>
  - Rating = 0 or 6 <br>
Expected Outcome:<br>
  - Error message displayed, rating not accepted<br>
    
**4. Use Case Testing**
Test Case: <br>
  - Verify user can edit an existing rating<br>
Input:<br>
  - Change rating from 3⭐ to 5⭐<br>
Expected Outcome:<br>
  - Rating is updated successfully<br>
    
**5. Use Case Testing**
Test Case:<br> 
  - Verify user can delete their rating<br>
Input:<br>
  - Delete submitted review<br>
Expected Outcome:<br>
  - Rating is removed from product page<br>
    
**6. Equivalence Partitioning**
Test Case:<br> 
  - Verify feedback text within valid length<br>
Input:<br>
  - Feedback = 100 characters<br>
Expected Outcome:<br>
  - Feedback is accepted and displayed<br>
    
**7. Boundary Value Analysis**
Test Case: <br>
  - Verify feedback exceeding maximum length (500 chars)<br>
Input:<br>
  - Feedback = 501 characters<br>
Expected Outcome:<br>
  - Error message displayed<br>

**8. Error Guessing**
Test Case: <br>
  - Submit rating without purchase<br>
Input:<br>
  - User without purchase attempts rating<br>
Expected Outcome:<br>
  - Rating is rejected<br>

**9. Error Guessing**
Test Case:<br> 
  - Submit empty rating and empty feedback
Input:<br>
  - No rating, no text
Expected Outcome:<br>
  - Error message displayed

## 2. Age Verification for Alcoholic Products

### Test Design Techniques
  - Boundary Value Analysis (BVA)
  - Equivalence Partitioning (EP)
  - Use Case Testing
  - Error Guessing

### Test Cases
**1. Use Case Testing**
Test Case: <br>
  - Verify modal appears when accessing alcoholic products
Input:<br>
  - Navigate to alcoholic category
Expected Outcome:<br>
  - Age verification modal is displayed
    
**2. Boundary Value Analysis**
Test Case:<br> 
  - Verify access for user exactly 18 years old
Input:<br>
  - DOB = Today - 18 years
Expected Outcome:<br>
  - Access granted
    
**3. Boundary Value Analysis**
Test Case:<br> 
  - Verify access for user just below 18
Input:<br>
  - DOB = Today - 18 years + 1 day
Expected Outcome:<br>
  - Access denied with error message
    
**4. Equivalence Partitioning**
Test Case: <br>
  - Verify access for valid adult users (>18)
Input:<br>
  - DOB = Today - 25 years
Expected Outcome:<br>
  - Access granted
    
**5. Equivalence Partitioning**
Test Case:<br> 
  - Verify access for underage users (<18)
Input:<br>
  - DOB = Today - 16 years
Expected Outcome:<br>
  - Access denied
    
**6. Error Guessing**
Test Case:<br> 
  - Submit empty input
Input:<br>
  - No DOB entered
Expected Outcome:<br>
  - Error message displayed
    
**7. Error Guessing**
Test Case:<br> 
  - Enter invalid date format
Input:<br>
  - "32-13-2020"
Expected Outcome:<br>
  - Validation error
    
**8. Security Testing**
Test Case:<br> 
  - Attempt to bypass modal
Input:<br>
  - Direct URL access or skip input
Expected Outcome:<br>
  - Access still restricted
    
**9. Use Case Testing**
Test Case: <br>
  - Verify session-based persistence
Input:<br>
  - Verify once, navigate away and return
Expected Outcome:<br>
  - Modal does not reappear during session

## 3. Shipping Cost Changes

### Test Design Techniques
  - Boundary Value Analysis (BVA)
  - Equivalence Partitioning (EP)
  - Use Case Testing
  - Error Guessing

### Test Cases
**1. Boundary Value Analysis**
Test Case: <br>
  - Verify shipping cost at threshold (20€)
Input:<br>
  - Cart total = 20€
Expected Outcome:<br>
  - Shipping fee = 5€
    
**2. Boundary Value Analysis**
Test Case:<br>
  - Verify shipping cost just above threshold
Input:<br>
  - Cart total = 20.01€
Expected Outcome:<br>
  - Free shipping applied
    
**3. Boundary Value Analysis**
Test Case: <br>
  - Verify shipping cost just below threshold
Input:<br>
  - Cart total = 19.99€
Expected Outcome:<br>
  - Shipping fee = 5€

**4. Equivalence Partitioning**
Test Case:<br> 
  - Verify free shipping for valid high-value orders
Input:<br>
  - Cart total = 50€
Expected Outcome:<br>
  - Shipping = 0€

**5. Use Case Testing**
Test Case:<br> 
  - Verify dynamic update when adding products
Input:<br>
  - Increase cart from 15€ => 25€
Expected Outcome:<br>
  - Shipping changes from 5€ => 0€

**6. Use Case Testing**
Test Case: <br>
  - Verify dynamic update when removing products
Input:<br>
  - Decrease cart from 25€ → 15€
Expected Outcome:<br>
  - Shipping changes from 0€ → 5€

**7. Error Guessing**
Test Case:<br> 
  - Apply discount affecting threshold
Input:<br>
  - Cart = 25€, apply discount → 18€
Expected Outcome:<br>
  - Shipping = 5€

**8. Use Case Testing**
Test Case:<br> 
  - Verify message for free shipping threshold
Input:<br>
  - Cart total = 15€
Expected Outcome:<br>
  - Message shows "Add 5€ more for free shipping"

**9. Error Guessing**
Test Case: <br>
  - Empty cart scenario
Input:<br>
  - No products in cart
Expected Outcome:<br>
  - No shipping cost displayed


