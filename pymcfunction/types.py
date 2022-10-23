from enum import Enum


class Gamemode(Enum):
    ADVENTURE = "adventure"
    CREATIVE = "creative"
    SPECTATOR = "spectator"
    SURVIVAL = "survival"
    NOT_ADVENTURE = "!adventure"
    NOT_CREATIVE = "!creative"
    NOT_SPECTATOR = "!spectator"
    NOT_SURVIVAL = "!survival"


class SortOrder(Enum):
    ARBITRARY = "arbitrary"
    FURTHEST = "furthest"
    NEAREST = "nearest"
    RANDOM = "random"


class Entity(Enum):
    # Update by running document.querySelectorAll("td").forEach(function(e) {if(e.classList.length == 0) {if(e.innerText != "") {console.log((e.innerText.split("(")[0].toLowerCase().replaceAll(" ", "_") + ' = "' + e.innerText.split("(")[1].split(")")[0] + '"').replace("\n", ""))}}}) on https://www.digminecraft.com/lists/entity_list_pc.php
    allay = "minecraft:allay"
    area_effect_cloud = "minecraft:area_effect_cloud"
    armor_stand = "minecraft:armor_stand"
    arrow = "minecraft:arrow"
    axolotl = "minecraft:axolotl"
    bat = "minecraft:bat"
    bee = "minecraft:bee"
    blaze = "minecraft:blaze"
    boat = "minecraft:boat"
    cat = "minecraft:cat"
    cave_spider = "minecraft:cave_spider"
    boat_with_chest = "minecraft:chest_boat"
    minecart_with_chest = "minecraft:chest_minecart"
    chicken = "minecraft:chicken"
    cod = "minecraft:cod"
    minecart_with_command_block = "minecraft:command_block_minecart"
    cow = "minecraft:cow"
    creeper = "minecraft:creeper"
    dolphin = "minecraft:dolphin"
    donkey = "minecraft:donkey"
    dragon_fireball = "minecraft:dragon_fireball"
    drowned = "minecraft:drowned"
    egg = "minecraft:egg"
    elder_guardian = "minecraft:elder_guardian"
    end_crystal = "minecraft:end_crystal"
    ender_dragon = "minecraft:ender_dragon"
    ender_pearl = "minecraft:ender_pearl"
    enderman = "minecraft:enderman"
    endermite = "minecraft:endermite"
    evoker = "minecraft:evoker"
    evoker_fangs = "minecraft:evoker_fangs"
    thrown_experience_bottle = "minecraft:experience_bottle"
    experience_orb = "minecraft:experience_orb"
    eye_of_ender = "minecraft:eye_of_ender"
    falling_block = "minecraft:falling_block"
    fireball = "minecraft:fireball"
    firework_rocket = "minecraft:firework_rocket"
    fox = "minecraft:fox"
    frog = "minecraft:frog"
    minecart_with_furnace = "minecraft:furnace_minecart"
    ghast = "minecraft:ghast"
    giant_zombie = "minecraft:giant"
    glow_item_frame = "minecraft:glow_item_frame"
    glow_squid = "minecraft:glow_squid"
    goat = "minecraft:goat"
    guardian = "minecraft:guardian"
    hoglin = "minecraft:hoglin"
    minecart_with_hopper = "minecraft:hopper_minecart"
    horse = "minecraft:horse"
    husk = "minecraft:husk"
    illusioner = "minecraft:illusioner"
    iron_golem = "minecraft:iron_golem"
    item = "minecraft:item"
    item_frame = "minecraft:item_frame"
    lead = "minecraft:leash_knot"
    lightning_bolt = "minecraft:lightning_bolt"
    llama = "minecraft:llama"
    llama_spit = "minecraft:llama_spit"
    magma_cube = "minecraft:magma_cube"
    marker = "minecraft:marker"
    minecart = "minecraft:minecart"
    mooshroom = "minecraft:mooshroom"
    mule = "minecraft:mule"
    ocelot = "minecraft:ocelot"
    painting = "minecraft:painting"
    panda = "minecraft:panda"
    parrot = "minecraft:parrot"
    phantom = "minecraft:phantom"
    pig = "minecraft:pig"
    piglin = "minecraft:piglin"
    piglin_brute = "minecraft:piglin_brute"
    pillager = "minecraft:pillager"
    polar_bear = "minecraft:polar_bear"
    thrown_potion = "minecraft:potion"
    pufferfish = "minecraft:pufferfish"
    rabbit = "minecraft:rabbit"
    ravager = "minecraft:ravager"
    salmon = "minecraft:salmon"
    sheep = "minecraft:sheep"
    shulker = "minecraft:shulker"
    shulker_bullet = "minecraft:shulker_bullet"
    silverfish = "minecraft:silverfish"
    skeleton = "minecraft:skeleton"
    skeleton_horse = "minecraft:skeleton_horse"
    slime = "minecraft:slime"
    small_fireball = "minecraft:small_fireball"
    snow_man_or_snow_golem = "minecraft:snow_golem"
    snowball = "minecraft:snowball"
    minecart_with_spawner = "minecraft:spawner_minecart"
    spectral_arrow = "minecraft:spectral_arrow"
    spider = "minecraft:spider"
    squid = "minecraft:squid"
    stray = "minecraft:stray"
    strider = "minecraft:strider"
    tadpole = "minecraft:tadpole"
    tnt = "minecraft:tnt"
    minecart_with_tnt = "minecraft:tnt_minecart"
    trader_llama = "minecraft:trader_llama"
    trident = "minecraft:trident"
    tropical_fish = "minecraft:tropical_fish"
    turtle = "minecraft:turtle"
    vex = "minecraft:vex"
    villager = "minecraft:villager"
    vindicator = "minecraft:vindicator"
    wandering_trader = "minecraft:wandering_trader"
    warden = "minecraft:warden"
    witch = "minecraft:witch"
    wither_boss = "minecraft:wither"
    wither_skeleton = "minecraft:wither_skeleton"
    wither_skeleton_skull = "minecraft:wither_skull"
    wolf = "minecraft:wolf"
    zoglin = "minecraft:zoglin"
    zombie = "minecraft:zombie"
    zombie_horse = "minecraft:zombie_horse"
    zombie_villager = "minecraft:zombie_villager"
    zombified_piglin = "minecraft:zombified_piglin"


class DataType(Enum):
    BLOCK = "block"
    ENTITY = "entity"
    STORAGE = "storage"


class AnchorType(Enum):
    EYES = "eyes"
    FEET = "feet"


class Dimension(Enum):
    OVERWORLD = "minecraft:overworld"
    NETHER = "minecraft:the_nether"
    END = "minecraft:the_end"


class StoreType(Enum):
    RESULT = "result"
    SUCCESS = "success"


class StoreDataType(Enum):
    BYTE = "byte"
    SHORT = "short"
    INT = "int"
    LONG = "long"
    FLOAT = "float"
    DOUBLE = "double"


class StoreBossbarPosition(Enum):
    VALUE = "value"
    MAX = "max"


class ScoreboardRenderType(Enum):
    HEARTS = "hearts"
    INTEGER = "integer"


class Weather(Enum):
    CLEAR = "clear"
    RAIN = "rain"
    THUNDER = "thunder"


class ContainerType(Enum):
    ENTITY = "entity"
    BLOCK = "block"
