from pymcfunction import *

execute().asEntity(selector("@e")).ifBlock("~ ~ ~", Block.GLASS).run(
    say("hi"), function("testdir/testtt")
)

item().replaceBlock("~ ~ ~", "0", Item.DIAMOND)

tag("@s").add("test")
