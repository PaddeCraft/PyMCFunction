from pymcfunction import *

execute().asEntity(selector("@e")).ifBlock("~ ~ ~", "minecraft:glass").run(
    say("hi"), function("testdir/testtt")
)

item().replaceBlock("~ ~ ~", "0", "minecraft:diamond")

tag("@s").add("test")
