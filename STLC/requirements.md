
# 🛒 GroceryMate — Feature Requirements

> 📋 [Home Task](https://masterschool.notion.site/Home-work-Requirements-08555225537749d6bbd8530cbdef6128) &nbsp;|&nbsp; 🌐 [Open GroceryMate App](https://grocerymate.masterschool.com/)

---

<p align="center">
  <a href="https://grocerymate.masterschool.com/auth">
    <img src="https://github.com/user-attachments/assets/0461d1cd-3a18-4dda-b6a1-2781c17703b2" width="600"/>
  </a>
</p>

---

## App Overview

The webshop includes the following core functionalities:

| Feature | Link |
|---|---|
| Register & Login | [/auth](https://grocerymate.masterschool.com/auth) |
| Search, Sort & Browse Categories | [/store](https://grocerymate.masterschool.com/store) |
| Add Products to Favorites | [/store/favs](https://grocerymate.masterschool.com/store/favs) |
| Add Products to Basket | [/store](https://grocerymate.masterschool.com/store) |
| Checkout (Billing, Shipping, Payment) | [/checkout](https://grocerymate.masterschool.com/checkout) |

---

## New Features

---

### 1. Product Rating System

**Vague Requirement**
> Users should be able to rate products with a 5-star system and have the option to add written feedback.

---

#### Questions

1. Can users rate a product more than once?
2. Are ratings restricted to users who purchased the product?
3. What are the minimum and maximum lengths for written feedback?
4. Can users edit or delete their ratings?
5. How is the average rating calculated and displayed?
6. Is there any moderation for inappropriate content?

---

#### Detailed Requirements

1. Users can rate a product using a 1 to 5 star system.
2. Each user can submit only one rating per product.
3. Users are allowed to rate a product only after purchasing it.
4. Users can edit or delete their rating at any time.
5. Users may optionally provide written feedback.
6. Written feedback must: 
&nbsp;&nbsp; Have a minimum length of 1 character
&nbsp;&nbsp; Have a maximum length of 500 characters
7. The average rating is displayed with one decimal precision (e.g., 4.3 ⭐).
8. Ratings are displayed publicly on the product page.

---

### 2. Age Verification for Alcoholic Products

**Vague Requirement**
> Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

---

#### Questions

1. Should age verification persist across sessions or require repeated input?
2. What happens if the user enters an invalid or underage value?
3. Can users bypass the verification modal?
4. What input format should be used (date of birth vs numeric age)?
5. Is user age data stored, and how is privacy handled?
6. What happens if the modal is closed without input?

---

#### Detailed Requirements

1. When a user navigates to the alcoholic products category, an age verification modal must appear.
2. Users must enter their date of birth (format: DD-MM-YYYY).
3. The system validates that the user is at least 18 years old.
4. If the user is under 18:<br>
&nbsp;&nbsp; Access to alcoholic products is denied.<br>
&nbsp;&nbsp; The following message is displayed: <mark>You are underage and cannot view alcohol products.<mark> <br>
&nbsp;&nbsp;&nbsp;&nbsp; If valid: <mark>Alchoholic products are allowed.<mark> <br>
5. Verification status is stored for the duration of the session only.<br>
&nbsp;&nbsp; After session expiration, verification must be repeated.
6. The modal cannot be bypassed without valid input.

---

### 3. Shipping Cost Changes

**Vague Requirement**
> Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

---

#### Questions

1. What is the exact threshold for free shipping?
2. Does the threshold include discounts?
3. Are shipping costs location-dependent?
4. How is shipping cost displayed to the user?
5. Is the user informed how much more is needed for free shipping?
6. What happens when cart value changes dynamically?

---

#### Detailed Requirements

1. Free shipping applies to orders with a total value greater than 20€.
2. Orders with a total value equal to or below 20€ incur a 5€ shipping fee.
3. The order total includes discounts when calculating shipping eligibility.
4. Shipping cost must be:
&nbsp;&nbsp; - - Dynamically updated whenever the cart changes  <br>
&nbsp;&nbsp; - - Clearly displayed in both cart and checkout pages  <br>
&nbsp;&nbsp; - - Users should see a message:  <br>
&nbsp;&nbsp&nbsp;&nbsp; - - "Add X€ more to qualify for free shipping"  <br>
