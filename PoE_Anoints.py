"""
    Some useless tool I made to check if anoints on items are worth scrapping for golden and/or silver oils

    For Path Of Exile 3.18 (Sentinel League)
    Made By Hubsik
    19.05.2022

    TODO:
        Highlights - DELETE ME
        X   Auto Resize Window On

    FIXME:
        X   Things like "Infused" and "Infused Flesh" show wrong annoint (first encountered anoint in array prob) UPDATE: There is a chance that this can repeat with other anoints
        X   Anoints with multi line enchant text dont show at all (wrong info in array; enchant is 2x in item text)

"""
#! Imports
import tkinter as GUI
from tkinter import scrolledtext as SCROLLEDTEXT
import pyperclip as PYPERCLIP
import functools as FUNCTOOLS
    #What are those?
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

#! Global Variables
Oil_List = {
    "Clear_Oil":"#707072",
    "Sepia_Oil":"#573211",
    "Amber_Oil":"#be641e",
    "Verdant_Oil":"#45b84a",
    "Teal_Oil":"#45b89e",
    "Azure_Oil":"#11348d",
    "Indigo_Oil":"#3d2e5f",
    "Violet_Oil":"#750bb8",
    "Crimson_Oil":"#d6130c",
    "Black_Oil":"#000000",
    "Opalescent_Oil":"#85e8f1",
    "Silver_Oil":"#7c7875",
    "Golden_Oil":"#b18a15",
}

