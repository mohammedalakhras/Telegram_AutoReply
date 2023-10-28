



# Telegram_AutoReply 
This repository on GitHub is a script to auto reply messages on Telegram account  with free hosting

## Overview
The "Telegram_AutoReply" project is a script hosted on GitHub that enables automatic replies to messages on Telegram account. This script is designed to be hosted for free, making it a cost-effective solution for users who want to automate their Telegram responses.

## Installation
  ### 1. Get your `api_hash`and `api_id`
  1. Open your web browser and navigate to [my.telegram.org](https://my.telegram.org/).
  2. Log in using your Telegram phone number. Telegram will send you a confirmation code via the Telegram app, not SMS.
  3. After logging in, click on 'API development tools'.
  4. Fill out the form with your application details. You can enter any name for your application and a short description.
  5. After you've filled out the form, click on 'Create application' at the end.
  6. You'll now be able to see your `api_id` and `api_hash`. These are important credentials, so make sure to keep them safe and do not share them with anyone.
  
  ### 2. Clone the repository
  
  
  ```bash
  git clone https://github.com/mohammedalakhras/Telegram_AutoReply
  ```
  
  ### 3. Move to project directory
  
  ```bash
  cd Telegram_AutoReply
  ```
  ### 4. Install the required packages
  
  ```bash
  pip install -r requirements.txt
  ```
  
  
  ### 5. run `app.py` 
  ```bash
  python app.py
  ```
  then you need to enter your phone and you will recive code to authentication.
  
  after that this code will create session file `anon.session` 
  then you must upload this file in direct link hosting  such as archive.org 
  then get direct link of `anon.session` becasue you need to use it in
  `sessionUrlFile` environment variable.

  ### 6. define environment variable 
  that will be used in  `init_session.py` file : `apiID` , `apiHash` , `phone`, `username` , `sessionUrlFile` 
  
###  Good Luck! 
