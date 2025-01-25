import base64 
import sys 
import getopt 
import os
import getpass


helpText = """
 CCCCC   RRRRR   Y  Y  TTTTTT  EEEEE  X   X  TTTTT
C        R   R   Y  Y    T     E       X X     T  
C        RRRRR    Y      T     EEEE     X      T  
C        R  R     Y      T     E       X X     T  
 CCCCC   R   R    Y      T     EEEEE  X   X    T  


        Usage: python crytext.py [OPTIONS]

Options:
  -e, --encrypt     Encrypt the input data using the specified algorithm.
  -d, --decrypt     Decrypt the encrypted data.
  -h, --help        Show this help message and exit.
  -f, --file        Specify the file path for input or output data.

Description:
 CryText is a tool designed by Dulanga Rukshan. This tool designed for encryption and decryption of files or text. 
 Use the following options to interact with the tool:

  -e: This option encrypts your input data (text or file) using the chosen encryption method.
  -d: This option decrypts the encrypted data and restores it to its original form.
  -h: If you need help or further details about how to use the tool, the `-h` option will display this help message.
  -f: Provide the file path to specify the location of the file you want to encrypt, decrypt, or process.

Examples:
  Encrypt a file:
    python crytext.py -f input.txt -e 

  Decrypt a file:
    python crytext.py -f encrypted.txt -d

  Show help:
    python crytext.py -h
"""

def welcomeMsg(): 
    toolArt = f"""
      CCCCC   RRRRR   Y   Y  TTTTT  EEEEE   X   X  TTTTT
     C        R   R    Y Y     T    E        X X     T   
     C        RRRRR     Y      T    EEEE      X      T   
     C        R  R      Y      T    E        X X     T   
      CCCCC   R   R     Y      T    EEEEE   X   X    T   

       ********CryText is a tool designed by Dulanga Rukshan. This tool designed for encryption and decryption of files or text.******** 

     Hello {getpass.getuser()}!. Welcome to my simple base64 file encoding & decoding tool. I encourage you to submit a review to this email what should i include to this tool - dulangarukshan@proton.me 

    """
    return toolArt



def main(support,asciiArt):
    longOptions = ["filepath", "encrypt", "decrypt", "help"]
    argumentsList = sys.argv[1:]
    #encrypt function
    def encodeText(y):
        try:
            y = y.encode("utf-8")   #this encode the password to bytes
            base = base64.b64encode(y) #this takes bytes and encoded to b64encode
            encrypt = base.decode("utf-8")  #this convert that b64encoded data to string format
            return encrypt

        except (base64.binascii.error, UnicodeEncodeError) as e :
            print(f"Error encodeing: {e}")
            return


    #decrypt function
    def decodeText(x):
        try:
            x = x.encode("utf-8") #this take result encoded password from encodePassword and change it to bytes
            baseDecode = base64.b64decode(x) #decode to b64decode again 
            basedecrypt = baseDecode.decode("utf-8") #this convert that baseDecode result to string
            return basedecrypt
        
        except(base64.error, UnicodeDecodeError) as e:
            print(f"Error decoding: {e}")
            return


    def encodingFile(filepath,filename,fileextension):
        try:
            with open(encode, "r") as file:
                print("Encrypting file...")
                with open(f"{filename}Encrypted.{fileextension}", "w") as encryptFile:                                           
                    for e in file:
                        encryptFile.write(f"{encodeText(e)}\n")                
            print(f"Encrypt file created!!!")
        except Exception as e:
            print(f"File named {filepath} has been encrypted as {filename}{fileextension}!!!")

    def decodingFile(filepath, filename, fileextension):
        try:
            with open(filepath, "r") as file:
                print("Decrypting file...")
                with open(f"{filename}Decrypt{fileextension}", "w") as decryptFile:
                    for d in file:
                        decryptFile.write(f"{decodeText(d)}\n")
            print(f"File named {filepath} has been decrypted as {filename}{fileextension}!!!")
        except Exception as e:
            print(f"Decrypting file error - {e}.")
                  
    try:
        arg, values = getopt.getopt(argumentsList, "f:edh", longOptions)
        filePath = None
        for opt, args in arg:
               if opt in ("-f", "--file"):
                   filePath = args
                    
               #to incrypt file using base64
               elif opt in ("-e","--encrypt") and filePath:
                   if filePath:
                       if os.path.exists(filePath):
                           print(asciiArt)
                           fileName, fileExtension = os.path.splitext(filePath)
                           encodingFile(filePath, fileName, fileExtension)
                       else:
                           print(asciiArt)
                           print(f"{filePath} not found!!!")            
 
                   else:
                       print("Error: file path is not specified! Use -f <file-path>.")


               #to decrypt file that been encrypt by base64 
               elif opt in ("-d", "--decrypt") and filePath:
                   if filePath: 
                       if os.path.exists(filePath):
                           print(asciiArt)
                           fileName,fileExtension = os.path.splitext(filePath)
                           decodingFile(filePath,fileName, fileExtension)                            
                       else:
                           print(asciiArt)
                           print(f"{filePath} not found!!!")
                   else:
                       print(f"Error file path is not specified! Use -f <file-path>.")

               elif opt in ("-h", "--help"):
                   print(support)
    except:
        print("Error")
if __name__ == "__main__":
    main(helpText,welcomeMsg())

















