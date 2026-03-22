# Online Shopping Cart System

## Overview
A Python OOP-based shopping cart system with products, users, cart operations, services, custom exceptions, and order history persistence.

## Folder Structure
- `main.py`
- `models/product.py`
- `models/cart.py`
- `models/user.py`
- `models/premium_user.py`
- `services/store_service.py`
- `services/cart_service.py`
- `exceptions/cart_exceptions.py`
- `utils/file_handler.py`
- `data/order_history.txt`
- `tests/test_cart.py`

## Features
- Add products to store inventory
- Add/remove products from cart
- Validate stock and product existence
- Checkout and save order history
- Premium user discount support

## Run
From `online_shopping_cart` folder:

```bash
python main.py
```

## Tests
From `online_shopping_cart` folder:

```bash
python -m unittest tests/test_cart.py -v
```
