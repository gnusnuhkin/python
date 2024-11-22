import pytest
from television import Television

def test_init():
    """Test TV."""
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    """Test the power."""
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    """Test the mute."""
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

def test_channel_up():
    """Test channel up."""
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    for _ in range(4):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down():
    """Test channel down."""
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    for _ in range(4):
        tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_up():
    """Test volume up."""
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    for _ in range(3):
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    """Test volume down."""
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
