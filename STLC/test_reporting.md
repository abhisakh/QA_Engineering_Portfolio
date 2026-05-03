> 📋 [Home Task](https://masterschool.notion.site/Homework-environment-setup-test-execution-test-reporting-2a56bf0bf46c49448753c7a2b4618fe6) &nbsp;|&nbsp; 🌐 [Open MarketMate App](https://grocerymate.masterschool.com/)

---

<p align="center">
  <a href="https://grocerymate.masterschool.com/auth">
    <img src="https://github.com/user-attachments/assets/0461d1cd-3a18-4dda-b6a1-2781c17703b2" width="600"/>
  </a>
</p>

---

<a id="table"></a>
## 📖 Table of Contents
- [Test Case => <mark>  1. Product Rating System</mark>  => <mark>1. Use Case Testing</mark>](#test1_1)
- [Test Case => <mark>  1. Product Rating System</mark>  => <mark>10. Error Guessing</mark>](#test1_10)
- [Test Case => <mark>  1. Product Rating System</mark>  => <mark> 3. Boundary Value Analysis</mark>](#test1_3)
- [Test Case => <mark> 2. Age Verification for Alcoholic Products</mark> => <mark>1. Use Case Testing</mark>](#test2_1)
- [Test Case => <mark> 2. Age Verification for Alcoholic Products</mark> => <mark>2. Boundary Value Analysis (BVA)</mark>](#test2_2)
- [Test Case => <mark> 2. Age Verification for Alcoholic Products</mark> => <mark>3. Error Guessing</mark>](#test2_3)
- [Test Case => <mark> 3. Shipping Cost Changes</mark> => <mark>1. Boundary Value Analysis (BVA)</mark>](#test3_1)
- [Test Case => <mark> 3. Shipping Cost Changes</mark> => <mark>5. Use Case Testing</mark>](#test3_5)
- [Test Case => <mark> 3. Shipping Cost Changes</mark> => <mark>2. Boundary Value Analysis (BVA)</mark>](#test3_2)
  - [Bug-001](#bug001)
  - [Bug-002](#bug002)
  - [Bug-003](#bug003)
- 

---

# 🧾 Test Report – MarketMate New Features

---
<a id ="test1_1"></a>
## Test Case => <mark>  1. Product Rating System</mark>  => <mark>1. Use Case Testing</mark>
<-- [Back](#table)
## Scenario 1: Valid Product Rating Submission

As a registered user who purchased a product(Loose Pears), I can successfully submit a rating and review. But I did not provided any comment

| Step# | Action                          | Expected outcome              | OK/NOK | URL                | Link to issue |
| ----- | ------------------------------- | ----------------------------- | ------ | ------------------ | ------------- |
| 1     | Go to webshop homepage          | Login portal is displayed     | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 2     | Log in with valid credentials(username:abhisakh_3 password: Abhi123)   | User is logged in             | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 3     | Navigate to Shop                | Date of birth page appeared   | OK     | [/auth](https://grocerymate.masterschool.com/store)|               |
| 4     | Enter valid date of birth(30.11.2000)       | Confirm button activated      | OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 5     | Click on Confirm                | Date of birth page disappeared| OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 6     | Click on a purchased product image(Loose Pears)    | Product detail page opens | OK   | [/product/123](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990)|      |
| 7a    | Select 4-star rating            | Rating is selected            |        |                    |               |
| 7b    | Enter "Good quality product"    | Text is accepted              |        |                    |               |
| 8     | Click send                      | Review is saved and displayed | OK     |                    |               |


| Image 1 | Image 2 |
| :---: | :---: |
| <img width="1118" alt="Screenshot 1" src="https://github.com/user-attachments/assets/855e2a61-0e4f-4cd2-a37e-37da10a0d1c4" /> | <img width="1118" alt="Screenshot 2" src="https://github.com/user-attachments/assets/d5b9c279-a8ed-449c-a52c-ea0cc59d8a76" /> |

---
<a id ="test1_10"></a>
## Test Case => <mark>  1. Product Rating System</mark>  => <mark>10. Error Guessing</mark>
<-- [Back](#table)
## Scenario 2: More 500 Character Submission During the Comment Editing
As a registered and logged-in user who purchased a product, I can edit a review and post more than 500 character.

| Step# | Action                          | Expected outcome              | OK/NOK | URL                | Link to issue |
| ----- | ------------------------------- | ----------------------------- | ------ | ------------------ | ------------- |
| 1     | Go to webshop homepage          | Login portal is displayed     | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 2     | Log in with valid credentials   | User is logged in             | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 3     | Navigate to Shop                | Date of birth page appeared   | OK     | [/auth](https://grocerymate.masterschool.com/store)|               |
| 4     | Enter valid date of birth       | Confirm button activated      | OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 5     | Click on Confirm                | Date of birth page disappeared| OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 6     | Click on a purchased product image(Loose Pears)    | Product detail page opens | OK   | [/product/123](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990)|      |
| 7a    | Select my earlier rating username = abhisakh_3    |             |        |                    |               |
| 7b    | Click on the three dots which is located at the upper right corner   | Text is accepted              |        |                    |               |
| 7c     | Pick the edit option            | Review panel will be displayed | OK     |                    |               |
| 7d     | Insert 1000 character           | Text is accepted   | NOK     |                    |               |
| 7e     |Click save changes           | Review posted | OK     |                    |     Bug-001           |


| Screenshot A | Screenshot B |
| :---: | :---: |
| <img width="500" src="https://github.com/user-attachments/assets/8caa8825-2462-40d3-95dd-f9a234c3e7c7" /> | <img width="500" src="https://github.com/user-attachments/assets/60166eed-b15f-4ae8-a80f-76a20288f3a8" /> |
| <img width="500" src="https://github.com/user-attachments/assets/92c1d48d-fb3a-4d44-9d3a-3cf3d1cc3f4b" /> | |


---
<a id ="test1_3"></a>
## Test Case => <mark>  1. Product Rating System</mark>  => <mark> 3. Boundary Value Analysis</mark>
<-- [Back](#table)
## Scenario 3: Invalid Product Rating Submission

As a registered and logged-in user who purchased a product, I can not submit a review without rating.

| Step | Action                          | Expected outcome              | OK/NOK | URL                | Link to issue |
| ----- | ------------------------------- | ----------------------------- | ------ | ------------------ | ------------- |
| 1     | Go to webshop homepage          | Login portal is displayed     | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 2     | Log in with valid credentials   | User is logged in             | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 3     | Navigate to Shop                | Date of birth page appeared   | OK     | [/auth](https://grocerymate.masterschool.com/store)|               |
| 4     | Enter valid date of birth       | Confirm button activated      | OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 5     | Click on Confirm                | Date of birth page disappeared| OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 6     | Click on a purchased product image(Loose Pears)    | Product detail page opens | OK   | [/product/123](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990)|      |
| 7a    | Don't select any star           |           |        |                    |               |
| 7b    | Enter "Good quality product"    | Text is accepted              |        |                    |               |
| 8     | Click send                      | "Invalid input for the field rating" | OK     |                    |               |

<img width="650" height=auto alt="Screenshot 2026-04-29 at 18 09 04" src="https://github.com/user-attachments/assets/48dfa340-4057-4955-b091-6497f230eedc" />

---

<a id ="test2_1"></a>

## Test Case => <mark> 2. Age Verification for Alcoholic Products</mark> => <mark>1. Use Case Testing</mark>
<-- [Back](#table)
## Scenario 4: Age Verification Modal Appears After Login

As a registered user, I should see an age verification modal immediately after logging into the system.

| Step | Action                                                                 | Expected outcome                             | OK/NOK | URL         | Link to issue |
| ----- | ---------------------------------------------------------------------- | -------------------------------------------- | ------ | ----------- | ------------- |
| 1     | Go to webshop homepage                                                 | Login portal is displayed                    | OK     | [/auth (https://grocerymate.masterschool.com/auth)   |               |
| 2     | Log in with valid credentials (username: abhisakh_3 password: Abhi123) | User is logged in                            | OK     | [/auth](https://grocerymate.masterschool.com/auth)   |               |
| 3     | System redirects after login                                           | Age verification modal appears automatically | OK     | [/store](https://grocerymate.masterschool.com/store) |               |


---

<a id ="test2_2"></a>

## Test Case => <mark> 2. Age Verification for Alcoholic Products</mark> => <mark>2. Boundary Value Analysis (BVA)</mark>
<-- [Back](#table)
## Scenario 5: Verify Access for User Exactly 18 Years Old
As a user who is exactly 18 years old, I should be granted access after completing age verification.

| Step  | Action                                                                 | Expected outcome               | OK/NOK | URL                                                          | Link to issue |
| ----- | ---------------------------------------------------------------------- | ------------------------------ | ------ | ------------------------------------------------------------ | ------------- |
| 1     | Go to webshop homepage                                                 | Login portal is displayed      | OK     | [/auth](https://grocerymate.masterschool.com/auth)           |               |
| 2     | Log in with valid credentials (username: abhisakh_3 password: Abhi123) | User is logged in              | OK     | [/auth](https://grocerymate.masterschool.com/auth)           |               |
| 3     | Age verification modal appears                                         | DOB input field is displayed   | OK     | [/store](https://grocerymate.masterschool.com/store)         |               |
| 4     | Enter DOB = 03.05.2018                                          | Confirm button becomes active  | OK     | [/store](https://grocerymate.masterschool.com/store)         |               |
| 5     | Click on Confirm                                                       | Modal disappears               | OK     | [/store](https://grocerymate.masterschool.com/store)         |               |
| 6     | Navigate to Alcoholic category                                         | Alcoholic products are visible | OK     | [/store/alcohol](https://grocerymate.masterschool.com/store) |               |

---

<a id ="test2_3"></a>
## Test Case => <mark> 2. Age Verification for Alcoholic Products</mark> => <mark>3. Error Guessing</mark>
<-- [Back](#table)
## Scenario 6: Submit Empty Date of Birth Input
As a user, I should not be able to proceed without entering a valid date of birth.

| Step | Action                                                                 | Expected outcome                                            | OK/NOK  | URL                                                  | Link to issue |
| ----- | ---------------------------------------------------------------------- | ----------------------------------------------------------- | ------- | ---------------------------------------------------- | ------------- |
| 1     | Go to webshop homepage                                                 | Login portal is displayed                                   | OK      | [/auth](https://grocerymate.masterschool.com/auth)   |               |
| 2     | Log in with valid credentials (username: abhisakh_3 password: Abhi123) | User is logged in                                           | OK      | [/auth](https://grocerymate.masterschool.com/auth)   |               |
| 3     | Age verification modal appears                                         | DOB input field is displayed                                | OK      | [/store](https://grocerymate.masterschool.com/store) |               |
| 4     | Leave DOB field empty                                                  | System should prevent submission and show validation error  | **NOK** | [/store](https://grocerymate.masterschool.com/store) | [BUG-002]     |
| 5     | Click on Confirm                                                       | User is redirected and shown message: "You are underage..." | **NOK** | [/store](https://grocerymate.masterschool.com/store) | [BUG-002]     |


---

<a id ="test3_1"></a>
## Test Case => <mark> 3. Shipping Cost Changes</mark> => <mark>1. Boundary Value Analysis (BVA)</mark>
<-- [Back](#table)
## Scenario 7: Verify Shipping Cost at Threshold Boundary (20€)

Registered user should be charged shipping when cart total is exactly at the threshold value.

### Test Data Used:
Kale (Fresh Vegetables) = 1€ each
Quantity used: 20 units → Total = 20€

| Step# | Action                                                                 | Expected outcome          | OK/NOK | URL                                                  | Link to issue |
| ----- | ---------------------------------------------------------------------- | ------------------------- | ------ | ---------------------------------------------------- | ------------- |
| 1     | Go to webshop homepage                                                 | Login portal is displayed | OK     | [/auth](https://grocerymate.masterschool.com/auth)   |               |
| 2     | Log in with valid credentials (username: abhisakh_3 password: Abhi123) | User is logged in         | OK     | [/auth](https://grocerymate.masterschool.com/auth)   |               |
| 3     | Navigate to Shop                                                       | Shop page is displayed    | OK     | [/store](https://grocerymate.masterschool.com/store) |               |
| 4     | Enter valid date of birth (29.04.2000)                                 | DOB input accepted        | OK     | [/store](https://grocerymate.masterschool.com/store) |               |
| 5     | Click Confirm                                                          | DOB modal disappears      | OK     | [/store](https://grocerymate.masterschool.com/store) |               |
| 6     | Add 20 units of Kale (1€ each)                                         | Cart total = 20€          | OK     | [/cart](https://grocerymate.masterschool.com/cart)   |               |
| 7     | View cart summary                                                      | Shipping fee = 5€ applied | OK     | [/cart](https://grocerymate.masterschool.com/cart)   |               |


---

<a id ="test3_5"></a>
## Test Case => <mark> 3. Shipping Cost Changes</mark> => <mark>5. Use Case Testing</mark>
<-- [Back](#table)
## Scenario 8: Shipment Fee Dynamically Updated (Shipping fee not updated when product value decreases below threshold 20 euro after adding producr value more than 20 euro.)

Registered user who want to purchase a product can bypass the shipping fees.

| Step# | Action                          | Expected outcome              | OK/NOK | URL                | Link to issue |
| ----- | ------------------------------- | ----------------------------- | ------ | ------------------ | ------------- |
| 1     | Go to webshop homepage          | Login portal is displayed     | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 2     | Log in with valid credentials (username: abhisakh_3 password: Abhi123)   | User is logged in             | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 3     | Navigate to Shop                | Date of birth page appeared   | OK     | [/auth](https://grocerymate.masterschool.com/store)|               |
| 4     | Enter valid date of birth(29.04.2010)       | Confirm button activated      | OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 5     | Click on Confirm                | Date of birth page disappeared| OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 6     | Navigate to Oranges             |                               | OK     |                                                     |      |
| 7     | Check the quantity, make it 1   | quantity field is 1           | OK     |                    |               |
| 8     | Click Add to cart               | Messege displayed "Item successfully added"|        |                    |               |
| 9     | Click on the Basket             | Redirected to checkout page | OK     | [/checkout](https://grocerymate.masterschool.com/checkout)|               |
| 10    | Check the shipment fee          | Should display 5 euro       | OK     | [/checkout](https://grocerymate.masterschool.com/checkout)|               |
| 11    | Increase the quantity to 23     | Shipment fee 0 euro         | OK     | [/checkout](https://grocerymate.masterschool.com/checkout)|               |
| 12    | Decrease the quantity to 10     | Shipment fee remains 0 euro | NOK     | [/checkout](https://grocerymate.masterschool.com/checkout)| Bug-003      |


| Screenshot 1 | Screenshot 2 |
| :---: | :---: |
| <img width="500" src="https://github.com/user-attachments/assets/a5925e3b-e131-4887-ab5d-df36ed5bcbd2" /> | <img width="500" src="https://github.com/user-attachments/assets/e102ce92-3be6-4caa-a5b7-61b93efb868e" /> |
| **Screenshot 3** | |
| <img width="500" src="https://github.com/user-attachments/assets/0ea0f04e-bc59-489e-b09e-91a723f72402" /> | |

---

<a id ="test3_2"></a>
## Test Case => <mark> 3. Shipping Cost Changes</mark> => <mark>2. Boundary Value Analysis (BVA)</mark>
<-- [Back](#table)

## Scenario 9: Verify Free Shipping Just Above Threshold (20.1€)
Registered user should receive free shipping when cart total exceeds 20€.

### Test Data Used:
Kale = 1€ × 19 units = 19€
Large Flat Mushrooms = 1.1€ × 1 unit = 1.1€
Total = 20.1€

| Step# | Action                                                                 | Expected outcome                          | OK/NOK | URL                                                  | Link to issue |
| ----- | ---------------------------------------------------------------------- | ----------------------------------------- | ------ | ---------------------------------------------------- | ------------- |
| 1     | Go to webshop homepage                                                 | Login portal is displayed                 | OK     | [/auth](https://grocerymate.masterschool.com/auth)   |               |
| 2     | Log in with valid credentials (username: abhisakh_3 password: Abhi123) | User is logged in                         | OK     | [/auth](https://grocerymate.masterschool.com/auth)   |               |
| 3     | Navigate to Shop                                                       | Shop page is displayed                    | OK     | [/store](https://grocerymate.masterschool.com/store) |               |
| 4     | Enter valid date of birth (29.04.2000)                                 | DOB input accepted                        | OK     | [/store](https://grocerymate.masterschool.com/store) |               |
| 5     | Click Confirm                                                          | DOB modal disappears                      | OK     | [/store](https://grocerymate.masterschool.com/store) |               |
| 6     | Add 19 Kale (1€ each)                                                  | Cart subtotal = 19€                       | OK     | [/cart](https://grocerymate.masterschool.com/cart)   |               |
| 7     | Add 1 Large Flat Mushroom (1.1€)                                       | Cart subtotal = 20.1€                     | OK     | [/cart](https://grocerymate.masterschool.com/cart)   |               |
| 8     | View cart summary                                                      | Shipping fee = 0€ (free shipping applied) | OK     | [/cart](https://grocerymate.masterschool.com/cart)   |               |




---

# TEST REPORT SECTION

---

<a id ="bug001"></a>
## 🐞 BUG-001: Review edit allows more than 500 characters
<-- [Back](#table)

---

**Title**

User is able to submit review with more than 500 characters during edit

---

**Priority**

High

---

**Reporter**

Abhisakh Sarma

---

**Date**

29 April 2026

---

**Environment**

TEST

---

**Application**

[MarketMate Webshop](https://grocerymate.masterschool.com/auth)

---

**Page**

Product Details Page (Review Section)
Example: https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990

---

**Browser / Operating System**

Chrome 123 / MacOS

---

**Repro Steps**
Navigate to webshop and log in with valid credentials
Navigate to a previously purchased product
Locate an existing review created by the user
Click on the three-dot menu (⋮) on the review
Select Edit option
Enter a review text exceeding 500 characters (e.g., 1000 characters)
Click on Save Changes

**Expected Result**

The system should prevent submission of review text exceeding 500 characters and display a validation error message.

**Actual Result**

The system accepts and saves the review with more than 500 characters without any validation or error.

---

Screenshots / Attachments

(Attach screenshot showing long review successfully saved)

| Screenshot A | Screenshot B |
| :---: | :---: |
| <img width="500" src="https://github.com/user-attachments/assets/8caa8825-2462-40d3-95dd-f9a234c3e7c7" /> | <img width="500" src="https://github.com/user-attachments/assets/60166eed-b15f-4ae8-a80f-76a20288f3a8" /> |
| <img width="500" src="https://github.com/user-attachments/assets/92c1d48d-fb3a-4d44-9d3a-3cf3d1cc3f4b" /> | |


---

**Additional Information**
* Validation appears to be applied during initial review creation but not enforced during editing
* This leads to inconsistent behavior between create vs edit flows
* May cause:
* ** UI issues (overflow text)
* ** Performance concerns (very large inputs)
* Likely missing frontend or backend validation on update API

---
<a id ="bug002"></a>
## 🐞 BUG-002 System allows empty DOB submission 
<-- [Back](#table)

-- 

Title: System allows empty DOB submission and treats user as underage

Description:
When the Date of Birth field is left empty and the user clicks "Confirm", the system does not block the action. Instead, it redirects the user and displays an "underage" message.

Expected Behavior:

DOB field should be mandatory
User should not proceed without entering a valid date
Proper validation error should be displayed

Actual Behavior:

Empty DOB is accepted
User is treated as underage
Redirect happens

Severity: High
Priority: High

---


<a id ="bug003"></a>
## 🐞 Bug Report
### BUG-003: Shipping cost not updated after cart value drops below threshold
<-- [Back](#table)

---

**Title**

Shipping cost remains 0€ after cart total drops below 20€

---

**Priority**

High

---

**Reporter**

Abhisakh Sarma

---

**Date**

29 April 2026

---

**Environment**

TEST

---

**Application**

[MarketMate Webshop](https://grocerymate.masterschool.com/auth)

---

**Page**

/[checkout](https://grocerymate.masterschool.com/checkout)

---

**Browser / Operating System**

Chrome 123 / MacOS

---

**Repro Steps**
1. Open webshop
2. Add product worth 25€ to cart
3. Navigate to cart
4. Verify shipping cost is 0€
5. Remove product to reduce total below 20€
6. Observe shipping cost

---

**Expected Result**

Shipping cost should update to 5€ when cart total drops below 20€

---

**Actual Result**

Shipping cost remains 0€ even after total drops below 20€

---

**Screenshots / Attachments**

| Screenshot 1 | Screenshot 2 |
| :---: | :---: |
| <img width="500" src="https://github.com/user-attachments/assets/a5925e3b-e131-4887-ab5d-df36ed5bcbd2" /> | <img width="500" src="https://github.com/user-attachments/assets/e102ce92-3be6-4caa-a5b7-61b93efb868e" /> |
| **Screenshot 3** | |
| <img width="500" src="https://github.com/user-attachments/assets/0ea0f04e-bc59-489e-b09e-91a723f72402" /> | |

---

**Additional Information**
* Shipping cart value resets only after page refresh.