Valuable_Amulet_Anoint_List = [
    # Anoint Only
    ["Golden_Oil", "Golden_Oil", "Azure_Oil", "Tranquility"],
    ["Golden_Oil", "Golden_Oil", "Crimson_Oil", "Tenacity"],
    ["Clear_Oil", "Golden_Oil", "Azure_Oil", "Cleansed_Thoughts"],     
    ["Clear_Oil", "Teal_Oil", "Violet_Oil", "Hardened_Scars"],
    ["Opalescent_Oil", "Black_Oil", "Black_Oil", "Way_of_the_Warrior"],
    ["Opalescent_Oil", "Silver_Oil", "Amber_Oil", "Mystic_Talents"],   
    ["Golden_Oil", "Golden_Oil", "Black_Oil", "Crusader"],
    ["Golden_Oil", "Golden_Oil", "Amber_Oil", "Vengeant_Cascade"],
    ["Clear_Oil", "Golden_Oil", "Violet_Oil", "Persistence"],
    ["Golden_Oil", "Verdant_Oil", "Black_Oil", "Deadly_Inclinations"],
    ["Golden_Oil", "Golden_Oil", "Violet_Oil", "Aspect_of_Stone"],
    # Rest
    ["Silver_Oil", "Verdant_Oil", "Crimson_Oil", "Lord_of_the_Dead"],
    ["Amber_Oil", "Amber_Oil", "Amber_Oil", "Path_of_the_Warrior"],
    ["Opalescent_Oil", "Sepia_Oil", "Black_Oil", "Adder's_Touch"],
    ["Clear_Oil", "Clear_Oil", "Crimson_Oil", "Successive_Detonations"],
    ["Verdant_Oil", "Teal_Oil", "Violet_Oil", "Razor's_Edge"],
    ["Clear_Oil", "Violet_Oil", "Black_Oil", "Acuity"],
    ["Teal_Oil", "Azure_Oil", "Violet_Oil", "Sacrifice"],
    ["Verdant_Oil", "Azure_Oil", "Black_Oil", "Safeguard"],
    ["Clear_Oil", "Silver_Oil", "Indigo_Oil", "Force_Shaper"],
    ["Teal_Oil", "Teal_Oil", "Teal_Oil", "Mystic_Bulwark"],
    ["Silver_Oil", "Verdant_Oil", "Azure_Oil", "Forces_of_Nature"],
    ["Clear_Oil", "Verdant_Oil", "Black_Oil", "Combat_Stamina"],
    ["Opalescent_Oil", "Indigo_Oil", "Black_Oil", "Careful_Conservationist"],
    ["Clear_Oil", "Clear_Oil", "Azure_Oil", "Cloth_and_Chain"],
    ["Golden_Oil", "Violet_Oil", "Black_Oil", "Arcane_Capacitor"],
    ["Clear_Oil", "Silver_Oil", "Amber_Oil", "Counterweight"],
    ["Verdant_Oil", "Black_Oil", "Black_Oil", "Righteous_Army"],
    ["Sepia_Oil", "Sepia_Oil", "Verdant_Oil", "Fending"],
    ["Clear_Oil", "Amber_Oil", "Crimson_Oil", "Toxic_Strikes"],
    ["Clear_Oil", "Golden_Oil", "Amber_Oil", "Swift_Venoms"],
    ["Clear_Oil", "Crimson_Oil", "Black_Oil", "Arcanist's_Dominion"],
    ["Golden_Oil", "Verdant_Oil", "Violet_Oil", "Disemboweling"],
    ["Golden_Oil", "Sepia_Oil", "Verdant_Oil", "Brutal_Blade"],
    ["Clear_Oil", "Sepia_Oil", "Teal_Oil", "Spiked_Bulwark"],
    ["Golden_Oil", "Sepia_Oil", "Sepia_Oil", "Spiritual_Command"],
    ["Crimson_Oil", "Crimson_Oil", "Crimson_Oil", "Coldhearted_Calculation"],
    ["Amber_Oil", "Amber_Oil", "Violet_Oil", "Soul_Siphon"],
    ["Teal_Oil", "Violet_Oil", "Black_Oil", "Essence_Sap"],
    ["Clear_Oil", "Clear_Oil", "Opalescent_Oil", "Eagle_Eye"],
    ["Azure_Oil", "Violet_Oil", "Crimson_Oil", "Light_Eater"],
    ["Opalescent_Oil", "Verdant_Oil", "Crimson_Oil", "Retaliation"],
    ["Opalescent_Oil", "Opalescent_Oil", "Azure_Oil", "Volatile_Mines"],
    ["Golden_Oil", "Crimson_Oil", "Crimson_Oil", "Arcane_Expanse"],
    ["Amber_Oil", "Azure_Oil", "Crimson_Oil", "Utmost_Might"],
    ["Azure_Oil", "Violet_Oil", "Violet_Oil", "Courage"],
    ["Golden_Oil", "Sepia_Oil", "Black_Oil", "Faith_and_Steel"],
    ["Sepia_Oil", "Sepia_Oil", "Crimson_Oil", "Precision"],
    ["Golden_Oil", "Violet_Oil", "Violet_Oil", "Born_to_Fight"],
    ["Golden_Oil", "Teal_Oil", "Teal_Oil", "Quick_Recovery"],
    ["Silver_Oil", "Verdant_Oil", "Indigo_Oil", "Vanquisher"],
    ["Golden_Oil", "Amber_Oil", "Amber_Oil", "Claws_of_the_Falcon"],
    ["Amber_Oil", "Verdant_Oil", "Violet_Oil", "Silent_Steps"],
    ["Sepia_Oil", "Verdant_Oil", "Black_Oil", "Will_of_Blades"],
    ["Azure_Oil", "Black_Oil", "Black_Oil", "Gravepact"],
    ["Clear_Oil", "Golden_Oil", "Golden_Oil", "Soul_of_Steel"],
    #["Silver_Oil", "Silver_Oil", "Crimson_Oil", "Infused"], # Moved To Fix Bugs
    ["Violet_Oil", "Black_Oil", "Black_Oil", "Disintegration"],
    ["Clear_Oil", "Sepia_Oil", "Violet_Oil", "Freedom_of_Movement"],
    ["Teal_Oil", "Crimson_Oil", "Black_Oil", "True_Strike"],
    ["Silver_Oil", "Violet_Oil", "Crimson_Oil", "Indomitable_Army"],
    ["Amber_Oil", "Verdant_Oil", "Teal_Oil", "Depth_Perception"],
    ["Golden_Oil", "Azure_Oil", "Azure_Oil", "Sanctum_of_Thought"],
    ["Silver_Oil", "Amber_Oil", "Amber_Oil", "Arcane_Will"],
    ["Opalescent_Oil", "Azure_Oil", "Black_Oil", "Serpent_Stance"],
    ["Opalescent_Oil", "Teal_Oil", "Black_Oil", "Master_Sapper"],
    ["Opalescent_Oil", "Sepia_Oil", "Teal_Oil", "Diamond_Skin"],
    ["Golden_Oil", "Crimson_Oil", "Black_Oil", "Savagery"],
    ["Azure_Oil", "Azure_Oil", "Azure_Oil", "Slaughter"],
    ["Clear_Oil", "Azure_Oil", "Azure_Oil", "Prodigal_Perfection"],
    ["Sepia_Oil", "Sepia_Oil", "Azure_Oil", "Instinct"],
    ["Amber_Oil", "Azure_Oil", "Violet_Oil", "Kinetic_Impacts"],
    ["Clear_Oil", "Verdant_Oil", "Azure_Oil", "Martial_Experience"],
    ["Clear_Oil", "Amber_Oil", "Teal_Oil", "Ironwood"],
    ["Opalescent_Oil", "Golden_Oil", "Violet_Oil", "Dismembering"],
    ["Verdant_Oil", "Teal_Oil", "Azure_Oil", "Sentinel"],
    ["Opalescent_Oil", "Verdant_Oil", "Azure_Oil", "Explosive_Impact"],
    ["Opalescent_Oil", "Opalescent_Oil", "Black_Oil", "Crackling_Speed"],
    ["Clear_Oil", "Clear_Oil", "Golden_Oil", "Lava_Lash"],
    ["Verdant_Oil", "Verdant_Oil", "Verdant_Oil", "Spirit_Void"],
    ["Sepia_Oil", "Teal_Oil", "Azure_Oil", "Dreamer"],
    ["Clear_Oil", "Amber_Oil", "Amber_Oil", "Might"],
    ["Silver_Oil", "Amber_Oil", "Azure_Oil", "Searing_Heat"],
    ["Golden_Oil", "Azure_Oil", "Black_Oil", "Reflexes"],
    ["Sepia_Oil", "Crimson_Oil", "Crimson_Oil", "Ash_Frost_and_Storm"],
    ["Silver_Oil", "Verdant_Oil", "Teal_Oil", "One_with_Evil"],
    ["Golden_Oil", "Amber_Oil", "Black_Oil", "Measured_Fury"],
    ["Azure_Oil", "Azure_Oil", "Violet_Oil", "Smashing_Strikes"],
    ["Clear_Oil", "Violet_Oil", "Crimson_Oil", "Flaying"],
    ["Opalescent_Oil", "Sepia_Oil", "Verdant_Oil", "Destroyer"],
    ["Opalescent_Oil", "Azure_Oil", "Azure_Oil", "Heart_of_Darkness"],
    ["Golden_Oil", "Golden_Oil", "Verdant_Oil", "Unnatural_Calm"],
    ["Clear_Oil", "Silver_Oil", "Azure_Oil", "Shaman's_Dominion"],
    ["Opalescent_Oil", "Verdant_Oil", "Verdant_Oil", "Versatility"],
    ["Sepia_Oil", "Amber_Oil", "Violet_Oil", "Shamanistic_Fury"],
    ["Golden_Oil", "Sepia_Oil", "Amber_Oil", "Goliath"],
    ["Verdant_Oil", "Teal_Oil", "Teal_Oil", "Mind_Drinker"],
    ["Sepia_Oil", "Azure_Oil", "Violet_Oil", "Entrench"],
    ["Silver_Oil", "Verdant_Oil", "Verdant_Oil", "High_Explosives"],
    ["Clear_Oil", "Amber_Oil", "Verdant_Oil", "Essence_Infusion"],
    ["Opalescent_Oil", "Amber_Oil", "Amber_Oil", "Divine_Wrath"],
    ["Opalescent_Oil", "Teal_Oil", "Violet_Oil", "Dark_Arts"],
    ["Silver_Oil", "Silver_Oil", "Sepia_Oil", "Wasting"],
    ["Teal_Oil", "Violet_Oil", "Violet_Oil", "Unstable_Munitions"],
    ["Verdant_Oil", "Verdant_Oil", "Crimson_Oil", "Farsight"],
    ["Teal_Oil", "Black_Oil", "Black_Oil", "Ribcage_Crusher"],
    ["Sepia_Oil", "Teal_Oil", "Black_Oil", "Divine_Judgement"],
    ["Opalescent_Oil", "Sepia_Oil", "Sepia_Oil", "Potency_of_Will"],
    ["Clear_Oil", "Golden_Oil", "Crimson_Oil", "Druidic_Rite"],
    ["Silver_Oil", "Verdant_Oil", "Violet_Oil", "King_of_the_Hill"],
    ["Teal_Oil", "Azure_Oil", "Black_Oil", "Finesse"],
    ["Golden_Oil", "Verdant_Oil", "Crimson_Oil", "Heart_of_Oak"],
    ["Silver_Oil", "Sepia_Oil", "Teal_Oil", "Winter_Spirit"],
    ["Silver_Oil", "Amber_Oil", "Verdant_Oil", "Tempest_Blast"],
    ["Clear_Oil", "Verdant_Oil", "Indigo_Oil", "Clever_Thief"],
    ["Clear_Oil", "Verdant_Oil", "Verdant_Oil", "Path_of_the_Hunter"],
    ["Silver_Oil", "Amber_Oil", "Indigo_Oil", "Deflection"],
    ["Opalescent_Oil", "Crimson_Oil", "Black_Oil", "Hex_Master"],
    ["Azure_Oil", "Violet_Oil", "Black_Oil", "Adamant"],
    ["Clear_Oil", "Opalescent_Oil", "Indigo_Oil", "Split_Shot"],
    ["Silver_Oil", "Golden_Oil", "Sepia_Oil", "Natural_Authority"],
    ["Azure_Oil", "Azure_Oil", "Black_Oil", "Sanctity"],
    ["Opalescent_Oil", "Indigo_Oil", "Violet_Oil", "Serpentine_Spellslinger"],
    ["Silver_Oil", "Indigo_Oil", "Violet_Oil", "Asylum"],
    ["Silver_Oil", "Silver_Oil", "Black_Oil", "Discipline_and_Training"],
    ["Amber_Oil", "Amber_Oil", "Verdant_Oil", "Quickstep"],
    ["Crimson_Oil", "Black_Oil", "Black_Oil", "Corruption"],
    ["Opalescent_Oil", "Azure_Oil", "Violet_Oil", "Ballistics"],
    ["Silver_Oil", "Silver_Oil", "Silver_Oil", "Sovereignty"],
    ["Golden_Oil", "Amber_Oil", "Verdant_Oil", "Disciple_of_the_Slaughter"],
    ["Opalescent_Oil", "Opalescent_Oil", "Golden_Oil", "Barbarism"],
    ["Silver_Oil", "Sepia_Oil", "Violet_Oil", "Lethality"],
    ["Sepia_Oil", "Violet_Oil", "Violet_Oil", "Grave_Intentions"],
    ["Sepia_Oil", "Teal_Oil", "Indigo_Oil", "Bastion_Breaker"],
    ["Golden_Oil", "Verdant_Oil", "Azure_Oil", "Breath_of_Flames"],
    ["Golden_Oil", "Black_Oil", "Black_Oil", "Inveterate"],
    ["Clear_Oil", "Sepia_Oil", "Verdant_Oil", "Ancestral_Knowledge"],
    ["Opalescent_Oil", "Sepia_Oil", "Crimson_Oil", "Soul_Thief"],
    ["Teal_Oil", "Teal_Oil", "Azure_Oil", "Steelwood_Stance"],
    ["Verdant_Oil", "Crimson_Oil", "Black_Oil", "One_With_Nature"],
    ["Silver_Oil", "Teal_Oil", "Crimson_Oil", "Blunt_Trauma"],
    ["Verdant_Oil", "Verdant_Oil", "Azure_Oil", "Arsonist"],
    ["Opalescent_Oil", "Golden_Oil", "Amber_Oil", "Dirty_Techniques"],
    ["Amber_Oil", "Amber_Oil", "Black_Oil", "Divine_Fury"],
    ["Clear_Oil", "Opalescent_Oil", "Sepia_Oil", "Berserking"],
    ["Silver_Oil", "Sepia_Oil", "Sepia_Oil", "Fangs_of_Frost"],
    ["Violet_Oil", "Crimson_Oil", "Crimson_Oil", "Light_of_Divinity"],
    ["Golden_Oil", "Teal_Oil", "Indigo_Oil", "Veteran_Soldier"],
    ["Clear_Oil", "Verdant_Oil", "Teal_Oil", "Robust"],
    ["Clear_Oil", "Amber_Oil", "Azure_Oil", "Poisonous_Fangs"],
    ["Clear_Oil", "Teal_Oil", "Crimson_Oil", "Warrior_Training"],
    ["Indigo_Oil", "Crimson_Oil", "Black_Oil", "Field_Medicine"],
    ["Opalescent_Oil", "Amber_Oil", "Teal_Oil", "Juggernaut"],
    ["Verdant_Oil", "Violet_Oil", "Black_Oil", "Aggressive_Bastion"],
    ["Clear_Oil", "Opalescent_Oil", "Violet_Oil", "Blade_Barrier"],
    ["Opalescent_Oil", "Opalescent_Oil", "Amber_Oil", "Fatal_Blade"],
    ["Opalescent_Oil", "Golden_Oil", "Sepia_Oil", "Art_of_the_Gladiator"],
    ["Amber_Oil", "Violet_Oil", "Violet_Oil", "Intuition"],
    ["Clear_Oil", "Golden_Oil", "Black_Oil", "Endurance"],
    ["Clear_Oil", "Verdant_Oil", "Violet_Oil", "Deep_Thoughts"],
    ["Sepia_Oil", "Verdant_Oil", "Violet_Oil", "Heavy_Draw"],
    ["Silver_Oil", "Azure_Oil", "Crimson_Oil", "Runesmith"],
    ["Verdant_Oil", "Verdant_Oil", "Teal_Oil", "Fury_Bolts"],
    ["Sepia_Oil", "Amber_Oil", "Azure_Oil", "Elemental_Focus"],
    ["Sepia_Oil", "Azure_Oil", "Crimson_Oil", "Clever_Construction"],
    ["Golden_Oil", "Amber_Oil", "Crimson_Oil", "Bloodless"],
    ["Silver_Oil", "Amber_Oil", "Crimson_Oil", "Explosive_Elements"],
    ["Silver_Oil", "Silver_Oil", "Golden_Oil", "Spiritual_Aid"],
    ["Opalescent_Oil", "Silver_Oil", "Indigo_Oil", "Natural_Remedies"],
    ["Clear_Oil", "Silver_Oil", "Black_Oil", "Purity_of_Flesh"],
    ["Sepia_Oil", "Verdant_Oil", "Azure_Oil", "Battle_Rouse"],
    ["Amber_Oil", "Azure_Oil", "Black_Oil", "Ambidexterity"],
    ["Opalescent_Oil", "Opalescent_Oil", "Opalescent_Oil", "Tireless"],
    ["Clear_Oil", "Silver_Oil", "Golden_Oil", "Vitality_Void"],
    ["Verdant_Oil", "Violet_Oil", "Violet_Oil", "Spinecruncher"],
    ["Sepia_Oil", "Teal_Oil", "Teal_Oil", "Deep_Wisdom"],
    ["Silver_Oil", "Violet_Oil", "Violet_Oil", "Merciless_Skewering"],
    ["Clear_Oil", "Opalescent_Oil", "Teal_Oil", "Wrecking_Ball"],
    ["Opalescent_Oil", "Sepia_Oil", "Azure_Oil", "Admonisher"],
    ["Silver_Oil", "Azure_Oil", "Violet_Oil", "Primeval_Force"],
    ["Teal_Oil", "Teal_Oil", "Black_Oil", "Warrior's_Blood"],
    ["Clear_Oil", "Indigo_Oil", "Black_Oil", "Assured_Strike"],
    ["Amber_Oil", "Crimson_Oil", "Crimson_Oil", "Nimbleness"],
    ["Verdant_Oil", "Crimson_Oil", "Crimson_Oil", "Arcane_Focus"],
    ["Opalescent_Oil", "Teal_Oil", "Teal_Oil", "Dazzling_Strikes"],
    ["Sepia_Oil", "Azure_Oil", "Black_Oil", "Primal_Spirit"],
    ["Teal_Oil", "Indigo_Oil", "Crimson_Oil", "Harpooner"],
    ["Silver_Oil", "Azure_Oil", "Black_Oil", "Arcane_Potency"],
    ["Clear_Oil", "Clear_Oil", "Amber_Oil", "Wisdom_of_the_Glade"],
    ["Clear_Oil", "Azure_Oil", "Black_Oil", "Twin_Terrors"],
    ["Golden_Oil", "Amber_Oil", "Azure_Oil", "Doom_Cast"],
    ["Opalescent_Oil", "Silver_Oil", "Violet_Oil", "Leadership"],
    ["Sepia_Oil", "Amber_Oil", "Indigo_Oil", "Replenishing_Remedies"],
    ["Azure_Oil", "Crimson_Oil", "Crimson_Oil", "Harrier"],
    ["Sepia_Oil", "Amber_Oil", "Teal_Oil", "Weathered_Hunter"],
    ["Amber_Oil", "Teal_Oil", "Black_Oil", "Defiance"],
    ["Verdant_Oil", "Verdant_Oil", "Black_Oil", "Trickery"],
    ["Golden_Oil", "Amber_Oil", "Indigo_Oil", "Presage"],
    ["Silver_Oil", "Teal_Oil", "Azure_Oil", "Gladiator's_Perseverance"],
    ["Silver_Oil", "Silver_Oil", "Violet_Oil", "Thick_Skin"],
    ["Clear_Oil", "Teal_Oil", "Black_Oil", "Arcane_Guarding"],
    ["Opalescent_Oil", "Opalescent_Oil", "Violet_Oil", "Bravery"],
    ["Sepia_Oil", "Sepia_Oil", "Amber_Oil", "Proficiency"],
    ["Teal_Oil", "Crimson_Oil", "Crimson_Oil", "Heartseeker"],
    ["Violet_Oil", "Violet_Oil", "Black_Oil", "Graceful_Assault"],
    ["Sepia_Oil", "Amber_Oil", "Black_Oil", "Cleaving"],
    ["Opalescent_Oil", "Verdant_Oil", "Teal_Oil", "Sleight_of_Hand"],
    ["Clear_Oil", "Amber_Oil", "Black_Oil", "Exceptional_Performance"],
    ["Amber_Oil", "Verdant_Oil", "Crimson_Oil", "Primal_Manifestation"],
    ["Opalescent_Oil", "Violet_Oil", "Black_Oil", "Claws_of_the_Hawk"],
    ["Opalescent_Oil", "Violet_Oil", "Crimson_Oil", "Disciple_of_the_Unyielding"],
    ["Sepia_Oil", "Azure_Oil", "Azure_Oil", "Claws_of_the_Magpie"],
    ["Clear_Oil", "Opalescent_Oil", "Opalescent_Oil", "Avatar_of_the_Hunt"],
    ["Clear_Oil", "Sepia_Oil", "Black_Oil", "Testudo"],
    ["Clear_Oil", "Clear_Oil", "Black_Oil", "Annihilation"],
    ["Clear_Oil", "Crimson_Oil", "Crimson_Oil", "Shaper"],
    ["Clear_Oil", "Clear_Oil", "Verdant_Oil", "Prowess"],
    ["Opalescent_Oil", "Amber_Oil", "Black_Oil", "Feller_of_Foes"],
    ["Verdant_Oil", "Teal_Oil", "Crimson_Oil", "Hatchet_Master"],
    ["Opalescent_Oil", "Silver_Oil", "Golden_Oil", "Tribal_Fury"],
    ["Golden_Oil", "Golden_Oil", "Golden_Oil", "Whispers_of_Doom"],
    ["Black_Oil", "Black_Oil", "Black_Oil", "Disciple_of_the_Forbidden"],
    ["Silver_Oil", "Violet_Oil", "Black_Oil", "Hematophagy"],
    ["Sepia_Oil", "Verdant_Oil", "Crimson_Oil", "Master_Fletcher"],
    ["Teal_Oil", "Violet_Oil", "Crimson_Oil", "Static_Blows"],
    ["Clear_Oil", "Sepia_Oil", "Amber_Oil", "Thief's_Craft"],
    ["Silver_Oil", "Golden_Oil", "Azure_Oil", "Golem_Commander"],
    ["Clear_Oil", "Clear_Oil", "Violet_Oil", "Practical_Application"],
    ["Clear_Oil", "Silver_Oil", "Crimson_Oil", "Death_Attunement"],
    ["Golden_Oil", "Sepia_Oil", "Azure_Oil", "Heart_of_Thunder"],
    ["Violet_Oil", "Crimson_Oil", "Black_Oil", "Fire_Walker"],
    ["Azure_Oil", "Azure_Oil", "Crimson_Oil", "Holy_Dominion"],
    ["Verdant_Oil", "Violet_Oil", "Crimson_Oil", "Butchery"],
    ["Silver_Oil", "Golden_Oil", "Teal_Oil", "Essence_Surge"],
    ["Clear_Oil", "Amber_Oil", "Violet_Oil", "Weapon_Artistry"],
    ["Silver_Oil", "Golden_Oil", "Golden_Oil", "Prismatic_Skin"],
    ["Amber_Oil", "Violet_Oil", "Crimson_Oil", "Utmost_Intellect"],
    ["Violet_Oil", "Violet_Oil", "Crimson_Oil", "Aspect_of_the_Lynx"],
    ["Silver_Oil", "Sepia_Oil", "Azure_Oil", "Blade_of_Cunning"],
    ["Amber_Oil", "Crimson_Oil", "Black_Oil", "Coordination"],
    ["Opalescent_Oil", "Sepia_Oil", "Indigo_Oil", "Surveillance"],
    ["Amber_Oil", "Violet_Oil", "Black_Oil", "Revelry"],
    ["Silver_Oil", "Amber_Oil", "Violet_Oil", "Taste_for_Blood"],
    ["Amber_Oil", "Verdant_Oil", "Black_Oil", "Rampart"],
    ["Golden_Oil", "Teal_Oil", "Black_Oil", "Savage_Wounds"],
    ["Verdant_Oil", "Azure_Oil", "Crimson_Oil", "Flash_Freeze"],
    ["Verdant_Oil", "Teal_Oil", "Black_Oil", "Enigmatic_Reach"],
    ["Sepia_Oil", "Indigo_Oil", "Crimson_Oil", "Mark_the_Prey"],
    ["Sepia_Oil", "Amber_Oil", "Crimson_Oil", "Entropy"],
    ["Indigo_Oil", "Violet_Oil", "Crimson_Oil", "Bannerman"],
    ["Opalescent_Oil", "Verdant_Oil", "Black_Oil", "Blacksmith's_Clout"],
    ["Clear_Oil", "Azure_Oil", "Crimson_Oil", "From_the_Shadows"],
    ["Silver_Oil", "Golden_Oil", "Crimson_Oil", "Void_Barrier"],
    ["Opalescent_Oil", "Silver_Oil", "Silver_Oil", "Skittering_Runes"],
    ["Clear_Oil", "Amber_Oil", "Indigo_Oil", "Harvester_of_Foes"],
    ["Indigo_Oil", "Indigo_Oil", "Crimson_Oil", "Unfaltering"],
    ["Indigo_Oil", "Indigo_Oil", "Indigo_Oil", "Powerful_Bond"],
    ["Amber_Oil", "Teal_Oil", "Crimson_Oil", "Whirling_Barrier"],
    ["Sepia_Oil", "Teal_Oil", "Crimson_Oil", "Utmost_Swiftness"],
    ["Sepia_Oil", "Violet_Oil", "Crimson_Oil", "Redemption"],
    ["Golden_Oil", "Teal_Oil", "Crimson_Oil", "Champion_of_the_Cause"],
    ["Silver_Oil", "Golden_Oil", "Black_Oil", "Revenge_of_the_Hunted"],
    ["Silver_Oil", "Teal_Oil", "Teal_Oil", "Devastating_Devices"],
    ["Verdant_Oil", "Azure_Oil", "Violet_Oil", "Forceful_Skewering"],
    ["Clear_Oil", "Sepia_Oil", "Sepia_Oil", "Agility"],
    ["Golden_Oil", "Golden_Oil", "Teal_Oil", "Golem's_Blood"],
    ["Golden_Oil", "Golden_Oil", "Indigo_Oil", "Anointed_Flesh"],
    ["Teal_Oil", "Indigo_Oil", "Violet_Oil", "Burning_Brutality"],
    ["Amber_Oil", "Amber_Oil", "Crimson_Oil", "Bladedancer"],
    ["Golden_Oil", "Golden_Oil", "Sepia_Oil", "Steadfast"],
    ["Clear_Oil", "Verdant_Oil", "Crimson_Oil", "Blast_Waves"],
    ["Clear_Oil", "Azure_Oil", "Violet_Oil", "Expeditious_Munitions"],
    ["Teal_Oil", "Teal_Oil", "Crimson_Oil", "Wandslinger"],
    ["Clear_Oil", "Golden_Oil", "Sepia_Oil", "Atrophy"],
    ["Sepia_Oil", "Crimson_Oil", "Black_Oil", "Storm_Weaver"],
    ["Golden_Oil", "Teal_Oil", "Azure_Oil", "Heart_of_Flame"],
    ["Clear_Oil", "Violet_Oil", "Violet_Oil", "Pain_Forger"],
    ["Opalescent_Oil", "Golden_Oil", "Teal_Oil", "Lust_for_Carnage"],
    ["Opalescent_Oil", "Violet_Oil", "Violet_Oil", "Hired_Killer"],
    ["Amber_Oil", "Amber_Oil", "Teal_Oil", "Thrill_Killer"],
    ["Opalescent_Oil", "Golden_Oil", "Black_Oil", "Assassination"],
    ["Indigo_Oil", "Violet_Oil", "Black_Oil", "Brand_Equity"],
    ["Violet_Oil", "Violet_Oil", "Violet_Oil", "Enigmatic_Defence"],
    ["Clear_Oil", "Sepia_Oil", "Crimson_Oil", "Galvanic_Hammer"],
    ["Silver_Oil", "Golden_Oil", "Verdant_Oil", "Ravenous_Horde"],
    ["Silver_Oil", "Golden_Oil", "Amber_Oil", "Ethereal_Feast"],
    ["Opalescent_Oil", "Opalescent_Oil", "Silver_Oil", "Blood_Drinker"],
    ["Opalescent_Oil", "Silver_Oil", "Teal_Oil", "Herbalism"],
    ["Teal_Oil", "Teal_Oil", "Violet_Oil", "Elder_Power"],
    ["Opalescent_Oil", "Golden_Oil", "Crimson_Oil", "Heart_of_Ice"],
    ["Golden_Oil", "Amber_Oil", "Violet_Oil", "Trick_Shot"],
    ["Opalescent_Oil", "Silver_Oil", "Black_Oil", "Piercing_Shots"],
    ["Teal_Oil", "Azure_Oil", "Azure_Oil", "Cannibalistic_Rite"],
    ["Clear_Oil", "Clear_Oil", "Silver_Oil", "Arcing_Blows"],
    ["Opalescent_Oil", "Golden_Oil", "Azure_Oil", "Master_of_Blades"],
    ["Silver_Oil", "Silver_Oil", "Azure_Oil", "Frenetic"],
    ["Silver_Oil", "Silver_Oil", "Teal_Oil", "Breath_of_Rime"],
    ["Opalescent_Oil", "Teal_Oil", "Crimson_Oil", "Longshot"],
    ["Opalescent_Oil", "Azure_Oil", "Crimson_Oil", "Dire_Torment"],
    ["Opalescent_Oil", "Golden_Oil", "Verdant_Oil", "Foresight"],
    ["Silver_Oil", "Silver_Oil", "Indigo_Oil", "Watchtowers"],
    ["Silver_Oil", "Black_Oil", "Black_Oil", "Stamina"],
    ["Sepia_Oil", "Black_Oil", "Black_Oil", "Carrion"],
    ["Silver_Oil", "Silver_Oil", "Verdant_Oil", "Instability"],
    ["Silver_Oil", "Azure_Oil", "Azure_Oil", "Bloodletting"],
    ["Clear_Oil", "Teal_Oil", "Teal_Oil", "Saboteur"],
    ["Opalescent_Oil", "Crimson_Oil", "Crimson_Oil", "Tolerance"],
    ["Golden_Oil", "Teal_Oil", "Violet_Oil", "Constitution"],
    ["Amber_Oil", "Teal_Oil", "Violet_Oil", "Vampirism"],
    ["Verdant_Oil", "Azure_Oil", "Azure_Oil", "Bone_Breaker"],
    ["Silver_Oil", "Teal_Oil", "Violet_Oil", "Swagger"],
    ["Silver_Oil", "Sepia_Oil", "Black_Oil", "Crystal_Skin"],
    ["Azure_Oil", "Crimson_Oil", "Black_Oil", "Dervish"],
    ["Verdant_Oil", "Verdant_Oil", "Violet_Oil", "Totemic_Zeal"],
    ["Verdant_Oil", "Teal_Oil", "Indigo_Oil", "Divine_Fervour"],
    ["Golden_Oil", "Verdant_Oil", "Teal_Oil", "Influence"],
    ["Crimson_Oil", "Crimson_Oil", "Black_Oil", "Essence_Extraction"],
    ["Silver_Oil", "Sepia_Oil", "Amber_Oil", "Destructive_Apparatus"],
    ["Silver_Oil", "Indigo_Oil", "Indigo_Oil", "Malicious_Intent"],
    ["Opalescent_Oil", "Silver_Oil", "Verdant_Oil", "Hearty"],
    ["Clear_Oil", "Golden_Oil", "Verdant_Oil", "Enduring_Bond"],
    ["Opalescent_Oil", "Amber_Oil", "Crimson_Oil", "Command_of_Steel"],
    ["Sepia_Oil", "Teal_Oil", "Violet_Oil", "Efficient_Explosives"],
    ["Clear_Oil", "Opalescent_Oil", "Golden_Oil", "Mana_Flows"],
    ["Amber_Oil", "Azure_Oil", "Azure_Oil", "Explosive_Runes"],
    ["Amber_Oil", "Indigo_Oil", "Black_Oil", "Infused_Flesh"],
    ["Silver_Oil", "Silver_Oil", "Crimson_Oil", "Infused"], # Moved To Fix Bugs
    ["Golden_Oil", "Azure_Oil", "Crimson_Oil", "Survivalist"],
    ["Golden_Oil", "Verdant_Oil", "Verdant_Oil", "Insightfulness"],
    ["Opalescent_Oil", "Verdant_Oil", "Indigo_Oil", "Panopticon"],
    ["Sepia_Oil", "Sepia_Oil", "Sepia_Oil", "Expertise"],
    ["Clear_Oil", "Clear_Oil", "Teal_Oil", "Physique"],
    ["Golden_Oil", "Amber_Oil", "Teal_Oil", "Snowforged"],
    ["Silver_Oil", "Sepia_Oil", "Verdant_Oil", "Life_Raker"],
    ["Clear_Oil", "Opalescent_Oil", "Verdant_Oil", "Blast_Radius"],
    ["Sepia_Oil", "Verdant_Oil", "Indigo_Oil", "Relentless"],
    ["Sepia_Oil", "Sepia_Oil", "Black_Oil", "Lightning_Walker"],
    ["Clear_Oil", "Opalescent_Oil", "Crimson_Oil", "Retribution"],
    ["Amber_Oil", "Verdant_Oil", "Verdant_Oil", "Aspect_of_the_Eagle"],
    ["Amber_Oil", "Teal_Oil", "Teal_Oil", "Sanctuary"],
    ["Silver_Oil", "Sepia_Oil", "Indigo_Oil", "Marked_for_Death"],
    ["Clear_Oil", "Opalescent_Oil", "Azure_Oil", "Strong_Arm"],
    ["Golden_Oil", "Indigo_Oil", "Black_Oil", "Season_of_Ice"],
    ["Golden_Oil", "Violet_Oil", "Crimson_Oil", "Fingers_of_Frost"],
    ["Clear_Oil", "Silver_Oil", "Verdant_Oil", "Hunter's_Gambit"],
    ["Opalescent_Oil", "Indigo_Oil", "Crimson_Oil", "Adjacent_Animosity"],
    ["Opalescent_Oil", "Silver_Oil", "Crimson_Oil", "Inexorable"],
    ["Golden_Oil", "Azure_Oil", "Violet_Oil", "Breath_of_Lightning"],
    ["Clear_Oil", "Opalescent_Oil", "Silver_Oil", "Overcharged"],
    ["Opalescent_Oil", "Sepia_Oil", "Amber_Oil", "Fleetfoot"],
    ["Opalescent_Oil", "Silver_Oil", "Sepia_Oil", "Master_of_the_Arena"],
    ["Silver_Oil", "Amber_Oil", "Teal_Oil", "Holy_Fire"],
    ["Sepia_Oil", "Sepia_Oil", "Teal_Oil", "Righteous_Decree"],
    ["Sepia_Oil", "Violet_Oil", "Black_Oil", "Mental_Rapidity"],
    ["Silver_Oil", "Crimson_Oil", "Black_Oil", "Overcharge"],
    ["Opalescent_Oil", "Amber_Oil", "Verdant_Oil", "Titanic_Impacts"],
    ["Sepia_Oil", "Amber_Oil", "Verdant_Oil", "Path_of_the_Savant"],
    ["Clear_Oil", "Clear_Oil", "Clear_Oil", "Alacrity"],
    ["Clear_Oil", "Silver_Oil", "Violet_Oil", "Fatal_Toxins"],
    ["Opalescent_Oil", "Golden_Oil", "Golden_Oil", "Charisma"],
    ["Teal_Oil", "Azure_Oil", "Crimson_Oil", "Fearsome_Force"],
    ["Opalescent_Oil", "Teal_Oil", "Azure_Oil", "Mysticism"],
    ["Silver_Oil", "Amber_Oil", "Black_Oil", "Fervour"],
    ["Silver_Oil", "Golden_Oil", "Violet_Oil", "Heart_of_the_Warrior"],
    ["Clear_Oil", "Clear_Oil", "Sepia_Oil", "Beef"],
    ["Opalescent_Oil", "Opalescent_Oil", "Sepia_Oil", "Prism_Weave"],
    ["Clear_Oil", "Teal_Oil", "Azure_Oil", "Fangs_of_the_Viper"],
    ["Opalescent_Oil", "Opalescent_Oil", "Crimson_Oil", "Vigour"],
    ["Opalescent_Oil", "Amber_Oil", "Azure_Oil", "Amplify"],
    ["Clear_Oil", "Silver_Oil", "Sepia_Oil", "Blade_Master"],
    ["Opalescent_Oil", "Opalescent_Oil", "Verdant_Oil", "Resourcefulness"],
    ["Golden_Oil", "Sepia_Oil", "Crimson_Oil", "Heart_and_Soul"],
    ["Amber_Oil", "Teal_Oil", "Azure_Oil", "Discord_Artisan"],
    ["Silver_Oil", "Silver_Oil", "Amber_Oil", "Arcane_Chemistry"],
    ["Opalescent_Oil", "Silver_Oil", "Azure_Oil", "Blood_Siphon"],
    ["Clear_Oil", "Opalescent_Oil", "Black_Oil", "Skull_Cracking"],
    ["Opalescent_Oil", "Opalescent_Oil", "Teal_Oil", "One_with_the_River"],
    ["Opalescent_Oil", "Verdant_Oil", "Violet_Oil", "Frost_Walker"],
    ["Silver_Oil", "Teal_Oil", "Black_Oil", "Cruel_Preparation"],
    ["Opalescent_Oil", "Amber_Oil", "Violet_Oil", "Throatseeker"],
    ["Silver_Oil", "Verdant_Oil", "Black_Oil", "Profane_Chemistry"],
    ["Golden_Oil", "Sepia_Oil", "Violet_Oil", "Written_in_Blood"],
    ["Opalescent_Oil", "Sepia_Oil", "Violet_Oil", "Melding"],
    ["Silver_Oil", "Crimson_Oil", "Crimson_Oil", "Devotion"],
    ["Amber_Oil", "Amber_Oil", "Azure_Oil", "Hasty_Reconstruction"],
    ["Golden_Oil", "Sepia_Oil", "Teal_Oil", "Nightstalker"],
    ["Clear_Oil", "Sepia_Oil", "Azure_Oil", "Dynamo"],
    ["Opalescent_Oil", "Opalescent_Oil", "Indigo_Oil", "Window_of_Opportunity"],
    ["Sepia_Oil", "Verdant_Oil", "Verdant_Oil", "Fusillade"],
    ["Opalescent_Oil", "Teal_Oil", "Indigo_Oil", "Deep_Breaths"],
    ["Amber_Oil", "Verdant_Oil", "Azure_Oil", "Executioner"],
    ["Teal_Oil", "Indigo_Oil", "Black_Oil", "Forethought"],
    ["Clear_Oil", "Golden_Oil", "Teal_Oil", "Growth_and_Decay"],
    ["Silver_Oil", "Sepia_Oil", "Crimson_Oil", "Deadly_Draw"],
    ["Indigo_Oil", "Indigo_Oil", "Black_Oil", "Undertaker"],
    ["Clear_Oil", "Silver_Oil", "Silver_Oil", "Arcane_Sanctuary"],
    ["Clear_Oil", "Black_Oil", "Black_Oil", "Acrimony"],
    ["Clear_Oil", "Opalescent_Oil", "Amber_Oil", "Brinkmanship"],
    ["Sepia_Oil", "Verdant_Oil", "Teal_Oil", "Decay_Ward"],
    ["Clear_Oil", "Silver_Oil", "Teal_Oil", "Backstabbing"],
    ["Sepia_Oil", "Sepia_Oil", "Violet_Oil", "Inspiring_Bond"],
    ["Amber_Oil", "Black_Oil", "Black_Oil", "Magmatic_Strikes"],
    ["Sepia_Oil", "Amber_Oil", "Amber_Oil", "Hard_Knocks"],
]

