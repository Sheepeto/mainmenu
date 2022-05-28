from ursina import *


class MainMenu():

    def __init__(self):

        self.StartGame = False

        window.color = color.rgba(0.25, 0.25, 0.25, 1)

        self.TitleText = Text(text="Untitled Platformer",
                              origin=(0, -5),
                              scale=3)

        self.VersionText = Text(text="Version: 1",
                                origin=(-3.25, 9),
                                scale=2)

        self.PlayGameButton = Button(text="Play Game",
                                     origin=(0, -0.5),
                                     scale=(0.5, 0.125))
        self.PlayGameButton.on_click = self.PlayGame

        self.CreditsButton = Button(text="Credits",
                                    origin=(0, 0.75),
                                    scale=(0.5, 0.125))
        self.CreditsButton.on_click = self.Credits

        self.ExitButton = Button(text="Exit",
                                 origin=(0, 2),
                                 scale=(0.5, 0.125))
        self.ExitButton.on_click = application.quit

        self.SettingsButton = Button(texture="Assets\Images\Kenny Assets\Icons\PNG\White\onex\gear",
                                     color=color.rgba(1, 1, 1, 1),
                                     origin=(8.4, -4.5),
                                     scale=0.1)
        self.SettingsButton.on_click = self.Settings

    def PlayGame(self):

        self.StartGame = True

    def Credits(self):

        self.PlayGameButton.text = ""
        self.CreditsButton.text = ""
        self.ExitButton.text = ""
        self.SettingsButton.disable()

        self.CreditsPanel = Panel(color=color.rgba(0, 0, 0, 255))

        self.CreditsText = Text("Credits",
                                parent=self.CreditsPanel,
                                origin=(0, -17))

        self.CreditsListText = Text("Made using a few Kenny Assets:\n\n"
                                    "1 bit platformer pack\n\n"
                                    "icon pack",
                                    parent=self.CreditsPanel,
                                    origin=(0, 0),
                                    scale=2)

        self.CreditsExitButton = Button(texture="Assets\Images\Kenny Assets\Icons\PNG\White\onex\cross",
                                        color=color.rgba(1, 1, 1, 1),
                                        origin=(8.4, -4.5),
                                        scale=0.1)
        self.CreditsExitButton.on_click = self.ExitCredits

    def ExitCredits(self):

        self.PlayGameButton.text = "Play Game"
        self.CreditsButton.text = "Credits"
        self.ExitButton.text = "Exit"
        self.SettingsButton.enable()

        self.CreditsPanel.disable()
        self.CreditsText.disable()
        self.CreditsExitButton.disable()
        self.CreditsListText.disable()

    def Settings(self):

        self.PlayGameButton.text = ""
        self.CreditsButton.text = ""
        self.ExitButton.text = ""
        self.SettingsButton.disable()

        self.SettingsPanel = Panel(color=color.rgba(0, 0, 0, 255))

        self.SettingsText = Text("Settings",
                                 parent=self.SettingsPanel,
                                 origin=(0, -17))

        self.SettingsExitButton = Button(texture="Assets\Images\Kenny Assets\Icons\PNG\White\onex\cross",
                                         color=color.rgba(1, 1, 1, 1),
                                         origin=(8.4, -4.5),
                                         scale=0.1)
        self.SettingsExitButton.on_click = self.ExitSettings

    def ExitSettings(self):

        self.PlayGameButton.text = "Play Game"
        self.CreditsButton.text = "Credits"
        self.ExitButton.text = "Exit"
        self.SettingsButton.enable()

        self.SettingsPanel.disable()
        self.SettingsText.disable()
        self.SettingsExitButton.disable()