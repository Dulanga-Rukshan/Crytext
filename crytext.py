import base64 
import sys 
import getopt 
import os

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
    python crytext.py -e -f input.txt

  Decrypt a file:
    python crytext.py -d -f encrypted.txt

  Show help:
    python crytext.py -h
"""

toolArt = """
  CCCCC   RRRRR   Y   Y  TTTTT  EEEEE   X   X  TTTTT
 C        R   R    Y Y     T    E        X X     T   
 C        RRRRR     Y      T    EEEE      X      T   
 C        R  R      Y      T    E        X X     T   
  CCCCC   R   R     Y      T    EEEEE   X   X    T   

   ********CryText is a tool designed by Dulanga Rukshan. This tool designed for encryption and decryption of files or text.******** 
 
"""



def main(support,asciiArt):
    longOptions = ["filepath", "encrypt", "decrypt", "help", "image"]
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
            

    try:
        arg, values = getopt.getopt(argumentsList, "f:e:d:h", longOptions)
        for opt, args in arg:
               #to incrypt file using base64
               if opt in ("-e","--encrypt"):
                    try:
                        print(asciiArt)
                        with open(args, "r") as file:
                            print("Encrypting file...")
                            with open("encrypted.txt", "w") as encryptFile:
                                for e in file:
                                    encryptFile.write(f"{encodeText(e)}\n")                
                        print(f"Encrypt file created!!!")
 
                    except FileNotFoundError:
                        print(f"{args} : file not found.")
                


               #to decrypt file that been encrypt by base64 
               elif opt in ("-d", "--decrypt"):
                  #to decrypt file using base64
                    try:
                        print(asciiArt)
                        if opt in ("-d", "--decrypt"):
                            with open(args, "r") as file:
                                print("Decrypting file...")
                                with open("decrypt.txt", "w") as decryptFile:
                                    for d in file:
                                        decryptFile.write(f"{decodeText(d)}\n")

                        elif opt in ("-i", "--image" and "-d", "--decrypt"):
                            with open("decrypt.jpg", "w") as decryptFile:
                                for d in file:
                                    
                        print("File has been decrypted!!!")

                    except FileNotFoundError:
                        print(f"{args} : file not found.")                    
                
               elif opt in ("-i", "--image"):
                   try:
                       print(asciiArt)
                       with open(args, "rb") as image:
                           print()

               elif opt in ("-f", "--file"):
                    print("File path is here.")
               elif opt in ("help", "--help"):
                    print("Help is here")
    except:
        print("Error")
if __name__ == "__main__":
    main(helpText,toolArt)

















