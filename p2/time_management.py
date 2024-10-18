import re

class Time:
    """
    Class that represents a time with AM/PM or 24 hours format.
    """
    TIME_FORMATS = ("AM", "PM", "24 HORAS")
    time_count = 0  # Counts the number of Time objects created

    def __init__(self):
        """
        Method to Initialize attributes to 0.
        """
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = "24 HORAS"
        Time.time_count += 1

    def __asign_format(self, pszFormat):
        """
        Checks pszFormat has correct value & assigns it to format.
        Converts to upper case to avoid problems with capitalization.
        Args:
        pszFormat: String with time format ("AM", "PM" or "24 HORAS").
        Returns:
        True if the format is correct, False otherwise.
        """
        pszFormat = pszFormat.upper()
        if pszFormat in Time.TIME_FORMATS:
            self.format = pszFormat
            return True
        return False

    def __is_24hour_format(self):
        """
        Checks if the time format is "24 HORAS".
        Returns:
        True if the format is "24 HORAS", False otherwise.
        """
        return self.format == "24 HORAS"

    def _is_valid_time(self):
        """
        Checks if the time is correct according to the format.
        Returns:
        True if the time is correct, False otherwise.
        """
        if self.__is_24hour_format():
            return 0 <= self.hours <= 23 and 0 <= self.minutes < 60 and 0 <= self.seconds < 60
        else:
            return 1 <= self.hours <= 12 and 0 <= self.minutes < 60 and 0 <= self.seconds < 60

    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):
        """
        Assigns a time to the class.
        Args:
        nHoras: Hours (1 to 12 AM/PM, 0 to 23 for 24 hours).
        nMinutos: Minutes (0 to 59).
        nSegundos: Seconds (0 to 59).
        pszFormato: Time format ("AM", "PM" or "24 HORAS").
        Returns:
        True if the time could be assigned correctly, False otherwise.
        """
        if self.__asign_format(pszFormato):
            self.hours = nHoras
            self.minutes = nMinutos
            self.seconds = nSegundos
            return self._is_valid_time()
        return False

    def get_time(self):
        """
        Returns the current time of the class.
        """
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        """
        Class method to create Time object from string.
        Args:
        time_string (str): A string representing time in the format "HH:MM:SS FORMAT".
        Returns:
        Time: new Time object with the parsed time.
        If the time string is invalid, print a message.
        """
        pattern = r"^(\d{2}):(\d{2}):(\d{2}) (AM|PM|24 HORAS)$"
        match = re.match(pattern, time_string, re.IGNORECASE)

        if match:
            hours, minutes, seconds, fmt = match.groups()
            hours, minutes, seconds = int(hours), int(minutes), int(seconds)
            new_time = cls()
            if new_time.set_time(hours, minutes, seconds, fmt):
                return new_time
        print("Formato de cadena de tiempo no válido.")
        return None

    @staticmethod
    def is_valid_format(time_format):
        """
        Static method to check if a given time format is valid.
        Args:
        time_format (str): The time format to check.
        Returns:
        bool: True if the format is valid (AM, PM, or 24 HORAS), False otherwise.
        """
        return time_format.upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        """
        Class method to get total number of Time objects created.
        Returns:
        int: The number of Time objects created.
        """
        return cls.time_count

def display_time(time_obj):
    """
    Function to display the time in formatted string.
    Args:
    time_obj (Time): The time object to display.
    Returns:
    str: Formatted time string.
    """
    return time_obj.get_time()

def main():
    current_time = None
    while True:
        print("\n--- Menú ---")
        print("1. Introducir una nueva hora")
        print("2. Mostrar hora actual")
        print("3. Crear hora a partir de una cadena")
        print("4. Salir")
        choice = input("Elija una opción: ")

        if choice == "1":
            try:
                hours = int(input("Introduzca las horas: "))
                minutes = int(input("Introduzca los minutos: "))
                seconds = int(input("Introduzca los segundos: "))
                fmt = input("Introduzca el formato (AM, PM, 24 HORAS): ").upper()

                if not Time.is_valid_format(fmt):
                    print("Formato de hora no válido.")
                    continue

                new_time = Time()
                if new_time.set_time(hours, minutes, seconds, fmt):
                    current_time = new_time
                    print("Hora establecida correctamente.")
                else:
                    print("Valores de hora no válidos.")

            except ValueError:
                print("Entrada no válida. Por favor, introduzca valores numéricos para horas, minutos y segundos.")

        elif choice == "2":
            if current_time:
                print(f"Hora actual: {display_time(current_time)}")
            else:
                print("No se ha establecido ninguna hora.")

        elif choice == "3":
            time_str = input("Introduzca la cadena de hora (HH:MM:SS FORMATO): ")
            new_time = Time.from_string(time_str)
            if new_time:
                current_time = new_time
                print(f"Hora establecida desde cadena: {display_time(current_time)}")

        elif choice == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

