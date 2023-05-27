# World of Warcraft Stat Extractor
Tool to extract stats from World of Warcraft.
It parses the World of Warcraft Armory and extracts the stats from the character page.

# Why?
The main problem I currently have (and yes, down the line characters in the example are Evokers) is that Armor still does not provide stats for Evokers.  
This tool simply prints out stats acquired from the gear, completely ignoring racial bonuses, spec bonuses, etc. (it does factor in gems)


## Usage
First of all, you need to install the dependencies:
```bash
pip install requirements.txt
```

Then, you need to create/modify `.env` file with the following content:
```
FIRST_CHARACTER_NAME=Chablasaurus
FIRST_CHARACTER_REALM=Ysondre
FIRST_CHARACTER_REGION=EU

SECOND_CHARACTER_NAME=Mentalmath
SECOND_CHARACTER_REALM=Tarren Mill
SECOND_CHARACTER_REGION=EU
```

**Where:**  
    -   `FIRST_CHARACTER_NAME` is the name of the first character you want to compare  
    -   `FIRST_CHARACTER_REALM` is the realm of the first character you want to compare  
    -   `FIRST_CHARACTER_REGION` is the region of the first character you want to compare  
    -   `SECOND_CHARACTER_NAME` is the name of the second character you want to compare  
    -   `SECOND_CHARACTER_REALM` is the realm of the second character you want to compare  
    -   `SECOND_CHARACTER_REGION` is the region of the second character you want to compare 


Finally, you can run the script:
```
python main.py
```

Upon completion, you will be presented with a table which will look similar to this one:

|                 | Chablasaurus | Mentalmath | difference | trend |
|-----------------|--------------|------------|------------|-------|
| Primary Stat    | 8513         | 7793       | 720        | more  |
| Stamina         | 22514        | 22089      | 425        | more  |
| Critical Strike | 3080         | 1959       | 1121       | more  |
| Versatility     | 648          | 867        | -219       | less  |
| Mastery         | 5264         | 6112       | -848       | less  |
| Haste           | 2534         | 3279       | -745       | less  |
| Speed           | 370          | 374        | -4         | less  |


**trend** is the trend of the difference between the two characters. (more - first character has more of this stat, less - second character has more of this stat)
**difference** is the difference between the two characters. (positive - first character has more of this stat, negative - second character has more of this stat)
