from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y, z)
blockType2 = mc.getBlock(x, y + 1, z)
if blockType == 9 and blockType2 ==9 :
    mc.postToChat("ur sinking dudster")
else :
    mc.postToChat("not submerged ;) ")
