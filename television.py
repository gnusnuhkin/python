class Television:
    """
    TV with channels, volume, power, and mute.
    """

    # Class variables constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the television with default values."""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__last_volume = self.MIN_VOLUME

    def power(self):
        """Toggle the power status of the TV."""
        self.__status = not self.__status

    def mute(self):
        """Toggle mute status when the TV is on."""
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__last_volume = self.__volume
                self.__volume = self.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__last_volume

    def channel_up(self):
        """Increase the channel by 1, looping back to MIN_CHANNEL after MAX_CHANNEL."""
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        """Decrease the channel by 1, looping back to MAX_CHANNEL after MIN_CHANNEL."""
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """Increase the volume by 1, unmuting if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__last_volume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease the volume by 1, unmuting if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__last_volume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Return the television's current status."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
