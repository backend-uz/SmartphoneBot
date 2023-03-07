# Smartphone shop bot

This is a bot for a smartphone shop. Using telegram bot API, it can be used to order a smartphone. It is written in python and uses the python-telegram-bot library.

## Objectives

- [x] Create a bot that can be used to order a smartphone
- [x] Use the telegram bot API
- [x] Use the python-telegram-bot library
- [x] Allowing users to easily navigate using menus
- [x] Using inline keyboards
- [x] Using callback queries
- [x] User can view products and specifications
- [x] User can add products to cart
- [x] User can view cart
- [x] User can get the total price of the cart
- [x] User can clear the cart
- [x] User can view contact information
- [x] User can view about information
- [x] User can view location
- [x] User can view email
- [x] User can view phone number
- [x] User can view address

## Features of the bot

1. Product browsing: The user can browse through the products and view the specifications of each product.

1. Cart: The user can add products to the cart and view the cart. The user can also clear the cart.

1. Contact information: The user can view the contact information of the shop.

1. About information: The user can view the about information of the shop.

1. Location: The user can view the location of the shop.

1. Email: The user can view the email of the shop.

1. Phone number: The user can view the phone number of the shop.

## Requirements

- Python 3.6 or higher
- python-telegram-bot library

## Bot menu map

1. Main menu

    - 🛍 View Products
    - 📦 View Cart
    - 📞 Contact Us
    - 📝 About Us

1. Contact Us

    - 📞 Phone number
    - 📌 Address
    - 📍 Location
    - 📧 Email

1. About menu

    - 📝 Company Information
    - 📝 Shipping & Returns
    - 📝 Privacy Policy

1. Cart menu

    - 🛒 Cart
    - 📦 Order
    - 📝 Clear cart

1. View Products
    - By Brand
        - Apple
        - Samsung
        - Xiaomi
        - Huawei
        - Oppo
        - Vivo

1. Under each brand

    - 🌄 Photo
    - 📱 Model
    - 💵 Price
    - 📦 Add to cart  
1. View Cart
   - View Items
   - Clear Cart
   - Checkout (Order)

## Structure of the bot

- The bot will have the following handlers:
  - start
  - about
  - contact
  - products
  - products_by_brand
  - cart
  - cancel

- The bot will have the following functions:

## List of tasks

- Start handler: The bot will send a welcome message and a main menu when the user starts the bot.

- Main menu.
The main menu will have 4 buttons: View Products, View Cart, Contact Us, About Us.
