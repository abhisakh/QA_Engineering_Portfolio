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
| 1     | Go to webshop homepage          | Homepage is displayed         | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 2     | Log in with valid credentials   | User is logged in             | OK     | [/auth](https://grocerymate.masterschool.com/auth)|               |
| 3     | Navigate to Shop                | Date of birth page appeared   | OK     | [/auth](https://grocerymate.masterschool.com/store)|               |
| 4     | Enter valid date of birth       | Confirm button activated      | OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 5     | Click on Confirm                | Date of birth page disappeared| OK     | [/store](https://grocerymate.masterschool.com/store)|             |
| 6     | Click to a purchased product image    | Product detail page opens | OK     | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f|      |
| 7a    | Select 4-star rating            | Rating is selected            |        |                    |               |
| 7b    | Enter "Good quality product"    | Text is accepted              |        |                    |               |
| 6     | Click send                      | Review is saved and displayed | OK     |                    |               |
