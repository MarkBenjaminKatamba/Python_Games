'''
This is probably the hardest one out of these 6 small projects. 
This will be similar to guessing the number, except we are guessing the word. 
The user needs to guess letters, Give the user no more than 6 attempts for 
guessing wrong letter. This will mean you will have to have a counter. 
You can download a ‘sowpods’ dictionary file or csv file to use as a way to 
get a random word to use.
===============================================================================
Useful Resource Links:
    1. https://thewordsearch.com/hangman
    2. https://en.wikipedia.org/wiki/Hangman_(game)
    3. a) https://www.downloadexcelfiles.com/wo_en/download-excel-file-list-african-countries-dependent-territories#.XvC3yGgzbDc 
       b) en.wikipedia.org/wiki/List_of_African_countries_by_population							
'''
import random
import string

def secretWord():
    