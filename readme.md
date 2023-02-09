# Jimmy Jazz Sneaker Bot
This program was created to aid in the purchase of a limited, high in demand sneaker. 

The Sneaker Bot strictly works on Jimmy Jazz's website, below.
* https://www.jimmyjazz.com/


## Instructions
* Clone repo down and access code.
* Download Chrome Driver at the below link.
    - https://chromedriver.chromium.org/downloads
    - Store your Chrome Driver download within your downloads folder. If you place it elsewhere, be sure to update the path in the buy_sneaker.py file on line 16.
* Update key values within the `variables` dictionary.
    - Note:
        - The brand, sneaker_full_name, and product_id keys must have the dashes in their values like it is in the product page's url. 
        - The product_select key value can be found within the page source when expecting a size option. `This field must be filled in`
* Fill in appropriate shipping and payment information.
 - If no address2 info is needed, be sure to comment out lines 78 & 92.
 - Line 133 should be edited based on full name on payment method.
* Line 158 is commented out for safety purposes when running the program. Be sure to comment in when trying to succesfully complete a purchase. 


* __Once__ ready to use, run program with the command `python buy_sneaker.py` or `python3 buy_sneaker.py`, depending on your version of python. 
    - I would recommend running program 5 minutes prior to the release time for the wanted sneaker.
* Good luck!

## Screenshots

## Technologies Used