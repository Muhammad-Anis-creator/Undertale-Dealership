# Undertale Car Dealership

---

## Description

This project is a Python game inspired by Undertale’s humor and aesthetics, combined with a car dealership simulation mechanic. The idea was to merge a narrative-driven style with an interactive shop system, creating a unique blend of RPG and resource-management gameplay.

The game mixes car dealership simulation with RPG-style progression, drawing inspiration from Undertale. Characters have unique personalities reflected in their dialogues, offering three options per brand. A detailed description of each car is then presented with the option to “buy” it.

Players interact with cars as if they were characters making customization choices. Visuals are handled via **pygame**, while image manipulation and GIF support are provided by **Pillow (PIL)**. This combination allows for sprite-like animations and dynamic rendering within the dealership environment.

---

## Files

- **project.py**  
  Contains the main game loop. Handles rendering the shop, player interactions, and loading resources such as images, sounds, and dialogue.

- **test_project.py**  
  Unit tests for helper functions like `load_car_data`, `gif_framerate`, and `draw_bought_box`. Written using `pytest`.

- **car_data.json** (if applicable)  
  Stores structured information about available cars, making it easy to edit or update without changing the main code.

- **assets/**  
  Contains images, GIFs, and sound effects used in the game.

---

## Design Choices

I considered using **Tkinter** for graphics but chose **Pygame** because it provides more control over animations and the game loop. **Pillow** was included for GIF support since Pygame alone does not handle them smoothly.

The game structure is organized to simplify development. I grouped and initialized variables inside the game loop to keep track of multiple elements. As a beginner, I opted for a more straightforward, “hardcoded” approach rather than attempting more advanced systems that would require a steep learning curve.

Typing effects using **textwrap** were implemented to display dialogue in a typewriter style, accompanied by sound effects, giving the game a more immersive Undertale-like feel. Speech bubbles and text presentation were designed to enhance the roleplay aspect, making the interactions more engaging and fun.

I used **JSON** for data storage, both to practice importing structured data and to allow easier editing of characters and cars.

I had initially planned to implement pixel-style sprites, but due to copyright restrictions and time constraints, I opted for realistic car images instead. Similarly, while more gameplay options and a receipt-tracking feature were considered, I focused on the core mechanics to manage the learning curve and ensure the project was functional and enjoyable.

Tests were written to verify data loading and rendering helper functions, rather than the full game loop, because automated testing of graphical interfaces is more complex.

---

## Future Improvements

- Expand dialogue and branching choices.  
- Add save/load functionality for inventory.  
- Improve animation smoothness with sprite sheets instead of GIF frames.  
- Build an installer or executable to make the game more accessible.

---

Overall, this project challenged me to integrate **game development, file handling, and image processing** in Python. Writing tests, managing external libraries, and debugging imports in different environments taught me valuable skills for handling real-world project complexity.
