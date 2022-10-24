Originally setup for use in Windows.  I will be testing in Linux soon.


1. cd to the webp_to_jpeg_converter folder

2. install the required packages referencing the requirements.txt file:
    pip install -r requirements.txt

3. The program will automatically generate the folders required.
    a. Prior to running the converter, if you want to convert some .webp files, create the folder:
        'convert_from'
        - This folder location must be in the same path as webp_convert.py
    b. Place the .webp files into that folder and let Python do the rest.

4. CLI: > python webp_convert.py
