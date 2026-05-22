## [Task 2](https://masterschool.notion.site/Homework-XPath-6c4229bd4ea1461a941010bbeb35365f)

Go the https://grocerymate.masterschool.com

1. Write the XPath for the highlighted icon/button given in the image below.

<img width="1897" height="101" alt="image" src="https://github.com/user-attachments/assets/e65f91fe-f6ee-44cc-90dd-682d7ed3bd07" />


```python
//div[@class='social-icon-cont']/div[1]
```

2. Now, open https://grocerymate.masterschool.com/auth.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c/cc352327-dcdd-485b-af91-87626247bbd9/image.png)

Write the XPath of all input fields (Email address, Password), sign in button, Create a new account link, and Go to Home link
#### email
```python
//input[@type='email']
```

#### password
```python
/input[@type='password']
```

#### Sign In Button
```python
//button[@type='submit']
```

#### Create a new account link
```python
//a[@class='switch-link']
```

#### Go to Home
```python
//a[@class='home-link']
```

3. Now, on the same link as in Part 2, click on Create a new account, you will see the following UI:

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c/1e193326-679b-4739-96c8-36af2dc7c43e/image.png)

Write the XPath for all input fields (Full Name, Email address, Password), Sign Up button.
#### Full Name
```python
//input[@placeholder='Full Name']
```

#### Email address,
```python
//input[@type='email']
```

#### Password
```python
//input[@type='password']
```

#### Sign Up button
```python
/button[@type='submit']
```


4. Go to https://grocerymate.masterschool.com/store, you will see the following UI:

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c/29c80beb-9478-4c6c-9ed0-104fe48162ad/image.png)

#### Write the XPath of **Confirm** button which you can see in the Modal.
    ```python
    //div[@class='modal-content']//button[text()='Confirm']
    ```

5. Go to the **Shop** page, write the XPath for:
    1. Quantity input of Oranges
    ```python
    //p[text()='Oranges']/ancestor::div[@class='card']//input[@class='quantity']
    ````

    2. Add to cart button for Oranges
    ```python
    //p[text()='Oranges']/ancestor::div[@class='card']//button[text()='Add to Cart']
    ```

    3. Add to wish list for Oranges
    ```python
    //p[text()='Oranges']/ancestor::div[@class='card']//button[contains(., '❤')]
    ```




