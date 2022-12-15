<h1 align="center">
 StoreFront Ecommerce
</h1>

<div align="center">

<!-- [![GitHub Workflow Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/ki3-qbt/graph-compiler/actions)
[![docs.rs](https://img.shields.io/badge/docs-passing-brightgreen)](https://github.com/ki3-qbt/graph-compiler/tree/gh-pages) -->
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-javascript](https://img.shields.io/badge/Made%20with-JavaScript-1f425f.svg)](https://www.javascript.com)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://shields.io/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
</div>

## Inspiration

StoreFront is an online ecommerce website where users can buy the most popular apparel items on the market right now. Customers can browse the many goods available, but in order to purchase one, they must first register. Following that, users will receive a verification email and will be able to login in. Furthermore, if they added products to the cart while not signed in, the items will not be lost, and they will be able to view all of the items in the cart once they sign in. Users can also make payments using Paypal or credit/debit cards.

Since COVID-19, the global surge in online buying has caused many e-commerce websites to work on enhancing their user experience in order to attract customers to continue shopping with them. I wanted to be able to build a website that consumers enjoy and combine all of the features seen in well-known companies such as Amazon. Hence, this led to the development of StoreFront.


`

## Technologies
- [`Django`](https://www.djangoproject.com/): Backend framework for setting up website and admin panel

- [`JavaScript`](https://www.javascript.com/): Used for creating orders, approving purchases and sending pop-up alerts

- [`HTML/CSS`](https://www.w3.org/standards/webdesign/htmlcss): Used to create appealing frontend

- [`PostgreSQL`](https://www.postgresql.org/): Stores user information, product variations, orders, payments, reviews

- [`AWS Elastic Beanstalk`](https://aws.amazon.com/elasticbeanstalk/): Platform used for deployment

- [`AWS S3 Buckets`](https://aws.amazon.com/s3/): Stores static and media files


## Getting Started
To run the projects locally and to implement other changes please follow these steps:

1. CD into the directory you want to app in and write:

    `git clone https://github.com/aayush3416/storefront-ecommerce.git`
    
    
2. Install all the packages

    `pip install -r requirements.txt`
  
3. Create a .env file in the root directory. See .env-sample:

    `EMAIL_HOST_USER=`
    
    `EMAIL_HOST_PASSWORD=`
    
4. Run the following command to use the app locally:

    `python manage.py runserver`
    
    
Enter your email address in the EMAIL_HOST_USER and your email password in the EMAIL_HOST_PASSWORD. This is crucial because once a new user registers, they won't get the activation link to verfiy their account.
  
## Usage

You can access the website right [here](http://storefront-env.eba-xz9bwhj2.us-west-2.elasticbeanstalk.com/).
## Demo



https://user-images.githubusercontent.com/87783633/207991500-6a0d4f61-4c69-4b3a-a845-d3a958b273f9.mp4