Ring_Anoints = [
    ["Clear_Oil","Clear_Oil","Your Chilling Towers deal 25% increased Damage"],
    ["Indigo_Oil","Violet_Oil","Your Meteor Towers create Burning Ground for 3 seconds on Hit"],
    ["Clear_Oil","Verdant_Oil","Your Meteor Towers deal 25% increased Damage"],
    ["Silver_Oil","Silver_Oil","Your Summoning Towers summon 2 additional Minions"],
    ["Clear_Oil","Silver_Oil","Your Arc Towers repeats 1 additional Times"],
    ["Silver_Oil","Black_Oil","Your Empowering Towers also grant 25% increased Damage"],
    ["Crimson_Oil","Crimson_Oil","Your Meteor Towers always Stun"],
    ["Sepia_Oil","Verdant_Oil","Minions summoned by Your Summoning Towers have 25% increased Damage"],
    ["Amber_Oil","Indigo_Oil","Your Arc Towers have 20% chance to inflict Sap"],
    ["Golden_Oil","Golden_Oil","All Towers in range of your Empowering Towers have 50% chance to deal Double Damage"],
    ["Opalescent_Oil","Sepia_Oil","Your Fireball Towers fire an additional 2 Projectiles"],
    ["Silver_Oil","Indigo_Oil","Your Lightning Storm Towers create Storms centred on Enemies"],
    ["Violet_Oil","Violet_Oil","Your Chilling Towers have 25% increased effect of Chill"],
    ["Opalescent_Oil","Silver_Oil","Your Chilling Towers freeze enemies for 0.2 seconds while they are affected by chilling beams"],
    ["Teal_Oil","Black_Oil","Your Imbuing Towers have 25% increased Range"],
    ["Silver_Oil","Violet_Oil","Your Empowering Towers also grant 20% increased Cast Speed"],
    ["Silver_Oil","Teal_Oil","Minions summoned by Your Summoning Towers have 50% increased Life"],
    ["Teal_Oil","Violet_Oil","Your Scout Towers have 25% increased Range"],
    ["Opalescent_Oil","Amber_Oil","Your Flamethrower Towers have 15% increased Cast Speed"],
    ["Verdant_Oil","Indigo_Oil","Your Freezebolt Towers have 20% chance to inflict Brittle"],
    ["Amber_Oil","Violet_Oil","Your Flamethrower Towers have 25% increased Range"],
    ["Opalescent_Oil","Black_Oil","Minions summoned by Your Sentinel Towers have 50% increased Life"],
    ["Indigo_Oil","Indigo_Oil","Minions summoned by Your Sentinel Towers Leech 2% of Damage as Life"],
    ["Clear_Oil","Amber_Oil","Your Fireball Towers deal 25% increased Damage"],
    ["Clear_Oil","Golden_Oil","Your Shock Nova Towers have 25% increased effect of Shock"],
    ["Indigo_Oil","Black_Oil","Minions summoned by Your Scout Towers inflict Malediction on Hit"],
    ["Silver_Oil","Amber_Oil","Your Temporal Towers effects decay 25% slower"],
    ["Sepia_Oil","Crimson_Oil","Your Lightning Storm Towers have 25% increased Range"],
    ["Amber_Oil","Azure_Oil","Your Imbuing Towers have 25% increased Effect"],
    #["Golden_Oil","Black_Oil","Your Shock Nova Towers repeats 2 additional Times (enchant) Your Shock Nova Towers have 30% increased area of effect per repeat (enchant)"],
    #["Golden_Oil","Black_Oil","Your Shock Nova Towers repeats 2 additional Times\nYour Shock Nova Towers have 30% increased area of effect per repeat (enchant)"],
    ["Golden_Oil","Black_Oil","Your Shock Nova Towers repeats 2 additional Times"],
    ["Opalescent_Oil","Teal_Oil","Minions summoned by Your Summoning Towers have 25% increased Movement Speed"],
    ["Golden_Oil","Indigo_Oil","Your Towers deal 10% increased Damage per Type of Tower Active"],
    ["Verdant_Oil","Teal_Oil","Your Stone Gaze Towers have 25% increased Duration"],
    ["Opalescent_Oil","Violet_Oil","Minions summoned by Your Sentinel Towers have 25% increased Movement Speed"],
    ["Sepia_Oil","Azure_Oil","Your Empowering Towers have 25% increased Effect"],
    ["Silver_Oil","Crimson_Oil","Your Imbuing Towers also grant 50% increased Critical Strike Chance"],
    ["Azure_Oil","Black_Oil","Your Smothering Towers have 25% increased Range"],
    ["Sepia_Oil","Teal_Oil","Your Lightning Storm Towers deal 25% increased Damage"],
    ["Verdant_Oil","Black_Oil","Your Empowering Towers have 25% increased Range"],
    ["Amber_Oil","Black_Oil","Your Stone Gaze Cage Towers have 25% increased Range"],
    ["Azure_Oil","Crimson_Oil","Your Fireball Towers have 15% increased Cast Speed"],
    ["Sepia_Oil","Black_Oil","Your Temporal Towers have 25% increased Range"],
    ["Clear_Oil","Violet_Oil","Your Freezebolt Towers have 25% increased Range"],
    ["Violet_Oil","Crimson_Oil","Your Flamethrower Towers deal full damage to Fire Enemies"],
    ["Verdant_Oil","Azure_Oil","Your Chilling Towers have 25% increased Range"],
    ["Opalescent_Oil","Crimson_Oil","Your Shock Nova Towers deal full damage to Lightning Enemies"],
    ["Golden_Oil","Crimson_Oil","Your Smothering Towers also grant 10% reduced Damage"],
    ["Clear_Oil","Black_Oil","Your Seismic Towers have 25% increased Range"],
    ["Sepia_Oil","Amber_Oil","Your Flamethrower Towers deal 25% increased Damage"],
    ["Opalescent_Oil","Indigo_Oil","Cages created by Your Glacial Cage Towers are 20% larger"],
    ["Indigo_Oil","Crimson_Oil","Enemies Petrified by Your Stone Gaze Towers take 10% increased Damage"],
    ["Verdant_Oil","Violet_Oil","Your Meteor Towers have 25% increased Range"],
    ["Azure_Oil","Indigo_Oil","Your Imbuing Towers also grant Onslaught"],
    ["Silver_Oil","Golden_Oil","Your Seismic Towers have 100% increased length and range of Cascades"],
    ["Black_Oil","Black_Oil","Your Lightning Storm Towers have 25% reduced Impact Delay"],
    ["Teal_Oil","Indigo_Oil","Your Temporal Towers also grant Stun Immunity"],
    ["Opalescent_Oil","Verdant_Oil","Your Meteor Towers drop an additional Meteor"],
    ["Sepia_Oil","Indigo_Oil","Your Flamethrower Towers have 20% chance to inflict Scorch"],
    ["Clear_Oil","Indigo_Oil","Your Smothering Towers also grant 10% chance to be Frozen, Shocked and Ignited"],
    ["Clear_Oil","Crimson_Oil","Your Shock Nova Towers have 25% increased Range"],
    ["Silver_Oil","Verdant_Oil","Your Stone Gaze Towers have 20% increased Cooldown Recovery Rate"],
    ["Verdant_Oil","Verdant_Oil","Your Arc Towers deal 25% increased Damage"],
    ["Silver_Oil","Azure_Oil","Your Scout Towers summon an additional minion"],
    ["Teal_Oil","Crimson_Oil","Your Glacial Cage Towers have 20% increased Cooldown Recovery Rate"],
    ["Clear_Oil","Teal_Oil","Minions summoned by Your Sentinel Towers have 25% increased Damage"],
    ["Amber_Oil","Amber_Oil","Minions summoned by Your Scout Towers have 25% increased Damage"],
    ["Verdant_Oil","Crimson_Oil","Your Freezebolt Tower deal full damage to Cold Enemies"],
    ["Amber_Oil","Teal_Oil","Your Seismic Towers deal 25% increased Damage"],
    ["Clear_Oil","Sepia_Oil","Your Freezebolt Towers deal 25% increased Damage"],
    ["Amber_Oil","Crimson_Oil","Your Arc Towers have 25% increased Range"],
    ["Sepia_Oil","Sepia_Oil","Your Glacial Cage Towers have 25% increased Duration"],
    ["Opalescent_Oil","Opalescent_Oil","Your Smothering Towers also grant 20% reduced Movement Speed"],
    #["Opalescent_Oil","Golden_Oil","Your Fireball Towers fire an additional 8 Projectiles (enchant) Your Fireball Towers Projectiles fire in a circle (enchant)"],
    #["Opalescent_Oil","Golden_Oil","Your Fireball Towers fire an additional 8 Projectiles\nYour Fireball Towers Projectiles fire in a circle (enchant)"],
    ["Opalescent_Oil","Golden_Oil","Your Fireball Towers fire an additional 8 Projectiles"],
    ["Silver_Oil","Sepia_Oil","Your Seismic Towers have 25% increased Stun Duration"],
    ["Azure_Oil","Violet_Oil","Your Sentinel Towers have 25% increased Range"],
    ["Opalescent_Oil","Azure_Oil","Minions summoned by Your Scout Towers have 25% increased Movement Speed"],
    ["Golden_Oil","Azure_Oil","Your Stone Gaze Towers have 20% reduced Petrification Delay"],
    ["Golden_Oil","Violet_Oil","Your Imbuing Towers also grant 50% increased Damage"],
    ["Azure_Oil","Azure_Oil","Your Summoning Towers have 25% increased Range"],
    ["Crimson_Oil","Black_Oil","Your Freezebolt Towers fire 2 additional Projectiles"],
    ["Teal_Oil","Teal_Oil","Your Smothering Towers have 25% increased Effect"],
    ["Golden_Oil","Teal_Oil","Your Temporal Towers also grant you 20% increased action speed"],
    ["Sepia_Oil","Violet_Oil","Your Fireball Towers have 25% increased Range"],
    ["Teal_Oil","Azure_Oil","Your Glacial Cage Towers have 25% increased Range"],
    ["Golden_Oil","Verdant_Oil","Your Seismic Towers have an additional Cascade"],
    ["Clear_Oil","Azure_Oil","Your Temporal Towers have 25% increased Effect"],
    ["Clear_Oil","Opalescent_Oil","Enemies inside Glacial Cage take 10% increased Damage"],
    ["Violet_Oil","Black_Oil","Your Chilling Towers have 25% increased Duration"],
    ["Golden_Oil","Amber_Oil","Your Arc Towers have 3 additional chains"],
    ["Golden_Oil","Sepia_Oil","Your Lightning Storm Towers have 25% increased explosion Area of Effect"],
    ["Amber_Oil","Verdant_Oil","Your Shock Nova Towers deal 25% increased Damage"],
]

