# RPG Game with LÖVE and Lua

## Overview

Welcome to an interactive RPG game experience! This project demonstrates how to build a tile-based RPG world using **LÖVE** (Love2D), a powerful framework for creating 2D games in Lua. Drawing inspiration from classic RPG games like *The Legend of Zelda*, *Stardew Valley*, and *Pokémon*, this project showcases the fundamental mechanics of game development: sprite rendering, collision detection, player movement, and tilemap-based level design.

## Project Description

This RPG game features:
- **Dynamic Tilemap System**: A grid-based world composed of tiles representing walkable floors and obstacles (trees)
- **Pixel Art Characters**: A playable character (dinosaur sprite) that you control throughout the game world
- **Collision Detection**: Seamless collision mechanics that prevent the player from walking through walls and obstacles
- **Smooth Player Movement**: Responsive keyboard controls with support for diagonal movement and normalized speed

The game world is rendered using custom pixel art sprites, creating an aesthetically pleasing retro-style RPG experience. The tilemap is defined through code, allowing for easy customization and expansion of the game world.

## Project Structure

```
RPG Game/
├── main.lua              (Main game loop - Entry point)
├── player.lua            (Player class with movement and collision handling)
├── map.lua               (Map class with tilemap data and collision detection)
├── Hungry-dino 2.png     (Player character sprite)
└── tree.png              (Obstacle/wall sprite)
```

### File Descriptions

**main.lua**
- Serves as the entry point for the LÖVE framework
- Implements the three core LÖVE callbacks: `love.load()`, `love.update()`, and `love.draw()`
- Initializes the player and map objects
- Manages the main game loop and renders all game elements

**player.lua**
- Defines the `Player` class with position, speed, and sprite data
- Handles player input (W, A, S, D keys and arrow keys)
- Updates player position each frame with collision-aware movement
- Renders the player sprite on the screen with proper scaling

**map.lua**
- Defines the `Map` class containing the tilemap data
- Represents the game world as a 2D grid where `1` = wall and `0` = floor
- Implements collision detection to check if a position overlaps with walls
- Renders the tilemap using tree sprites for obstacles

## Prerequisites

Before running this project, ensure you have the following installed:

- **LÖVE 2D Framework** (version 11.x or later)
  - Download from: [love2d.org](https://love2d.org/)
  - Installation instructions are available on their official website

## Getting Started

### Installation

1. **Clone or download the project** to your local machine
2. **Place sprite images** in the project directory:
   - `Hungry-dino 2.png` - Player character sprite (approximately 32x32 pixels)
   - `tree.png` - Obstacle/wall sprite (approximately 32x32 pixels)

3. **Ensure all files are in the same directory**:
   - main.lua
   - player.lua
   - map.lua
   - Sprite image files

## Controls

Use the following keys to navigate the game world:

| Key(s) | Action |
|--------|--------|
| **W** or **↑** | Move Up |
| **S** or **↓** | Move Down |
| **A** or **←** | Move Left |
| **D** or **→** | Move Right |
| **ESC** | Quit Game |

**Note**: Diagonal movement is supported and normalized to maintain consistent speed in all directions.

## Game Mechanics

### Movement System
- The player moves at a constant speed of 120 pixels per second
- Movement input is processed each frame based on keyboard state
- Diagonal movement is automatically normalized to prevent faster movement on diagonals

### Collision Detection
- The game uses axis-aligned bounding box (AABB) collision detection
- The player's collision size is defined as a 20x20 pixel square
- Collision checks occur separately on X and Y axes for smooth corner-sliding behavior
- The tilemap defines obstacles at a 32x32 pixel tile size

### Tilemap Data
The game world is represented as a 2D array:
- `1` = Wall/Obstacle (rendered as a tree sprite)
- `0` = Floor/Walkable area

Players cannot walk through tiles marked as walls.

## Customization Guide

### Changing Sprites
Replace the sprite image files with your own pixel art:
- Keep dimensions around 32x32 or 64x64 pixels for best results
- Ensure filenames match those referenced in the code

## Technical Details

### LÖVE Framework Callbacks

**love.load()**
- Called once when the game starts
- Initializes the window, player, and map objects

**love.update(dt)**
- Called every frame with `dt` (delta time) in seconds
- Updates player position based on input

**love.draw()**
- Called every frame after update
- Renders the background, tilemap, and player sprite

This ensures visual consistency across different sprite dimensions.

## Learning Outcomes

This project demonstrates fundamental game development concepts:
- ✓ Game loop architecture
- ✓ Object-oriented programming in Lua
- ✓ Sprite-based graphics rendering
- ✓ Input handling and player control
- ✓ Collision detection algorithms
- ✓ Tilemap-based level design
- ✓ Delta-time independent movement

## Credits
Ellie.P from Codedex Community
