

     CCCCC   RRRRR   Y   Y  TTTTT  EEEEE   X   X  TTTTT
    C        R   R    Y Y     T    E        X X     T   
    C        RRRRR     Y      T    EEEE      X      T   
    C        R  R      Y      T    E        X X     T   
     CCCCC   R   R     Y      T    EEEEE   X   X    T   

# CryText - Encryption and Decryption Tool

CryText is a Python based base64 tool designed for encrypting and decryption of files or text. Whether you're looking to protect sensitive information or need a quick way to securely share data, CryText makes it simple and effective.


## Features

- **Encrypt Text or Files**: Easily encrypt your text or file data using a specified encryption algorithm.
- **Decrypt Encrypted Data**: Decrypt your encrypted text or files back to their original form.
- **Command-Line Interface**: Easy-to-use CLI interface for quick operations.
- **File Support**: Encrypt and decrypt both text and file data by specifying the file path.

##File types supported 

.txt, .csv, .log, .json, .xml, .yaml, .md, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .odt, .ods, .odp, .py, .java, .js, .html, .css, .c, .cpp, .php, .rb, .ts, .sh


## Installation

1. Clone this repository to your local machine:
  
        git clone https://github.com/Dulanga-Rukshan/crytext.git
        cd crytext
        python3 crytext.py 

    Ensure that you have Python installed ( Python 3.x ).
  
        cd crytext
   
   Ensure that you have Python installed (preferably Python 3.x).

Usage

The basic syntax for using CryText is:

python3 crytext.py [OPTIONS]

Options

    -e, --encrypt: Encrypt the input data using the specified algorithm.
    -d, --decrypt: Decrypt the encrypted data.
    -h, --help: Show the help message with all options and details.
    -f, --file: Specify the file path for input or output data.

Examples

Encrypt a File:

     python3 crytext.py -f input.txt -e

Decrypt a File:

     python3 crytext.py  -f encrypted.txt -d


Show Help:

    python3 crytext.py -h

Description

CryText is a tool designed by Dulanga Rukshan for encryption and decryption of files. With this tool, you can secure your data with ease by using the command-line interface and various options for encryption and decryption.

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements, bug fixes, or new features.

    Designed by Dulanga Rukshan.