Settings = {
    #* Actual Settings
    "Stay_On_Top": True,
    "Resizable": False,
    "Work_In_Tray": False,
    "Show_Copied_Text": True,

    #* Window Size
    "Full_Size": "664x540",
    "Min_Size": "400x130",

    #* Misc
    "Version": "1.3",
    "Padding": 3,
}

#! Functions
def Check_Anoint_v2():
    #! Variables
    Copied_Text = PYPERCLIP.paste()
    Counter = 0

    #! Edit TextBox
    TextBox.delete("1.0", GUI.END)
    TextBox.insert("1.0", Copied_Text)

    #! Check If Item Is Corrupted
    if ("Corrupted" in Copied_Text):
        print("Corrupted - Cannot Extract Oils")

    #! If Item Is An Amulet
    elif ("Amulet" in Copied_Text):
        print("AMULET")

        if ("Allocates" in Copied_Text):
            for x in range(len(Valuable_Amulet_Anoint_List)):
                Anoint_Name = Underscore_To_SpaceBar(Valuable_Amulet_Anoint_List[x][3])

                if (Anoint_Name in Copied_Text):
                    Oil_1 = Valuable_Amulet_Anoint_List[x][0]
                    Oil_2 = Valuable_Amulet_Anoint_List[x][1]
                    Oil_3 = Valuable_Amulet_Anoint_List[x][2]
                    print(f"#1: {Oil_1}\n#2: {Oil_2}\n#3: {Oil_3}")

                    Label_1.config(text=f"{Anoint_Name}")
                    Label_2.config(text="Oil #1: ")
                    Label_3.config(text="Oil #2: ")
                    Label_4.config(text="Oil #3: ")
                    Label_5.config(text=f"{Underscore_To_SpaceBar(Oil_1)}", fg=Oil_List[Oil_1])
                    Label_6.config(text=f"{Underscore_To_SpaceBar(Oil_2)}", fg=Oil_List[Oil_2])
                    Label_7.config(text=f"{Underscore_To_SpaceBar(Oil_3)}", fg=Oil_List[Oil_3])

                    break

            if (Counter == len(Valuable_Amulet_Anoint_List)):
                print("ERROR: Wrong Amulet Anoint")

                Label_1.config(text="ERROR: Wrong Amulet Anoint")
                Label_2.config(text="")
                Label_3.config(text="")
                Label_4.config(text="")
                Label_5.config(text="", fg="black")
                Label_6.config(text="", fg="black")
                Label_7.config(text="", fg="black")
        else:
            print("AMULET - Not Anointed")

    #! If Item Is A Ring
    elif ("Ring" in Copied_Text):
        print("RING")

        for x in range(len(Ring_Anoints)):
            Effect = Ring_Anoints[x][2]

            if (Effect in Copied_Text):
                Oil_1 = Ring_Anoints[x][0]
                Oil_2 = Ring_Anoints[x][1]
                
                print(f"#1: {Oil_1}\n#2: {Oil_2}")

                if ("Your Shock Nova Towers repeats 2 additional Times" in Effect):
                    Effect = "Your Shock Nova Towers repeats 2 additional Times\nYour Shock Nova Towers have 30% increased area of effect per repeat"
                elif ("Your Fireball Towers fire an additional 8 Projectiles" in Effect):
                    Effect = "Your Fireball Towers fire an additional 8 Projectiles\nYour Fireball Towers Projectiles fire in a circle"


                Label_1.config(text=f"{Effect}")
                Label_2.config(text="Oil #1: ")
                Label_3.config(text="Oil #2: ")
                Label_5.config(text=f"{Underscore_To_SpaceBar(Oil_1)}", fg=Oil_List[Oil_1])
                Label_6.config(text=f"{Underscore_To_SpaceBar(Oil_2)}", fg=Oil_List[Oil_2])
                Label_4.config(text="")
                Label_7.config(text="")

                break

        if (Counter == len(Ring_Anoints)):
            print("ERROR: Wrong Ring Anoint")

            Label_1.config(text="ERROR: Wrong Ring Anoint")
            Label_2.config(text="")
            Label_3.config(text="")
            Label_4.config(text="")
            Label_5.config(text="", fg="black")
            Label_6.config(text="", fg="black")
            Label_7.config(text="")

    #! If Clipboard Content Is Wrong
    else:
        print("ERROR: Wrong Clipboard Content")

        Label_1.config(text="ERROR: Wrong Clipboard Content")
        Label_2.config(text="")
        Label_3.config(text="")
        Label_4.config(text="")
        Label_5.config(text="")
        Label_6.config(text="")
        Label_7.config(text="")

