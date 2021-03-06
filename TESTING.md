# Table of Contents
- [Testing](#testing)
  * [Manual testing information](#manual-testing-information)
    + [Feature 1 Navigation Bar and Homepage](#feature-1-navigation-bar-and-homepage)
      - [User Stories Steps 1](#user-stories-steps-1)
      - [User Story Testing Results 1](#user-story-testing-results-1)
    + [Feature 2 Footer](#feature-2-footer)
      - [User Stories Steps 2](#user-stories-steps-2)
      - [User Story Testing Results 2](#user-story-testing-results-2)
    + [Feature 3 Register](#feature-3-register)
      - [User Stories feature 3](#user-stories-feature-3)
      - [User Stories Steps 3](#user-stories-steps-3)
      - [User Story Testing Results 3](#user-story-testing-results-3)
    + [Feature 4 Login](#feature-4-login)
      - [User Stories feature 4](#user-stories-feature-4)
      - [User Stories Steps 4](#user-stories-steps-4)
      - [User Story Testing Results 4](#user-story-testing-results-4)
    + [Feature 5 Products and Product Detail Pages](#feature-5-products-and-product-detail-pages)
      - [User Stories feature 5](#user-stories-feature-5)
      - [User Stories Steps 5](#user-stories-steps-5)
      - [User Story Testing Results 5](#user-story-testing-results-5)
    + [Feature 6 Profile Page](#feature-6-profile-page)
      - [User Stories feature 6](#user-stories-feature-6)
      - [User Stories Steps 6](#user-stories-steps-6)
      - [User Story Testing Results 6](#user-story-testing-results-6)
    + [Feature 07 Product Management](#feature-07-product-management)
      - [User Story 07-1](#user-story-07-1)
      - [User Story Steps 07-1](#user-story-steps-07-1)
      - [User Story Testing Results 07-1](#user-story-testing-results-07-1)
      - [User Story 07-2](#user-story-07-2)
      - [User Story Steps 07-2](#user-story-steps-07-2)
      - [User Story Testing Results 07-2](#user-story-testing-results-07-2)
      - [User Story 07-3](#user-story-07-3)
      - [User Story Steps 07-3](#user-story-steps-07-3)
      - [User Story Testing Results 07-3](#user-story-testing-results-07-3)
    + [Feature 08 shopping bag](#feature-08-shopping-bag)
      - [User Stories feature 08](#user-stories-feature-08)
      - [User Stories Steps 08](#user-stories-steps-08)
      - [User Story Testing Results 08](#user-story-testing-results-08)
    + [Feature 9 Admin](#feature-9-admin)
      - [User Story 9-1](#user-story-9-1)
      - [User Story Steps 9-1](#user-story-steps-9-1)
      - [User Story Testing Results 9-1](#user-story-testing-results-9-1)
      - [User Story 9-2](#user-story-9-2)
      - [User Story Steps 9-2](#user-story-steps-9-2)
      - [User Story Testing Results 9-2](#user-story-testing-results-9-2)
      - [User Story 9-3](#user-story-9-3)
      - [User Story Steps 9-3](#user-story-steps-9-3)
      - [User Story Testing Results 9-3](#user-story-testing-results-9-3)
      - [User Story 9-4](#user-story-9-4)
      - [User Story Steps 9-4](#user-story-steps-9-4)
      - [User Story Testing Results 9-4](#user-story-testing-results-9-4)
    + [Feature 10 blog page](#feature-10-blog-page)
      - [User Stories Steps 10](#user-stories-steps-10)
      - [User Story Testing Results 10](#user-story-testing-results-10)
    + [Feature 11 Blog Item Management](#feature-11-blog-item-management)
      - [User Stories Steps 11](#user-stories-steps-11)
      - [User Story Testing Results 11](#user-story-testing-results-11)
    + [Feature 12 sale items page](#feature-12-sale-items-page)
      - [User Stories Steps 12](#user-stories-steps-12)
      - [User Story Testing Results 12](#user-story-testing-results-12)
- [Code Validators and Website Analysis](#code-validators-and-website-analysis)
  * [HTML Markup Validation Service](#html-markup-validation-service)
  * [CSS Validation Service](#css-validation-service)
  * [PEP8online](#pep8online)

## Manual testing information
Testing was completed on the following browsers and device types

Device Number | Physical/Emulator | Device Name | Device Type | Browser | Version
------------ | ------------ | ------------- | ------------- | ------------- | -------------
1 | Emulator | iPadMini | Tablet | Chrome Emulator | 94.0 |
2 | Emulator | iPhone X | Mobile | Chrome Emulator | 94.0 |
3 | Emulator | iPhone 5/SE | Mobile | Chrome Emulator | 94.0 |

- Below are the test results for testing the website requirements against a range of browsers and devices
- For the purpose of the screenshots I used a Chrome emulator for desktop, tablet and mobile


### Feature 1 Navigation Bar and Homepage
#### User Stories Steps 1
1. Navigate to https://ci-ms5-pinkaccessories.herokuapp.com, and click on the My Account link as a regular user
2. Login to the website with a valid username and password, and click on the My Account link
3. Navigate to the "All Products" filter, and then click By Price
4. Navigate to the "All Products" filter, and then click By Rating
5. Navigate to the "All Products" filter, and then click By Category
6. Navigate to the "Necklaces" filter, and filter by Necklaces
7. Navigate to the "Earrings" filter, and filter by Earrings
8. Navigate to the "Bracelets" filter, and filter by Bracelets
9. Navigate to the "Scarves" filter, and filter by Bracelets
10. Navigate to the "Hats" filter, and filter by Bracelets
11. Navigate to the "Fascinators" filter, and filter by Fascinators
12. Navigate to the "Totes" filter, and filter by Totes
13. Navigate to the "Clutchs" filter, and filter by Bracelets
14. Click the Logout link under My profile and logout
15. Login as an admin user

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The homepage is displayed, Login and Register links are displayed under My Account and the footer items are displayed with website links(Register/Login) | [Desktop](readme/testing/homepage_notloggedin_desktop.png)  | [Tablet](readme/testing/homepage_notloggedin_ipad.png)  | [Mobile](readme/testing/homepage_notloggedin_iphone.png)  | Passed |
Step 2 | The homepage is displayed with a header logo(desktop), search box(expands on tablet/mobile), My account, Favourites and shopping bag icons. My Profile/Logout is visible under My Account and the footer contains links for My Profile, Blog and Sale   | [Desktop](readme/testing/homepage_loggedin_desktop.png) | [Tablet](readme/testing/homepage_notloggedin_ipad.png)  | [Mobile](readme/testing/homepage_loggedin_iphone.png) | Passed |
Step 3 | Products on the page are filtered by Price (Low-High) | [Desktop](readme/testing/products_filterpricelow_desktop.png) | [Tablet](readme/testing/products_filterpricelow_ipad.png)  | [Mobile](readme/testing/products_filterpricelow_iphone.png)  | Passed |
Step 4 | Products on the page are filtered by Rating (High-Low) | [Desktop](readme/testing/products_filterpricehigh_desktop.png)  | [Tablet](readme/testing/products_filterpricehigh_ipad.png) | [Mobile](readme/testing/products_filterpricehigh_iphone.png)  | Passed |
Step 5 | Products on the page are filtered by Category (A-Z) | [Desktop](readme/testing/products_filterA_Z_desktop.png)  | [Tablet](readme/testing/products_filterA_Z_ipad.png)  | [Mobile](readme/testing/products_filterA_Z_iphone.png) | Passed  |
Step 6 | Products on the page are filtered by Necklaces | [Desktop](readme/testing/category_necklace_desktop.png) | [Tablet](readme/testing/category_necklace_ipad.png)  | [Mobile](readme/testing/category_necklace_iphone.png) | Passed  |
Step 7 | Products on the page are filtered by Earrings | [Desktop](readme/testing/category_earrings_desktop.png)  | [Tablet](readme/testing/category_earrings_ipad.png)  | [Mobile](readme/testing/category_earrings_iphone.png)  | Passed |
Step 8 | Products on the page are filtered by Bracelets | [Desktop](readme/testing/category_bracelets_desktop.png)| [Tablet](readme/testing/category_bracelets_ipad.png)  | [Mobile](readme/testing/category_bracelets_iphone.png)  | Passed |
Step 9 | Products on the page are filtered by Scarves | [Desktop](readme/testing/category_scarves_desktop.png) | [Tablet](readme/testing/category_scarves_ipad.png) | [Mobile](readme/testing/category_scarves_iphone.png)  | Passed |
Step 10 | Products on the page are filtered by Hats | [Desktop](readme/testing/category_scarves_desktop.png) | [Tablet](readme/testing/category_scarves_ipad.png)  | [Mobile](readme/testing/category_scarves_iphone.png)  | Passed |
Step 11 | Products on the page are filtered by Facinators | [Desktop](readme/testing/category_fascinator_desktop.png) | [Tablet](readme/testing/category_fascinator_ipad.png)  | [Mobile](readme/testing/category_fascinator_iphone.png) | Passed |
Step 12 | Products on the page are filtered by Totes | [Desktop](readme/testing/category_tote_desktop.png) | [Tablet](readme/testing/category_tote_ipad.png)  | [Mobile](readme/testing/category_tote_iphone.png) | Passed |
Step 13 | Products on the page are filtered by Clutchs | [Desktop](readme/testing/category_clutch_desktop.png) | [Tablet](readme/testing/category_clutch_ipad.png) | [Mobile](readme/testing/category_clutch_iphone.png)  | Passed |
Step 14 | The user is logged out | [Desktop](readme/testing/loggingout_desktop.png)  | [Tablet](readme/testing/loggingout_ipad.png)  | [Mobile](/workspace/CI-MS5-PinkAccessories/readme/testing/loggingout_iphone.png) | Passed |
Step 15 | The homepage is displayed with a header logo(desktop), search box(expands on tablet/mobile), My Account and shopping bag icons. Product Management/Blog Item Management/My Profile/Logout is visible under My Account and the footer contains links for Product Management  | [Desktop](readme/testing/homepage_admin_desktop.png)  | [Tablet](readme/testing/homepage_admin_ipad.png)  | [Mobile](readme/testing/homepage_admin_iphone.png)  | Passed |

### Feature 2 Footer
#### User Stories Steps 2
1. As an unauthenticated user scroll down to the footer on the homepage 
2. As an admin user scroll down to the footer on the homepage 
3. As a non admin authenticated user scroll down to the footer on the homepage
4. Provide email address to register for newsletter

#### User Story Testing Results 2
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The footer items are displayed with website links (Jewellery, Bags, Scarves, login, register, newsletter) | [Desktop](readme/testing/unauthenticated_user_footer_desktop.png) | [Tablet](readme/testing/unauthenticated_user_footer_tablet.png)  | [Mobile](readme/testing/unauthenticated_user_footer_mobile.png)  | Passed |
Step 2 | The footer items are displayed with website links (Jewellery, Bags, Scarves, product management, blog management, newsletter) | [Desktop](readme/testing/admin_user_footer_desktop.png) | [Tablet](readme/testing/admin_user_footer_tablet.png) | [Mobile](readme/testing/admin_user_footer_mobile.png)  | Passed |
Step 3 | The footer items are displayed with website links (Jewellery, Bags, Scarves, my profile, blog, sale, newsletter) | [Desktop](readme/testing/authenticated_user_desktop.png) | [Tablet](readme/testing/authenticated_user_tablet.png) | [Mobile](readme/testing/authenticated_user_mobile.png) | Passed |
Step 5 | The users email address is added to mailchimps contact tab | [Desktop](readme/testing/mailchimp_desktop.png) | [Tablet]| [Mobile]| Passed |

### Feature 3 Register
#### User Stories feature 3
- User Story 3.1: As a regular user I can register on the website by providing an email address, email address(confirmation), username, password, password confirmation
- User Story 3.1: As a regular user I will receive an email to verify my account after registering
- User Story 3.1: As a regular user I can log in to my account once I click on the verification link in the email I receive regarding my registration

#### User Stories Steps 3
1. As a regular user, navigate to the registration page, fill in email address, email address(confirmation), username, password, password confirmation and click Sign Up
2. Open the email received
3. Click on the verification link in the email received
4. Confirm the email address for the account
5. Sign in to the account
6. Attempt to register with the same account and do not fill in all the mandatory fields: email address, email address(confirmation), username, password, password confirmation

#### User Story Testing Results 3
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The user registers for an account | [Desktop](readme/testing/register_desktop.png)  | [Tablet](readme/testing/register_ipad.png)  | [Mobile](readme/testing/register_iphone.png)  | Passed  |
Step 2 | The user receives the email | [Desktop](readme/testing/verifyemail_desktop.png)  | [Tablet](readme/testing/verifyemail_ipad.png)  | [Mobile](readme/testing/verifyemail_iphone.png)  | Passed  |
Step 3 | The user clicks on the verification link | [Desktop](readme/testing/confirmemail_desktop.png) | [Tablet](readme/testing/confirmemail_ipad.png) | [Mobile](readme/testing/confirmemail_iphone.png)  | Passed  |
Step 4 | The user confirms the email address | [Desktop](readme/testing/emailedconfirmed_desktop.png)  | [Tablet](readme/testing/emailedconfirmed_ipad.png)  | [Mobile](readme/testing/emailedconfirmed_iphone.png) | Passed  |
Step 5 | The user logs in to the site | [Desktop](readme/testing/successfullysignedin_desktop.png)  | [Tablet](readme/testing/successfullysignedin_ipad.png)  | [Mobile](readme/testing/successfullysignedin_iphone.png) | Passed  |
Step 6 | A message is displayed to the user | [Desktop](readme/testing/fiedsrequired_desktop.png) | [Tablet](readme/testing/fieldsrequired_ipad.png) | [Mobile](readme/testing/fieldsrequired_iphone.png)  | Passed  | 

### Feature 4 Login
#### User Stories feature 4
- User Story 4.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 4.2: As an admin/regular user I can request a new password if I forget my current password. I will receive an email to reset my password. Once I reset I can log in
#### User Stories Steps 4
1. Attempt to log in to the website with an account that does not exist or an incorrect password
2. Request a new password
3. Login to the site with the correct account details
#### User Story Testing Results 4
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | A message is displayed to the user | [Desktop](readme/testing/loginfails_desktop.png)  | [Tablet](readme/testing/loginfails_ipad.png)  | [Mobile](readme/testing/loginfails_iphone.png)  | Passed |
Step 2 | The user receives an email where they can reset their password | [Desktop](readme/testing/password_reset_email.png)  |  |  | Passed |
Step 3 | The user can successfully log in | [Desktop](readme/testing/password_updated_desktop.png)  | [Tablet](readme/testing/password_updated_ipad.png)  | [Mobile](readme/testing/password_updated_iphone.png)  | Passed |

### Feature 5 Products and Product Detail Pages
#### User Stories feature 5
- User Story 5.1: As a regular user I can view the products page with product count and with each product image, title, category, price and presale price(if applicable)
- User Story 5.2: As a regular user I can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- User Story 5.3: As a regular user if I click on a product I will be navigated to the product detail page
- User Story 5.4: As a regular user I can view the product image, description, colour, code, rating, category, description
- User Story 5.5: As a regular user I can click on the Keep Shopping button on the product detail page, and it will navigate the user to the products page
- User Story 5.6: As a regular user I can set the product size(if applicable for the product) and quantity for a product (one plus)
- User Story 5.7: As an admin user I can view the Add product page by clicking on the Product Management link.
- User Story 5.8: As an admin user I can view the Edit product page by clicking on the Edit button on the product. 
- User Story 5.9: As an admin user I can click on a product, and I am navigated to the product detail page. I can edit or delete the product by clicking on the Edit or Delete links on the page

#### User Stories Steps 5
1. As a regular user login to the website and navigate to the products page
2. Sort the products from Price(High to Low)
3. Click on a product
4. Click on product with size e.g Camel Pom Pom Hat
5. Add a product(bags) to the bag, with a quantity of 2
6. As an admin user login and click on the add product(Product Management)
7. Click on the edit button on the products page or in the product detail page and edit the product
8. As an admin user delete a product


#### User Story Testing Results 5
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The products page is displayed | [Desktop](readme/testing/products_desktop.png)  | [Tablet](readme/testing/products_ipad.png)  | [Mobile](readme/testing/products_iphone.png)  | Passed |
Step 2 | The products are sorted High to Low | [Desktop](readme/testing/product_price_desktop.png)  | [Tablet](readme/testing/product_price_ipad.png)  | [Mobile](readme/testing/product_price_iphone.png)  | Passed |
Step 3 | The product detail is displayed | [Desktop](readme/testing/product_detail_desktop.png)  | [Tablet](readme/testing/product_detail_ipad.png)  | [Mobile](readme/testing/product_detail_iphone.png)  | Passed |
Step 4 | Size drop down is displayed for user to select size | [Desktop](readme/testing/product_size_desktop.png)  | [Tablet](readme/testing/product_size_tablet.png)  | [Mobile](readme/testing/product_size_mobile.png)  | Passed |
Step 5 | The 2 products are added | [Desktop](readme/testing/add_bad_to_cart_desktop.png)  | [Tablet](readme/testing/add_bad_to_cart_ipad.png)  | [Mobile](readme/testing/add_bad_to_cart_iphone.png)  | Passed |
Step 6 | The add product page is displayed | [Desktop](readme/testing/add_product_desktop.png)  | [Tablet](readme/testing/add_product_ipad.png)  | [Mobile](readme/testing/add_product_iphone.png)  | Passed |
Step 7 | The edit product page is displayed | [Desktop](readme/testing/edit_product_desktop.png)  | [Tablet](readme/testing/edit_product_ipad.png)  | [Mobile](readme/testing/edit_product_iphone.png)  | Passed |
Step 8 | Delete a product notification displayed | [Desktop](readme/testing/delete_product_desktop.png)  | [Tablet](readme/testing/delete_product_ipad.png)  | [Mobile](readme/testing/delete_product_iphone.png)  | Passed |

### Feature 6 Profile Page
#### User Stories feature 6
- User Story 9.1: As a regular user I can view my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.2: As a regular user I can update my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.3: As a regular user I can view my order history(Order Number, Date, Items and Order Total)
- User Story 9.4: As a regular user I can click on an order number to view the order information (Order number, Order date/time, Full Name, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total)

#### User Stories Steps 6
1. Click on the My Profile link under My Account
2. Update one field in the default delivery information (Street Address 2)
3. Click on an order number

#### User Story Testing Results 6
Step | Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The users default delivery information and order history is displayed  | [Desktop](readme/testing/shopper_profile_desktop.png)  | [Tablet](readme/testing/shopper_profile_ipad.png)  | [Mobile](readme/testing/shopper_profile_iphone.png)  | Passed |
Step 2 | The users default delivery information is updated and displayed (Street Address 1)  | [Desktop](readme/testing/profile_update_desktop.png)  | [Tablet](readme/testing/profile_update_ipad.png)  | [Mobile](readme/testing/profile_update_iphone.png)  | Passed |
Step 3 | The users order details is displayed | [Desktop](readme/testing/order_history_desktop.png)  | [Tablet](readme/testing/order_history_ipad.png)  | [Mobile](readme/testing/order_history_iphone.png)  | Passed |

### Feature 07 Product Management
#### User Story 07. 1
- User Story 07.1 : As an admin user I can add a product by clicking on the Product Management link in My Account. I must enter a name, category, price, colour, code, description and can optionally has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, upload an image and click the Add Product button. Clicking cancel navigates the user to the product page.

#### User Story Steps 07-1
- Step 1: As an admin user login navigate to Product Management under MyAccount, and add details to a product and click the Add Product button
- Step 2: Click on the product detail for the product

#### User Story Testing Results 07.1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The add product page is displayed | [Desktop](readme/testing/addproduct_desktop.png)  | [Tablet](readme/testing/addproduct_ipad.png)  | [Mobile](readme/testing/addproduct_iphone.png)  | Passed |
Step 2 | The product detail is displayed | [Desktop](readme/testing/addedproduct_desktop.png)  | [Tablet](readme/testing/addedproduct_ipad.png)  | [Mobile](readme/testing/addedproduct_iphone.png)  | Passed |

#### User Story 07-2
- User Story 07.2: As an admin user I can edit a product by clicking on the Edit button on the Products page for the product. I can update the name, category, price, colour, code, description, has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, update an image and click the 
Edit Product button. Clicking cancel navigates the user to the product page

#### User Story Steps 07-2
- Step 1: As an admin user login and navigate to a product in the products page and click on a product, and click the Edit button
- Step 2: Update the product, for example the price
#### User Story Testing Results 07-2
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The edit product page is displayed | [Desktop](readme/testing/edit_product_desktop.png)  | [Tablet](readme/testing/edit_product_ipad.png)  | [Mobile](readme/testing/edit_product_iphone.png)  | Passed |
Step 2 | The product detail is updated with the new price| [Desktop](readme/testing/edited_product_desktop.png)  | [Tablet](readme/testing/edited_product_ipad.png)  | [Mobile](readme/testing/edited_product_iphone.png)  | Passed |

#### User Story 07-3
- User Story 07.3: As an admin user I can delete a product by clicking on the Delete button on the product. A success message will appear to confirm the product has been successfully deleted.
#### User Story Steps 07-3
- Step 1: As an admin user login navigate to a product in the products page and click the Delete button
- Step 2: Delete the product
#### User Story Testing Results 07-3
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 2 | The product is deleted, the count is reduced, success message appears| [Desktop](readme/testing/delete_product_desktop.png)  | [Tablet](readme/testing/delete_product_ipad.png)  | [Mobile](readme/testing/delete_product_iphone.png)  | Passed |


#### User Stories feature 08 shopping bag
- User Story 08.1: As a regular user I can click on a product, set the size(if applicable) and quantity, click Add to Bag and the product will be added to my bag, a message displayed 
- User Story 08.2: As a regular user I can click on the bag icon, I will be brought to my bag. If there are no items in the bag, a message will be displayed
- User Story 08.3: As a regular user I can click on the bag icon, I will be brought to my bag. If there are items, the product image, detail, price, quantity, subtotal will be displayed for the item. The bag total, delivery(if applicable), grand total would be displayed
- User Story 08.4: As a regular user I can update the quantity or remove an item from my shopping bag
- User Story 08.5: As a regular user I can click on the Secure Checkout button on the bag page, and I will be brought to the Checkout page
- User Story 08.6: As a regular user on the checkout page I can set my details(Full Name, email address, both mandatory) and Delivery Information(Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory), which is populated from my profile if filled in
- User Story 08.7: As a regular user on the checkout page I can view the order summary(item image, title, size, quantity, subtotal, order total, delivery, grand total)
- User Story 08.8: As a regular user on the checkout page if I click "Save this delivery information to my profile", the details entered will be saved on the users profile
- User Story 08.9: As a regular user on the checkout page I can enter a credit card number(16 digits), expiry date(2 digits/2digits), cvc(3 digits) and a postal code(up to 5 digits), these fields are mandatory
- User Story 08.10: As a regular user on the checkout page if I click the Keep Shopping button I will be navigated to the products page
- User Story 08.11: As a regular user on the checkout page if I click the Complete Order button, and the transaction is not successful, a message will be displayed
- User Story 08.12: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the user will be navigated to a checkout success page, and an email is sent to the user
- User Story 08.13: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the order is saved to my order history in My profile page
- User Story 08.14: As a regular user on the checkout success page, the Order details will be displayed (Order number, Order date/time, Full NameStreet Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total) and a link to the sales item page is displayed
- User Story 08.15: As a regular user not logged in, I can add items to my bag and make a purchase

#### User Stories Steps 08
Note: Some screenshots show dollars, I have since changed all instances to euros
1. As a regular user add some items to your bag, so the order is less than 99 euros
2. Empty the bag
3. Add the items back into the bag
4. Add the items back into the bag, and Update the quantity on one item by one, so the order goes above 99 euros
5. Checkout the order
6. Complete the order form
7. Go to the order details on the users my profile page
8. Logout, and as a user not logged in add items to a bag 
8. Checkout and complete the purchase
#### User Story Testing Results 08
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The items are added to the bag, and there is a delivery charge(10%) and message displayed | [Desktop](readme/testing/add_product_to_bag_desktop.png)  | [Tablet](readme/testing/add_product_to_bag_ipad.png)  | [Mobile](readme/testing/add_product_to_bag_iphone.png)  | Passed |
Step 2 | A message "Your bag is empty" is displayed with a button to go shopping | [Desktop](readme/testing/empty_bag_desktop.png)  | [Tablet](readme/testing/empty_bag_ipad.png)  | [Mobile](readme/testing/empty_bag_iphone.pngG)  | Passed |
Step 3 | The items are added to the bag, and there is a delivery charge(10%) and message displayed | [Desktop](readme/testing/shopping_bag_desktop.png)  | [Tablet](readme/testing/shopping_bag_ipad.png)  | [Mobile](readme/testing/shopping_bag_iphone.png)  | Passed |
Step 4 | The items are added to the bag, and there is no delivery charge | [Desktop](readme/testing/no_delivery_charge_desktop.png)  | [Tablet](readme/testing/no_delivery_charge_ipad.png)  | [Mobile](readme/testing/no_delivery_charge_iphone.png)  | Passed |
Step 5 | The order is complete | [Desktop](readme/testing/complete_order_form_desktop.png)  | [Tablet](readme/testing/complete_order_form_ipad.png)  | [Mobile](readme/testing/complete_order_form_iphone.png)  | Passed |
Step 6 | The order is displayed on the "my profile" page | [Desktop](readme/testing/order_history_desktop.png)  | [Tablet](readme/testing/order_history_ipad.png)  | [Mobile](readme/testing/order_history_iphone.png)  | Passed |
Step 7 | The purchase is successful and the checkout success page is displayed | [Desktop](readme/testing/thank_you_desktop.png)  | [Tablet](readme/testing/thank_you_ipad.png)  | [Mobile](readme/testing/thank_you_iphone.png)  | Passed |


### Feature 9 Admin
#### User Story 9-1
- User Story 13.1: As an admin user I can view users orders in the django admin page and can view order number, date, full name, order total, delivery cost, grand total
#### User Story Steps 9-1
- Step 1: As an admin user login navigate to https://8000-lime-jackal-9mgfiw2b.ws-eu33.gitpod.io/admin/checkout/order/
#### User Story Testing Results 9-1
Step| Result | Result  | Status
------------ | ------------ | ------------- | ------------- 
Step 1 | The orders are displayed | [Result](/workspace/CI-MS5-PinkAccessories/readme/testing/admin_order_desktop.png)  | Passed |

#### User Story  9-2
- User Story 9.2: As an admin user I can view products in the django admin page and can view a products code, name, category, has sizes, price, presale price, rating, image, image url
#### User Story Steps 9-2
- Step 1: As an admin user navigate to https://ci-ms5-pinkaccessories.herokuapp.com/admin/products/product/
#### User Story Testing Results 9-2
Step| Result | Result  | Status
------------ | ------------ | ------------- | ------------- 
Step 1 | The products are displayed | [Result](readme/testing/admin_products.png)   | Passed |

#### User Story 9.3
- User Story 13.10: As an admin user I can view users in the django admin page and can search by username and email address and  filter by staff status, superuser status and active status
#### User Story Steps 9.3
- Step 1: As an admin user navigate to  and filter on non superuser status
#### User Story Testing Results 9.3
Step| Result | Result  | Status
------------ | ------------ | ------------- | ------------- 
Step 1 | The non superuser users are displayed | [Result](readme/testing/admin_users.png)   | Passed |


#### User Story 9.4
- User Story 13.15: As an admin user I can view categories in the django admin page and can view a category name and friendly name
#### User Story Steps 9.4
- Step 1: As an admin user navigate to https://8000-lime-jackal-9mgfiw2b.ws-eu33.gitpod.io/admin/products/category/
#### User Story Testing Results 9.4
Step| Result | Result  | Status
------------ | ------------ | ------------- | ------------- 
Step 1 | The categories are displayed | [Result](readme/testing/admin_categories.png)   | Passed |

### Feature 10 Blog Page
#### User Stories feature 10
- User Story 8.1: As a regular user I can view 4 blog items on a page with a blog image, and 150 characters of the blog item text and a read more button
- User Story 8.2: As a regular user I can click on the read more button on the Blog page, I will be navigated to the blog item with a blog item image, content and any comments will be displayed
- User Story 8.3: As a regular user I can add a comment to a "blog" item
- User Story 8.4: As a regular user I can delete a comment that I had originally added on a "blog item"
- User Story 8.5: As a regular user who has not registered or logged into the website, I cannot add a comment to a "blog item"

#### User Stories Steps 10
1. As a regular user click on the Blog page 
2. Click on the read more button on a "blog item"   
3. Add a comment to a "blog item" 
4. Delete a comment from a "blog item"
5. As a regular user not logged in, select a Blog item and try to add a comment

#### User Story Testing Results 10
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The blog page is displayed | [Desktop](readme/testing/blog_items_desktop.png)  | [Tablet](readme/testing/blog_items_tablet.png)  | [Mobile](readme/testing/blog_items_mobile.png)  | Passed |
Step 2 | The blog item is displayed | [Desktop](readme/testing/blog_item_desktop.png)  | [Tablet](readme/testing/blog_item_tablet.png)  | [Mobile](readme/testing/blog_item_mobile.png)  | Passed |
Step 3 | The comment is added  | [Desktop](readme/testing/comment_added_desktop.png)  | [Tablet](readme/testing/comment_added_tablet.png)  | [Mobile](readme/testing/comment_added_mobile.png)  | Passed |
Step 4 | The comment is deleted | [Desktop](readme/testing/coment_deleted_desktop.png)  | [Tablet](readme/testing/coment_deleted_tablet.png)  | [Mobile](readme/testing/coment_deleted_desktop.png)  | Passed |
Step 5 | A comment cannot be added | [Desktop](readme/testing/unauthenticated_user_comment_desktop.png)  | [Tablet](readme/testing/unauthenticated_user_comment_tablet.png)  | [Mobile](readme/testing/unauthenticated_user_comment_mobile.png)  | Passed |


### Feature 11 Blog Item Management
#### User Stories feature 11
- User Story 11.1: As an admin user I can view Blog items by clicking on the Blog Item Management link under My account. The blog item count and title, create date, status(Published or Draft), and Edit and Delete buttons is displayed
- User Story 11.2: As an admin user if there are more than four blog items added, the page is paginated
- User Story 11.3: As an admin user I can add a blog item, by clicking on the Add button. I can enter a Title and content, add an image and set the item to Published or Draft
- User Story 11.4: As an admin user I can edit a blog item, by clicking on the Edit button for the blog item. I can update a Title and blog item text, update an image and update the item to Published or Draft
- User Story 11.5: As an admin user if a blog item is set to Draft, admin and regular users will NOT see this item on the Blog Page.
- User Story 11.6: As an admin user if a blog item is set to Published, admin regular users will see this item on the Blog Page.
- User Story 11.7: As an admin user I can delete a blog item

#### User Stories Steps 11
1. As an admin user click on the Blog Item Management under My account
2. Click on the Add blog item button to add a blog item with text and image
3. Click on the Edit blog item button to update a "blog item"
4. Click on the Blog page to see Published items and click on the edited blog item, Draft items are not displayed
5. Delete a "blog item"

#### User Story Testing Results 11
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The manage blog items page is displayed | [Desktop](readme/testing/manage_blog_items_desktop.PNG)  | [Tablet](readme/testing/manage_blog_items_tablet.PNG)  | [Mobile](readme/testing/manage_blog_items_mobile.PNG)  | Passed |
Step 2 | The add blog item page is displayed and the blog item is added| [Desktop](readme/testing/add_blog_item_desktop.PNG)  | [Tablet](readme/testing/add_blog_item_tablet.png)  | [Mobile](readme/testing/add_blog_item_mobile.png)  | Passed |
Step 3 | The edit blog item page is displayed and the blog item is updated| [Desktop](readme/testing/edited_blog_item_desktop.png)  | [Tablet](readme/testing/edited_blog_item_tablet.png)  | [Mobile](readme/testing/edited_blog_item_mobile.png)  | Passed |
Step 4 | The published blog item is displayed | [Desktop](readme/testing/blog_items_desktop.png)  | [Tablet](readme/testing/blog_items_tablet.png)  | [Mobile](readme/testing/blog_items_mobile.png)  | Passed |
Step 5 | The blog item is deleted | [Desktop](readme/testing/delete_blog_item_desktop.png)  | [Tablet](readme/testing/delete_blog_item_tablet.png)  | [Mobile](readme/testing/delete_blog_item_mobile.png)  | Passed |

### Feature 12 Sale items page
#### User Stories feature 12
- User Story 6.1: As a regular user I can view the products with sale prices, the product image, category, presale price and price is displayed
- User Story 6.2: As a regular user if I click on a product in the sale items, I am navigated to the product detail page for that product

#### User Stories Steps 12
1. Click on the sale items in the header
2. Click on a product in the sale items 

#### User Story Testing Results 12
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The sale items and count are displayed | [Desktop](readme/testing/sale_items_desktop.PNG)  | [Tablet](readme/testing/sale_items_desktop.PNG)  | [Mobile](readme/testing/sale_items_desktop.PNG)  | Passed |
Step 2 | The product detail is displayed | [Desktop](readme/testing/sale_item_desktop.png)  | [Tablet](readme/testing/sale_item_tablet.png)  | [Mobile](readme/testing/sale_item_mobile.png)  | Passed |


# Code Validators and Website Analysis
The website's pages was tested against the following validators:

## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
bag/templates/bag/bag.html  | 0 errors and 0 contrast errors| [Results](readme/testing/bag_w3validation.png) 
checkout/templates/checkout/checkout.html | 0 errors and 0 contrast errors| [Results](readme/testing/checkout_w3validation.png)  
checkout/templates/checkout/checkout_success.html | 0 errors and 0 contrast errors| [Results](readme/testing/checkout_success_w3validation.png)  
home/templates/home/index.html | 0 errors and 0 contrast errors| [Results](readme/testing/index_w3validation.png)
products/templates/products/add_product.html | 0 errors and 0 contrast errors| [Results](readme/testing/add_product_w3validation.png)
products/templates/products/edit_product.html | 0 errors and 0 contrast errors| [Results](readme/testing/add_product_w3validation.png)  
products/templates/products/product_detail.html | 0 errors and 0 contrast errors| [Results](readme/testing/products_detail_w3validation.png) 
products/templates/products/products.html | 0 errors and 0 contrast errors| [Results](readme/testing/products_w3validation.png)     
profile/templates/profile/profile.html | 0 errors and 0 contrast errors| [Results](readme/testing/profile_w3validation.png)  
profile/templates/profile/order_history.html | 0 errors and 0 contrast errors| [Results](readme/testing/order_history_w3validation.png)  
templates/allauth/account/login.html | 0 errors and 0 contrast errors| [Results](readme/testing/login_w3validation.png)
templates/allauth/account/logout.html | 0 errors and 0 contrast errors| [Results](readme/testing/logout_w3validation.png)
templates/allauth/account/register.html | 0 errors and 0 contrast errors| [Results](readme/testing/registraion_w3validation.png) 
templates/allauth/account/password_change.html | 0 errors and 0 contrast errors| [Results](readme/testing/forgot_password_w3validation.png)
templates/allauth/account/password_reset.html | 0 errors and 0 contrast errors| [Results](readme/testing/reset_password_w3validation.png)
templates/allauth/account/password_reset_done.html | 0 errors and 0 contrast errors| [Results](readme/testing/password_reset_done_w3validation.png)
templates/allauth/account/verification_sent.html | 0 errors and 0 contrast errors| [Results](readme/testing/password_reset_sent_w3validation.pngg)
products/templates/products/sale_items.html | 0 errors and 0 contrast errors| [Results](readme/testing/w3_sale_items.png) 
blog/templates/blog/blog_item.html | 0 errors and 0 contrast errors| [Results](readme/testing/w3_add_blog_item.png)   
blog/templates/blog/edit_blog_item.html | 0 errors and 0 contrast errors| [Results](readme/testing/w3_edit_blog_item.png)  
blog/templates/blog/manage_blog_items.html | 0 errors and 0 contrast errors| [Results](readme/testing/w3_manage_blog_item.png) 
blog/templates/blog/blog.html| 0 errors and 0 contrast errors| [Results](readme/testing/w3_blog_items.png)  
blog/templates/blog/blog_item.html | 0 errors and 0 contrast errors| [Results](readme/testing/w3_blog_item.png)    
<br>

## CSS Validation Service
I used https://jigsaw.w3.org/css-validator/ to validate the css(style.css)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
static/css/base.css | Passed, No errors found | [Results](readme/testing/base_css_validation.png) 
checkout/static/checkout/css/checkout.css | Passed, No errors found | [Results](readme/testing/checkout_css_validation.png)

## PEP8online
- PEP8online was used to analyse the Python files (https://pep8online.com/)
- One of the main errors on several files was to ensure the character count was less than 80 characters

Page | Result 
------------ | ------------- 
bag/admin.py | No errors/warnings 
bag/apps.py | No errors/warnings 
bag/contexts.py | No errors/warnings 
bag/models.py | No errors/warnings 
bag/urls.py | No errors/warnings 
bag/views.py | No errors/warnings 
checkout/admin.py | No errors/warnings 
checkout/apps.py | No errors/warnings 
checkout/forms.py | No errors/warnings 
checkout/models.py | No errors/warnings 
checkout/signals.py | No errors/warnings 
checkout/urls.py | No errors/warnings 
checkout/views.py | No errors/warnings 
checkout/webhook_handler.py | No errors/warnings 
checkout/webhooks.py | No errors/warnings 
home/admin.py | No errors/warnings 
home/apps.py | No errors/warnings 
home/models.py | No errors/warnings 
home/urls.py | No errors/warnings 
home/views.py | No errors/warnings 
products/admin.py | No errors/warnings 
products/apps.py | No errors/warnings 
products/forms.py | No errors/warnings 
products/models.py | No errors/warnings 
products/urls.py | No errors/warnings 
products/views.py | No errors/warnings 
products/widgets.py | No errors/warnings 
profiles/admin.py | No errors/warnings 
profiles/apps.py | No errors/warnings 
profiles/forms.py | No errors/warnings 
profiles/models.py | No errors/warnings 
profiles/urls.py | No errors/warnings 
profiles/views.py | No errors/warnings 
custom_storages.py | No errors/warnings
manage.py | No errors/warnings
blog/admin.py | No errors/warnings 
blog/apps.py | No errors/warnings 
blog/models.py | No errors/warnings 
blog/urls.py | No errors/warnings 
blog/views.py | No errors/warnings 
blog/forms.py | No errors/warnings 

