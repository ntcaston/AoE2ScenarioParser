# Datasets
The project currently contains multiple datasets. These are currently pretty basic and only contain the in-editor options. You can retrieve access to the datasets by importing them. 

```py
# Information about the conditions & effects and their attributes
from AoE2ScenarioParser.datasets import conditions
from AoE2ScenarioParser.datasets import effects

# Information of unit/tech/terrain name and their ID
from AoE2ScenarioParser.datasets import techs
from AoE2ScenarioParser.datasets import units
from AoE2ScenarioParser.datasets import buildings
from AoE2ScenarioParser.datasets import terrains

# Enum of players
from AoE2ScenarioParser.datasets.players import Player
```

Current datasets are:

- conditions
- effects
- buildings
- units
- techs
- players
- terrains

---
&nbsp;
## Conditions & Effects

The conditions and effects datasets are very usefull when creating triggers. You can use them to get the ID of an effect or condition using it's name.

```py
conditions.object_in_area   # 5
effects.patrol              # 19
```

When you created a condition or effect inside of a trigger you can check what needs to be added to the effect to actually function. This is different in every editor (`CTRL + Q` for PyCharm) but you can also just check the github page. 
```py
trigger = trigger_manager.add_trigger("Trigger0")
effect = trigger.add_effect(effects.change_diplomacy)

# Checking the docs for effects.change_diplomacy will show:
"""
Attributes for the **change_diplomacy** effect are:
- diplomacy
- player_source
- player_target
"""
```
You can use this information to edit this effect:
```py
effect.diplomacy = 0  # Ally (1 = Neutral, 3 = Enemy) <- Datasets for this will be added
effect.player_source = Player.ONE.value
effect.player_target = Player.TWO.value
```
If you want to find the `ID` using the String name or the other way around of the condition or effect you can use the `Bidict` like so:
```py
effects.effect_names(0)     # none
effects.effect_names(11)    # create_object
effects.effect_names.inverse("create_object")           # 11
effects.effect_names.inverse("acknowledge_ai_signal")   # 50

conditions.condition_names[5]   # objects_in_area
conditions.condition_names[11]  # object_selected
conditions.condition_names.inverse["capture_object"]    # 7
conditions.condition_names.inverse["units_garrisoned"]  # 18
```
*Tip: You can use the following to make the names look nicer (Credits: T-West)*
```py
from AoE2ScenarioParser.helper import helper
helper.pretty_print_name(conditions.condition_names[11])  # Object Selected
```

---
&nbsp;
## Units, Buildings and Techs

The Units and Buildings datasets are very usefull when adding units. They're also, together with the the Techs dataset, very usefull when adding or editing triggers.

For adding units it'll look something like the following:
```py
unit_manager.add_unit(Player.ONE, units.conquistador, x=10, y=20)
unit_manager.add_unit(Player.TWO, units.paladin, x=20, y=20)
unit_manager.add_unit(Player.GAIA, buildings.feitoria, x=21, y=63)
```

With the triggers you can do similiar stuff like:
```py
...
effect = trigger.add_effect(effects.create_object)
effect.object_list_unit_id = units.man_at_arms      # <-- Can use either units  
effect.object_list_unit_id = buildings.blacksmith   # <-- or buildings
...
```
or:
```py
...
effect = trigger.add_effect(effects.research_technology)
effect.player_source = Player.THREE.value
effect.technology = techs.bloodlines  # <--
...
```
Just like effects and conditions there is a `Bidict` within the dataset which you can use to translate the `ID -> Name` or `(inverse) Name -> ID`.

```py
units.unit_names[40]            # cataphract
buildings.building_names[598]   # outpost
techs.tech_names[60]            # elite_conquistador

units.unit_names.inverse['galleon']         # 442
buildings.building_names.inverse['stable']  # 101
techs.tech_names.inverse['guard_tower']     # 140
```

---
&nbsp;
## Terrains

The Terrain dataset has been added __but it's currently not very usefull__ as it's not supported to interact with terrain. It does exist and works as follows:

```py
terrains.beach              # 2
terrains.forest_oak         # 10
terrains.underbush_leaves   # 71
```

---
&nbsp;
## Players

For selecting players it can be as easy as typing `1`. Unfortunately not all parts of the scenario file are structured like: `0: Gaia, 1: Player1 ... 8: Player8`. So because of this a representation layer has been added. It's a simple Enum which looks like this:
```py
class Player(Enum):
    GAIA = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
```
For now some places (like effect attributes (as seen above)) do not support these Enum values. That said, it's still recommended to use them for consistency. You can do this by adding `.value` behind the Enum as: 
```py
Player.GAIA.value == 0  # True
```

---

End of the Datasets cheatsheet. [Return to README](./../README.md)