def SpaceBar_To_Underscore(Text = ""):
    return Text.replace(" ", "_")

def Underscore_To_SpaceBar(Text = ""):
    return Text.replace("_", " ")

def MenuBar_Options(Option = "Stay On Top", Oil = ""):
    print(f"--- === ---\nWIP - MenuBar: {Option}")
    
    #* Exit
    if (Option == "Exit"):
        if (Settings["Work_In_Tray"] == False):
            Window.destroy()
        else:
            #TODO: Minimalize Window To Tray
            Window.withdraw()
            image = Image.open("icon.ico")
            Tray_Menu = (item("Exit", Tray_Exit), item("Show", Tray_Show))
            icon = pystray.Icon("Name", image, "WIP", Tray_Menu)
            icon.run()
    
    #* Stay On Top
    elif (Option == "Stay On Top"):
        if (Settings["Stay_On_Top"] == False):
            Settings["Stay_On_Top"] = True
            Window.attributes("-topmost", True)
        else:
            Settings["Stay_On_Top"] = False
            Window.attributes("-topmost", False)

    #* Resizable
    elif (Option == "Resizable"):
        if (Settings["Resizable"] == False):
            Settings["Resizable"] = True
            Window.resizable(True, True)
        else:
            Settings["Resizable"] = False
            Window.resizable(False, False)

    #* Show Copied Text
    elif (Option == "Show Copied Text"):
        #TODO: Add some auto resize (to something not defined in settings)
        #print(Window.winfo_screenmmwidth())
        #print(Window.winfo_screenheight())

        #New_Window_Size = f"{Window.winfo_screenmmwidth()}x{Window.winfo_screenheight()}"

        if (Settings["Show_Copied_Text"] == False):
            Settings["Show_Copied_Text"] = True
            Label_0.grid(row=0, column=0, columnspan=2)
            TextBox.grid(row=1, column=0, columnspan=2)

            #Window.geometry("%dx%d" % (Window.winfo_screenmmwidth(), Window.winfo_screenheight()))
            #Window.geometry(New_Window_Size)
            Window.geometry(Settings["Full_Size"])
        else:
            Settings["Show_Copied_Text"] = False
            Label_0.grid_forget()
            TextBox.grid_forget()

            #Window.geometry("%dx%d" % (Window.winfo_screenmmwidth(), Window.winfo_screenheight()))
            #Window.geometry(New_Window_Size)
            Window.geometry(Settings["Min_Size"])
    
    #* Work In Tray
    elif (Option == "Work In Tray"):
        if (Settings["Work_In_Tray"]):
            Settings["Work_In_Tray"] = False
        else:
            Settings["Work_In_Tray"] = True

    #* Highlight
    elif (Option == "Highlight"):
        #TODO: WIP
        Temp_Key = "Highlight_" + Oil

        if (Settings[Temp_Key]):
            Settings[Temp_Key] = False
        else:
            Settings[Temp_Key] = True

        print(Settings)

        pass
    
    #* Error
    else:
        print(f"ERROR - No Menu: '{Option}'")

