# Abar H Label
Labeling the photo of the license plate based on the name of the license plate itself

## Folder Structure
There should be **3** folders next to the program.
- The main folder of labels is called `images`.
- The modified photos folder is called `output_dir`.
- Unknown fold labels are called `unknown`.
The labels whose values are reviewed and recorded are stored in the output_dir folder.
Labels whose values are unrecognizable are put in the unknown folder.

## Label Structure
Labels that this software processes must be stored with a naming structure: <br>
`123..C12345_DatetimeToStr.Format` <br>
Sample: `319Q87131_16601459966049.png` <br>
The characters after _ are removed and the characters before it are the same as the license plate number. <br>
These are changed based on a certain format and finally become in a format like this: <br>
`12C12345.Format` <br>
Sample: `39Q87123.png` <br><br>
![ScreenShot](./screenshot.png) 