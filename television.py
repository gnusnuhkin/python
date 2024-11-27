class Television:
    """
    TV with channels, volume, power, and mute.
    """

    # Class variables constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Default values."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__last_volume: int = Television.MIN_VOLUME

    def power(self) -> None:
        """Power status of the TV."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute status when the TV is on."""
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__last_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__last_volume

    def channel_up(self) -> None:
        """Increase the channel by 1"""
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decrease the channel by 1"""
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by 1."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__last_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by 1."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__last_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the television's current status"""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
