> 📋 [Home Task](https://masterschool.notion.site/Homework-environment-setup-test-execution-test-reporting-2a56bf0bf46c49448753c7a2b4618fe6) &nbsp;|&nbsp; 🌐 [Open MarketMate App](https://grocerymate.masterschool.com/)

---

<p align="center">
  <a href="https://grocerymate.masterschool.com/auth">
    <img src="https://github.com/user-attachments/assets/0461d1cd-3a18-4dda-b6a1-2781c17703b2" width="600"/>
  </a>
</p>

---


# 🧾 Test Report – Webshop New Features

## Scenario 1: Valid Product Rating Submission

As a logged-in user who purchased a product, I can successfully submit a rating and review.

| Step# | Action                          | Expected outcome              | OK/NOK | URL                | Link to issue |
| ----- | ------------------------------- | ----------------------------- | ------ | ------------------ | ------------- |
| 1     | Go to webshop homepage          | Homepage is displayed         | OK     | /store             |               |
| 2     | Log in with valid credentials   | User is logged in             | OK     | /auth              |               |
| 3     | Navigate to a purchased product | Product detail page opens     | OK     | /store/product/123 |               |
| 4a    | Select 4-star rating            | Rating is selected            |        |                    |               |
| 4b    | Enter "Good quality product"    | Text is accepted              |        |                    |               |
| 5     | Submit review                   | Review is saved and displayed | OK     |                    |               |
