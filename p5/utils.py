import uuid
from typing import List

def leer_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter an integer.")

def leer_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a float.")

def crear_menu(options: List[str]) -> int:
    print("Menu Options:")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    return leer_int("Choose an option: ")

def generar_id() -> str:
    return str(uuid.uuid4())[:8]  # Returns a unique ID with the first 8 characters of UUID

