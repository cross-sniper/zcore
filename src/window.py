import pygame
from typing import Callable
from time import time
from .helpers import nonWorking

pygame.init()

_keystates: dict[str, bool] = {}
_lastKeyStates: dict[str, bool] = {}


def createWindow(width: int, height: int, title: str) -> pygame.Surface:
    """
    this creates a window,
    Args:
        width: the width of the window
        height: the height of the window
        title: the title of the window
    """
    window: pygame.Surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return window


def isKeyDown(key: str) -> bool:
    """
    Checks if a key is currently pressed down.

    Args:
        key: The key code.

    Returns:
        bool: True if the key is pressed, False otherwise.
    """
    return _keystates.get(key, False)


# @nonWorking(reason="the current implementation does not handle checking the actual state of the key")
def isKeyPressed(key: str) -> bool:
    """
    Checks if the key was just pressed

    Args:
        key(str): the name of the key you want to check

    Returns:
        bool: True if the key was just clicked, False otherwise
    """
    current_state = _keystates.get(key, False)
    last_state = _lastKeyStates.get(key, False)
    _lastKeyStates[key] = current_state

    # Return True if current state is True and last state is False (key was just pressed)
    return current_state and not last_state


def mainLoop(gameLoop: Callable):
    """
    Main loop for the game.

    Args:
        gameLoop: A callable that represents the game loop, which takes the delta time as an argument.
    """
    # Main loop
    _running = True
    dt = 0.1
    lastTime = time()

    while _running:
        # Handle events
        dt = time() - lastTime
        lastTime = time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _running = False
            elif event.type == pygame.KEYDOWN:
                _keystates[event.unicode] = True
                _lastKeyStates[event.unicode] = False
            elif event.type == pygame.KEYUP:
                _keystates[event.unicode] = False
                _lastKeyStates[event.unicode] = True

        gameLoop(dt)

        pygame.display.flip()

    pygame.quit()
