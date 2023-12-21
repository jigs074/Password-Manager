import json, hashlib, getpass, os, pyperclip, sys
from cryptography.fernet import Fernet 

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode()) # this line converts the password string into the sequence of bytes which is then fed to the hash function. 
    return sha256.hexdigest()
# we will use a key here . Please note that the key we will use here to encrypt our passwords will be the one we will use to decrypt it. If we will use another key, it will give errors. 
# Function to generate a secret key 

def generate_key():
    return Fernet.generate_key()

# Initiliaze the Fernet cipher with the generated key 

def Initiliaze_cipher(key): 
    return Fernet(key)


def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password): 
    return cipher.decrypt(encrypted_password.encode()).decode()

# function to register the user

def register_user(username, master_password):
    # Encrypt the master password before storing it in the database
    hashed_master_password = hash_password(master_password)
    user_data= {username: username , master_password: hashed_master_password}
    file_name = 'user_data.json'
    if os.path.exists(file_name) and os.path.getsize(file_name) == 0:
        with open(file_name, 'w') as file: 
            json.dump(user_data, file)
            print("User {username} has been registered successfully")
    else:
        with open(file_name, 'x') as file: # Here the file is created in the exclusive creation mode which will make sure that the file will not be overwritten if it already exists.
            json.dump(user_data, file)
            print("User {username} has been registered successfully")
            
            
        
#Function to log in the user 
 
def login(username, entered_password):
      try:
          with open('user_data.json', 'r') as file:
              user_data = json.load(file)
              stored_password_hash = user_data.get('master_password')
              entered_password_hash = hash_password(entered_password)
              if entered_password == stored_password_hash and username == user_data.get('username'):
                  print("\nThe login is successfull.. \n")
              else :
                  print("Invalid Login credentials. Please use the credentials you used to register.\n")
                  sys.exit()
      except Exception: 
          print("You have not registered before. Please do that. \n ")
          sys.exit()
          

def view_websites():
    try:
        with open('passwords.json', 'r') as data:
             view = json.load(data)
             print("\n Websites you saved ... \n")
             for x in view:
                 print(x['website'])
        print('\n')
            
    except FileNotFoundError:
        print("\n You have not saved any passwords!\n")
        
          
   #load or generate the encryption key 
   
key_filename = 'encryption_key.key'
if os.path.exists(key_filename):
    with open(key_filename, rb) as key_file:
         key = key_file.read()
else:
     key = generate_key()
     with open(key_filename, 'rb') as key_file:
          key_file.write(key)

cipher = Initiliaze_cipher(key)

# Function to add saved passwords

def add_password(website, password):
    # Check if passwords.json exists
    if not os.path.exists('passwords.json'):
        # If passwords.json doesn't exist, initialize it with an empty list
        data = []
    else:
        # Load existing data from passwords.json
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            # Handle the case where passwords.json is empty or invalid JSON.
            data = []
    
    encrypted_password = encrypt_password(cipher,password)
    
    # create a dictionary to store website and password 
    password_entry = {'website': website, 'password': encrypted_password}
    data.append(password_entry)
    
    with open('passwords.json', 'w') as file:
         json.dump(data, file, indent = 4)
         
  
    
        
            
              
           
          
      
     
     