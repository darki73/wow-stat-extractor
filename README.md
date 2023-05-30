# World of Warcraft Stat Extractor
Tool to extract stats from World of Warcraft.  
It parses the World of Warcraft Armory and extracts the stats from the character page, but it is not recommended to use it, as it is against the ToS.   
It also supports retrieving stats from Battle.net API, and it is recommended to use it instead of Armory, as it is not against the ToS.

You can always fall back to Armory by setting `BATTLE_NET_MAKE_IT_LEGAL` to `false` in `.env` file.  
This will make the script use Armory instead of Battle.net API and will always nag you to use Battle.net API instead.
If you are unfamiliar with Battle.net API, you can read more about it [here](https://develop.battle.net/documentation/guides/getting-started).  
And if it is all too complicated for you, you can always set `BATTLE_NET_MAKE_IT_LEGAL` to `false` and use Armory instead.

The usage of Armory is not condoned by Blizzard (and I certainly do not condone it), but it is there if you want to use it.

# Why?
The main problem I currently have (and yes, down the line characters in the example are Evokers) is that Armory still does not provide stats for Evokers.
This tool prints out stats acquired from gear, and for select classes (which are configured), it also prints out percentages with class / spec bonuses.
It will always include stats acquired from gems and enchantments.


## Usage
First of all, you need to install the dependencies:
```bash
pip install requirements.txt
```

Then, you need to create/modify `.env` file with the following content:
```
BATTLE_NET_MAKE_IT_LEGAL=true
BATTLE_NET_ACCESS_TOKEN=
BATTLE_NET_SECRET_TOKEN=

FIRST_CHARACTER_NAME=Chablasaurus
FIRST_CHARACTER_REALM=Ysondre
FIRST_CHARACTER_REGION=EU

SECOND_CHARACTER_NAME=Mentalmath
SECOND_CHARACTER_REALM=Tarren Mill
SECOND_CHARACTER_REGION=EU
```

**Where:**  
    -   `BATTLE_NET_MAKE_IT_LEGAL` is a boolean which indicates whether you want to use the Battle.net API.  
    -   `BATTLE_NET_ACCESS_TOKEN` is the access token you get from Battle.net API.  
    -   `BATTLE_NET_SECRET_TOKEN` is the secret token you get from Battle.net API.  
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

|                 | Chablasaurus  | Mentalmath    | Difference | Trend |
|-----------------|---------------|---------------|------------|-------|
| Stamina         | 22501         | 22220         | 281        | ➕    |
| Strength        | 0             | 0             | 0          | ➖    |
| Agility         | 0             | 0             | 0          | ➖    |
| Intellect       | 8690          | 8557          | 133        | ➕    |
| Critical Strike | 2728 / 20.16% | 1515 / 13.42% | 1213       | ➕    |
| Haste           | 3008 / 17.69% | 3279 / 19.29% | -271       | ➖    |
| Mastery         | 5324 / 96.44% | 6112 / 107.39%| -788       | ➖    |
| Versatility     | 648 / 3.16%   | 867 / 4.23%   | -219       | ➖    |
| Leech           | 0             | 0             | 0          | ➖    |
| Avoidance       | 200           | 838           | -638       | ➖    |


**trend** is the trend of the difference between the two characters. (more - first character has more of this stat, less - second character has more of this stat)  
**difference** is the difference between the two characters. (positive - first character has more of this stat, negative - second character has more of this stat)
