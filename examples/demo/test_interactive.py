import yaml
from gibson2.core.physics.robot_locomotors import Turtlebot
from gibson2.core.simulator import Simulator
from gibson2.core.physics.scene import BuildingScene, StadiumScene
from gibson2.utils.utils import parse_config
import pytest
import pybullet as p
import numpy as np
import pygame

pygame.init()
size=width,height=1024,256;screen=pygame.display.set_mode(size)

def get_pressed(unicode_keys):
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    for key in unicode_keys:
        if len(key) == 0:
            return key
        key_char = chr(key[0])
        key_const = getattr(pygame, 'K_{}'.format(key_char))
        if keys[key_const]:
            return key


config = parse_config('../configs/turtlebot_p2p_nav_house2.yaml')

s = Simulator(mode='gui', resolution=512)
scene = BuildingScene('American')
s.import_scene(scene)
turtlebot = Turtlebot(config)
s.import_robot(turtlebot)
for i in range(1000):
    # turtlebot.apply_action([1.0, 1.0])
    key = get_pressed(turtlebot.keys_to_action)
    if key in turtlebot.keys_to_action:
        turtlebot.apply_action(turtlebot.keys_to_action[key])
    s.step()
    rgb = s.renderer.render_robot_cameras(modes=('rgb'))

s.disconnect()