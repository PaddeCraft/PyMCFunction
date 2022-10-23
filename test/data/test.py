from pymcfunction import *

execute().asEntity(selector("@e")).ifBlock("~ ~ ~", "minecraft:glass").run(
    say("hi"), function("testdir/testtt")
)