def Tray_Exit(icon, item):
    print("WIP - Exit")
    icon.stop()
    Window.destroy()

def Tray_Show(icon, item):
    print("WIP - Exit")
    icon.stop()
    Window.after(0, Window.deiconify())

def WIP():
    print(Settings)

#! Main
if __name__ == "__main__":
    #* Start
    Window = GUI.Tk()
    Window.title("PoE - Anoint Check")
    Window.geometry(Settings["Full_Size"])
    Window.protocol("WM_DELETE_WINDOW", FUNCTOOLS.partial(MenuBar_Options, "Exit"))
    Window.attributes("-topmost", Settings["Stay_On_Top"])
    if (Settings["Resizable"] == False):
        Window.resizable(False, False)

    #* GUI Elements
    Label_0 = GUI.Label(Window, text="Copied Text:")
    Label_0.grid(row=0, column=0, columnspan=2)

    TextBox = SCROLLEDTEXT.ScrolledText(Window)
    TextBox.grid(row=1, column=0, columnspan=2)

    Button_1 = GUI.Button(Window, text="Check Annoint", command=Check_Anoint_v2, padx=Settings["Padding"], pady=Settings["Padding"])
    Button_1.grid(row=2, column=0, columnspan=2)

    Label_1 = GUI.Label(Window, text=f"Anoint: WIP", padx=Settings["Padding"], pady=Settings["Padding"])
    Label_1.grid(row=3, column=0, columnspan=2)

    Label_2 = GUI.Label(Window, text=f"Oil #1:", padx=Settings["Padding"], pady=Settings["Padding"])
    Label_2.grid(row=4, column=0)

    Label_3 = GUI.Label(Window, text=f"Oil #2:", padx=Settings["Padding"], pady=Settings["Padding"])
    Label_3.grid(row=5, column=0)

    Label_4 = GUI.Label(Window, text=f"Oil #3:", padx=Settings["Padding"], pady=Settings["Padding"])
    Label_4.grid(row=6, column=0)

    Label_5 = GUI.Label(Window, padx=Settings["Padding"], pady=Settings["Padding"])
    Label_5.grid(row=4, column=1)

    Label_6 = GUI.Label(Window, padx=Settings["Padding"], pady=Settings["Padding"])
    Label_6.grid(row=5, column=1)

    Label_7 = GUI.Label(Window, padx=Settings["Padding"], pady=Settings["Padding"])
    Label_7.grid(row=6, column=1)

    #* Menu
    MenuBar = GUI.Menu(Window)

        #* Menu - Variables
    Settings_StayOnTop = GUI.BooleanVar()
    Settings_Resizable = GUI.BooleanVar()
    Settings_WorkInTray = GUI.BooleanVar()
    Settings_CopiedText = GUI.BooleanVar()

    Menu_CheckBoxes = [Settings_StayOnTop, Settings_Resizable, Settings_WorkInTray, Settings_CopiedText]

    CheckBox_Counter = 0
    for Key, Value in Settings.items():
        #print(f"Settings{Key}: {Value}")
        if (Key == "Full_Size" or Key == "Min_Size" or Key == "Version" or Key == "Padding"):
            continue

        if (Value == True):
            Menu_CheckBoxes[CheckBox_Counter].set(1)

        CheckBox_Counter += 1

        #* Menu - Settings
    MenuBar_Settings = GUI.Menu(MenuBar, tearoff=0)
    MenuBar_Settings.add_checkbutton(label="Stay On Top", command=FUNCTOOLS.partial(MenuBar_Options, "Stay On Top"), onvalue=1, offvalue=0, variable=Settings_StayOnTop)
    MenuBar_Settings.add_checkbutton(label="Resizable", command=FUNCTOOLS.partial(MenuBar_Options, "Resizable"), onvalue=1, offvalue=0, variable=Settings_Resizable)
    MenuBar_Settings.add_checkbutton(label="Work In Tray", command=FUNCTOOLS.partial(MenuBar_Options, "Work In Tray"), onvalue=1, offvalue=0, variable=Settings_WorkInTray)
    MenuBar_Settings.add_checkbutton(label="Show Copied Text", command=FUNCTOOLS.partial(MenuBar_Options, "Show Copied Text"), onvalue=1, offvalue=0, variable=Settings_CopiedText)
    MenuBar_Settings.add_separator()
    MenuBar_Settings.add_command(label="Exit", command=FUNCTOOLS.partial(MenuBar_Options, "Exit"))
    MenuBar_Settings.add_separator()
    MenuBar_Settings.add_command(label="WIP: Print Settings", command=WIP)
    MenuBar_Settings.add_separator()
    MenuBar_Settings.add_command(label=f"Version: {Settings['Version']}", state=GUI.DISABLED, activebackground="#f0f0f0")

        #* Menu - End
    MenuBar.add_cascade(label="Settings", menu=MenuBar_Settings)
    Window.config(menu=MenuBar)

    Window.mainloop()