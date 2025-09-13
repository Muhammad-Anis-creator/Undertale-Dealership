#-------------------------------
# Libraries
#-------------------------------


import pygame # game mechanics
from PIL import Image, ImageEnhance # Image, Gif rendering
import random  # implement randomness in speech
import textwrap  #  undertale typing effect
import json # import car info
 
#----------------------------------------
# Class Blueprint 
#-----------------------------------------

class UndertaleCharacters:

    """

    Purpose : blueprint/organization of the 5 characters (Sans, Chara, Flowey, Papyrus, Toriel) and backgrounds

    Attribues:
        image(str) : picture of the character from the "Character.gif"
        typing_sound(str) : sound when the text is being written
        last_update (int) : track the appearence of letters
        frame_delay_ms (int) : time between gif frame changes
        frame_index : keep track of the no. of frames for image
        surface : where it's being placed
    
    Methods:
        gif frames (): this helps put the images into a frame list
        gif framerate (): helps change the frames for the gif animation
    
    """


    #intialising each object of this class
    def __init__(self, image, typing_sound = None):
        self._image = image 
        self.typing__sound = typing_sound


    #getters
    @property
    def typing_sound(self):
        return self.typing__sound 
    
    @property
    def image(self):
        return self._image



    def gif_frames(self):

        """
        input : Images
        output : Images in a list

        """


        frames = []
        image_gif = Image.open(self.image)
        try:
            while True:
                frames.append(image_gif.copy())
                image_gif.seek(image_gif.tell() + 1)
        except EOFError:
            pass
        
        return frames  
    



#-----------------------------------------------------
# Constants
#-----------------------------------------------------




#speech Text
SANS_JOKES = [ 
    "Heya. Welcome to the world of cars... don't worry, I won't drive you crazy... yet.",

    "You lookin' for wheels or laughs? Maybe both.",

    "You know, I could tell you the top speed of every car here... but I'll just let the graphics do the talking.",

    "Fast cars, pixelated jokes... welcome aboard.",

    "Sit tight. I'll guide you through these... vehicular adventures.",
]

SANS_TEXT_MAIN = [
    "Alright, here is the scoop, buddy, weve got a pretty wild lineup parked here - Toyota, Jetour, Flowey, and Toriel. Yeah, I know, its like a car show crashed into a weird dream... ",

    "but Im rollin with it. Were still out scavengin for more car experts, but for now, thats the gang. Wanna see what theyre packin?",

    "Just click an option, and one of my pals - or, uh, mortal enemies - will take the wheel and show ya around. So kick back, take a look,",

    "and if you ever need a dose of top-grade, bone-dry humor... you know where to find me. Ill be right here, ready to hit you with a pun so bad it stalls the engine.",
    ]

SANS_PUNS = [
    "When does a skeleton laugh?...........When someone tickles his funny bone!",

    "Why don't skeletons fight each other?...........They don't have the guts",

    "What do skeletons hate the most about wind?...........Nothing, it goes right through them.",

    "Papyrus stood by the fire for too long............Now he's BONE-dry",

    "That annoying dog came back and stole more of our bones. He even ran off with Papyrus' left leg!...........You could say he didn't leave him with a leg to stand on!",

    "What do you call a skeleton snake?...........A rattler!",

    "Have you seen my brother?...........I have a BONE to pick with him.",

    "Cruisers are fun... they really help you roll with the punches... or the ribs.",

    "This Toyota moves so fast, it's scary... almost spine-tingling.",

    "Hybrid cars are great... they save fuel and skeleton bones alike.",

    "Toyota's got more SUVs than I've got bones.",

    "Jetour... sounds like a pun... but it's actually a car.",

    "BMW stands for 'blazing my way'... nah, just kidding, it's Bavarian Motor Works.",

    "Fun fact: the fastest car here could probably outrun me... barely.",

    "Caution: some of these cars might make your wallet lighter than my skull.",
]

CHARA_MAIN_TEXT =[
    "Heh... so you want to know about Toyota, huh? They're famous for building cars that last forever.",
    "Fun fact: the Toyota Corolla is the best-selling car in the world with over 50 million sold! Anyway... take a look. Which one will you choose?",

]

FLOWEY_MAIN_TEXT = [
    "Howdy, friend~! Heehee... looks like you've stumbled upon something special! Not just any ol' hunk of metal, no, no... This is Jetour! Sleek, shiny, and oh sosmooooth. It's not just a car... it's a companion on your journey!",
"Imagine it zipping down the road, the wind in your hair, the world racing past! With Jetour, every trip feels like an adventure! And guess what? It's waiting just for you.",
"Aaaaw, don't be shy... step inside! I promise it'll take you exactly where you want to go. Heehee... or maybe even somewhere you didn't expect…"
]

PAPYRUS_MAIN_TEXT = [
    "NYEH HEH HEH! HUMAN! Feast your eyes upon the HONDA! It is strong! It is reliable! It is... as COOL as I AM! With this magnificent machine,",
    "you'll SPEED along the highways with GREATNESS and STYLE! Buy a Honda, and you'll practically be a member of the ROYAL GUARD already! NYEH HEH HEH!"
]

TORIEL_MAIN_TEXT = [
    "Hello, my child… Ah, I see you are searching for something safe, something comfortable. May I suggest the BMW?",
    "It will cradle you gently as you travel, protecting you as if it were family. Its strength and grace will carry you far, without worry.",
    "Please, take care on the road... and let the BMW take care of you."
]

WINDOW_SIZE = (1280, 720)

#colours
WHITE = (255, 255, 255)
BLACK = (0,0,0)

CHARA_COLOR = [(255, 255, 153), (220, 200, 200), (160, 50, 50)] #chara page colours
FLOWEY_COLOR = [(255, 153, 153), (255,204,204), (204,102,102)] #flowey page colours 
PAPYRUS_COLOR = [(153, 204, 255), (204,229,255),(102,153,204)] #papyrus page colours
TORIEL_COLOR = [(204, 153, 255), (229,204,255), (153,102,204)] #toriel page colours




#speech Bubble
SPEECH_BUBBLE_BORDER_RADIUS = 20  
SPEECH_BUBBLE_SIZE = (750,250)
SPEECH_BUBBLE_POS = (475,450)


#escape Button
ESCAPE_BUTTON_SIZE = (150,100)

#animations
FRAME_DELAY_MS = 100 #when to swtich frames
PADDING = 10 


#text
CHARACTER_WIDTH = 37
TYPING_DELAY = 70


#character Box Variables
CHARATER_BOX = (125,125) #pos
CAR_NAME_ANIMATION_SIZE = (100,50) 
TARGET_Y = 330  #end-point of car name animation (sans page)
TARGET_YX = 390 #end-point of car name animation (chara page)
HOVER_EFFECT = (20,20)



#character intializations

#sans
SANS_IMAGE = "Assets/Character Pictures/Sans.gif"
SANS_TYPING_SOUND = "Assets/Others/Sans.wav"

#chara
CHARA_IMAGE = "Assets/Character Pictures/chara.gif"
CHARA_TYPING_SOUND = "Assets/Others/Chara.wav"

#flowey
FLOWEY_IMAGE = "Assets/Character Pictures/Flowey.gif"
FLOWEY_TYPING_SOUND = "Assets/Others/Flowey.wav"

#papyrus
PAPYRUS_IMAGE = "Assets/Character Pictures/Papyrus.png"
PAPYRUS_TYPING_SOUND = "Assets/Others/Papyrus.wav"

#poriel
TORIEL_IMAGE = "Assets/Character Pictures/Toriel.png"
TORIEL_TYPING_SOUND = "Assets/Others/Toriel.wav"

#---------------------------------------------------------------------------------
# Chara Toyota
#--------------------------------------------------------------------------------

#toyota cars
LAND_CRUISER_PATH = "Assets/Car Pictures/Toyota_Land_Cruiser.jpg"
CAMRY_PATH = "Assets/Car Pictures/Toyota_Camry.jpg"
FORTUNER_PATH = "Assets/Car Pictures/Toyota_Fortuner.jpg"


LAND_CRUISER_ICON = "Assets/Car Pictures/suv-car-icon.png"
CAMRY_ICON = "Assets/Car Pictures/sedan-car-icon.png"
FORTUNER_ICON = "Assets/Car Pictures/hatchback-car-icon.png"


#-----------------------------------------------------------------------------
# Flowey Jetour 
#-----------------------------------------------------------------------------

X70_PLUS_PATH = "Assets/Car Pictures/Jetour_X70_Plus.jpg"
X90_PLUS_PATH = "Assets/Car Pictures/Jetour_X90_Plus.jpg"
DASHING_PATH ="Assets/Car Pictures/Jetour_Dashing.jpg"



X70_PLUS_ICON = "Assets/Car Pictures/suv-car-icon.png"
X90_PLUS_ICON = "Assets/Car Pictures/suv-car-icon.png"
DASHING_ICON = "Assets/Car Pictures/suv-car-icon.png"


#-----------------------------------------------------------------------------
# PAPYRUS HONDA 
#-----------------------------------------------------------------------------

CR_V_PATH = "Assets/Car Pictures/Honda_CR-V.jpg"
ACCORD_PATH = "Assets/Car Pictures/Honda_Accord.jpg"
CITY_PATH ="Assets/Car Pictures/Honda_City.jpg"



CR_V_ICON = "Assets/Car Pictures/suv-car-icon.png"
ACCORD_ICON = "Assets/Car Pictures/sedan-car-icon.png"
CITY_ICON = "Assets/Car Pictures/sedan-car-icon.png"

#-----------------------------------------------------------------------------
# TORIEL BMW
#-----------------------------------------------------------------------------

X7_PATH = "Assets/Car Pictures/Bmw_X7.jpg"
PATH_530i = "Assets/Car Pictures/Bmw_530i.jpg"
i4_PATH ="Assets/Car Pictures/Bmw_i4_eDrive40.jpg"



X7_ICON = "Assets/Car Pictures/suv-car-icon.png"
ICON_530i = "Assets/Car Pictures/sedan-car-icon.png"
i4_ICON = "Assets/Car Pictures/suv-car-icon.png"




#--------------------------------------------------------------------
# Pygame Setup
#-------------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(WHITE)

# Intialization Variables


FONT = pygame.font.Font(r"Assets\Others\undertale.ttf" , 25)
pygame.mixer.init()

#---------------------------------------------------
# Functions
#---------------------------------------------------



def character_box(
        surface,  box_color ,
        border_color, mouse_pos ,alpha,
        pos , size = CHARATER_BOX ,
        hover_effect = HOVER_EFFECT ,
        border_radius = 10,
        clicked = None,
        car_page = None
        ):

    """
    Purpose : forms a small box with the name of car (e.g toyata) and allows it to glow 

    Input :
    
        surface: screen to paste this on
        box_color : color of the box
        border_color : color of the border
        mouse_pos :  check if it's over the box
        alpha : fading effect
        pos : where it's present
        size : size of box
        hover_effect : extent of englarged when mouse present
        border_radius : the size of the border

    """

    box_rect = pygame.Rect(pos[0], pos[1], size[0], size[1])


    temp_surface = pygame.Surface((size[0], size[1]), pygame.SRCALPHA)
    temp_surface.fill((*box_color, alpha))
    surface.blit(temp_surface, pos)
    
    if box_rect.collidepoint(mouse_pos):
        hover_rect = box_rect.inflate(hover_effect[0] , hover_effect[1])
        pygame.draw.rect(surface, border_color, hover_rect, border_radius)

        if clicked:
            car_page = True 


    return box_rect, car_page 



def load_car_data(file_path):
    
    """
    Purpose : load the data from JSON files
    
    """

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found!")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: {file_path} is not valid JSON! ({e})")
        return None


def speech_bubble(surface, pos=SPEECH_BUBBLE_POS , bubble_color = BLACK, speech_bubble_size = SPEECH_BUBBLE_SIZE, border_color = WHITE ):
    
    """
    Purpose : make a black bubble with white surface inside
    
    """
   

    bubble_rect = pygame.Rect(pos[0], pos[1], speech_bubble_size[0]  , speech_bubble_size[1])


    pygame.draw.rect(surface, bubble_color, bubble_rect , border_radius = 20)
    pygame.draw.rect(surface, border_color , bubble_rect, 2, border_radius=20 )



