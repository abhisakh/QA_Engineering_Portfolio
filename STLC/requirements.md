
# [Home Task](https://masterschool.notion.site/Home-work-Requirements-08555225537749d6bbd8530cbdef6128)

## 👉 [Open grocerymate App](https://grocerymate.masterschool.com/)

<p align="center">
  <a href="https://grocerymate.masterschool.com/auth">
    <img src="https://github.com/user-attachments/assets/0461d1cd-3a18-4dda-b6a1-2781c17703b2" width="600"/>
  </a>
</p>

---

The webshop has the following basic functionalities:

- [Register and login functionality](https://grocerymate.masterschool.com/auth)
- [Searching for products, sorting on price, categories of products](https://grocerymate.masterschool.com/store)
- [Add products to favorites](https://grocerymate.masterschool.com/store/favs)
- [Add products to basket](https://grocerymate.masterschool.com/store)
- [Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)](https://grocerymate.masterschool.com/checkout)

## New features

### **1. Product Rating System**
**Vague Requirement:**  
**Requirement:**  
Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions:**  
--- **1.** Can a user rate a product multiple times, or only once per account?  
--- **2.** Are ratings allowed only after purchasing the product, or for any user?  
--- **3.** What is the maximum/minimum length for written feedback?  
--- **4.** Can users edit or delete their rating after submitting it?  
--- **5.** How is the average rating calculated and displayed (rounding, decimals)?  
--- **6.** Are inappropriate or offensive reviews moderated or filtered?  

**Detailed Requirement:**  
--- **1.** Users can rate products from 1 to 5 stars.    
--- **2.** Each user can submit only one rating per product.  
--- **3.** Users can optionally add written feedback (e.g., 1–500 characters).    
--- **4.** Users can edit or delete their review.  
--- **5.** Average rating is displayed with one decimal (e.g., 4.3 ⭐).  
--- **6.** Reviews are moderated for inappropriate content.  

### **2. Age Verification for Alcoholic Products**  
**Vague Requirement:**  
**Requirement:**   
Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions:**  
--- **1.** What happens if the user enters an age below 18?.   
--- **2.** Is the age verification required every time or only once per session/account?  
--- **3.** Can users bypass the modal by refreshing or using a direct link?  
--- **4.** What input format is accepted (number only, date of birth, etc.)?  
--- **5.** Is the entered age stored, and if so, how is user privacy handled?  
--- **6.** What happens if the user closes the modal without entering data?    

**Detailed Requirement:**  
--- **1.** A modal appears when accessing alcoholic products.  
--- **2.** Users must enter their age (numeric input).  
--- **3.** Access is granted only if age ≥ 18.  
--- **4.** Users under 18 are blocked with a message.  
--- **5.** Verification persists during the session.  
--- **6.** Modal cannot be bypassed via direct URL access.  

### **3. Shipping Cost Changes**  
**Vague Requirement:**  
**Requirement:**  
Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions:**  
--- **1.** What is the exact threshold for free shipping?  
--- **2.** Does the threshold include taxes and discounts or only product price?  
--- **3.** How is shipping displayed in the cart and checkout?  
--- **4.** What happens if the order total changes after applying a discount?  
--- **5.** Are shipping costs the same for all locations?  
--- **6.** Is the user clearly informed how much more is needed for free shipping?  

**Detailed Requirement:**  
--- **1.** Free shipping applies for orders above €X (e.g., €50).  
--- **2.** Orders below €X incur a fixed shipping fee (e.g., €5).  
--- **3.** Shipping cost is dynamically updated in the cart.  
--- **4.** Discounts affect the total used for shipping calculation.  
--- **5.** A message shows how much more is needed for free shipping.  
--- **6.** Shipping cost is clearly displayed before checkout.  




