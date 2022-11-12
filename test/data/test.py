from pymcfunction import *

execute().asEntity(selector("@e")).ifBlock("~ ~ ~", Block.GLASS).run(
    say("hi"), function("testdir/testtt")
)

item().replaceBlock("~ ~ ~", "0", Item.DIAMOND)

tag("@s").add("test")

effect("@e").give(Effect.DARKNESS)
effect("@e").give(Effect.DARKNESS, 12)
effect("@e").give(Effect.DARKNESS, 12, 255)
effect("@e").give(Effect.DARKNESS, 12, 255, True)

effect("@e").clear()
effect("@e").clear(Effect.DARKNESS)
