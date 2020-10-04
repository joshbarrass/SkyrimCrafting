# Skyrim Crafting Helper

Program designed to help find the best ways to make profit in Skyrim using Smithing and Alchemy.

[![Build Status](https://api.travis-ci.com/joshbarrass/SkyrimCrafting.svg?branch=master)](https://travis-ci.com/joshbarrass/SkyrimCrafting)
[![Code Climate](https://codeclimate.com/github/joshbarrass/SkyrimCrafting/badges/gpa.svg)](https://codeclimate.com/github/joshbarrass/SkyrimCrafting)
[![Test Coverage](https://codeclimate.com/github/joshbarrass/SkyrimCrafting/badges/coverage.svg)](https://codeclimate.com/github/joshbarrass/SkyrimCrafting/coverage)
[![Issue Count](https://codeclimate.com/github/joshbarrass/SkyrimCrafting/badges/issue_count.svg)](https://codeclimate.com/github/joshbarrass/SkyrimCrafting)

**Disclaimer:** this repository is still a work in progress. When (or if) it becoems useful in its own right is very much dependent on whether I get the time to work on it. You are welcome to add contributions if you think they would be helpful, but, given the current bare state of the repo, I would prefer if you raised an issue first and allowed me to share my thoughts on the matter. Due to how (relatively) little has been done, it is not outwardly clear where the project is going, and I may have design decisions in mind that I do not wish to compromise on that might cause a PR to be rejected if you do not consult me first.

## Introduction

Whilst there are many tools out there already that aim to solve the same problem as this one, I have never managed to find one that does exactly what I desire. Most seem to be focused on crafting based on what you already have in your inventory, and only return the objective value of the resultant items. This tool aims to fill that gap. By taking into account the player's speech levels/perks/bonuses and a merchant's inventory, as well as the relevant crafting skills and the player's existing inventory, this tool aims to help you make the most profit you can, even if that profit requires you to buy items. I want to take into account the buy and sell prices in the game to give you a true idea of how much gold your crafting will make you, all in one single tool.

## Data

In order to do this, the program obviously needs an understanding of the game's items. This data has been taken primarily from [the UESP](en.uesp.net) (and which I am very thankful for). The goal is to be able to construct a database of all the potion and crafting ingredients in the game, which will provide an efficient way of searching this data to look for recipes. This will be useful to players who aren't interested in the tool's money-making functions, but simply desire an offline copy of the game's recipes to look through themselves.

## Roadmap

 - [x] Database structure to properly, but also generically, represent the game's recipes
 - [ ] Populate database with alchemy items and effects
 - [ ] Implement alchemy logic
   - [ ] Correct potion and properties from two or three ingredients (and skills!)
   - [ ] Optimising potion properties (e.g. gold, magnitude, etc.) for a list of known ingredients
 - [ ] Populate database with crafting items and recipes
 - [ ] Implement crafting logic
   - [ ] Correct crafting result and properties given the right number of ingredients (and skills!)
   - [ ] Optimising for gold/experience for a list of known ingredients
     - [ ] Should be recursive, e.g. being able to make an iron ingot from iron ore to then use in crafting
 - [ ] Implement Speechcraft logic