def car_name_animation(
        surface, mouse_detection_rect,
        car_name_alpha_current , color ,
        mouse_pos, pos = (0,0),
        size = CAR_NAME_ANIMATION_SIZE ,
        target_location = (0,0) , text = "",
        font = FONT, text_color = BLACK 
        ):

    """
    Purpose : Creates a fading + sliding animation for a car name when the mouse hovers over its area.

    Input:
        surface: The main screen or surface to draw on.
        mouse_detection_rect: Rect area to check if mouse is hovering.
        car_name_alpha_current: Current alpha (transparency) value of the box.
        color: Background color of the animation box.
        mouse_pos: Current mouse position.
        pos: Starting position of the animation box.
        size: Size of the animation box.
        target_location: Final Y position the box should slide towards.
        text: Optional text to display (e.g. car name).
        font: Font used for rendering text.
        text_color: Color of the text.

    Returns:
        pos_new (tuple): Updated position of the box.
        car_name_alpha_current (int): Updated alpha value for fade effect.

    """

    temp_surface = pygame.Surface((size[0], size[1]), pygame.SRCALPHA)
    temp_surface.fill ((*color, car_name_alpha_current))
    

    if text and font:
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(size[0]//2, size[1]//2))
        temp_surface.blit(text_surface, text_rect)

    surface.blit(temp_surface, pos)    

    y = pos[1]

    if mouse_detection_rect.collidepoint(mouse_pos):
        car_name_alpha_current = min(255, car_name_alpha_current + 5)
        y = min(target_location[1], y + 2)
    else:
        y =  pos[1]
    
    pos_new = (pos[0], y)
    return pos_new , car_name_alpha_current




def typewriter_effect(
        surface, index,
        text, font = FONT ,
        text_color = WHITE, char_width = CHARACTER_WIDTH ,
        pos= (400,400), type_padding = PADDING
        ):

    """
    purpose: displays text on the screen with a typewriter effect, showing up to 'index' characters. Automatically wraps long lines to fit the specified character width.

    Args:
        surface: Pygame surface to draw the text on.
        index: Number of characters from 'text' to display (for typing animation).
        text: Full string to display.
        font: Pygame font to render text.
        text_color: Color of the text.
        char_width: Maximum characters per line.
        pos: Top-left position to start drawing the text.
        type_padding: Extra padding inside the text box.

    """

    displayed_text = "".join(text[:index])

    lines = textwrap.wrap(displayed_text, char_width)
    y = pos[1] + type_padding 

    for line in lines:
        text_surface = font.render(line, True, text_color )
        surface.blit(text_surface, (pos[0] + 2* type_padding, y))
        y += (font.get_linesize() + 10)



def typewriter_animation(current_time, last_typing_time, index, text , sound ):

    """
    Purpose : Handles the logic for revealing text one character at a time (typewriter effect).

    Args:
        current_time: Current time in milliseconds (e.g., pygame.time.get_ticks()).
        last_typing_time: Time when the last character was revealed.
        index: Current number of characters shown from 'text'.
        text: Full string to display.
        sound: Pygame sound object to play for each typed character.

    Returns:
        last_typing_time: Updated time when this character was revealed.
        index: Updated number of characters to display next frame.

    """


    if index < len(text):
        char = text[index]
        if char not in [" ", "\n"]:
            sound.play()
        last_typing_time = current_time 
        index += 1
    return last_typing_time, index 



def escape_button(
        surface, color,  border_color,
        highlight_color, alpha,
        mouse_pos,clicked, main_page,
        current_page,  button_size= ESCAPE_BUTTON_SIZE,
        pos=(0,0) , font = FONT ,
        hover_effect = HOVER_EFFECT,
        text_name = "Esc"
         ):

    """
    Purpose : Creates an interactive "Escape" button that can be used to return to the main page.

    Args:
        surface: Pygame surface to draw the button on.
        color: Base color of the button.
        border_color: Color of the border when hovered.
        highlight_color: Overlay color for hover effect.
        alpha: Current alpha value for the hover highlight.
        mouse_pos: Current mouse position (tuple) for hover detection.
        clicked: Boolean indicating if the mouse was clicked this frame.
        main_page: Boolean flag for whether the main page is active.
        current_page: Boolean flag for whether the current page is active.
        button_size: Tuple (width, height) for button size.
        pos: Top-left position of the button on the surface.
        font: Pygame font for rendering the "Esc" text.
        hover_effect: Tuple (width_increase, height_increase) for border enlargement on hover.

    Returns:
        main_page: Updated main_page status (True if button clicked).
        current_page: Updated current_page status (False if button clicked).
        alpha: Updated alpha value for hover highlight effect.


    """

    escape_box = pygame.Rect(pos[0], pos[1], button_size[0], button_size[1])
    
    highlight_surf = pygame.Surface(button_size, pygame.SRCALPHA)
    highlight_surf.fill((*highlight_color, alpha))

    pygame.draw.rect(surface, color, escape_box)

    if escape_box.collidepoint(mouse_pos):

        alpha = min(255, alpha + 10)
        surface.blit(highlight_surf, pos)

        hover_rect = escape_box.inflate(hover_effect[0],hover_effect[1])
        pygame.draw.rect(surface, border_color, hover_rect, 4, border_radius=0)

        if clicked and alpha > 100:
            main_page = True
            current_page = False
    else:

        alpha = max(0, alpha - 10)
    
    if font:
        text_surface = font.render(text_name, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=escape_box.center)
        surface.blit(text_surface, text_rect)
    
    return main_page, current_page, alpha


def gif_framerate(surface_list, last_update, frame_index, current_time, frame_delay_ms = FRAME_DELAY_MS , current_alpha=None  ):

    """
    Purpose : Handles GIF frame animation.

    Input:
        surface_list (list): List of Pygame surfaces for frames.
        last_update (int): Last time frame was updated (pygame.time.get_ticks()).
        frame_index (int): Current frame index.
        frame_delay_ms (int): Delay between frames in milliseconds.
        current_alpha (int, optional): Alpha value (0-255) to apply for fade effects.

    Returns:
        tuple: (current_frame_surface, new_frame_index, new_last_update)
    """

    if (current_time - last_update) > frame_delay_ms:
        frame_index = (frame_index + 1) % len(surface_list)
        last_update = current_time




    frame = surface_list[frame_index]
    if current_alpha is not None:
        frame.set_alpha(current_alpha)

    return frame, frame_index, last_update

def draw_bought_box(screen,  bought_color = (0,200,0),size = (200,200),pos = (0,0), font = None , text_color=(255,255,255)):
    """
    Draws a rectangle with the text 'Bought' centered inside.

    Parameters:
        screen     : pygame surface to draw on
        font       : pygame font object
        position   : (x, y) tuple (top-left corner of rectangle)
        size       : (width, height) of rectangle
        color      : (R, G, B) color of rectangle
        text_color : (R, G, B) color of text (default: white)
    """

    # Rectangle
    rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
    pygame.draw.rect(screen, bought_color, rect, border_radius=10)

    # Text
    text_surface = font.render("Bought", True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    return rect


#----------------------------------------------------------------------------------
# Game Loop 
#------------------------------------------------------------------------------------


def main():
    running = True

    #------------------------------------------------------------------
    # Initialize Characters
    #--------------------------------------------------------------------



    #sans
    sans = UndertaleCharacters(
        SANS_IMAGE ,
        typing_sound= SANS_TYPING_SOUND
        )
    
    sans_frames = sans.gif_frames()
    del sans_frames[0]
    sans_frames = [_.resize((600, 500)) for _ in sans_frames]
    sans_surface = [pygame.image.frombytes(_.tobytes(), _.size , _.mode) for _ in sans_frames]


    #chara
    chara = UndertaleCharacters(
        CHARA_IMAGE,
        typing_sound = CHARA_TYPING_SOUND,
        )
    
    chara_frames = chara.gif_frames() 
    del chara_frames[0]
    chara_frames = [_.resize((100, 100)) for _ in chara_frames]
    chara_surface = [pygame.image.frombytes(_.tobytes(), _.size, _.mode) for _ in chara_frames]


    chara_frames_2 = [_.resize((300, 200)) for _ in chara_frames]
    chara_surface_2 = [pygame.image.frombytes(_.tobytes(), _.size, _.mode) for _ in chara_frames_2]


    #flowey
    flowey = UndertaleCharacters(
        FLOWEY_IMAGE,
        typing_sound= FLOWEY_TYPING_SOUND,
        )
    

    flowey_frames = flowey.gif_frames()
    flowey_frames = [frame for i, frame in enumerate(flowey_frames) if i != 0 and i < 7]
    flowey_frames = [_.resize((100,100)) for _ in flowey_frames]
    flowey_surface = [pygame.image.frombytes(_.tobytes(), _.size, _.mode ) for _ in flowey_frames]

    flowey_frames_2 = [_.resize((300, 200)) for _ in flowey_frames]
    flowey_surface_2 = [pygame.image.frombytes(_.tobytes(), _.size, _.mode) for _ in flowey_frames_2]



    #papyrus
    papyrus = UndertaleCharacters(
        PAPYRUS_IMAGE,
        typing_sound = PAPYRUS_TYPING_SOUND,
        )
    

    papyrus_surface = pygame.image.load(papyrus.image)
    papyrus_surface = pygame.transform.scale(papyrus_surface, (100, 100))

    papyrus_surface_2 = pygame.image.load(papyrus.image)
    papyrus_surface_2 = pygame.transform.scale(papyrus_surface_2, (300, 200))


    #toriel 
    toriel = UndertaleCharacters(
        TORIEL_IMAGE,
        typing_sound = TORIEL_TYPING_SOUND,
        )
    

    toriel_surface = pygame.image.load(toriel.image)
    toriel_surface = pygame.transform.scale(toriel_surface, (100, 100))

    toriel_surface_2 = pygame.image.load(toriel.image)
    toriel_surface_2 = pygame.transform.scale(toriel_surface_2, (300, 200))




    #-----------------------------------------------------
    # Convert GIF frames to alpha surfaces
    #-----------------------------------------------------


    sans_surface = [_.convert_alpha() for _ in sans_surface]
    chara_surface = [_.convert_alpha() for _ in chara_surface]
    flowey_surface = [_.convert_alpha() for _ in flowey_surface] 




    #-----------------------------------------------------
    # Initialize Backgrounds
    #-----------------------------------------------------
    #background 
    brightness_factor = 0.6 #background brightness

    # Intializing Background via the "Undertale class"
    background_sans = UndertaleCharacters("Assets/Background/Car-Background.gif")
    background_sans_frames = background_sans.gif_frames()
    del background_sans_frames[0]

    background_sans_frames = [
        ImageEnhance.Brightness(frame).enhance( brightness_factor)
        for frame in background_sans_frames
    ]
    sans_background_surface = [
        pygame.transform.scale( 
            pygame.image.frombytes(_.tobytes(), _.size, _.mode) , (WINDOW_SIZE)
        )
        for _ in background_sans_frames]



    # Intializing Chara_Background via the "Undertale class"
    background_chara = UndertaleCharacters("Assets/Background/Chara-Background.gif")
    chara_background_frames = background_chara.gif_frames()
    del chara_background_frames[0]
    chara_background_frames = [
        ImageEnhance.Brightness(frame).enhance( brightness_factor)
        for frame in chara_background_frames
    ]
    chara_background_surface = [
        pygame.transform.scale( 
            pygame.image.frombytes(_.tobytes(), _.size, _.mode) , (WINDOW_SIZE)
        )
        for _ in chara_background_frames]


    # Intializing Flowey_Background via the "Undertale class"
    background_flowey = UndertaleCharacters("Assets/Background/Flowey-Background.gif")
    flowey_background_frames = background_flowey.gif_frames()
    flowey_background_frames = [
        ImageEnhance.Brightness(frame.convert("RGB")).enhance(brightness_factor)
        for frame in flowey_background_frames
    ]
    flowey_background_surface = [
        pygame.transform.scale( 
            pygame.image.frombytes(_.tobytes(), _.size, _.mode) , (WINDOW_SIZE)
        )
        for _ in flowey_background_frames]



    # Intializing Papyrus_Background via the "Undertale class"
    background_papyrus = UndertaleCharacters("Assets/Background/Papyrus-Background.gif")
    papyrus_background_frames = background_papyrus.gif_frames()
    papyrus_background_frames = [
        ImageEnhance.Brightness(frame.convert("RGB")).enhance(brightness_factor)
        for frame in papyrus_background_frames
    ]
    papyrus_background_surface = [
        pygame.transform.scale( 
            pygame.image.frombytes(_.tobytes(), _.size, _.mode) , (WINDOW_SIZE)
        )
        for _ in papyrus_background_frames]




    # Intializing Toriel_Background via the "Undertale class"
    background_toriel = UndertaleCharacters("Assets/Background/Toriel-Background.gif")
    toriel_background_frames = background_toriel.gif_frames()
    toriel_background_frames = [
        ImageEnhance.Brightness(frame.convert("RGB")).enhance(brightness_factor)
        for frame in toriel_background_frames
    ]
    toriel_background_surface = [
        pygame.transform.scale( 
            pygame.image.frombytes(_.tobytes(), _.size, _.mode) , (WINDOW_SIZE)
        )
        for _ in toriel_background_frames]



    #-----------------------------------------------------
    # Typing Sounds
    #-----------------------------------------------------

    sans_typing_sound = pygame.mixer.Sound(sans.typing_sound)
    sans_typing_sound.set_volume(0.4)
    chara_typing_sound = pygame.mixer.Sound(chara.typing_sound)
    flowey_typing_sound = pygame.mixer.Sound(flowey.typing_sound)
    papyrus_typing_sound = pygame.mixer.Sound(papyrus.typing_sound)
    toriel_typing_sound = pygame.mixer.Sound(toriel.typing_sound)
    
        

    #--------------------------------------------------------------------------
    # Load Car Data
    #-------------------------------------------------------------------------

    brand_name_1 = "bmw"
    brand_name_2 = "honda"
    brand_name_3 = "toyota"
    brand_name_4 = "jetour"


    bmw_data = load_car_data(f"Assets/Car Data/{brand_name_1}.json")
    honda_data = load_car_data(f"Assets/Car Data/{brand_name_2}.json")
    toyota_data = load_car_data(f"Assets/Car Data/{brand_name_3}.json")
    jetour_data = load_car_data(f"Assets/Car Data/{brand_name_4}.json")


    #---------------------------------------------------------------------------------
    # Toriel Honda
    #------------------------------------------------------------------------------------
    
    X7_data = None
    for model in bmw_data["models"]:
        if model["name"] == "X7":
            X7_data = model
            break

    #toriel cars Text
    TORIEL_X7_TEXT_1 = [
        f"""Name: {X7_data["name"]}
        Type: {X7_data["type"]}
        Year: {X7_data["year"]}
        Price (QAR): {X7_data["price_qar"]}
        Engine: {X7_data["engine"]}
        Horsepower: {X7_data["horsepower"]}
        Top Speed: {X7_data["top_speed"]}
        Fuel Type: {X7_data["fuel_type"]}
        Features: {", ".join(X7_data["features"])}"""
    ]

    TORIEL_X7_TEXT_2 = [
        f"""Description: {X7_data["description"]}"""
    ]


    i530_data = None
    for model in bmw_data["models"]:
        if model["name"] ==  "530i":
            i530_data = model
            break

    #toriel cars Text
    TORIEL_530_TEXT_1 = [
        f"""Name: {i530_data["name"]}
        Type: {i530_data["type"]}
        Year: {i530_data["year"]}
        Price (QAR): {i530_data["price_qar"]}
        Engine: {i530_data["engine"]}
        Horsepower: {i530_data["horsepower"]}
        Top Speed: {i530_data["top_speed"]}
        Fuel Type: {i530_data["fuel_type"]}
        Features: {", ".join(i530_data["features"])}"""
    ]

    TORIEL_530_TEXT_2 = [
        f"""Description: {i530_data["description"]}"""
    ]


    i4_data = None
    for model in bmw_data["models"]:
        if model["name"] == "i4 eDrive40":
            i4_data = model
            break

    #toriel cars Text
    TORIEL_i4_TEXT_1 = [
        f"""Name: {i4_data["name"]}
        Type: {i4_data["type"]}
        Year: {i4_data["year"]}
        Price (QAR): {i4_data["price_qar"]}
        Engine: {i4_data["engine"]}
        Horsepower: {i4_data["horsepower"]}
        Top Speed: {i4_data["top_speed"]}
        Fuel Type: {i4_data["fuel_type"]}
        Features: {", ".join(i4_data["features"])}"""
    ]

    TORIEL_i4_TEXT_2 = [
        f"""Description: {i4_data["description"]}"""
    ]
    #---------------------------------------------------------------------------------
    # Papyrus Honda
    #------------------------------------------------------------------------------------
    
    CR_V_data = None
    for model in honda_data["models"]:
        if model["name"] == "CR-V":
            CR_V_data = model
            break

    #papyrus cars Text
    PAPYRUS_CR_V_TEXT_1 = [
        f"""Name: {CR_V_data["name"]}
        Type: {CR_V_data["type"]}
        Year: {CR_V_data["year"]}
        Price (QAR): {CR_V_data["price_qar"]}
        Engine: {CR_V_data["engine"]}
        Horsepower: {CR_V_data["horsepower"]}
        Top Speed: {CR_V_data["top_speed"]}
        Fuel Type: {CR_V_data["fuel_type"]}
        Features: {", ".join(CR_V_data["features"])}"""
    ]

    PAPYRUS_CR_V_TEXT_2 = [
        f"""Description: {CR_V_data["description"]}"""
    ]


    accord_data = None
    for model in honda_data["models"]:
        if model["name"] == "Accord":
            accord_data = model
            break

    #papyrus cars Text
    PAPYRUS_ACCORD_TEXT_1 = [
        f"""Name: {accord_data["name"]}
        Type: {accord_data["type"]}
        Year: {accord_data["year"]}
        Price (QAR): {accord_data["price_qar"]}
        Engine: {accord_data["engine"]}
        Horsepower: {accord_data["horsepower"]}
        Top Speed: {accord_data["top_speed"]}
        Fuel Type: {accord_data["fuel_type"]}
        Features: {", ".join(accord_data["features"])}"""
    ]

    PAPYRUS_ACCORD_TEXT_2 = [
        f"""Description: {accord_data["description"]}"""
    ]


    city_data = None
    for model in honda_data["models"]:
        if model["name"] == "City":
            city_data = model
            break

    #flowey cars Text
    PAPYRUS_CITY_TEXT_1 = [
        f"""Name: {city_data["name"]}
        Type: {city_data["type"]}
        Year: {city_data["year"]}
        Price (QAR): {city_data["price_qar"]}
        Engine: {city_data["engine"]}
        Horsepower: {city_data["horsepower"]}
        Top Speed: {city_data["top_speed"]}
        Fuel Type: {city_data["fuel_type"]}
        Features: {", ".join(city_data["features"])}"""
    ]

    PAPYRUS_CITY_TEXT_2 = [
        f"""Description: {city_data["description"]}"""
    ]
    

    #---------------------------------------------------------------------------------
    # Flowey Jetour
    #------------------------------------------------------------------------------------
    
    x70_plus_data = None
    for model in jetour_data["models"]:
        if model["name"] == "X70 Plus":
            x70_plus_data = model
            break

    #flowey cars Text
    FLOWEY_X70_PLUS_TEXT_1 = [
        f"""Name: {x70_plus_data["name"]}
        Type: {x70_plus_data["type"]}
        Year: {x70_plus_data["year"]}
        Price (QAR): {x70_plus_data["price_qar"]}
        Engine: {x70_plus_data["engine"]}
        Horsepower: {x70_plus_data["horsepower"]}
        Top Speed: {x70_plus_data["top_speed"]}
        Fuel Type: {x70_plus_data["fuel_type"]}
        Features: {", ".join(x70_plus_data["features"])}"""
    ]

    FLOWEY_X70_PLUS_TEXT_2 = [
        f"""Description: {x70_plus_data["description"]}"""
    ]


    x90_plus_data = None
    for model in jetour_data["models"]:
        if model["name"] == "X90 Plus":
            x90_plus_data = model
            break

    #flowey cars Text
    FLOWEY_X90_PLUS_TEXT_1 = [
        f"""Name: {x90_plus_data["name"]}
        Type: {x90_plus_data["type"]}
        Year: {x90_plus_data["year"]}
        Price (QAR): {x90_plus_data["price_qar"]}
        Engine: {x90_plus_data["engine"]}
        Horsepower: {x90_plus_data["horsepower"]}
        Top Speed: {x90_plus_data["top_speed"]}
        Fuel Type: {x90_plus_data["fuel_type"]}
        Features: {", ".join(x90_plus_data["features"])}"""
    ]

    FLOWEY_X90_PLUS_TEXT_2 = [
        f"""Description: {x90_plus_data["description"]}"""
    ]


    dashing_data = None
    for model in jetour_data["models"]:
        if model["name"] == "Dashing":
            dashing_data = model
            break

    #flowey cars Text
    FLOWEY_DASHING_TEXT_1 = [
        f"""Name: {dashing_data["name"]}
        Type: {dashing_data["type"]}
        Year: {dashing_data["year"]}
        Price (QAR): {dashing_data["price_qar"]}
        Engine: {dashing_data["engine"]}
        Horsepower: {dashing_data["horsepower"]}
        Top Speed: {dashing_data["top_speed"]}
        Fuel Type: {dashing_data["fuel_type"]}
        Features: {", ".join(dashing_data["features"])}"""
    ]

    FLOWEY_DASHING_TEXT_2 = [
        f"""Description: {dashing_data["description"]}"""
    ]
    


    #-----------------------------------------------------
    # Chara Toyota 
    #-----------------------------------------------------

    camry_data = None
    for model in toyota_data["models"]:
        if model["name"] == "Camry":
            camry_data = model
            break

    #chara cars Text
    CHARA_CAMRY_TEXT_1 = [
        f"""Name: {camry_data["name"]}
        Type: {camry_data["type"]}
        Year: {camry_data["year"]}
        Price (QAR): {camry_data["price_qar"]}
        Engine: {camry_data["engine"]}
        Horsepower: {camry_data["horsepower"]}
        Top Speed: {camry_data["top_speed"]}
        Fuel Type: {camry_data["fuel_type"]}
        Features: {", ".join(camry_data["features"])}"""
    ]

    CHARA_CAMRY_TEXT_2 = [
        f"""Description: {camry_data["description"]}"""
    ]





    fortuner_data = None
    for model in toyota_data["models"]:
        if model["name"] == "Fortuner":
            fortuner_data = model
            break

    #chara cars Text
    CHARA_FORTUNER_TEXT_1 = [
        f"""Name: {fortuner_data["name"]}
        Type: {fortuner_data["type"]}
        Year: {fortuner_data["year"]}
        Price (QAR): {fortuner_data["price_qar"]}
        Engine: {fortuner_data["engine"]}
        Horsepower: {fortuner_data["horsepower"]}
        Top Speed: {fortuner_data["top_speed"]}
        Fuel Type: {fortuner_data["fuel_type"]}
        Features: {", ".join(fortuner_data["features"])}"""
    ]

    CHARA_FORTUNER_TEXT_2 = [
        f"""Description: {fortuner_data["description"]}"""
    ]





    land_cruiser_data = None
    for model in toyota_data["models"]:
        if model["name"] == "Land Cruiser":
            land_cruiser_data = model
            break

        #chara cars Text
    CHARA_LAND_CRUISER_TEXT_1 = [
        f"""Name: {land_cruiser_data["name"]}
        Type: {land_cruiser_data["type"]}
        Year: {land_cruiser_data["year"]}
        Price (QAR): {land_cruiser_data["price_qar"]}
        Engine: {land_cruiser_data["engine"]}
        Horsepower: {land_cruiser_data["horsepower"]}
        Top Speed: {land_cruiser_data["top_speed"]}
        Fuel Type: {land_cruiser_data["fuel_type"]}
        Features: {", ".join(land_cruiser_data["features"])}"""
    ]

    CHARA_LAND_CRUISER_TEXT_2 = [
        f"""Description: {land_cruiser_data["description"]}"""
    ]
    
    #---------------------------------------------------------
    # Toyota
    #-------------------------------------------------------

    toyota_camry = pygame.image.load(CAMRY_PATH)
    toyota_fortuner = pygame.image.load(FORTUNER_PATH)
    toyota_land_cruiser = pygame.image.load(LAND_CRUISER_PATH)

    toyota_camry = pygame.transform.scale(toyota_camry, (500, 300))
    toyota_fortuner = pygame.transform.scale(toyota_fortuner, (500, 300))
    toyota_land_cruiser = pygame.transform.scale(toyota_land_cruiser, (500, 300))


    toyota_camry_icon = pygame.image.load(CAMRY_ICON)
    toyota_fortuner_icon = pygame.image.load(FORTUNER_ICON)
    toyota_land_cruiser_icon = pygame.image.load(LAND_CRUISER_ICON)

    toyota_camry_icon = pygame.transform.scale(toyota_camry_icon, (150, 150))
    toyota_fortuner_icon = pygame.transform.scale(toyota_fortuner_icon, (150, 150))
    toyota_land_cruiser_icon = pygame.transform.scale(toyota_land_cruiser_icon, (150, 150))

    chara_bought_button_alpha=0



    camry_alpha = 0
    fortuner_alpha = 0
    land_cruiser_alpha = 0
        


    #-------------------------------------------------------------------------------
    # Jetour
    #----------------------------------------------------------------------------

    jetour_x70_plus = pygame.image.load(X70_PLUS_PATH)
    jetour_x90_plus = pygame.image.load(X90_PLUS_PATH)
    jetour_dashing = pygame.image.load(DASHING_PATH)

    jetour_x70_plus = pygame.transform.scale(jetour_x70_plus, (500, 300))
    jetour_x90_plus = pygame.transform.scale(jetour_x90_plus, (500, 300))
    jetour_dashing = pygame.transform.scale(jetour_dashing, (500, 300))


    jetour_x70_plus_icon = pygame.image.load(X70_PLUS_ICON)
    jetour_x90_plus_icon = pygame.image.load(X90_PLUS_ICON)
    jetour_dashing_icon = pygame.image.load(DASHING_ICON)

    jetour_x70_plus_icon = pygame.transform.scale(jetour_x70_plus_icon, (150, 150))
    jetour_x90_plus_icon = pygame.transform.scale(jetour_x90_plus_icon, (150, 150))
    jetour_dashing_icon = pygame.transform.scale(jetour_dashing_icon, (150, 150))

    flowey_bought_button_alpha=0



    x70_plus_alpha = 0
    x90_plus_alpha = 0
    dashing_alpha = 0


    #-----------------------------------------------------------------------------
    # PAPYRUS HONDA 
    #-----------------------------------------------------------------------------



    honda_cr_v = pygame.image.load(CR_V_PATH)
    honda_accord = pygame.image.load(ACCORD_PATH)
    honda_city = pygame.image.load(CITY_PATH)

    honda_cr_v = pygame.transform.scale(honda_cr_v, (500, 300))
    honda_accord = pygame.transform.scale(honda_accord, (500, 300))
    honda_city = pygame.transform.scale(honda_city, (500, 300))

    honda_cr_v_icon = pygame.image.load(CR_V_ICON)
    honda_accord_icon = pygame.image.load(ACCORD_ICON)
    honda_city_icon = pygame.image.load(CITY_ICON)

    honda_cr_v_icon = pygame.transform.scale(honda_cr_v_icon, (150, 150))
    honda_accord_icon = pygame.transform.scale(honda_accord_icon, (150, 150))
    honda_city_icon = pygame.transform.scale(honda_city_icon, (150, 150))

    papyrus_bought_button_alpha=0

    cr_v_alpha = 0
    accord_alpha = 0
    city_alpha = 0

    #-----------------------------------------------------------------------------
    # TORIEL BMW
    #-----------------------------------------------------------------------------

    bmw_x7 = pygame.image.load(X7_PATH)
    bmw_530i = pygame.image.load(PATH_530i)
    bmw_i4 = pygame.image.load(i4_PATH)

    bmw_x7 = pygame.transform.scale(bmw_x7, (500, 300))
    bmw_530i = pygame.transform.scale(bmw_530i, (500, 300))
    bmw_i4 = pygame.transform.scale(bmw_i4, (500, 300))

    bmw_x7_icon = pygame.image.load(X7_ICON)
    bmw_530i_icon = pygame.image.load(ICON_530i)
    bmw_i4_icon = pygame.image.load(i4_ICON)

    bmw_x7_icon = pygame.transform.scale(bmw_x7_icon, (150, 150))
    bmw_530i_icon = pygame.transform.scale(bmw_530i_icon, (150, 150))
    bmw_i4_icon = pygame.transform.scale(bmw_i4_icon, (150, 150))

    toriel_bought_button_alpha = 0

    x7_alpha = 0
    _530i_alpha = 0
    i4_alpha = 0
    #-----------------------------------------------------
    # Initial Game Variables
    #-----------------------------------------------------
    
    #page checks
    sans_page = True 

    #chara pages
    chara_page_1 = False
    chara_camry_page_2 = False
    chara_fortuner_page_2 = False
    chara_land_cruiser_page_2 = False

    chara_camry_submit_page = False
    chara_fortuner_submit_page = False
    chara_land_cruiser_submit_page = False
 
    #flowey pages
    flowey_page_1 = False
    flowey_x70_plus_page_2 = False
    flowey_x90_plus_page_2 = False
    flowey_dashing_page_2 = False

    flowey_x70_plus_submit_page = False
    flowey_x90_plus_submit_page = False
    flowey_dashing_submit_page = False

    papyrus_page_1 = False
    papyrus_cr_v_page_2 = False
    papyrus_accord_page_2 = False
    papyrus_city_page_2 = False

    papyrus_cr_v_submit_page = False
    papyrus_accord_submit_page = False
    papyrus_city_submit_page = False


    toriel_page_1 = False
    toriel_x7_page_2 = False
    toriel_530i_page_2 = False
    toriel_i4_page_2 = False

    toriel_x7_submit_page = False
    toriel_530i_submit_page = False
    toriel_i4_submit_page = False

    #last typing times
    sans_last_typing_time = pygame.time.get_ticks()
    chara_last_typing_time = pygame.time.get_ticks()
    flowey_last_typing_time = pygame.time.get_ticks()
    papyrus_last_typing_time = pygame.time.get_ticks()
    toriel_last_typing_time = pygame.time.get_ticks()

    #Speech Typing index
    #sans
    sans_joke_typing_index = 0
    sans_pun_typing_index = 0
    sans_main_typing_index = 0
    sans_pun_line_index = random.randint(0, len(SANS_PUNS)-1)
    sans_joke_line_index = random.randint(0, len(SANS_JOKES)-1)
    sans_line_index = 0

    #chara
    chara_main_typing_index = 0
    chara_line_index = 0

    chara_camry_line_index = 0
    chara_camry_typing_index_1 = 0
    chara_camry_typing_index_2 = 0

    chara_fortuner_line_index = 0
    chara_fortuner_typing_index_1 = 0
    chara_fortuner_typing_index_2 = 0


    chara_land_cruiser_line_index = 0
    chara_land_cruiser_typing_index_1 = 0
    chara_land_cruiser_typing_index_2 = 0


    #flowey
    flowey_main_typing_index = 0
    flowey_line_index = 0

    flowey_x70_plus_line_index = 0
    flowey_x70_plus_typing_index_1 = 0
    flowey_x70_plus_typing_index_2 = 0

    flowey_x90_plus_line_index = 0
    flowey_x90_plus_typing_index_1 = 0
    flowey_x90_plus_typing_index_2 = 0


    flowey_dashing_line_index = 0
    flowey_dashing_typing_index_1 = 0
    flowey_dashing_typing_index_2 = 0

    #papyrus
    papyrus_main_typing_index = 0
    papyrus_line_index = 0

    papyrus_cr_v_line_index = 0
    papyrus_cr_v_typing_index_1 = 0
    papyrus_cr_v_typing_index_2 = 0

    papyrus_accord_line_index = 0
    papyrus_accord_typing_index_1 = 0
    papyrus_accord_typing_index_2 = 0

    papyrus_city_line_index = 0
    papyrus_city_typing_index_1 = 0
    papyrus_city_typing_index_2 = 0


    #toriel
    toriel_main_typing_index = 0
    toriel_line_index = 0

    toriel_x7_line_index = 0
    toriel_x7_typing_index_1 = 0
    toriel_x7_typing_index_2 = 0

    toriel_530i_line_index = 0
    toriel_530i_typing_index_1 = 0
    toriel_530i_typing_index_2 = 0

    toriel_i4_line_index = 0
    toriel_i4_typing_index_1 = 0
    toriel_i4_typing_index_2 = 0

    # Speech Effects
    typing_delay_betw_speeches = 1500


   #mouse / interaction
    clicked_sans_tally = 0
    clicked_chara_tally = 0
    clicked_flowey_tally = 0
    clicked_papyrus_tally = 0
    clicked_toriel_tally = 0

    #track first-time events
    chara_page_time = 0
    chara_current_time = 0

    flowey_page_time = 0
    flowey_current_time = 0

    papyrus_page_time = 0
    papyrus_current_time = 0

    toriel_page_time = 0
    papyrus_current_time = 0

    #track if page_changed
    page_changed = False


    #track if first_time in main page
    sans_first_time = True
    chara_first_time = True
    flowey_first_time = True
    papyrus_first_time = True
    toriel_first_time = True
    
    #sliding in overlay
    chara_camry_overlay_alpha = 0
    chara_fortuner_overlay_alpha = 0
    chara_land_cruiser_overlay_alpha = 0


    flowey_x70_plus_overlay_alpha = 0
    flowey_x90_plus_overlay_alpha = 0
    flowey_dashing_overlay_alpha = 0

    papyrus_cr_v_overlay_alpha = 0
    papyrus_accord_overlay_alpha = 0
    papyrus_city_overlay_alpha = 0

    toriel_x7_overlay_alpha = 0
    toriel_530i_overlay_alpha = 0
    toriel_i4_overlay_alpha = 0

    #3rd page 2nd text typing timing
    chara_camry_first_text_complete = False
    chara_fortuner_first_text_complete = False
    chara_land_cruiser_first_text_complete = False

    flowey_x70_plus_first_text_complete = False
    flowey_x90_plus_first_text_complete = False
    flowey_dashing_first_text_complete = False

    papyrus_cr_v_first_text_complete = False
    papyrus_accord_first_text_complete = False
    papyrus_city_first_text_complete = False

    toriel_x7_first_text_complete = False
    toriel_530i_first_text_complete = False
    toriel_i4_first_text_complete = False


    #slide in 3rd page
    chara_camry_slide_in = True
    chara_fortuner_slide_in = True
    chara_land_cruiser_slide_in = True

    flowey_x70_plus_slide_in = True
    flowey_x90_plus_slide_in = True
    flowey_dashing_slide_in = True

    papyrus_cr_v_slide_in = True
    papyrus_accord_slide_in = True
    papyrus_city_slide_in = True

    toriel_x7_slide_in = True
    toriel_530i_slide_in = True
    toriel_i4_slide_in = True

    #bought buttons
    chara_camry_bought_overlay_alpha = 0
    chara_fortuner_bought_overlay_alpha = 0
    chara_land_cruiser_bought_overlay_alpha = 0

    flowey_x70_plus_bought_overlay_alpha = 0
    flowey_x90_plus_bought_overlay_alpha = 0
    flowey_dashing_bought_overlay_alpha = 0

    papyrus_cr_v_bought_overlay_alpha = 0
    papyrus_accord_bought_overlay_alpha = 0
    papyrus_city_bought_overlay_alpha = 0

    toriel_x7_bought_overlay_alpha = 0
    toriel_530i_bought_overlay_alpha = 0
    toriel_i4_bought_overlay_alpha = 0


    #slid out 3rd page
    chara_camry_slide_out = False
    chara_fortuner_slide_out = False
    chara_land_cruiser_slide_out = False

    flowey_x70_plus_slide_out = False
    flowey_x90_plus_slide_out = False
    flowey_dashing_slide_out = False

    papyrus_cr_v_slide_out = False
    papyrus_accord_slide_out = False
    papyrus_city_slide_out = False

    toriel_x7_slide_out = False
    toriel_530i_slide_out = False
    toriel_i4_slide_out = False


    #animation work
    chara_escape_button_alpha = 0
    chara_camry_escape_button_alpha = 0
    chara_fortuner_escape_button_alpha = 0
    chara_land_cruiser_escape_button_alpha = 0

    flowey_escape_button_alpha = 0
    flowey_x70_plus_escape_button_alpha = 0
    flowey_x90_plus_escape_button_alpha = 0
    flowey_dashing_escape_button_alpha = 0

    papyrus_escape_button_alpha = 0
    papyrus_cr_v_escape_button_alpha = 0
    papyrus_accord_escape_button_alpha = 0
    papyrus_city_escape_button_alpha = 0

    toriel_escape_button_alpha = 0
    toriel_x7_escape_button_alpha = 0
    toriel_530i_escape_button_alpha = 0
    toriel_i4_escape_button_alpha = 0


    #sliding page movement muttons
    chara_camry_panel_x = 1280
    chara_fortuner_panel_x = 1280
    chara_land_cruiser_panel_x = 1280

    flowey_x70_plus_panel_x = 1280
    flowey_x90_plus_panel_x = 1280
    flowey_dashing_panel_x = 1280

    papyrus_cr_v_panel_x = 1280
    papyrus_accord_panel_x = 1280
    papyrus_city_panel_x = 1280

    toriel_x7_panel_x = 1280
    toriel_530i_panel_x = 1280
    toriel_i4_panel_x = 1280

    #Buy buttons alpha
    chara_buy_button_alpha = 0
    flowey_buy_button_alpha = 0
    papyrus_buy_button_alpha = 0
    toriel_buy_button_alpha = 0

    #alpha work
    sans_character_current_alpha = 0
    sans_current_alpha = 0

    chara_current_alpha = 0
    flowey_current_alpha = 0
    papyrus_current_alpha = 0
    toriel_current_alpha = 0


    #for the car icons
    chara_cars_alpha = 0
    flowey_cars_alpha = 0
    papyrus_cars_alpha =0
    toriel_cars_alpha = 0


   #sans's page car name alpha
    sans_chara_alpha = 0
    sans_flowey_alpha = 0
    sans_papyrus_alpha = 0
    sans_toriel_alpha = 0



    #frame index gif checks
    frame_index_sans = 0
    frame_index_sans_background  = 0


    frame_index_chara = 0
    frame_index_chara_background = 0


    frame_index_flowey = 0
    frame_index_flowey_background = 0

    frame_index_papyrus_background = 0


    frame_index_toriel_background = 0

    # gif movements
    sans_last_update = 0
    sans_background_last_update = 0

    chara_last_update = 0
    chara_background_last_update = 0
    
    flowey_last_update = 0
    flowey_background_last_update = 0


    papyrus_background_last_update = 0


    toriel_background_last_update =0

    #character positions 

    chara_pos = (197, 300) #image pos
    camry_pos = (225,400) #image pos
    fortuner_pos = (600,400) #image pos
    land_cruiser_pos = (950,400) #image pos



    flowey_pos = (453, 300) #image pos
    x70_plus_pos = (225,400) #image pos
    x90_plus_pos = (600,400) #image pos
    dashing_pos = (950,400) #image pos



    papyrus_pos = (709, 300) #image pos
    cr_v_pos = (225,400) #image pos
    accord_pos = (600,400) #image pos
    city_pos = (950,400) #image pos

    toriel_pos = (965, 300) #image pos
    x7_pos = (225,400) #image pos
    _530i_pos = (600,400) #image pos
    i4_pos = (950,400) #image pos
        
    #dialogue/typewriter
    sans_dialogue = "None"
    previous_dialogue = "None"


    chara_dialogue = "None"
    flowey_dialogue = "None"
    papyrus_dialogue = "None"
    toriel_dialogue = "None"






  #-------------------------------------------------
  # Game Loop
  #--------------------------------------------------

    while running:
        



        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                clicked = True
            else:
                clicked = False

        mouse_pos = pygame.mouse.get_pos()
            
        #---------------------------------------------------------------
        # Time Tracking
        #----------------------------------------------------------------
        
        sans_current_time = pygame.time.get_ticks()

        chara_current_time = (sans_current_time - chara_page_time)

        flowey_current_time = (sans_current_time - flowey_page_time)

        papyrus_current_time = (sans_current_time - papyrus_page_time)

        toriel_current_time = (sans_current_time - toriel_page_time)


        
        #sans time tracking
        sans_current_2000_more = False 
        sans_current_btw_3000_13000 = False
        sans_current_14000_more = False


        
        #chara time tracking:
        chara_current_2000_more = False
        chara_current_4000_more = False

        #flowey time tracking:
        flowey_current_2000_more = False
        flowey_current_4000_more = False


        #papyrus time tracking:
        papyrus_current_2000_more = False
        papyrus_current_4000_more = False

        #toriel time tracking:
        toriel_current_2000_more = False
        toriel_current_4000_more = False



        #sans changes as time changes
        if sans_page:
            if 3000 >sans_current_time > 2000:
                sans_current_2000_more = True  
            if 3000 < sans_current_time < 13000:
                sans_current_btw_3000_13000 = True
            if sans_current_time > 14000:
                sans_current_14000_more = True 

        #chara changes as time changes
        if chara_page_1:
            if chara_current_time > 2000:    
                chara_current_2000_more = True
            if chara_current_time > 4000:
                chara_current_4000_more = True

        #flowey changes as time changes
        if flowey_page_1:
            if flowey_current_time > 2000:    
                flowey_current_2000_more = True
            if flowey_current_time > 4000:
                flowey_current_4000_more = True

        #paprysu changes as time changes
        if papyrus_page_1:
            if papyrus_current_time > 2000:
                papyrus_current_2000_more = True
            if papyrus_current_time > 4000:
                papyrus_current_4000_more = True

        #toriel changes as time changes
        if toriel_page_1:
            if toriel_current_time > 2000:
                toriel_current_2000_more = True
            if toriel_current_time > 4000:
                toriel_current_4000_more = True

        #-----------------------------------------------------------
        # Sans's Dialogue Progression Logic
        # ------------------------------------------------------------


        if clicked and sans_page:
            clicked_sans_tally += 1


        if sans_first_time:
            if sans_current_2000_more or clicked_sans_tally == 1:
                sans_dialogue = "Intro 1"
            if sans_current_btw_3000_13000 or clicked_sans_tally == 2:
                sans_dialogue = "Intro 2"
            if sans_current_14000_more or clicked_sans_tally == 3:
                sans_dialogue = "Main Speech"
            if clicked_sans_tally > 3:
                sans_dialogue = "Choices"
        else:
            sans_dialogue = "Puns + Choices"



        
        #reset indices if we've completed all dialogue
        if sans_line_index >= len(SANS_TEXT_MAIN):
            sans_line_index = 0
            sans_first_time = False
            sans_dialogue = "Choices"

        


        #------------------------------------------------------------
        # Chara's  Progression Logic
        #------------------------------------------------------------

        if clicked and chara_page_1:
            clicked_chara_tally += 1

            

        if chara_current_2000_more or clicked_chara_tally > 0:
            chara_dialogue = "Intro 1"
        if chara_current_4000_more or clicked_chara_tally > 1:
            chara_dialogue = "Main Speech"
    
        
        #reset indices if we've completed all dialogue
        if not chara_line_index <= len(CHARA_MAIN_TEXT) or clicked_chara_tally > 2:
            chara_dialogue = "Choices"


        #------------------------------------------------------------
        # Flowey's  Progression Logic
        #------------------------------------------------------------

        if clicked and flowey_page_1:
            clicked_flowey_tally += 1

            

        if flowey_current_2000_more or clicked_flowey_tally > 0:
            flowey_dialogue = "Intro 1"
        if flowey_current_4000_more or clicked_flowey_tally > 1:
            flowey_dialogue = "Main Speech"
    
        
        #reset indices if we've completed all dialogue
        if not flowey_line_index <= len(FLOWEY_MAIN_TEXT) or clicked_flowey_tally > 2:
            flowey_dialogue = "Choices"

        #------------------------------------------------------------
        # Papyrus's  Progression Logic
        #------------------------------------------------------------

        if clicked and papyrus_page_1:
            clicked_papyrus_tally += 1

            

        if papyrus_current_2000_more or clicked_papyrus_tally > 0:
            papyrus_dialogue = "Intro 1"
        if papyrus_current_4000_more or clicked_papyrus_tally > 1:
            papyrus_dialogue = "Main Speech"
    
        
        #reset indices if we've completed all dialogue
        if not papyrus_line_index <= len(PAPYRUS_MAIN_TEXT) or clicked_papyrus_tally > 2:
            papyrus_dialogue = "Choices"


        #------------------------------------------------------------------
        # Toriel's Progression Logic
        #-----------------------------------------------------------------

        if clicked and toriel_page_1:
            clicked_toriel_tally +=1

        if toriel_current_2000_more or clicked_toriel_tally >0:
            toriel_dialogue = "Intro 1"
        if toriel_current_4000_more or clicked_toriel_tally >1:
            toriel_dialogue = "Main Speech"

        #reset indecis if we've completed all dialogue
        if not toriel_line_index <= len(TORIEL_MAIN_TEXT) or clicked_toriel_tally>2:
            toriel_dialogue = "Choices"



        #-----------------------------------------------------------------------------------------------------
        # Sans' Page 
        #------------------------------------------------------------------------------------------------------

        if sans_page:


            #------------------------------------------------------------------------------
            # San's Basic Set up
            #------------------------------------------------------------------------------

            if sans_dialogue in ["None", "Intro 1", "Intro 2", "Main Speech", "Puns + Choices"]:

                bg_frame, frame_index_sans_background, sans_background_last_update = gif_framerate(
                sans_background_surface,
                sans_background_last_update,
                frame_index_sans_background,
                current_time= sans_current_time,
                frame_delay_ms= FRAME_DELAY_MS
                )

                screen.blit(bg_frame, (0, 0))


            if sans_dialogue in ["Intro 1", "Intro 2", "Main Speech", "Puns + Choices"]:

                speech_bubble(screen, pos=SPEECH_BUBBLE_POS, bubble_color= BLACK , border_color= WHITE)

                sans_current_alpha = min(255, sans_current_alpha + 5)

                san_frame, frame_index_sans, sans_last_update = gif_framerate(
                    sans_surface,        
                    sans_last_update,    
                    frame_index_sans,
                    current_time= sans_current_time,    
                    frame_delay_ms=FRAME_DELAY_MS,      
                    current_alpha= sans_current_alpha        
                )


                screen.blit(san_frame, (-90, 400))


            #------------------------------------------------------------------------------
            # San's Pun
            #------------------------------------------------------------------------------

            if sans_dialogue in ["Puns + Choices"]:
                    
                if previous_dialogue != "Puns + Choices":
                    sans_pun_line_index = random.randint(0, len(SANS_PUNS) - 1)

                typewriter_effect(
                    screen,
                    sans_pun_typing_index,
                    SANS_PUNS[sans_pun_line_index],
                    FONT, char_width= CHARACTER_WIDTH,
                    pos=SPEECH_BUBBLE_POS,
                    type_padding=PADDING,
                    text_color=WHITE
                )


                if (sans_current_time - sans_last_typing_time) >= TYPING_DELAY and sans_pun_typing_index < len(SANS_PUNS[sans_pun_line_index]):
                    sans_last_typing_time, sans_pun_typing_index = typewriter_animation(
                        sans_current_time,
                        sans_last_typing_time,
                        sans_pun_typing_index,
                        SANS_PUNS[sans_pun_line_index],
                        sans_typing_sound
                    )

                previous_dialogue = "Puns + Choices"



            #------------------------------------------------------------------------------
            # San's Introduction Lines
            #------------------------------------------------------------------------------


            if sans_dialogue in ["Intro 2"]:
                    
                    typewriter_effect(
                        screen,
                        sans_joke_typing_index, 
                        SANS_JOKES[sans_joke_line_index],
                        FONT, char_width=CHARACTER_WIDTH, 
                        pos= SPEECH_BUBBLE_POS, type_padding=10,
                        text_color= WHITE
                        )
                

                    if (sans_current_time - sans_last_typing_time) >= TYPING_DELAY and sans_joke_typing_index < len(SANS_JOKES[sans_joke_line_index]) :
                        sans_last_typing_time, sans_joke_typing_index = typewriter_animation(
                            sans_current_time,
                            sans_last_typing_time,
                            sans_joke_typing_index,
                            SANS_JOKES[sans_joke_line_index] ,
                            sans_typing_sound
                            )

            #------------------------------------------------------------------------------
            # San's Main Speech Lines
            #------------------------------------------------------------------------------


            if  sans_dialogue in ["Main Speech"]:

                typewriter_effect(
                    screen,
                    sans_main_typing_index,
                    SANS_TEXT_MAIN[sans_line_index],
                    FONT,
                    char_width = CHARACTER_WIDTH,
                    pos= SPEECH_BUBBLE_POS,
                    type_padding= PADDING,
                    )
                


                if (sans_current_time - sans_last_typing_time) >= TYPING_DELAY and sans_main_typing_index < len(SANS_TEXT_MAIN[sans_line_index]):
                    sans_last_typing_time, sans_main_typing_index = typewriter_animation(
                        sans_current_time,
                        sans_last_typing_time,
                        sans_main_typing_index, 
                        SANS_TEXT_MAIN[sans_line_index] ,
                        sans_typing_sound
                        )
                    
                if (sans_current_time - sans_last_typing_time) >= typing_delay_betw_speeches:
                    if sans_main_typing_index >= len(SANS_TEXT_MAIN[sans_line_index]):
                        sans_main_typing_index = 0
                        if sans_line_index < len(SANS_TEXT_MAIN):
                            sans_line_index += 1


            #------------------------------------------------------------------------------
            # San's Finishing Set up
            #------------------------------------------------------------------------------

            if  sans_dialogue in ["Choices","Puns + Choices"]:


                sans_character_current_alpha = min( 255, sans_character_current_alpha + 5)


                #character 
                chara_surface[0].set_alpha(sans_character_current_alpha)
                flowey_surface[0].set_alpha(sans_character_current_alpha)
                papyrus_surface.set_alpha(sans_character_current_alpha)
                toriel_surface.set_alpha(sans_character_current_alpha)
                

                #------------------------------------------------------------------------------
                # San's Choices Character Animation
                #------------------------------------------------------------------------------

                chara_box_detect, _ = character_box(
                    screen,
                    BLACK ,
                    CHARA_COLOR[0] ,
                    mouse_pos ,
                    sans_character_current_alpha,
                    pos = (207,187)
                    ) # chara



                flowey_box_detect , _ = character_box(
                    screen,
                    BLACK ,
                    FLOWEY_COLOR[0],
                    mouse_pos ,
                    sans_character_current_alpha,
                    pos = (463,187)
                    ) # flowey
                

                papyrus_box_detect, _ = character_box(
                    screen,
                    BLACK ,
                    PAPYRUS_COLOR[0] ,
                    mouse_pos ,
                    sans_character_current_alpha,
                    pos = (719,187)
                    ) # papryus
                

                toriel_box_detect, _ = character_box(
                    screen,
                    BLACK ,
                    TORIEL_COLOR[0] ,
                    mouse_pos ,
                    sans_character_current_alpha,
                    pos = (975,187)
                    ) # toriel
                
                #------------------------------------------------------------------------------
                # San's Choices Car Name Animation
                #------------------------------------------------------------------------------


                chara_pos, sans_chara_alpha = car_name_animation(
                    screen, chara_box_detect,  sans_chara_alpha, (255,255,153), mouse_pos, pos= chara_pos,
                    size= (150, 50), target_location = (chara_pos[0], TARGET_Y),
                    text = "Toyota" , font= FONT 
                )
                
                flowey_pos, sans_flowey_alpha = car_name_animation(
                    screen, flowey_box_detect, sans_flowey_alpha, (255,153,153), mouse_pos, 
                    pos= flowey_pos, size = (150,50), target_location = ( flowey_pos[0], TARGET_Y),
                    text = "Jetour" , font=FONT 
                )

                papyrus_pos, sans_papyrus_alpha = car_name_animation(
                    screen,papyrus_box_detect, sans_papyrus_alpha , (153,204,255), mouse_pos, 
                    pos= papyrus_pos , size = (150, 50), target_location=(papyrus_pos[0], TARGET_Y),
                    text= "Honda", font= FONT 
                )

                toriel_pos, sans_toriel_alpha= car_name_animation(
                    screen, toriel_box_detect , sans_toriel_alpha, (204,153, 255), mouse_pos, 
                    pos= toriel_pos, size= (125,50), target_location=(toriel_pos[0], TARGET_Y),
                    text = "BMW", font = FONT
                )

                #------------------------------------------------------------------------------
                # San's  Character BLIT
                #------------------------------------------------------------------------------


                screen.blit(chara_surface[0] , (220,200))
                screen.blit(flowey_surface[0] , (476,200))
                screen.blit(papyrus_surface, (732, 200))
                screen.blit(toriel_surface, (988, 200))


                #------------------------------------------------------------------------------
                # San's Change Pages
                #------------------------------------------------------------------------------


                if chara_box_detect.collidepoint(mouse_pos) and clicked:
                    sans_page = False
                    chara_page_1 = True
                    chara_camry_page_2 = False
                    sans_first_time = False



                if flowey_box_detect.collidepoint(mouse_pos) and clicked:
                    sans_page = False
                    flowey_page_1 = True
                    sans_first_time = False



                if papyrus_box_detect.collidepoint(mouse_pos) and clicked:
                    sans_page = False
                    papyrus_page_1 = True
                    sans_first_time = False


                if toriel_box_detect.collidepoint(mouse_pos) and clicked:
                    sans_page = False
                    toriel_page_1 = True
                    sans_first_time = False


        #-----------------------------------------------------------------------------------------------------
        # Chara's Page 
        #------------------------------------------------------------------------------------------------------


        if chara_page_1:

            #------------------------------------------------------------------------------
            # Chara's Basic Set up
            #------------------------------------------------------------------------------

            if chara_first_time:
                chara_page_time = sans_current_time    
            chara_first_time = False



            if chara_dialogue in ["None", "Intro" ,"Main Speech", "Choices"]:

                chara_bg_frame, frame_index_chara_background, chara_background_last_update = gif_framerate(
                    chara_background_surface,       
                    chara_background_last_update,    
                    frame_index_chara_background,
                    current_time= chara_current_time,    
                    frame_delay_ms=FRAME_DELAY_MS   
                    )

                screen.blit(chara_bg_frame, (0, 0))



            #------------------------------------------------------------------------------
            # Chara's Introduction Lines
            #------------------------------------------------------------------------------


                page_changed , chara_page_1, chara_escape_button_alpha = escape_button(
                    screen, color = (100, 10, 10) ,
                    alpha= chara_escape_button_alpha,
                    border_color=CHARA_COLOR[2],
                    highlight_color=(180, 40, 40),
                    mouse_pos= mouse_pos,
                    clicked= clicked, main_page=sans_page,
                    current_page= chara_page_1,
                    button_size=(100,50), pos = (50, 50)
                    )



                if page_changed:
                    sans_page = True
                    chara_page_1 = False
                    chara_camry_page_2 = False
                    chara_first_time = False
                    previous_dialogue = "None"
                    sans_pun_line_index = 0
                    sans_pun_typing_index = 0





            if chara_dialogue in ["Intro", "Main Speech", "Choices"]:

                speech_bubble(screen, pos=SPEECH_BUBBLE_POS, bubble_color= CHARA_COLOR[1] , border_color= CHARA_COLOR[2])

                chara_current_alpha = min(255, chara_current_alpha + 5)

                frame, frame_index_chara, chara_last_update = gif_framerate(
                    chara_surface_2,        
                    chara_last_update,    
                    frame_index_chara,
                    current_time= chara_current_time,    
                    frame_delay_ms= FRAME_DELAY_MS,      
                    current_alpha= chara_current_alpha        
                )
            

                screen.blit(frame, (80, 505))
            

            #------------------------------------------------------------------------------
            # Chara's Main Speech Lines
            #------------------------------------------------------------------------------


            if  chara_dialogue in ["Main Speech"]:
                try:

                    typewriter_effect(
                        screen,
                        chara_main_typing_index,
                        CHARA_MAIN_TEXT[chara_line_index],
                        FONT,
                        BLACK,
                        char_width = CHARACTER_WIDTH,
                        pos=SPEECH_BUBBLE_POS,
                        type_padding= PADDING,
                        )

                    

                    if (chara_current_time - chara_last_typing_time) >= TYPING_DELAY and chara_main_typing_index < len(CHARA_MAIN_TEXT[chara_line_index]):
                        chara_last_typing_time, chara_main_typing_index = typewriter_animation(
                            chara_current_time,
                            chara_last_typing_time,
                            chara_main_typing_index, 
                            CHARA_MAIN_TEXT[chara_line_index] ,
                            chara_typing_sound
                            )
                        
                    if (chara_current_time - chara_last_typing_time) >= typing_delay_betw_speeches:
                        if chara_main_typing_index >= len(CHARA_MAIN_TEXT[chara_line_index]):
                            chara_main_typing_index = 0
                            if chara_line_index < len(CHARA_MAIN_TEXT):
                                chara_line_index += 1
                
                except IndexError:
                    chara_dialogue = "Choices"



            #------------------------------------------------------------------------------
            # Chara's Finishing Set up
            #------------------------------------------------------------------------------


            if chara_dialogue in ["Choices"]:


                toyota_camry.set_alpha(chara_cars_alpha)
                toyota_fortuner.set_alpha(chara_cars_alpha) 
                toyota_land_cruiser.set_alpha(chara_cars_alpha)


                chara_cars_alpha = min( 255,chara_cars_alpha + 5)

                #------------------------------------------------------------------------------
                # Chara's Choices Car Animation
                #------------------------------------------------------------------------------
               
                
                camry_box_detect , chara_camry_page_2= character_box(
                    screen, (72, 179, 224) ,
                    (241,73,77) , mouse_pos ,
                    alpha= chara_cars_alpha,
                    pos = (207, 175), size = (200,200), 
                    hover_effect= (30,30),
                    border_radius= 5,
                    clicked= clicked,
                    car_page= chara_camry_page_2
                    )

                fortuner_box_detect, chara_fortuner_page_2 = character_box(
                    screen,  (72, 179, 224) ,
                    (241,73,77), mouse_pos ,
                    alpha=chara_cars_alpha,pos = (591, 175), size = (200,200) ,
                    hover_effect= (30,30)  ,
                    border_radius= 5,
                    clicked= clicked,
                    car_page=chara_fortuner_page_2
                    ) 

                
  
                land_cruiser_box_detect, chara_land_cruiser_page_2 = character_box(
                    screen, (72, 179, 224)  ,
                    (241,73,77) ,mouse_pos ,
                    alpha= chara_cars_alpha,
                    pos = (975, 175),size = (200,200) ,
                    hover_effect= (30,30)  ,
                    border_radius= 5,
                    clicked= clicked,
                    car_page = chara_land_cruiser_page_2
                    ) 
                



                #------------------------------------------------------------------------------
                # Chara's Choices Car Name Animation
                #------------------------------------------------------------------------------

                camry_pos, camry_alpha = car_name_animation(
                    screen,camry_box_detect, camry_alpha , (241,73,77), mouse_pos, 
                    pos=camry_pos , size = (150, 50), target_location=(225, TARGET_YX),
                    text= "Camry", font= FONT 
                )


                fortuner_pos , fortuner_alpha = car_name_animation(
                    screen, fortuner_box_detect, fortuner_alpha, (241,73,77), mouse_pos, 
                    pos= fortuner_pos, size = (180,50), target_location = (600, TARGET_YX),
                    text = "Fortuner" , font=FONT 
                )



                land_cruiser_pos , land_cruiser_alpha = car_name_animation(
                    screen, land_cruiser_box_detect,  land_cruiser_alpha, (241,73,77), mouse_pos, pos= land_cruiser_pos,
                    size= (250, 50), target_location = (950, TARGET_YX),
                    text = "Land Cruiser" , font= FONT 
                )
                

                #------------------------------------------------------------------------------
                # Chara's  Car BLIT
                #------------------------------------------------------------------------------

                screen.blit(toyota_camry_icon, (225,200))
                screen.blit(toyota_fortuner_icon, (620,200))
                screen.blit(toyota_land_cruiser_icon, (1000,200))


                #--------------------------------------------------------------------------------
                # Chara's Camry Page
                #----------------------------------------------------------------------------------

                if chara_camry_page_2:
                    

                    #---------------------------------------------------------------------------
                    # Page Movement Logic
                    #-----------------------------------------------------------------------------

                    if chara_camry_slide_in:


                        if chara_camry_panel_x  >= 270:  
                            chara_camry_panel_x  -= 50
                        if chara_camry_panel_x  < 280:
                            chara_camry_overlay_alpha = min(150, chara_camry_overlay_alpha + 5)
                            


                    if chara_camry_slide_out:

                        if chara_camry_panel_x  < 1280:  
                            chara_camry_panel_x  += 50
                            chara_camry_overlay_alpha = max(0, chara_camry_overlay_alpha - 50)

                        if chara_camry_panel_x > 1270:
                            chara_camry_slide_in = True
                            chara_camry_page_2 = False
                            chara_camry_slide_out = False
                                            
                    
                    #----------------------------------------------------------------------------------------
                    # Main Side-Slide for Camry
                    #-----------------------------------------------------------------------------------------

                    if chara_camry_panel_x < 280:
                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                        overlay.fill((50,50,50,chara_camry_overlay_alpha))
                        screen.blit(overlay,(0,0))
                            

                        panel_rect = pygame.Rect(chara_camry_panel_x , 0,1200, 720)
                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                        chara_camry_slide_out , chara_camry_slide_in, chara_camry_escape_button_alpha = escape_button(
                            screen, color = (100, 10, 10) ,
                            alpha= chara_camry_escape_button_alpha,
                            border_color=CHARA_COLOR[2],
                            highlight_color=(180, 40, 40),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=chara_camry_slide_out,
                            current_page= chara_camry_slide_in,
                            button_size=(150,50), pos = (250, 50),
                            text_name="Back"
                            )

                        screen.blit(toyota_camry, (650, 50))

                        chara_camry_submit_page, _, chara_buy_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= chara_buy_button_alpha,
                            border_color=(144, 238, 144),
                            highlight_color=(144, 238, 144),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=chara_camry_submit_page,
                            current_page= _,
                            button_size=(150,50), pos = (1100, 600),
                            text_name="Buy"
                            )


                        #----------------------------------------------------------------------------------
                        # Camry Typing 
                        #------------------------------------------------------------------------------------

           
                        typewriter_effect(
                            screen,
                            chara_camry_typing_index_1, 
                            CHARA_CAMRY_TEXT_1[chara_camry_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(250, 180), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                                            
                        typewriter_effect(
                            screen,
                            chara_camry_typing_index_2 if chara_camry_first_text_complete else 0,  
                            CHARA_CAMRY_TEXT_2[chara_camry_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(680, 380), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                        


                        if not chara_camry_first_text_complete:

                            if (chara_current_time - chara_last_typing_time) >= TYPING_DELAY and chara_camry_typing_index_1 < len(CHARA_CAMRY_TEXT_1[chara_camry_line_index]):
                                chara_last_typing_time, chara_camry_typing_index_1 = typewriter_animation(
                                    chara_current_time,
                                    chara_last_typing_time,
                                    chara_camry_typing_index_1,
                                    CHARA_CAMRY_TEXT_1[chara_camry_line_index],
                                    chara_typing_sound
                                )
                            elif chara_camry_typing_index_1 >= len(CHARA_CAMRY_TEXT_1[chara_camry_line_index]):

                                chara_camry_first_text_complete = True
                                chara_last_typing_time = chara_current_time  

                        else:

                            if (chara_current_time - chara_last_typing_time) >= TYPING_DELAY and chara_camry_typing_index_2 < len(CHARA_CAMRY_TEXT_2[chara_camry_line_index]):
                                chara_last_typing_time, chara_camry_typing_index_2 = typewriter_animation(
                                    chara_current_time,
                                    chara_last_typing_time,
                                    chara_camry_typing_index_2,
                                    CHARA_CAMRY_TEXT_2[chara_camry_line_index],
                                    chara_typing_sound
                                )



                        if chara_camry_submit_page:


                            chara_camry_bought_overlay_alpha = min(150, chara_camry_bought_overlay_alpha + 5)  

                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                            bought_overlay.fill((50, 50, 50, chara_camry_bought_overlay_alpha))
                            screen.blit(bought_overlay, (0, 0))



                            box_size = (400, 200)
                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                            _,  chara_camry_submit_page, chara_bought_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= chara_bought_button_alpha,
                            border_color=(0, 200, 0),
                            highlight_color=(0, 200, 0),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=_,
                            current_page= chara_camry_submit_page,
                            button_size=box_size, pos = (box_x, box_y),
                            text_name="Bought"
                            )

                #--------------------------------------------------------------------------------
                # Chara's Fortuner Page
                #---------------------------------------------------------------------------------

                if chara_fortuner_page_2:
                                    
                                    

                                    #---------------------------------------------------------------------------
                                    # Page Movement Logic
                                    #-----------------------------------------------------------------------------

                                    if chara_fortuner_slide_in:


                                        if chara_fortuner_panel_x  >= 270:  
                                            chara_fortuner_panel_x  -= 50
                                        if chara_fortuner_panel_x  < 280:
                                            chara_fortuner_overlay_alpha = min(150, chara_fortuner_overlay_alpha + 5)
                                            


                                    if chara_fortuner_slide_out:

                                        if chara_fortuner_panel_x  < 1280:  
                                            chara_fortuner_panel_x  += 50
                                            chara_fortuner_overlay_alpha = max(0, chara_fortuner_overlay_alpha - 50)

                                        if chara_fortuner_panel_x > 1270:
                                            chara_fortuner_slide_in = True
                                            chara_fortuner_page_2 = False
                                            chara_fortuner_slide_out = False
                                                            
                                    
                                    #----------------------------------------------------------------------------------------
                                    # Main Side-Slide for Fortuner
                                    #-----------------------------------------------------------------------------------------

                                    if chara_fortuner_panel_x < 280:
                                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                                        overlay.fill((50,50,50,chara_fortuner_overlay_alpha))
                                        screen.blit(overlay,(0,0))
                                            

                                        panel_rect = pygame.Rect(chara_fortuner_panel_x , 0,1200, 720)
                                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                                        chara_fortuner_slide_out , chara_fortuner_slide_in, chara_fortuner_escape_button_alpha = escape_button(
                                            screen, color = (100, 10, 10) ,
                                            alpha= chara_fortuner_escape_button_alpha,
                                            border_color=CHARA_COLOR[2],
                                            highlight_color=(180, 40, 40),
                                            mouse_pos= mouse_pos,
                                            clicked= clicked, main_page=chara_fortuner_slide_out,
                                            current_page= chara_fortuner_slide_in,
                                            button_size=(150,50), pos = (250, 50),
                                            text_name="Back"
                                            )

                                        screen.blit(toyota_fortuner, (650, 50))

                                        chara_fortuner_submit_page, _, chara_buy_button_alpha = escape_button(
                                            screen, color = (0, 200, 0) ,
                                            alpha= chara_buy_button_alpha,
                                            border_color=(144, 238, 144),
                                            highlight_color=(144, 238, 144),
                                            mouse_pos= mouse_pos,
                                            clicked= clicked, main_page= chara_fortuner_submit_page,
                                            current_page= _,
                                            button_size=(150,50), pos = (1100, 600),
                                            text_name="Buy"
                                            )


                                        #----------------------------------------------------------------------------------
                                        # Fortuner Typing 
                                        #------------------------------------------------------------------------------------

                        
                                        typewriter_effect(
                                            screen,
                                            chara_fortuner_typing_index_1, 
                                            CHARA_FORTUNER_TEXT_1[chara_fortuner_line_index],
                                            FONT, 
                                            char_width=20, 
                                            pos=(250, 180), 
                                            type_padding=PADDING,
                                            text_color=BLACK
                                        )
                                                                            
                                        typewriter_effect(
                                            screen,
                                            chara_fortuner_typing_index_2 if chara_fortuner_first_text_complete else 0,  
                                            CHARA_FORTUNER_TEXT_2[chara_fortuner_line_index],
                                            FONT, 
                                            char_width=20, 
                                            pos=(680, 380), 
                                            type_padding=PADDING,
                                            text_color=BLACK
                                        )
                                                        


                                        if not chara_fortuner_first_text_complete:

                                            if (chara_current_time - chara_last_typing_time) >= TYPING_DELAY and chara_fortuner_typing_index_1 < len(CHARA_FORTUNER_TEXT_1[chara_fortuner_line_index]):
                                                chara_last_typing_time, chara_fortuner_typing_index_1 = typewriter_animation(
                                                    chara_current_time,
                                                    chara_last_typing_time,
                                                    chara_fortuner_typing_index_1,
                                                    CHARA_FORTUNER_TEXT_1[chara_fortuner_line_index],
                                                    chara_typing_sound
                                                )
                                            elif chara_fortuner_typing_index_1 >= len(CHARA_FORTUNER_TEXT_1[chara_fortuner_line_index]):

                                                chara_fortuner_first_text_complete = True
                                                chara_last_typing_time = chara_current_time  

                                        else:

                                            if (chara_current_time - chara_last_typing_time) >= TYPING_DELAY and chara_fortuner_typing_index_2 < len(CHARA_FORTUNER_TEXT_2[chara_fortuner_line_index]):
                                                chara_last_typing_time, chara_fortuner_typing_index_2 = typewriter_animation(
                                                    chara_current_time,
                                                    chara_last_typing_time,
                                                    chara_fortuner_typing_index_2,
                                                    CHARA_FORTUNER_TEXT_2[chara_fortuner_line_index],
                                                    chara_typing_sound
                                                )



                                        if chara_fortuner_submit_page:


                                            chara_fortuner_bought_overlay_alpha = min(150, chara_fortuner_bought_overlay_alpha + 5)  

                                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                                            bought_overlay.fill((50, 50, 50, chara_fortuner_bought_overlay_alpha))
                                            screen.blit(bought_overlay, (0, 0))



                                            box_size = (400, 200)
                                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                                            _,  chara_fortuner_submit_page, chara_bought_button_alpha = escape_button(
                                            screen, color = (0, 200, 0) ,
                                            alpha= chara_bought_button_alpha,
                                            border_color=(0, 200, 0),
                                            highlight_color=(0, 200, 0),
                                            mouse_pos= mouse_pos,
                                            clicked= clicked, main_page=_,
                                            current_page= chara_fortuner_submit_page,
                                            button_size=box_size, pos = (box_x, box_y),
                                            text_name="Bought"
                                            )
                
                #--------------------------------------------------------------------------------
                # Chara's Land Cruiser Page
                #----------------------------------------------------------------------------------

                if chara_land_cruiser_page_2:

                    #---------------------------------------------------------------------------
                    # Page Movement Logic
                    #-----------------------------------------------------------------------------

                    if chara_land_cruiser_slide_in:


                        if chara_land_cruiser_panel_x  >= 270:  
                            chara_land_cruiser_panel_x  -= 50
                        if chara_land_cruiser_panel_x  < 280:
                            chara_land_cruiser_overlay_alpha = min(150, chara_land_cruiser_overlay_alpha + 5)
                            


                    if chara_land_cruiser_slide_out:

                        if chara_land_cruiser_panel_x  < 1280:  
                            chara_land_cruiser_panel_x  += 50
                            chara_land_cruiser_overlay_alpha = max(0, chara_land_cruiser_overlay_alpha - 50)

                        if chara_land_cruiser_panel_x > 1270:
                            chara_land_cruiser_slide_in = True
                            chara_land_cruiser_page_2 = False
                            chara_land_cruiser_slide_out = False
                                            
                    
                    #----------------------------------------------------------------------------------------
                    # Main Side-Slide for Camry
                    #-----------------------------------------------------------------------------------------

                    if chara_land_cruiser_panel_x < 280:
                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                        overlay.fill((50,50,50,chara_land_cruiser_overlay_alpha))
                        screen.blit(overlay,(0,0))
                            

                        panel_rect = pygame.Rect(chara_land_cruiser_panel_x , 0,1200, 720)
                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                        chara_land_cruiser_slide_out , chara_land_cruiser_slide_in, chara_land_cruiser_escape_button_alpha = escape_button(
                            screen, color = (100, 10, 10) ,
                            alpha= chara_land_cruiser_escape_button_alpha,
                            border_color=CHARA_COLOR[2],
                            highlight_color=(180, 40, 40),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=chara_land_cruiser_slide_out,
                            current_page= chara_land_cruiser_slide_in,
                            button_size=(150,50), pos = (250, 50),
                            text_name="Back"
                            )

                        screen.blit(toyota_land_cruiser, (650, 50))

                        chara_land_cruiser_submit_page, _, chara_buy_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= chara_buy_button_alpha,
                            border_color=(144, 238, 144),
                            highlight_color=(144, 238, 144),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page= chara_land_cruiser_submit_page,
                            current_page= _,
                            button_size=(150,50), pos = (1100, 600),
                            text_name="Buy"
                            )


                        #----------------------------------------------------------------------------------
                        # Camry Typing 
                        #------------------------------------------------------------------------------------

        
                        typewriter_effect(
                            screen,
                            chara_land_cruiser_typing_index_1, 
                            CHARA_LAND_CRUISER_TEXT_1[chara_land_cruiser_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(250, 120), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                                            
                        typewriter_effect(
                            screen,
                            chara_land_cruiser_typing_index_2 if chara_land_cruiser_first_text_complete else 0,  
                            CHARA_LAND_CRUISER_TEXT_2[chara_land_cruiser_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(680, 380), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                        


                        if not chara_land_cruiser_first_text_complete:

                            if (chara_current_time - chara_last_typing_time) >= TYPING_DELAY and chara_land_cruiser_typing_index_1 < len(CHARA_LAND_CRUISER_TEXT_1[chara_land_cruiser_line_index]):
                                chara_last_typing_time, chara_land_cruiser_typing_index_1 = typewriter_animation(
                                    chara_current_time,
                                    chara_last_typing_time,
                                    chara_land_cruiser_typing_index_1,
                                    CHARA_LAND_CRUISER_TEXT_1[chara_land_cruiser_line_index],
                                    chara_typing_sound
                                )
                            elif chara_land_cruiser_typing_index_1 >= len(CHARA_LAND_CRUISER_TEXT_1[chara_land_cruiser_line_index]):

                                chara_land_cruiser_first_text_complete = True
                                chara_last_typing_time = chara_current_time  

                        else:

                            if (chara_current_time - chara_last_typing_time) >= TYPING_DELAY and chara_land_cruiser_typing_index_2 < len(CHARA_LAND_CRUISER_TEXT_2[chara_land_cruiser_line_index]):
                                chara_last_typing_time, chara_land_cruiser_typing_index_2 = typewriter_animation(
                                    chara_current_time,
                                    chara_last_typing_time,
                                    chara_land_cruiser_typing_index_2,
                                    CHARA_LAND_CRUISER_TEXT_2[chara_land_cruiser_line_index],
                                    chara_typing_sound
                                )



                        if chara_land_cruiser_submit_page:


                            chara_land_cruiser_bought_overlay_alpha = min(150, chara_land_cruiser_bought_overlay_alpha + 5)  

                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                            bought_overlay.fill((50, 50, 50, chara_land_cruiser_bought_overlay_alpha))
                            screen.blit(bought_overlay, (0, 0))



                            box_size = (400, 200)
                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                            _,  chara_land_cruiser_submit_page, chara_bought_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= chara_bought_button_alpha,
                            border_color=(0, 200, 0),
                            highlight_color=(0, 200, 0),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=_,
                            current_page= chara_land_cruiser_submit_page,
                            button_size=box_size, pos = (box_x, box_y),
                            text_name="Bought"
                            )

        #-----------------------------------------------------------------------------------------------------
        # Flowey's Page 
        #------------------------------------------------------------------------------------------------------

        if flowey_page_1:

            #------------------------------------------------------------------------------
            # Flowey's Basic Set up
            #------------------------------------------------------------------------------

            if flowey_first_time:
                flowey_page_time = sans_current_time    
            flowey_first_time = False



            if flowey_dialogue in ["None", "Intro" ,"Main Speech", "Choices"]:

                flowey_bg_frame, frame_index_flowey_background, flowey_background_last_update = gif_framerate(
                    flowey_background_surface,       
                    flowey_background_last_update,    
                    frame_index_flowey_background,
                    current_time= flowey_current_time,    
                    frame_delay_ms=FRAME_DELAY_MS   
                    )

                screen.blit(flowey_bg_frame, (0, 0))



            #------------------------------------------------------------------------------
            # Flowey's Introduction Lines
            #------------------------------------------------------------------------------


                page_changed , flowey_page_1, flowey_escape_button_alpha = escape_button(
                    screen, color = (100, 10, 10) ,
                    alpha= flowey_escape_button_alpha,
                    border_color=FLOWEY_COLOR[2],
                    highlight_color=(180, 40, 40),
                    mouse_pos= mouse_pos,
                    clicked= clicked, main_page=sans_page,
                    current_page= flowey_page_1,
                    button_size=(100,50), pos = (50, 50)
                    )



                if page_changed:
                    sans_page = True
                    flowey_page_1 = False
                    flowey_x70_plus_page_2 = False
                    flowey_first_time = False
                    previous_dialogue = "None"
                    sans_pun_line_index = 0
                    sans_pun_typing_index = 0





            if flowey_dialogue in ["Intro", "Main Speech", "Choices"]:

                speech_bubble(screen, pos=SPEECH_BUBBLE_POS, bubble_color= FLOWEY_COLOR[1] , border_color= FLOWEY_COLOR[2])

                flowey_current_alpha = min(255, flowey_current_alpha + 5)

                frame, frame_index_flowey, flowey_last_update = gif_framerate(
                    flowey_surface_2,        
                    flowey_last_update,    
                    frame_index_flowey,
                    current_time= flowey_current_time,    
                    frame_delay_ms= FRAME_DELAY_MS,      
                    current_alpha= flowey_current_alpha        
                )
            

                screen.blit(frame, (80, 505))
            

            #------------------------------------------------------------------------------
            # Flowey's Main Speech Lines
            #------------------------------------------------------------------------------


            if  flowey_dialogue in ["Main Speech"]:
                try:

                    typewriter_effect(
                        screen,
                        flowey_main_typing_index,
                        FLOWEY_MAIN_TEXT[flowey_line_index],
                        FONT,
                        BLACK,
                        char_width = CHARACTER_WIDTH,
                        pos=SPEECH_BUBBLE_POS,
                        type_padding= PADDING,
                        )

                    

                    if (flowey_current_time - flowey_last_typing_time) >= TYPING_DELAY and flowey_main_typing_index < len(FLOWEY_MAIN_TEXT[flowey_line_index]):
                        flowey_last_typing_time, flowey_main_typing_index = typewriter_animation(
                            flowey_current_time,
                            flowey_last_typing_time,
                            flowey_main_typing_index, 
                            FLOWEY_MAIN_TEXT[flowey_line_index] ,
                            flowey_typing_sound
                            )
                        
                    if (flowey_current_time - flowey_last_typing_time) >= typing_delay_betw_speeches:
                        if flowey_main_typing_index >= len(FLOWEY_MAIN_TEXT[flowey_line_index]):
                            flowey_main_typing_index = 0
                            if flowey_line_index < len(FLOWEY_MAIN_TEXT):
                                flowey_line_index += 1
                
                except IndexError:
                    flowey_dialogue = "Choices"



            #------------------------------------------------------------------------------
            # Flowey's Finishing Set up
            #------------------------------------------------------------------------------


            if flowey_dialogue in ["Choices"]:


                jetour_x70_plus.set_alpha(flowey_cars_alpha)
                jetour_x90_plus.set_alpha(flowey_cars_alpha) 
                jetour_dashing.set_alpha(flowey_cars_alpha)


                flowey_cars_alpha = min( 255,flowey_cars_alpha + 5)

                #------------------------------------------------------------------------------
                # Flowey's Choices Car Animation
                #------------------------------------------------------------------------------
               
                
                x70_plus_box_detect , flowey_x70_plus_page_2= character_box(
                    screen, (72, 179, 224) ,
                    (241,73,77) , mouse_pos ,
                    alpha= flowey_cars_alpha,
                    pos = (207, 175), size = (200,200), 
                    hover_effect= (30,30),
                    border_radius= 5,
                    clicked= clicked,
                    car_page= flowey_x70_plus_page_2
                    )

                x90_plus_box_detect, flowey_x90_plus_page_2 = character_box(
                    screen,  (72, 179, 224) ,
                    (241,73,77), mouse_pos ,
                    alpha=flowey_cars_alpha,pos = (591, 175), size = (200,200) ,
                    hover_effect= (30,30)  ,
                    border_radius= 5,
                    clicked= clicked,
                    car_page=flowey_x90_plus_page_2
                    ) 

                
  
                dashing_box_detect, flowey_dashing_page_2 = character_box(
                    screen, (72, 179, 224)  ,
                    (241,73,77) ,mouse_pos ,
                    alpha= flowey_cars_alpha,
                    pos = (975, 175),size = (200,200) ,
                    hover_effect= (30,30)  ,
                    border_radius= 5,
                    clicked= clicked,
                    car_page = flowey_dashing_page_2
                    ) 
                



                #------------------------------------------------------------------------------
                # Flowey's Choices Car Name Animation
                #------------------------------------------------------------------------------

                x70_plus_pos, x70_plus_alpha = car_name_animation(
                    screen,x70_plus_box_detect, x70_plus_alpha , (241,73,77), mouse_pos, 
                    pos=x70_plus_pos , size = (150, 50), target_location=(225, TARGET_YX),
                    text= "X70 Plus", font= FONT 
                )


                x90_plus_pos , x90_plus_alpha = car_name_animation(
                    screen, x90_plus_box_detect, x90_plus_alpha, (241,73,77), mouse_pos, 
                    pos= x90_plus_pos, size = (180,50), target_location = (600, TARGET_YX),
                    text = "X90 Plus" , font=FONT 
                )



                dashing_pos , dashing_alpha = car_name_animation(
                    screen, dashing_box_detect,  dashing_alpha, (241,73,77), mouse_pos, pos= dashing_pos,
                    size= (250, 50), target_location = (950, TARGET_YX),
                    text = "Dashing" , font= FONT 
                )
                

                #------------------------------------------------------------------------------
                # Flowey's  Car BLIT
                #------------------------------------------------------------------------------

                screen.blit(jetour_x70_plus_icon, (225,200))
                screen.blit(jetour_x90_plus_icon, (620,200))
                screen.blit(jetour_dashing_icon, (1000,200))


                #--------------------------------------------------------------------------------
                # Flowey's X70 Plus Page
                #----------------------------------------------------------------------------------

                if flowey_x70_plus_page_2:
                    

                    #---------------------------------------------------------------------------
                    # Page Movement Logic
                    #-----------------------------------------------------------------------------

                    if flowey_x70_plus_slide_in:


                        if flowey_x70_plus_panel_x  >= 270:  
                            flowey_x70_plus_panel_x  -= 50
                        if flowey_x70_plus_panel_x  < 280:
                            flowey_x70_plus_overlay_alpha = min(150, flowey_x70_plus_overlay_alpha + 5)
                            


                    if flowey_x70_plus_slide_out:

                        if flowey_x70_plus_panel_x  < 1280:  
                            flowey_x70_plus_panel_x  += 50
                            flowey_x70_plus_overlay_alpha = max(0, flowey_x70_plus_overlay_alpha - 50)

                        if flowey_x70_plus_panel_x > 1270:
                            flowey_x70_plus_slide_in = True
                            flowey_x70_plus_page_2 = False
                            flowey_x70_plus_slide_out = False
                                            
                    
                    #----------------------------------------------------------------------------------------
                    # Main Side-Slide for X70 Plus
                    #-----------------------------------------------------------------------------------------

                    if flowey_x70_plus_panel_x < 280:
                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                        overlay.fill((50,50,50,flowey_x70_plus_overlay_alpha))
                        screen.blit(overlay,(0,0))
                            

                        panel_rect = pygame.Rect(flowey_x70_plus_panel_x , 0,1200, 720)
                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                        flowey_x70_plus_slide_out , flowey_x70_plus_slide_in, flowey_x70_plus_escape_button_alpha = escape_button(
                            screen, color = (100, 10, 10) ,
                            alpha= flowey_x70_plus_escape_button_alpha,
                            border_color=FLOWEY_COLOR[2],
                            highlight_color=(180, 40, 40),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=flowey_x70_plus_slide_out,
                            current_page= flowey_x70_plus_slide_in,
                            button_size=(150,50), pos = (250, 50),
                            text_name="Back"
                            )

                        screen.blit(jetour_x70_plus, (650, 50))

                        flowey_x70_plus_submit_page, _, flowey_buy_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= flowey_buy_button_alpha,
                            border_color=(144, 238, 144),
                            highlight_color=(144, 238, 144),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=flowey_x70_plus_submit_page,
                            current_page= _,
                            button_size=(150,50), pos = (1100, 600),
                            text_name="Buy"
                            )


                        #----------------------------------------------------------------------------------
                        # X70 Plus Typing 
                        #------------------------------------------------------------------------------------

           
                        typewriter_effect(
                            screen,
                            flowey_x70_plus_typing_index_1, 
                            FLOWEY_X70_PLUS_TEXT_1[flowey_x70_plus_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(250, 180), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                                            
                        typewriter_effect(
                            screen,
                            flowey_x70_plus_typing_index_2 if flowey_x70_plus_first_text_complete else 0,  
                            FLOWEY_X70_PLUS_TEXT_2[flowey_x70_plus_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(680, 380), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                        


                        if not flowey_x70_plus_first_text_complete:

                            if (flowey_current_time - flowey_last_typing_time) >= TYPING_DELAY and flowey_x70_plus_typing_index_1 < len(FLOWEY_X70_PLUS_TEXT_1[flowey_x70_plus_line_index]):
                                flowey_last_typing_time, flowey_x70_plus_typing_index_1 = typewriter_animation(
                                    flowey_current_time,
                                    flowey_last_typing_time,
                                    flowey_x70_plus_typing_index_1,
                                    FLOWEY_X70_PLUS_TEXT_1[flowey_x70_plus_line_index],
                                    flowey_typing_sound
                                )
                            elif flowey_x70_plus_typing_index_1 >= len(FLOWEY_X70_PLUS_TEXT_1[flowey_x70_plus_line_index]):

                                flowey_x70_plus_first_text_complete = True
                                flowey_last_typing_time = flowey_current_time  

                        else:

                            if (flowey_current_time - flowey_last_typing_time) >= TYPING_DELAY and flowey_x70_plus_typing_index_2 < len(FLOWEY_X70_PLUS_TEXT_2[flowey_x70_plus_line_index]):
                                flowey_last_typing_time, flowey_x70_plus_typing_index_2 = typewriter_animation(
                                    flowey_current_time,
                                    flowey_last_typing_time,
                                    flowey_x70_plus_typing_index_2,
                                    FLOWEY_X70_PLUS_TEXT_2[flowey_x70_plus_line_index],
                                    flowey_typing_sound
                                )



                        if flowey_x70_plus_submit_page:


                            flowey_x70_plus_bought_overlay_alpha = min(150, flowey_x70_plus_bought_overlay_alpha + 5)  

                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                            bought_overlay.fill((50, 50, 50, flowey_x70_plus_bought_overlay_alpha))
                            screen.blit(bought_overlay, (0, 0))



                            box_size = (400, 200)
                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                            _,  flowey_x70_plus_submit_page, flowey_bought_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= flowey_bought_button_alpha,
                            border_color=(0, 200, 0),
                            highlight_color=(0, 200, 0),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=_,
                            current_page= flowey_x70_plus_submit_page,
                            button_size=box_size, pos = (box_x, box_y),
                            text_name="Bought"
                            )

                #--------------------------------------------------------------------------------
                # Flowey's X90 Plus Page
                #---------------------------------------------------------------------------------

                if flowey_x90_plus_page_2:
                                    
                                    

                                    #---------------------------------------------------------------------------
                                    # Page Movement Logic
                                    #-----------------------------------------------------------------------------

                                    if flowey_x90_plus_slide_in:


                                        if flowey_x90_plus_panel_x  >= 270:  
                                            flowey_x90_plus_panel_x  -= 50
                                        if flowey_x90_plus_panel_x  < 280:
                                            flowey_x90_plus_overlay_alpha = min(150, flowey_x90_plus_overlay_alpha + 5)
                                            


                                    if flowey_x90_plus_slide_out:

                                        if flowey_x90_plus_panel_x  < 1280:  
                                            flowey_x90_plus_panel_x  += 50
                                            flowey_x90_plus_overlay_alpha = max(0, flowey_x90_plus_overlay_alpha - 50)

                                        if flowey_x90_plus_panel_x > 1270:
                                            flowey_x90_plus_slide_in = True
                                            flowey_x90_plus_page_2 = False
                                            flowey_x90_plus_slide_out = False
                                                            
                                    
                                    #----------------------------------------------------------------------------------------
                                    # Main Side-Slide for X90 Plus
                                    #-----------------------------------------------------------------------------------------

                                    if flowey_x90_plus_panel_x < 280:
                                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                                        overlay.fill((50,50,50,flowey_x90_plus_overlay_alpha))
                                        screen.blit(overlay,(0,0))
                                            

                                        panel_rect = pygame.Rect(flowey_x90_plus_panel_x , 0,1200, 720)
                                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                                        flowey_x90_plus_slide_out , flowey_x90_plus_slide_in, flowey_x90_plus_escape_button_alpha = escape_button(
                                            screen, color = (100, 10, 10) ,
                                            alpha= flowey_x90_plus_escape_button_alpha,
                                            border_color=FLOWEY_COLOR[2],
                                            highlight_color=(180, 40, 40),
                                            mouse_pos= mouse_pos,
                                            clicked= clicked, main_page=flowey_x90_plus_slide_out,
                                            current_page= flowey_x90_plus_slide_in,
                                            button_size=(150,50), pos = (250, 50),
                                            text_name="Back"
                                            )

                                        screen.blit(jetour_x90_plus, (650, 50))

                                        flowey_x90_plus_submit_page, _, flowey_buy_button_alpha = escape_button(
                                            screen, color = (0, 200, 0) ,
                                            alpha= flowey_buy_button_alpha,
                                            border_color=(144, 238, 144),
                                            highlight_color=(144, 238, 144),
                                            mouse_pos= mouse_pos,
                                            clicked= clicked, main_page= flowey_x90_plus_submit_page,
                                            current_page= _,
                                            button_size=(150,50), pos = (1100, 600),
                                            text_name="Buy"
                                            )


                                        #----------------------------------------------------------------------------------
                                        # X90 Plus Typing 
                                        #------------------------------------------------------------------------------------

                        
                                        typewriter_effect(
                                            screen,
                                            flowey_x90_plus_typing_index_1, 
                                            FLOWEY_X90_PLUS_TEXT_1[flowey_x90_plus_line_index],
                                            FONT, 
                                            char_width=20, 
                                            pos=(250, 180), 
                                            type_padding=PADDING,
                                            text_color=BLACK
                                        )
                                                                            
                                        typewriter_effect(
                                            screen,
                                            flowey_x90_plus_typing_index_2 if flowey_x90_plus_first_text_complete else 0,  
                                            FLOWEY_X90_PLUS_TEXT_2[flowey_x90_plus_line_index],
                                            FONT, 
                                            char_width=20, 
                                            pos=(680, 380), 
                                            type_padding=PADDING,
                                            text_color=BLACK
                                        )
                                                        


                                        if not flowey_x90_plus_first_text_complete:

                                            if (flowey_current_time - flowey_last_typing_time) >= TYPING_DELAY and flowey_x90_plus_typing_index_1 < len(FLOWEY_X90_PLUS_TEXT_1[flowey_x90_plus_line_index]):
                                                flowey_last_typing_time, flowey_x90_plus_typing_index_1 = typewriter_animation(
                                                    flowey_current_time,
                                                    flowey_last_typing_time,
                                                    flowey_x90_plus_typing_index_1,
                                                    FLOWEY_X90_PLUS_TEXT_1[flowey_x90_plus_line_index],
                                                    flowey_typing_sound
                                                )
                                            elif flowey_x90_plus_typing_index_1 >= len(FLOWEY_X90_PLUS_TEXT_1[flowey_x90_plus_line_index]):

                                                flowey_x90_plus_first_text_complete = True
                                                flowey_last_typing_time = flowey_current_time  

                                        else:

                                            if (flowey_current_time - flowey_last_typing_time) >= TYPING_DELAY and flowey_x90_plus_typing_index_2 < len(FLOWEY_X90_PLUS_TEXT_2[flowey_x90_plus_line_index]):
                                                flowey_last_typing_time, flowey_x90_plus_typing_index_2 = typewriter_animation(
                                                    flowey_current_time,
                                                    flowey_last_typing_time,
                                                    flowey_x90_plus_typing_index_2,
                                                    FLOWEY_X90_PLUS_TEXT_2[flowey_x90_plus_line_index],
                                                    flowey_typing_sound
                                                )



                                        if flowey_x90_plus_submit_page:


                                            flowey_x90_plus_bought_overlay_alpha = min(150, flowey_x90_plus_bought_overlay_alpha + 5)  

                                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                                            bought_overlay.fill((50, 50, 50, flowey_x90_plus_bought_overlay_alpha))
                                            screen.blit(bought_overlay, (0, 0))



                                            box_size = (400, 200)
                                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                                            _,  flowey_x90_plus_submit_page, flowey_bought_button_alpha = escape_button(
                                            screen, color = (0, 200, 0) ,
                                            alpha= flowey_bought_button_alpha,
                                            border_color=(0, 200, 0),
                                            highlight_color=(0, 200, 0),
                                            mouse_pos= mouse_pos,
                                            clicked= clicked, main_page=_,
                                            current_page= flowey_x90_plus_submit_page,
                                            button_size=box_size, pos = (box_x, box_y),
                                            text_name="Bought"
                                            )
                
                #--------------------------------------------------------------------------------
                # Flowey's Dashing Page
                #----------------------------------------------------------------------------------

                if flowey_dashing_page_2:

                    #---------------------------------------------------------------------------
                    # Page Movement Logic
                    #-----------------------------------------------------------------------------

                    if flowey_dashing_slide_in:


                        if flowey_dashing_panel_x  >= 270:  
                            flowey_dashing_panel_x  -= 50
                        if flowey_dashing_panel_x  < 280:
                            flowey_dashing_overlay_alpha = min(150, flowey_dashing_overlay_alpha + 5)
                            


                    if flowey_dashing_slide_out:

                        if flowey_dashing_panel_x  < 1280:  
                            flowey_dashing_panel_x  += 50
                            flowey_dashing_overlay_alpha = max(0, flowey_dashing_overlay_alpha - 50)

                        if flowey_dashing_panel_x > 1270:
                            flowey_dashing_slide_in = True
                            flowey_dashing_page_2 = False
                            flowey_dashing_slide_out = False
                                            
                    
                    #----------------------------------------------------------------------------------------
                    # Main Side-Slide for Dashing
                    #-----------------------------------------------------------------------------------------

                    if flowey_dashing_panel_x < 280:
                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                        overlay.fill((50,50,50,flowey_dashing_overlay_alpha))
                        screen.blit(overlay,(0,0))
                            

                        panel_rect = pygame.Rect(flowey_dashing_panel_x , 0,1200, 720)
                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                        flowey_dashing_slide_out , flowey_dashing_slide_in, flowey_dashing_escape_button_alpha = escape_button(
                            screen, color = (100, 10, 10) ,
                            alpha= flowey_dashing_escape_button_alpha,
                            border_color=FLOWEY_COLOR[2],
                            highlight_color=(180, 40, 40),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=flowey_dashing_slide_out,
                            current_page= flowey_dashing_slide_in,
                            button_size=(150,50), pos = (250, 50),
                            text_name="Back"
                            )

                        screen.blit(jetour_dashing, (650, 50))

                        flowey_dashing_submit_page, _, flowey_buy_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= flowey_buy_button_alpha,
                            border_color=(144, 238, 144),
                            highlight_color=(144, 238, 144),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page= flowey_dashing_submit_page,
                            current_page= _,
                            button_size=(150,50), pos = (1100, 600),
                            text_name="Buy"
                            )


                        #----------------------------------------------------------------------------------
                        # Dashing Typing 
                        #------------------------------------------------------------------------------------

        
                        typewriter_effect(
                            screen,
                            flowey_dashing_typing_index_1, 
                            FLOWEY_DASHING_TEXT_1[flowey_dashing_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(250, 120), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                                            
                        typewriter_effect(
                            screen,
                            flowey_dashing_typing_index_2 if flowey_dashing_first_text_complete else 0,  
                            FLOWEY_DASHING_TEXT_2[flowey_dashing_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(680, 380), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                        


                        if not flowey_dashing_first_text_complete:

                            if (flowey_current_time - flowey_last_typing_time) >= TYPING_DELAY and flowey_dashing_typing_index_1 < len(FLOWEY_DASHING_TEXT_1[flowey_dashing_line_index]):
                                flowey_last_typing_time, flowey_dashing_typing_index_1 = typewriter_animation(
                                    flowey_current_time,
                                    flowey_last_typing_time,
                                    flowey_dashing_typing_index_1,
                                    FLOWEY_DASHING_TEXT_1[flowey_dashing_line_index],
                                    flowey_typing_sound
                                )
                            elif flowey_dashing_typing_index_1 >= len(FLOWEY_DASHING_TEXT_1[flowey_dashing_line_index]):

                                flowey_dashing_first_text_complete = True
                                flowey_last_typing_time = flowey_current_time  

                        else:

                            if (flowey_current_time - flowey_last_typing_time) >= TYPING_DELAY and flowey_dashing_typing_index_2 < len(FLOWEY_DASHING_TEXT_2[flowey_dashing_line_index]):
                                flowey_last_typing_time, flowey_dashing_typing_index_2 = typewriter_animation(
                                    flowey_current_time,
                                    flowey_last_typing_time,
                                    flowey_dashing_typing_index_2,
                                    FLOWEY_DASHING_TEXT_2[flowey_dashing_line_index],
                                    flowey_typing_sound
                                )



                        if flowey_dashing_submit_page:


                            flowey_dashing_bought_overlay_alpha = min(150, flowey_dashing_bought_overlay_alpha + 5)  

                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                            bought_overlay.fill((50, 50, 50, flowey_dashing_bought_overlay_alpha))
                            screen.blit(bought_overlay, (0, 0))



                            box_size = (400, 200)
                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                            _,  flowey_dashing_submit_page, flowey_bought_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= flowey_bought_button_alpha,
                            border_color=(0, 200, 0),
                            highlight_color=(0, 200, 0),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=_,
                            current_page= flowey_dashing_submit_page,
                            button_size=box_size, pos = (box_x, box_y),
                            text_name="Bought"
                            )
        
        #-----------------------------------------------------------------------------------------------------
        # Papyrus's Page 
        #------------------------------------------------------------------------------------------------------

        if papyrus_page_1:

            #------------------------------------------------------------------------------
            # Papyrus's Basic Set up
            #------------------------------------------------------------------------------

            if papyrus_first_time:
                papyrus_page_time = sans_current_time    
            papyrus_first_time = False



            if papyrus_dialogue in ["None", "Intro" ,"Main Speech", "Choices"]:

                papyrus_bg_frame, frame_index_papyrus_background, papyrus_background_last_update = gif_framerate(
                    papyrus_background_surface,       
                    papyrus_background_last_update,    
                    frame_index_papyrus_background,
                    current_time= papyrus_current_time,    
                    frame_delay_ms=FRAME_DELAY_MS   
                    )

                screen.blit(papyrus_bg_frame, (0, 0))



            #------------------------------------------------------------------------------
            # Papyrus's Introduction Lines
            #------------------------------------------------------------------------------


                page_changed , papyrus_page_1, papyrus_escape_button_alpha = escape_button(
                    screen, color = (100, 10, 10) ,
                    alpha= papyrus_escape_button_alpha,
                    border_color= PAPYRUS_COLOR[2],
                    highlight_color=(180, 40, 40),
                    mouse_pos= mouse_pos,
                    clicked= clicked, main_page=sans_page,
                    current_page= papyrus_page_1,
                    button_size=(100,50), pos = (50, 50)
                    )



                if page_changed:
                    sans_page = True
                    papyrus_page_1 = False
                    papyrus_cr_v_page_2 = False
                    papyrus_accord_page_2 = False
                    papyrus_city_page_2 = False
                    papyrus_first_time = False
                    previous_dialogue = "None"


            if papyrus_dialogue in ["Intro", "Main Speech", "Choices"]:

                speech_bubble(screen, pos=SPEECH_BUBBLE_POS, bubble_color= PAPYRUS_COLOR[1] , border_color= PAPYRUS_COLOR[2])


                papyrus_current_alpha = min(255, papyrus_current_alpha + 5)

                papyrus_image_with_alpha = papyrus_surface_2.copy()

                papyrus_image_with_alpha.set_alpha(papyrus_current_alpha)


                screen.blit(papyrus_image_with_alpha, (80, 505))

            #------------------------------------------------------------------------------
            # Papyrus's Main Speech Lines
            #------------------------------------------------------------------------------


            if  papyrus_dialogue in ["Main Speech"]:
                try:

                    typewriter_effect(
                        screen,
                        papyrus_main_typing_index,
                        PAPYRUS_MAIN_TEXT[papyrus_line_index],
                        FONT,
                        BLACK,
                        char_width = CHARACTER_WIDTH,
                        pos=SPEECH_BUBBLE_POS,
                        type_padding= PADDING,
                        )

                    

                    if (papyrus_current_time - papyrus_last_typing_time) >= TYPING_DELAY and papyrus_main_typing_index < len(PAPYRUS_MAIN_TEXT[papyrus_line_index]):
                        papyrus_last_typing_time, papyrus_main_typing_index = typewriter_animation(
                            papyrus_current_time,
                            papyrus_last_typing_time,
                            papyrus_main_typing_index, 
                            PAPYRUS_MAIN_TEXT[papyrus_line_index] ,
                            papyrus_typing_sound
                            )
                        
                    if (papyrus_current_time - papyrus_last_typing_time) >= typing_delay_betw_speeches:
                        if papyrus_main_typing_index >= len(PAPYRUS_MAIN_TEXT[papyrus_line_index]):
                            papyrus_main_typing_index = 0
                            if papyrus_line_index < len(PAPYRUS_MAIN_TEXT):
                                papyrus_line_index += 1
                
                except IndexError:
                    papyrus_dialogue = "Choices"



            #------------------------------------------------------------------------------
            # Papyrus's Finishing Set up
            #------------------------------------------------------------------------------


            if papyrus_dialogue in ["Choices"]:


                honda_cr_v.set_alpha(papyrus_cars_alpha)
                honda_accord.set_alpha(papyrus_cars_alpha) 
                toyota_land_cruiser.set_alpha(papyrus_cars_alpha)


                papyrus_cars_alpha = min( 255,papyrus_cars_alpha + 5)

                #------------------------------------------------------------------------------
                # Papyrus's Choices Car Animation
                #------------------------------------------------------------------------------
               
                
                cr_v_box_detect , papyrus_cr_v_page_2= character_box(
                    screen, (72, 179, 224) ,
                    (241,73,77) , mouse_pos ,
                    alpha= papyrus_cars_alpha,
                    pos = (207, 175), size = (200,200), 
                    hover_effect= (30,30),
                    border_radius= 5,
                    clicked= clicked,
                    car_page= papyrus_cr_v_page_2
                    )

                accord_box_detect, papyrus_accord_page_2 = character_box(
                    screen,  (72, 179, 224) ,
                    (241,73,77), mouse_pos ,
                    alpha=papyrus_cars_alpha,pos = (591, 175), size = (200,200) ,
                    hover_effect= (30,30)  ,
                    border_radius= 5,
                    clicked= clicked,
                    car_page=papyrus_accord_page_2
                    ) 

                
  
                city_box_detect, papyrus_city_page_2 = character_box(
                    screen, (72, 179, 224)  ,
                    (241,73,77) ,mouse_pos ,
                    alpha= papyrus_cars_alpha,
                    pos = (975, 175),size = (200,200) ,
                    hover_effect= (30,30)  ,
                    border_radius= 5,
                    clicked= clicked,
                    car_page = papyrus_city_page_2
                    ) 
                



                #------------------------------------------------------------------------------
                # Papyrus's Choices Car Name Animation
                #------------------------------------------------------------------------------

                cr_v_pos, cr_v_alpha = car_name_animation(
                    screen,cr_v_box_detect, cr_v_alpha , (241,73,77), mouse_pos, 
                    pos=cr_v_pos , size = (150, 50), target_location=(225, TARGET_YX),
                    text= "CR-V", font= FONT 
                )


                accord_pos , accord_alpha = car_name_animation(
                    screen, accord_box_detect, accord_alpha, (241,73,77), mouse_pos, 
                    pos= accord_pos, size = (180,50), target_location = (600, TARGET_YX),
                    text = "Accord" , font=FONT 
                )



                city_pos , city_alpha = car_name_animation(
                    screen, city_box_detect,  city_alpha, (241,73,77), mouse_pos, pos= city_pos,
                    size= (250, 50), target_location = (950, TARGET_YX),
                    text = "City" , font= FONT 
                )
                

                #------------------------------------------------------------------------------
                # Papyrus's  Car BLIT
                #------------------------------------------------------------------------------

                screen.blit(honda_cr_v_icon, (225,200))
                screen.blit(honda_accord_icon, (620,200))
                screen.blit(honda_city_icon, (1000,200))


                #--------------------------------------------------------------------------------
                # Papyrus's CR-V Page
                #----------------------------------------------------------------------------------

                if papyrus_cr_v_page_2:
                    

                    #---------------------------------------------------------------------------
                    # Page Movement Logic
                    #-----------------------------------------------------------------------------

                    if papyrus_cr_v_slide_in:


                        if papyrus_cr_v_panel_x  >= 270:  
                            papyrus_cr_v_panel_x  -= 50
                        if papyrus_cr_v_panel_x  < 280:
                            papyrus_cr_v_overlay_alpha = min(150, papyrus_cr_v_overlay_alpha + 5)
                            


                    if papyrus_cr_v_slide_out:

                        if papyrus_cr_v_panel_x  < 1280:  
                            papyrus_cr_v_panel_x  += 50
                            papyrus_cr_v_overlay_alpha = max(0, papyrus_cr_v_overlay_alpha - 50)

                        if papyrus_cr_v_panel_x > 1270:
                            papyrus_cr_v_slide_in = True
                            papyrus_cr_v_page_2 = False
                            papyrus_cr_v_slide_out = False
                                            
                    
                    #----------------------------------------------------------------------------------------
                    # Main Side-Slide for CR-V
                    #-----------------------------------------------------------------------------------------

                    if papyrus_cr_v_panel_x < 280:
                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                        overlay.fill((50,50,50,papyrus_cr_v_overlay_alpha))
                        screen.blit(overlay,(0,0))
                            

                        panel_rect = pygame.Rect(papyrus_cr_v_panel_x , 0,1200, 720)
                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                        papyrus_cr_v_slide_out , papyrus_cr_v_slide_in, papyrus_cr_v_escape_button_alpha = escape_button(
                            screen, color = (100, 10, 10) ,
                            alpha= papyrus_cr_v_escape_button_alpha,
                            border_color=PAPYRUS_COLOR[2],
                            highlight_color=(180, 40, 40),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=papyrus_cr_v_slide_out,
                            current_page= papyrus_cr_v_slide_in,
                            button_size=(150,50), pos = (250, 50),
                            text_name="Back"
                            )

                        screen.blit(honda_cr_v, (650, 50))

                        papyrus_cr_v_submit_page, _, papyrus_buy_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= papyrus_buy_button_alpha,
                            border_color=(144, 238, 144),
                            highlight_color=(144, 238, 144),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=papyrus_cr_v_submit_page,
                            current_page= _,
                            button_size=(150,50), pos = (1100, 600),
                            text_name="Buy"
                            )


                        #----------------------------------------------------------------------------------
                        # CR-V Typing 
                        #------------------------------------------------------------------------------------

           
                        typewriter_effect(
                            screen,
                            papyrus_cr_v_typing_index_1, 
                            PAPYRUS_CR_V_TEXT_1[papyrus_cr_v_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(250, 180), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                                            
                        typewriter_effect(
                            screen,
                            papyrus_cr_v_typing_index_2 if papyrus_cr_v_first_text_complete else 0,  
                            PAPYRUS_CR_V_TEXT_2[papyrus_cr_v_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(680, 380), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                        


                        if not papyrus_cr_v_first_text_complete:

                            if (papyrus_current_time - papyrus_last_typing_time) >= TYPING_DELAY and papyrus_cr_v_typing_index_1 < len(PAPYRUS_CR_V_TEXT_1[papyrus_cr_v_line_index]):
                                papyrus_last_typing_time, papyrus_cr_v_typing_index_1 = typewriter_animation(
                                    papyrus_current_time,
                                    papyrus_last_typing_time,
                                    papyrus_cr_v_typing_index_1,
                                    PAPYRUS_CR_V_TEXT_1[papyrus_cr_v_line_index],
                                    papyrus_typing_sound
                                )
                            elif papyrus_cr_v_typing_index_1 >= len(PAPYRUS_CR_V_TEXT_1[papyrus_cr_v_line_index]):

                                papyrus_cr_v_first_text_complete = True
                                papyrus_last_typing_time = papyrus_current_time  

                        else:

                            if (papyrus_current_time - papyrus_last_typing_time) >= TYPING_DELAY and papyrus_cr_v_typing_index_2 < len(PAPYRUS_CR_V_TEXT_2[papyrus_cr_v_line_index]):
                                papyrus_last_typing_time, papyrus_cr_v_typing_index_2 = typewriter_animation(
                                    papyrus_current_time,
                                    papyrus_last_typing_time,
                                    papyrus_cr_v_typing_index_2,
                                    PAPYRUS_CR_V_TEXT_2[papyrus_cr_v_line_index],
                                    papyrus_typing_sound
                                )



                        if papyrus_cr_v_submit_page:


                            papyrus_cr_v_bought_overlay_alpha = min(150, papyrus_cr_v_bought_overlay_alpha + 5)  

                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                            bought_overlay.fill((50, 50, 50, papyrus_cr_v_bought_overlay_alpha))
                            screen.blit(bought_overlay, (0, 0))



                            box_size = (400, 200)
                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                            _,  papyrus_cr_v_submit_page, papyrus_bought_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= papyrus_bought_button_alpha,
                            border_color=(0, 200, 0),
                            highlight_color=(0, 200, 0),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=_,
                            current_page= papyrus_cr_v_submit_page,
                            button_size=box_size, pos = (box_x, box_y),
                            text_name="Bought"
                            )

                #--------------------------------------------------------------------------------
                # Papyrus's Accord Page
                #---------------------------------------------------------------------------------

                if papyrus_accord_page_2:
                    
                                    
                    #---------------------------------------------------------------------------
                    # Page Movement Logic
                    #-----------------------------------------------------------------------------

                    if papyrus_accord_slide_in:


                        if papyrus_accord_panel_x  >= 270:  
                            papyrus_accord_panel_x  -= 50
                        if papyrus_accord_panel_x  < 280:
                            papyrus_accord_overlay_alpha = min(150, papyrus_accord_overlay_alpha + 5)
                            


                    if papyrus_accord_slide_out:

                        if papyrus_accord_panel_x  < 1280:  
                            papyrus_accord_panel_x  += 50
                            papyrus_accord_overlay_alpha = max(0, papyrus_accord_overlay_alpha - 50)

                        if papyrus_accord_panel_x > 1270:
                            papyrus_accord_slide_in = True
                            papyrus_accord_page_2 = False
                            papyrus_accord_slide_out = False
                                            
                    
                    #----------------------------------------------------------------------------------------
                    # Main Side-Slide for Accord
                    #-----------------------------------------------------------------------------------------

                    if papyrus_accord_panel_x < 280:
                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                        overlay.fill((50,50,50,papyrus_accord_overlay_alpha))
                        screen.blit(overlay,(0,0))
                            

                        panel_rect = pygame.Rect(papyrus_accord_panel_x , 0,1200, 720)
                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                        papyrus_accord_slide_out , papyrus_accord_slide_in, papyrus_accord_escape_button_alpha = escape_button(
                            screen, color = (100, 10, 10) ,
                            alpha= papyrus_accord_escape_button_alpha,
                            border_color=PAPYRUS_COLOR[2],
                            highlight_color=(180, 40, 40),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=papyrus_accord_slide_out,
                            current_page= papyrus_accord_slide_in,
                            button_size=(150,50), pos = (250, 50),
                            text_name="Back"
                            )

                        screen.blit(honda_accord, (650, 50))

                        papyrus_accord_submit_page, _, papyrus_buy_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= papyrus_buy_button_alpha,
                            border_color=(144, 238, 144),
                            highlight_color=(144, 238, 144),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page= papyrus_accord_submit_page,
                            current_page= _,
                            button_size=(150,50), pos = (1100, 600),
                            text_name="Buy"
                            )


                        #----------------------------------------------------------------------------------
                        # Accord Typing 
                        #------------------------------------------------------------------------------------

        
                        typewriter_effect(
                            screen,
                            papyrus_accord_typing_index_1,
                            PAPYRUS_ACCORD_TEXT_1[papyrus_accord_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(250, 180), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                                            
                        typewriter_effect(
                            screen,
                            papyrus_accord_typing_index_2 if papyrus_accord_first_text_complete else 0,  
                            PAPYRUS_ACCORD_TEXT_2[papyrus_accord_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(680, 380), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                        

                        if not papyrus_accord_first_text_complete:

                            if (papyrus_current_time - papyrus_last_typing_time) >= TYPING_DELAY and papyrus_accord_typing_index_1 < len(PAPYRUS_ACCORD_TEXT_1[papyrus_accord_line_index]):
                                papyrus_last_typing_time, papyrus_accord_typing_index_1 = typewriter_animation(
                                    papyrus_current_time,
                                    papyrus_last_typing_time,
                                    papyrus_accord_typing_index_1,
                                    PAPYRUS_ACCORD_TEXT_1[papyrus_accord_line_index],
                                    papyrus_typing_sound
                                )
                            elif papyrus_accord_typing_index_1 >= len(PAPYRUS_ACCORD_TEXT_1[papyrus_accord_line_index]):

                                papyrus_accord_first_text_complete = True
                                papyrus_last_typing_time = papyrus_current_time  

                        else:

                            if (papyrus_current_time - papyrus_last_typing_time) >= TYPING_DELAY and papyrus_accord_typing_index_2 < len(PAPYRUS_ACCORD_TEXT_2[papyrus_accord_line_index]):
                                papyrus_last_typing_time, papyrus_accord_typing_index_2 = typewriter_animation(
                                    papyrus_current_time,
                                    papyrus_last_typing_time,
                                    papyrus_accord_typing_index_2,
                                    PAPYRUS_ACCORD_TEXT_2[papyrus_accord_line_index],
                                    papyrus_typing_sound
                                )



                        if papyrus_accord_submit_page:


                            papyrus_accord_bought_overlay_alpha = min(150, papyrus_accord_bought_overlay_alpha + 5)  

                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                            bought_overlay.fill((50, 50, 50, papyrus_accord_bought_overlay_alpha))
                            screen.blit(bought_overlay, (0, 0))



                            box_size = (400, 200)
                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                            _,  papyrus_accord_submit_page, papyrus_bought_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= papyrus_bought_button_alpha,
                            border_color=(0, 200, 0),
                            highlight_color=(0, 200, 0),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=_,
                            current_page= papyrus_accord_submit_page,
                            button_size=box_size, pos = (box_x, box_y),
                            text_name="Bought"
                            )

                #--------------------------------------------------------------------------------
                # Papyrus's City Page
                #----------------------------------------------------------------------------------

                if papyrus_city_page_2:

                    #---------------------------------------------------------------------------
                    # Page Movement Logic
                    #-----------------------------------------------------------------------------

                    if papyrus_city_slide_in:


                        if papyrus_city_panel_x  >= 270:  
                            papyrus_city_panel_x  -= 50
                        if papyrus_city_panel_x  < 280:
                            papyrus_city_overlay_alpha = min(150, papyrus_city_overlay_alpha + 5)
                            


                    if papyrus_city_slide_out:

                        if papyrus_city_panel_x  < 1280:  
                            papyrus_city_panel_x  += 50
                            papyrus_city_overlay_alpha = max(0, papyrus_city_overlay_alpha - 50)

                        if papyrus_city_panel_x > 1270:
                            papyrus_city_slide_in = True
                            papyrus_city_page_2 = False
                            papyrus_city_slide_out = False
                                            
                    
                    #----------------------------------------------------------------------------------------
                    # Main Side-Slide for cr_v
                    #-----------------------------------------------------------------------------------------

                    if papyrus_city_panel_x < 280:
                        overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                        overlay.fill((50,50,50,papyrus_city_overlay_alpha))
                        screen.blit(overlay,(0,0))
                            

                        panel_rect = pygame.Rect(papyrus_city_panel_x , 0,1200, 720)
                        pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                        papyrus_city_slide_out , papyrus_city_slide_in, papyrus_city_escape_button_alpha = escape_button(
                            screen, color = (100, 10, 10) ,
                            alpha= papyrus_city_escape_button_alpha,
                            border_color=PAPYRUS_COLOR[2],
                            highlight_color=(180, 40, 40),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=papyrus_city_slide_out,
                            current_page= papyrus_city_slide_in,
                            button_size=(150,50), pos = (250, 50),
                            text_name="Back"
                            )

                        screen.blit(honda_city, (650, 50))

                        papyrus_city_submit_page, _, papyrus_buy_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= papyrus_buy_button_alpha,
                            border_color=(144, 238, 144),
                            highlight_color=(144, 238, 144),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page= papyrus_city_submit_page,
                            current_page= _,
                            button_size=(150,50), pos = (1100, 600),
                            text_name="Buy"
                            )


                        #----------------------------------------------------------------------------------
                        # cr_v Typing 
                        #------------------------------------------------------------------------------------

        
                        typewriter_effect(
                            screen,
                            papyrus_city_typing_index_1, 
                            PAPYRUS_CITY_TEXT_1[papyrus_city_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(250, 120), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                                            
                        typewriter_effect(
                            screen,
                            papyrus_city_typing_index_2 if papyrus_city_first_text_complete else 0,  
                            PAPYRUS_CITY_TEXT_2[papyrus_city_line_index],
                            FONT, 
                            char_width=20, 
                            pos=(680, 380), 
                            type_padding=PADDING,
                            text_color=BLACK
                        )
                                        


                        if not papyrus_city_first_text_complete:

                            if (papyrus_current_time - papyrus_last_typing_time) >= TYPING_DELAY and papyrus_city_typing_index_1 < len(PAPYRUS_CITY_TEXT_1[papyrus_city_line_index]):
                                papyrus_last_typing_time, papyrus_city_typing_index_1 = typewriter_animation(
                                    papyrus_current_time,
                                    papyrus_last_typing_time,
                                    papyrus_city_typing_index_1,
                                    PAPYRUS_CITY_TEXT_1[papyrus_city_line_index],
                                    papyrus_typing_sound
                                )
                            elif papyrus_city_typing_index_1 >= len(PAPYRUS_CITY_TEXT_1[papyrus_city_line_index]):

                                papyrus_city_first_text_complete = True
                                papyrus_last_typing_time = papyrus_current_time  

                        else:

                            if (papyrus_current_time - papyrus_last_typing_time) >= TYPING_DELAY and papyrus_city_typing_index_2 < len(PAPYRUS_CITY_TEXT_2[papyrus_city_line_index]):
                                papyrus_last_typing_time, papyrus_city_typing_index_2 = typewriter_animation(
                                    papyrus_current_time,
                                    papyrus_last_typing_time,
                                    papyrus_city_typing_index_2,
                                    PAPYRUS_CITY_TEXT_2[papyrus_city_line_index],
                                    papyrus_typing_sound
                                )



                        if papyrus_city_submit_page:


                            papyrus_city_bought_overlay_alpha = min(150, papyrus_city_bought_overlay_alpha + 5)  

                            bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                            bought_overlay.fill((50, 50, 50, papyrus_city_bought_overlay_alpha))
                            screen.blit(bought_overlay, (0, 0))



                            box_size = (400, 200)
                            box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                            box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                            _,  papyrus_city_submit_page, papyrus_bought_button_alpha = escape_button(
                            screen, color = (0, 200, 0) ,
                            alpha= papyrus_bought_button_alpha,
                            border_color=(0, 200, 0),
                            highlight_color=(0, 200, 0),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=_,
                            current_page= papyrus_city_submit_page,
                            button_size=box_size, pos = (box_x, box_y),
                            text_name="Bought"
                            )

        #-----------------------------------------------------------------------------------------------------
        # Toriel's Page 
        #------------------------------------------------------------------------------------------------------

        if toriel_page_1:

                    #------------------------------------------------------------------------------
                    # Toriel's Basic Set up
                    #------------------------------------------------------------------------------

                    if toriel_first_time:
                        toriel_page_time = sans_current_time    
                    toriel_first_time = False



                    if toriel_dialogue in ["None", "Intro" ,"Main Speech", "Choices"]:

                        toriel_bg_frame, frame_index_toriel_background, toriel_background_last_update = gif_framerate(
                            toriel_background_surface,       
                            toriel_background_last_update,    
                            frame_index_toriel_background,
                            current_time= toriel_current_time,    
                            frame_delay_ms=FRAME_DELAY_MS   
                            )

                        screen.blit(toriel_bg_frame, (0, 0))



                    #------------------------------------------------------------------------------
                    # Toriel's Introduction Lines
                    #------------------------------------------------------------------------------


                        page_changed , toriel_page_1, toriel_escape_button_alpha = escape_button(
                            screen, color = (100, 10, 10) ,
                            alpha= toriel_escape_button_alpha,
                            border_color=TORIEL_COLOR[2],
                            highlight_color=(180, 40, 40),
                            mouse_pos= mouse_pos,
                            clicked= clicked, main_page=sans_page,
                            current_page= toriel_page_1,
                            button_size=(100,50), pos = (50, 50)
                            )



                        if page_changed:
                            sans_page = True
                            toriel_page_1 = False
                            toriel_x7_page_2 = False
                            toriel_first_time = False
                            previous_dialogue = "None"
                            sans_pun_line_index = 0
                            sans_pun_typing_index = 0





                    if toriel_dialogue in ["Intro", "Main Speech", "Choices"]:

                        speech_bubble(screen, pos=SPEECH_BUBBLE_POS, bubble_color= TORIEL_COLOR[1] , border_color= TORIEL_COLOR[2])

                    
                        toriel_current_alpha = min(255, toriel_current_alpha + 5)


                        toriel_image_with_alpha = toriel_surface_2.copy()


                        toriel_image_with_alpha.set_alpha(toriel_current_alpha)


                        screen.blit(toriel_image_with_alpha, (80, 505))

                    #------------------------------------------------------------------------------
                    # Toriel's Main Speech Lines
                    #------------------------------------------------------------------------------


                    if  toriel_dialogue in ["Main Speech"]:
                        try:

                            typewriter_effect(
                                screen,
                                toriel_main_typing_index,
                                TORIEL_MAIN_TEXT[toriel_line_index],
                                FONT,
                                BLACK,
                                char_width = CHARACTER_WIDTH,
                                pos=SPEECH_BUBBLE_POS,
                                type_padding= PADDING,
                                )

                            

                            if (toriel_current_time - toriel_last_typing_time) >= TYPING_DELAY and toriel_main_typing_index < len(TORIEL_MAIN_TEXT[toriel_line_index]):
                                toriel_last_typing_time, toriel_main_typing_index = typewriter_animation(
                                    toriel_current_time,
                                    toriel_last_typing_time,
                                    toriel_main_typing_index, 
                                    TORIEL_MAIN_TEXT[toriel_line_index] ,
                                    toriel_typing_sound
                                    )
                                
                            if (toriel_current_time - toriel_last_typing_time) >= typing_delay_betw_speeches:
                                if toriel_main_typing_index >= len(TORIEL_MAIN_TEXT[toriel_line_index]):
                                    toriel_main_typing_index = 0
                                    if toriel_line_index < len(TORIEL_MAIN_TEXT):
                                        toriel_line_index += 1
                        
                        except IndexError:
                            toriel_dialogue = "Choices"



                    #------------------------------------------------------------------------------
                    # Toriel's Finishing Set up
                    #------------------------------------------------------------------------------


                    if toriel_dialogue in ["Choices"]:


                        bmw_x7.set_alpha(toriel_cars_alpha)
                        bmw_530i.set_alpha(toriel_cars_alpha) 
                        bmw_i4.set_alpha(toriel_cars_alpha)


                        toriel_cars_alpha = min( 255,toriel_cars_alpha + 5)

                        #------------------------------------------------------------------------------
                        # Toriel's Choices Car Animation
                        #------------------------------------------------------------------------------
                    
                        
                        x7_box_detect , toriel_x7_page_2= character_box(
                            screen, (72, 179, 224) ,
                            (241,73,77) , mouse_pos ,
                            alpha= toriel_cars_alpha,
                            pos = (207, 175), size = (200,200), 
                            hover_effect= (30,30),
                            border_radius= 5,
                            clicked= clicked,
                            car_page= toriel_x7_page_2
                            )

                        _530i_box_detect, toriel_530i_page_2 = character_box(
                            screen,  (72, 179, 224) ,
                            (241,73,77), mouse_pos ,
                            alpha=toriel_cars_alpha,pos = (591, 175), size = (200,200) ,
                            hover_effect= (30,30)  ,
                            border_radius= 5,
                            clicked= clicked,
                            car_page=toriel_530i_page_2
                            ) 

                        
        
                        i4_box_detect, toriel_i4_page_2 = character_box(
                            screen, (72, 179, 224)  ,
                            (241,73,77) ,mouse_pos ,
                            alpha= toriel_cars_alpha,
                            pos = (975, 175),size = (200,200) ,
                            hover_effect= (30,30)  ,
                            border_radius= 5,
                            clicked= clicked,
                            car_page = toriel_i4_page_2
                            ) 
                        



                        #------------------------------------------------------------------------------
                        # Toriel's Choices Car Name Animation
                        #------------------------------------------------------------------------------

                        x7_pos, x7_alpha = car_name_animation(
                            screen,x7_box_detect, x7_alpha , (241,73,77), mouse_pos, 
                            pos=x7_pos , size = (150, 50), target_location=(225, TARGET_YX),
                            text= "X7", font= FONT 
                        )


                        _530i_pos , _530i_alpha = car_name_animation(
                            screen, _530i_box_detect, _530i_alpha, (241,73,77), mouse_pos, 
                            pos= _530i_pos, size = (180,50), target_location = (600, TARGET_YX),
                            text = "530i" , font=FONT 
                        )



                        i4_pos , i4_alpha = car_name_animation(
                            screen, i4_box_detect,  i4_alpha, (241,73,77), mouse_pos, pos= i4_pos,
                            size= (250, 50), target_location = (950, TARGET_YX),
                            text = "i4" , font= FONT 
                        )
                        

                        #------------------------------------------------------------------------------
                        # Toriel's  Car BLIT
                        #------------------------------------------------------------------------------

                        screen.blit(bmw_x7_icon, (225,200))
                        screen.blit(bmw_530i_icon, (620,200))
                        screen.blit(bmw_i4_icon, (1000,200))


                        #--------------------------------------------------------------------------------
                        # Toriel's X7 Page
                        #----------------------------------------------------------------------------------

                        if toriel_x7_page_2:
                            

                            #---------------------------------------------------------------------------
                            # Page Movement Logic
                            #-----------------------------------------------------------------------------

                            if toriel_x7_slide_in:


                                if toriel_x7_panel_x  >= 270:  
                                    toriel_x7_panel_x  -= 50
                                if toriel_x7_panel_x  < 280:
                                    toriel_x7_overlay_alpha = min(150, toriel_x7_overlay_alpha + 5)
                                    


                            if toriel_x7_slide_out:

                                if toriel_x7_panel_x  < 1280:  
                                    toriel_x7_panel_x  += 50
                                    toriel_x7_overlay_alpha = max(0, toriel_x7_overlay_alpha - 50)

                                if toriel_x7_panel_x > 1270:
                                    toriel_x7_slide_in = True
                                    toriel_x7_page_2 = False
                                    toriel_x7_slide_out = False
                                                    
                            
                            #----------------------------------------------------------------------------------------
                            # Main Side-Slide for X7
                            #-----------------------------------------------------------------------------------------

                            if toriel_x7_panel_x < 280:
                                overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                                overlay.fill((50,50,50,toriel_x7_overlay_alpha))
                                screen.blit(overlay,(0,0))
                                    

                                panel_rect = pygame.Rect(toriel_x7_panel_x , 0,1200, 720)
                                pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                                toriel_x7_slide_out , toriel_x7_slide_in, toriel_x7_escape_button_alpha = escape_button(
                                    screen, color = (100, 10, 10) ,
                                    alpha= toriel_x7_escape_button_alpha,
                                    border_color=TORIEL_COLOR[2],
                                    highlight_color=(180, 40, 40),
                                    mouse_pos= mouse_pos,
                                    clicked= clicked, main_page=toriel_x7_slide_out,
                                    current_page= toriel_x7_slide_in,
                                    button_size=(150,50), pos = (250, 50),
                                    text_name="Back"
                                    )

                                screen.blit(bmw_x7, (650, 50))

                                toriel_x7_submit_page, _, toriel_buy_button_alpha = escape_button(
                                    screen, color = (0, 200, 0) ,
                                    alpha= toriel_buy_button_alpha,
                                    border_color=(144, 238, 144),
                                    highlight_color=(144, 238, 144),
                                    mouse_pos= mouse_pos,
                                    clicked= clicked, main_page=toriel_x7_submit_page,
                                    current_page= _,
                                    button_size=(150,50), pos = (1100, 600),
                                    text_name="Buy"
                                    )


                                #----------------------------------------------------------------------------------
                                # X7 Typing 
                                #------------------------------------------------------------------------------------

                
                                typewriter_effect(
                                    screen,
                                    toriel_x7_typing_index_1, 
                                    TORIEL_X7_TEXT_1[toriel_x7_line_index],
                                    FONT, 
                                    char_width=20, 
                                    pos=(250, 180), 
                                    type_padding=PADDING,
                                    text_color=BLACK
                                )
                                                                    
                                typewriter_effect(
                                    screen,
                                    toriel_x7_typing_index_2 if toriel_x7_first_text_complete else 0,  
                                    TORIEL_X7_TEXT_2[toriel_x7_line_index],
                                    FONT, 
                                    char_width=20, 
                                    pos=(680, 380), 
                                    type_padding=PADDING,
                                    text_color=BLACK
                                )
                                                


                                if not toriel_x7_first_text_complete:

                                    if (toriel_current_time - toriel_last_typing_time) >= TYPING_DELAY and toriel_x7_typing_index_1 < len(TORIEL_X7_TEXT_1[toriel_x7_line_index]):
                                        toriel_last_typing_time, toriel_x7_typing_index_1 = typewriter_animation(
                                            toriel_current_time,
                                            toriel_last_typing_time,
                                            toriel_x7_typing_index_1,
                                            TORIEL_X7_TEXT_1[toriel_x7_line_index],
                                            toriel_typing_sound
                                        )
                                    elif toriel_x7_typing_index_1 >= len(TORIEL_X7_TEXT_1[toriel_x7_line_index]):

                                        toriel_x7_first_text_complete = True
                                        toriel_last_typing_time = toriel_current_time  

                                else:

                                    if (toriel_current_time - toriel_last_typing_time) >= TYPING_DELAY and toriel_x7_typing_index_2 < len(TORIEL_X7_TEXT_2[toriel_x7_line_index]):
                                        toriel_last_typing_time, toriel_x7_typing_index_2 = typewriter_animation(
                                            toriel_current_time,
                                            toriel_last_typing_time,
                                            toriel_x7_typing_index_2,
                                            TORIEL_X7_TEXT_2[toriel_x7_line_index],
                                            toriel_typing_sound
                                        )



                                if toriel_x7_submit_page:


                                    toriel_x7_bought_overlay_alpha = min(150, toriel_x7_bought_overlay_alpha + 5)  

                                    bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                                    bought_overlay.fill((50, 50, 50, toriel_x7_bought_overlay_alpha))
                                    screen.blit(bought_overlay, (0, 0))



                                    box_size = (400, 200)
                                    box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                                    box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                                    _,  toriel_x7_submit_page, toriel_bought_button_alpha = escape_button(
                                    screen, color = (0, 200, 0) ,
                                    alpha= toriel_bought_button_alpha,
                                    border_color=(0, 200, 0),
                                    highlight_color=(0, 200, 0),
                                    mouse_pos= mouse_pos,
                                    clicked= clicked, main_page=_,
                                    current_page= toriel_x7_submit_page,
                                    button_size=box_size, pos = (box_x, box_y),
                                    text_name="Bought"
                                    )

                        #--------------------------------------------------------------------------------
                        # Toriel's 530i Page
                        #---------------------------------------------------------------------------------

                        if toriel_530i_page_2:
                                            
                                            

                            #---------------------------------------------------------------------------
                            # Page Movement Logic
                            #-----------------------------------------------------------------------------

                            if toriel_530i_slide_in:


                                if toriel_530i_panel_x  >= 270:  
                                    toriel_530i_panel_x  -= 50
                                if toriel_530i_panel_x  < 280:
                                    toriel_530i_overlay_alpha = min(150, toriel_530i_overlay_alpha + 5)
                                    


                            if toriel_530i_slide_out:

                                if toriel_530i_panel_x  < 1280:  
                                    toriel_530i_panel_x  += 50
                                    toriel_530i_overlay_alpha = max(0, toriel_530i_overlay_alpha - 50)

                                if toriel_530i_panel_x > 1270:
                                    toriel_530i_slide_in = True
                                    toriel_530i_page_2 = False
                                    toriel_530i_slide_out = False
                                                    
                            
                            #----------------------------------------------------------------------------------------
                            # Main Side-Slide for 530i
                            #-----------------------------------------------------------------------------------------

                            if toriel_530i_panel_x < 280:
                                overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                                overlay.fill((50,50,50,toriel_530i_overlay_alpha))
                                screen.blit(overlay,(0,0))
                                    

                                panel_rect = pygame.Rect(toriel_530i_panel_x , 0,1200, 720)
                                pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                                toriel_530i_slide_out , toriel_530i_slide_in, toriel_530i_escape_button_alpha = escape_button(
                                    screen, color = (100, 10, 10) ,
                                    alpha= toriel_530i_escape_button_alpha,
                                    border_color=TORIEL_COLOR[2],
                                    highlight_color=(180, 40, 40),
                                    mouse_pos= mouse_pos,
                                    clicked= clicked, main_page=toriel_530i_slide_out,
                                    current_page= toriel_530i_slide_in,
                                    button_size=(150,50), pos = (250, 50),
                                    text_name="Back"
                                    )

                                screen.blit(bmw_530i, (650, 50))

                                toriel_530i_submit_page, _, toriel_buy_button_alpha = escape_button(
                                    screen, color = (0, 200, 0) ,
                                    alpha= toriel_buy_button_alpha,
                                    border_color=(144, 238, 144),
                                    highlight_color=(144, 238, 144),
                                    mouse_pos= mouse_pos,
                                    clicked= clicked, main_page= toriel_530i_submit_page,
                                    current_page= _,
                                    button_size=(150,50), pos = (1100, 600),
                                    text_name="Buy"
                                    )


                            #----------------------------------------------------------------------------------
                            # 530i Typing 
                            #------------------------------------------------------------------------------------

                            
                            typewriter_effect(
                                screen,
                                toriel_530i_typing_index_1, 
                                TORIEL_530_TEXT_1[toriel_530i_line_index],
                                FONT, 
                                char_width=20, 
                                pos=(250, 180), 
                                type_padding=PADDING,
                                text_color=BLACK
                                )
                                                                                
                            typewriter_effect(
                                screen,
                                toriel_530i_typing_index_2 if toriel_530i_first_text_complete else 0,  
                                TORIEL_530_TEXT_2[toriel_530i_line_index],
                                FONT, 
                                char_width=20, 
                                pos=(680, 380), 
                                type_padding=PADDING,
                                text_color=BLACK
                                )
                                                                


                            if not toriel_530i_first_text_complete:

                                if (toriel_current_time - toriel_last_typing_time) >= TYPING_DELAY and toriel_530i_typing_index_1 < len(TORIEL_530_TEXT_1[toriel_530i_line_index]):
                                    toriel_last_typing_time, toriel_530i_typing_index_1 = typewriter_animation(
                                        toriel_current_time,
                                        toriel_last_typing_time,
                                        toriel_530i_typing_index_1,
                                        TORIEL_530_TEXT_1[toriel_530i_line_index],
                                        toriel_typing_sound
                                    )
                                elif toriel_530i_typing_index_1 >= len(TORIEL_530_TEXT_1[toriel_530i_line_index]):

                                    toriel_530i_first_text_complete = True
                                    toriel_last_typing_time = toriel_current_time  

                            else:

                                if (toriel_current_time - toriel_last_typing_time) >= TYPING_DELAY and toriel_530i_typing_index_2 < len(TORIEL_530_TEXT_2[toriel_530i_line_index]):
                                    toriel_last_typing_time, toriel_530i_typing_index_2 = typewriter_animation(
                                        toriel_current_time,
                                        toriel_last_typing_time,
                                        toriel_530i_typing_index_2,
                                        TORIEL_530_TEXT_2[toriel_530i_line_index],
                                        toriel_typing_sound
                                    )



                            if toriel_530i_submit_page:


                                toriel_530i_bought_overlay_alpha = min(150, toriel_530i_bought_overlay_alpha + 5)  

                                bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                                bought_overlay.fill((50, 50, 50, toriel_530i_bought_overlay_alpha))
                                screen.blit(bought_overlay, (0, 0))



                                box_size = (400, 200)
                                box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                                box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                                _,  toriel_530i_submit_page, toriel_bought_button_alpha = escape_button(
                                screen, color = (0, 200, 0) ,
                                alpha= toriel_bought_button_alpha,
                                border_color=(0, 200, 0),
                                highlight_color=(0, 200, 0),
                                mouse_pos= mouse_pos,
                                clicked= clicked, main_page=_,
                                current_page= toriel_530i_submit_page,
                                button_size=box_size, pos = (box_x, box_y),
                                text_name="Bought"
                                )
                    
                        #--------------------------------------------------------------------------------
                        # Toriel's i4 Page
                        #----------------------------------------------------------------------------------

                        if toriel_i4_page_2:

                            #---------------------------------------------------------------------------
                            # Page Movement Logic
                            #-----------------------------------------------------------------------------

                            if toriel_i4_slide_in:


                                if toriel_i4_panel_x  >= 270:  
                                    toriel_i4_panel_x  -= 50
                                if toriel_i4_panel_x  < 280:
                                    toriel_i4_overlay_alpha = min(150, toriel_i4_overlay_alpha + 5)
                                    


                            if toriel_i4_slide_out:

                                if toriel_i4_panel_x  < 1280:  
                                    toriel_i4_panel_x  += 50
                                    toriel_i4_overlay_alpha = max(0, toriel_i4_overlay_alpha - 50)

                                if toriel_i4_panel_x > 1270:
                                    toriel_i4_slide_in = True
                                    toriel_i4_page_2 = False
                                    toriel_i4_slide_out = False
                                                    
                            
                            #----------------------------------------------------------------------------------------
                            # Main Side-Slide for X7
                            #-----------------------------------------------------------------------------------------

                            if toriel_i4_panel_x < 280:
                                overlay = pygame.Surface((270,720), pygame.SRCALPHA)
                                overlay.fill((50,50,50,toriel_i4_overlay_alpha))
                                screen.blit(overlay,(0,0))
                                    

                                panel_rect = pygame.Rect(toriel_i4_panel_x , 0,1200, 720)
                                pygame.draw.rect(screen, (240, 240, 240), panel_rect)

                                toriel_i4_slide_out , toriel_i4_slide_in, toriel_i4_escape_button_alpha = escape_button(
                                    screen, color = (100, 10, 10) ,
                                    alpha= toriel_i4_escape_button_alpha,
                                    border_color=TORIEL_COLOR[2],
                                    highlight_color=(180, 40, 40),
                                    mouse_pos= mouse_pos,
                                    clicked= clicked, main_page=toriel_i4_slide_out,
                                    current_page= toriel_i4_slide_in,
                                    button_size=(150,50), pos = (250, 50),
                                    text_name="Back"
                                    )

                                screen.blit(bmw_i4, (650, 50))

                                toriel_i4_submit_page, _, toriel_buy_button_alpha = escape_button(
                                    screen, color = (0, 200, 0) ,
                                    alpha= toriel_buy_button_alpha,
                                    border_color=(144, 238, 144),
                                    highlight_color=(144, 238, 144),
                                    mouse_pos= mouse_pos,
                                    clicked= clicked, main_page= toriel_i4_submit_page,
                                    current_page= _,
                                    button_size=(150,50), pos = (1100, 600),
                                    text_name="Buy"
                                    )


                                #----------------------------------------------------------------------------------
                                # X7 Typing 
                                #------------------------------------------------------------------------------------

                
                                typewriter_effect(
                                    screen,
                                    toriel_i4_typing_index_1, 
                                    TORIEL_i4_TEXT_1[toriel_i4_line_index],
                                    FONT, 
                                    char_width=20, 
                                    pos=(250, 120), 
                                    type_padding=PADDING,
                                    text_color=BLACK
                                )
                                                                    
                                typewriter_effect(
                                    screen,
                                    toriel_i4_typing_index_2 if toriel_i4_first_text_complete else 0,  
                                    TORIEL_i4_TEXT_2[toriel_i4_line_index],
                                    FONT, 
                                    char_width=20, 
                                    pos=(680, 380), 
                                    type_padding=PADDING,
                                    text_color=BLACK
                                )
                                                


                                if not toriel_i4_first_text_complete:

                                    if (toriel_current_time - toriel_last_typing_time) >= TYPING_DELAY and toriel_i4_typing_index_1 < len(TORIEL_i4_TEXT_1[toriel_i4_line_index]):
                                        toriel_last_typing_time, toriel_i4_typing_index_1 = typewriter_animation(
                                            toriel_current_time,
                                            toriel_last_typing_time,
                                            toriel_i4_typing_index_1,
                                            TORIEL_i4_TEXT_1[toriel_i4_line_index],
                                            toriel_typing_sound
                                        )
                                    elif toriel_i4_typing_index_1 >= len(TORIEL_i4_TEXT_1[toriel_i4_line_index]):

                                        toriel_i4_first_text_complete = True
                                        toriel_last_typing_time = toriel_current_time  

                                else:

                                    if (toriel_current_time - toriel_last_typing_time) >= TYPING_DELAY and toriel_i4_typing_index_2 < len(TORIEL_i4_TEXT_2[toriel_i4_line_index]):
                                        toriel_last_typing_time, toriel_i4_typing_index_2 = typewriter_animation(
                                            toriel_current_time,
                                            toriel_last_typing_time,
                                            toriel_i4_typing_index_2,
                                            TORIEL_i4_TEXT_2[toriel_i4_line_index],
                                            toriel_typing_sound
                                        )



                                if toriel_i4_submit_page:


                                    toriel_i4_bought_overlay_alpha = min(150, toriel_i4_bought_overlay_alpha + 5)  

                                    bought_overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
                                    bought_overlay.fill((50, 50, 50, toriel_i4_bought_overlay_alpha))
                                    screen.blit(bought_overlay, (0, 0))



                                    box_size = (400, 200)
                                    box_x = (WINDOW_SIZE[0] - box_size[0]) // 2
                                    box_y = (WINDOW_SIZE[1] - box_size[1]) // 2


                                    _,  toriel_i4_submit_page, toriel_bought_button_alpha = escape_button(
                                    screen, color = (0, 200, 0) ,
                                    alpha= toriel_bought_button_alpha,
                                    border_color=(0, 200, 0),
                                    highlight_color=(0, 200, 0),
                                    mouse_pos= mouse_pos,
                                    clicked= clicked, main_page=_,
                                    current_page= toriel_i4_submit_page,
                                    button_size=box_size, pos = (box_x, box_y),
                                    text_name="Bought"
                                    )
                
        pygame.display.flip()


    pygame.quit()



#---------------------------------------------------------------------------------------------------------
# Main() Intialisation
#------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()







