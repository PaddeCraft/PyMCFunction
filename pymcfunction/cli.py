import os
import json
import toml
import time
import typer
import shutil

from io import StringIO
from pathlib import Path
from contextlib import redirect_stdout
from tkinter.filedialog import asksaveasfilename


app = typer.Typer()


def getConfig():
    pathParts = Path(os.getcwd()).parts
    config = None
    for i in reversed(range(len(pathParts))):
        rootPath = os.path.join(*pathParts[: i + 1])
        cfgFile = os.path.join(rootPath, "pymcfunctionconfig.toml")
        try:
            if os.path.isfile(cfgFile):
                config = toml.load(cfgFile)
                break
        except Exception:
            pass
    if config == None:
        print(
            "Could not find config file at this and containing paths. "
            + "Did you initialize a project and have the permission to read the file?"
        )
        raise typer.Exit(1)
    if True in [config["namespace"] == "", config["compiled_folder_name"] == ""]:
        print("Please set 'namespace' and 'compiled_folder_name' before compiling.")
        raise typer.Exit(1)
    return (
        config,
        cfgFile,
        rootPath,
        os.path.join(config["datapack_folder"], config["compiled_folder_name"]),
    )


@app.command()
def init(dir: str = typer.Option(".", "--dir", "-d")):
    if os.path.isdir(dir):
        if len(os.listdir()) != 0:
            print("The directory is not empty.")
            raise typer.Exit(1)
    else:
        try:
            os.makedirs(dir)
        except Exception as e:
            print("Could not create directory.\nException: " + str(e))
            raise typer.Exit(1)
    with open(os.path.join(dir, "pymcfunctionconfig.toml"), "w", encoding="UTF-8") as c:
        toml.dump(
            {
                "namespace": "",
                "compiled_folder_name": "",
                "description": "",
                "datapack_folder": os.getcwd(),
                "pack_version": 8,
                "includes": {},
            },
            c,
        )
        os.makedirs(os.path.join(dir, "data"))


@app.command()
def compile():
    config, cfgFile, rootPath, outFolder = getConfig()

    specialFunctions = {"load": [], "tick": []}
    if os.path.isdir(outFolder):
        print("Removing out folder...")
        shutil.rmtree(outFolder)
        print("Removed out folder!")
    print("Starting compilation process...\n")
    Path(outFolder).mkdir(parents=True)
    with open(os.path.join(outFolder, "pack.mcmeta"), "w+", encoding="UTF-8") as mcmeta:
        json.dump(
            {
                "pack": {
                    "pack_format": config["pack_version"],
                    "description": config["description"],
                }
            },
            mcmeta,
        )
    datapath = os.path.join(rootPath, "data")
    for root, _, files in os.walk(datapath):
        for dpfile in files:
            pth = os.path.join(root, dpfile)
            f = pth.replace(datapath, "")
            if f[0] == os.sep:
                f = f[1:]
            out = (
                os.path.join(
                    outFolder, "data", config["namespace"], "functions", f
                ).removesuffix(".py")
                + ".mcfunction"
            )
            print("> " + f)
            with open(pth, "r", encoding="UTF-8") as fl:
                content = fl.read()
            statements = []
            current = ""
            brackets = 0

            for c in content:
                if c == "(":
                    brackets += 1
                if c == ")":
                    brackets -= 1
                if c == "\n" and brackets == 0:
                    if current != "":
                        statements.append(current)
                        current = ""
                else:
                    current += c
            if current != "":
                statements.append(current)

            lines = []
            imports = ""
            removelist = []
            for s in statements:
                if s.split(" ")[0] in ["import", "from"]:
                    imports += s + "\n"
                    removelist.append(s)
                if s == "##pymcfunction-tick":
                    specialFunctions["tick"].append(
                        config["namespace"] + ":" + f.removesuffix(".py")
                    )
                elif s == "##pymcfunction-load":
                    specialFunctions["load"].append(
                        config["namespace"] + ":" + f.removesuffix(".py")
                    )
                if len(s) > 0:
                    if s[0] == "#":
                        removelist.append(s)

            # Yes, this is needed because of weird python behaviour
            for r in removelist:
                statements.remove(r)

            for s in statements:
                code = (
                    imports
                    + "\n_output = "
                    + s
                    + "\nif type(_output) == str: print(_output)"
                )
                try:
                    stdout = StringIO()
                    with redirect_stdout(stdout):
                        exec(code)
                    lines.append(stdout.getvalue().strip("\n"))
                except Exception as e:
                    print("\n" + str(e) + "\n\nCode used:\n" + code)
                    print(f"\n\nError while compiling {f}!")
                    print(statements)
                    raise typer.Abort()
            # Write to file
            Path(os.path.split(out)[0]).mkdir(parents=True, exist_ok=True)
            with open(out, "w+", encoding="UTF-8") as outfile:
                outfile.write(
                    "\n".join(lines).replace(
                        "@@PYMCFUNCTION-NAMESPACE", config["namespace"]
                    )
                )
    Path(os.path.join(outFolder, "data", "minecraft", "tags", "functions")).mkdir(
        parents=True
    )
    with open(
        os.path.join(outFolder, "data", "minecraft", "tags", "functions", "load.json"),
        "w+",
        encoding="UTF-8",
    ) as f:
        json.dump({"values": specialFunctions["load"]}, f)
    with open(
        os.path.join(outFolder, "data", "minecraft", "tags", "functions", "tick.json"),
        "w+",
        encoding="UTF-8",
    ) as f:
        json.dump({"values": specialFunctions["tick"]}, f)

    print("\nCompilation process finished without errors!")


@app.command()
def publish():
    config, cfgFile, rootPath, outFolder = getConfig()
    files = [("Zip Files", "*.zip")]
    file = asksaveasfilename(
        filetypes=files,
        defaultextension=files,
        title="Save packaged datapack...",
        confirmoverwrite=True,
        initialfile=f'{config["compiled_folder_name"]}-{int(time.time())}.zip',
    )
    print(file)
    if file.lower()[-4:] == ".zip":
        file = file[:-4]
    print(file)
    compile()
    print("\nMaking archive...")
    shutil.make_archive(file, "zip", outFolder)
    print("Created archive!")
