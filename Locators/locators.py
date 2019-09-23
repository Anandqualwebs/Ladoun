class locators():

#product Page

    eng_change_xpath = "//span[@class='side-navbar-btn'][contains(text(),' English ')]"
    add_cart_product_xpath = "//button[@id='product-addtocart-button']"

#Checkout Page

    no_email_xpath = "//label[3]"
    name_xpath = "//input[@id='billing_firstname']"
    address_xpath = "//input[@id='billing_addressline0']"
    phone_xpath = "//input[@id='billing_mobile']"
    select_country_xpath = "//select[@id='billing_country']"
    select_state_xpath = "//select[@id='billing_state']"
    select_city_xpath = "//select[@id='select_billing_city']"
    click_verify_xpath = "//div[@id='billing-new-address-form']/div[@name='billingAddress.mobile']//input[@name='sendOtp']"
    click_verify_otp_xpath = "//a[@class='button action verifyOtp']"
    enter_card_name_xpath = "//input[@id='payfort_fort_mp2_card_holder_name']"
    enter_card_number_xpath = "//input[@id='payfort_fort_mp2_card_number']"
    enter_card_cvv_xpath = "//input[@id='payfort_fort_mp2_cvv']"
    select_month_xpath = "//select[@id='payfort_fort_mp2_expiry_month']"
    select_year_xpath = "//select[@id='payfort_fort_mp2_expiry_year']"
    click_place_order_xpath = "//button[@class='iwd_opc_button active iwd_opc_place_order_button']"
    click_cod_xpath = "//div[@id='checkout-payment-method-load']//label[2]//input[1]"

#Registration Page

    create_account_button_xpath = "//a[@class='action create primary']"
    create_account_name_xpath = "//div[@class='column main']//input[@id='firstname']"
    create_account_email_xpath = "//fieldset[@class='fieldset create account']//input[@id='email_address']"
    create_account_password_xpath = "//div[@class='column main']//input[@id='password']"
    create_account_con_password_xpath = "//div[@class='column main']//input[@id='password-confirmation']"
    create_account_submit_xpath = "//div[@class='column main']//button[@class='action submit primary']"

#Login page

    enter_email_xpath = "//form[@id='login-form']//fieldset[@class='fieldset login']//input[@id='email']"
    enter_password_xpath = "//form[@id='login-form']//fieldset[@class='fieldset login']//input[@id='pass']"
    click_login_xpath = "//button[@id='send2']//span[contains(text(),'Login')]"
    logout_xpath = "//a[contains(text(),'Logout')]"
    invalid_credential_error_xpath = "//div[contains(text(),'Invalid login or password.')]"

#Forgot Pass Page
    click_forgot_password_xpath = "//a[@class='action remind']"
    enter_forgot_email_xpath = "//div[@class='field email required']//input[@id='email_address']"
    click_reset_password_xpath = "//span[contains(text(),'Reset My Password')]"
    reset_email_sent_xpath = "//div[@class='message-success success message']"

#Profile Dashboard
    dashboard_xpath = "//strong[contains(text(),'My Account')]"

    click_change_pass_xpath = "//a[@class='action change-password']"

    enter_name_xpath = "//fieldset[@class='fieldset info']//input[@id='firstname']"
    enter_current_password_xpath = "//input[@id='current-password']"
    enter_new_password_xpath = "//div[@class='field new password required']//input[@id='password']"
    enter_confirm_new_password_xpath = "//div[@class='field confirm password required']//input[@id='password-confirmation']"
    click_save_xpath = "//span[contains(text(),'Save')]"
    password_changed_success_msg_xpath = "//div[contains(text(),'You saved the account information.')]"

    click_change_name_xpath = "//div[@class='box box-information']//a[@class='action edit']"

    click_address_tab_link_text = "Address Book"
    click_account_dashboard_link_text = "Account Dashboard"
    click_add_new_address_xpath = "//span[contains(text(),'Add New Address')]"

    enter_new_name_xpath = "//fieldset[@class='fieldset']//input[@id='firstname']"
    enter_company_xpath = "//input[@id='company']"
    enter_phone_xpath = "//input[@id='telephone']"
    enter_fax_xpath = "//input[@id='fax']"
    enter_street_address_one = "//input[@id='street_1']"
    enter_street_address_two = "//input[@id='street_2']"
    select_new_country_xpath = "//select[@id='country']"
    select_new_state_xpath = "//select[@id='region_id']"
    enter_new_city_xpath = "//input[@id='city']"
    enter_zip_xpath = "//input[@id='zip']"
    billing_address_checkbox_xpath = "//span[contains(text(),'Use as my default billing address')]"
    shipping_address_checkbox_xpath = "//div[@class='field choice set shipping']//label[@class='label']"
    click_save_address_xpath = "//button[@class='action save primary']"

#ProductPage
    product_side_images_check_xpath = "//div[@class='fotorama__thumb-border']"

    Product_main_images_check_xpath = "//img[@class='fotorama__img']"
    product_code_avail_check_xpath = "//div[@class='product-info-stock-sku']"
    product_quantity_enter_xpath = "//input[@id='qty']"
    product_add_to_cart_click_xpath = "//button[@id='product-addtocart-button']"
    product_like_click_xpath = "//span[@class='like-bordered-span']"
    product_details_click_xpath = "//a[@id='tab-label-product.info.description-title']"
    product_more_info_click_xpath = "//div[@id='tab-label-additional']"
    product_more_info_refer_check_xpath = "//div[@id='tab-label-additional']"
    product_review_click_xpath = "//a[@id='tab-label-reviews-title']"
    product_review_text_click_xpath = "//a[@class='action add']"
    product_review_text_refer_check_xpath = "//strong[contains(text(),'Write Your Own Review')]"






