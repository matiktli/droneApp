import os
import pygame

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""
    BTN_NAMES = {
        0: 'x',
        1: 'circle',
        2: 'triangle',
        3: 'square',
        4: 'L1',
        5: 'R1',
        6: 'L2',
        7: 'R2',
        8: 'share',
        9: 'options',
        10: 'ps4_btn',
        11: 'left_analog',
        12: 'right_analog',
        13: 'touchpad'
    }
    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""
        
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        def getButtonsData(doPrint = False):
            btnsData = {}
            for key in range(13):
                if key in self.BTN_NAMES.keys():
                    key_name = self.BTN_NAMES.get(key)
                    btnsData[key_name] = self.controller.get_button(key)
                    if doPrint and self.controller.get_button(key):
                        print('BTN pressed: ', key_name, ' -> ', key)
            return btnsData

        while True:
            for event in pygame.event.get():
                self.button_data = getButtonsData()
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value,2)
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value
                return self.button_data, self.axis_data, self.hat_data