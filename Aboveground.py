from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(x, z)
if pos.y < highestBlockY:
    mc.postToChat("u are below the ground dude")
else:
    mc.postToChat("u are above the gorund dude")
