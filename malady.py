#!/usr/bin/python3
# +---------------------------+
# | Python Malady Interpreter |
# +---------------------------+----------+
# | by Martín del Río (github.com/lartu) |
# +--------------------------------------+
import sys

VERSION = "1.0"

def throwError(msg):
    print(f"Error: {msg}")
    quit(1)

def evaluateParameters():
    # Evaluate each parameter passed
    for arg in sys.argv:
        if arg == "-h" or arg == "--help":
            print(f"\n * Usage:\n \033[1;33mmalady source_file\033[0m")
            print(f"\n * About:")
            print(f" \033[1;33mMalady\033[0m is an esolang based executing text replacements\n on a source, following user defined \033[1;36mrules\033[0m.")
            print(f"\n Each rule occupies one entire line of code. Rule lines\n begin with the character '\033[1;35m>\033[0m', and follow the format")
            print(f" '\033[1;35m>conditions|replacements\033[0m'. Conditions are comma\n separated values that must be matched in any non-rule")
            print(f" line (or lines) of the source code in order to trigger\n the rule. If all the tokens are found in the source,")
            print(f" the \033[1;33mreplacements\033[0m are executed. Replacements are comma\n sepparated '\033[1;34moldvalue->newvalue\033[0m' statements. An \033[1;36moldvalue\033[0m")
            print(f" of '\033[1;36m*\033[0m' matches any character. If a condition is preceded\n by '\033[1;35m~\033[0m', that token will trigger if it ISN'T found in the")
            print(f" source. Execution halts when there are no characters left\n in the source.")
            print(f"\n * Example: add A and B in C:")
            print(f" \033[1;33m>A:I|A:I->A:,C:->C:I")
            print(f" >B:I|B:I->B:,C:->C:I")
            print(f" >~A:I,~B:I|*->")
            print(f" A:IIIII")
            print(f" B:III")
            print(f" C:I\033[0m\n")
            quit(0)
        elif arg == "-v" or arg == "--version":
            print(f"\n Hi there! This is \033[1;33mMalady {VERSION}\033[0m,")
            print(f" by \033[1;35mMartín del Río\033[0m (www.lartu.net).")
            print(f"\n You can get the Malady source\n code at \033[1;36mgithub.com/lartu/malady\033[0m.")
            print(f"\n Malady may be copied only under\n the terms of the GNU General")
            print(f" Public License 3.0, which may be\n found in the Malady repository.\n")
            quit(0)
        elif arg == "-c": # Read from command line
            sourceFile = None
        else:
            sourceFile = arg
    # If no source file was provided
    if sourceFile == "":
        throwError("Please provide a valid source file.")
    return sourceFile

def loadSourceFile(sourceFile):
    try:
        sourceCode = open(sourceFile, "r").read()
        return sourceCode
    except:
        throwError(f"Error loading file '{sourceFile}'.")

def getRules(sourceCode):
    lines = sourceCode.split("\n")
    rules = []
    sourceWithoutLines = ""
    for line in lines:
        # Lines that start with > are a replacement rule
        if len(line) > 0 and line[0] == ">":
            line = line[1:]
            rule_conditions = []
            rule_replacements = []
            parts = line.split("|")
            conditions = parts[0].split(",")
            replacements = parts[1].split(",")
            for condition in conditions:
                expected = True
                condition = condition
                if len(condition) > 0 and condition[0] == "~":
                    expected = False
                    condition = condition[1:]
                rule_conditions.append((condition, expected))
            for replacement in replacements:
                parts = replacement.split("->")
                re_from = parts[0]
                re_to = parts[1]
                rule_replacements.append((re_from, re_to))
            rules.append((rule_conditions, rule_replacements))
        else:
            sourceWithoutLines += "\n" + line
    return (rules, sourceWithoutLines[1:])

def execute(program):
    rules = program[0]
    source = program[1]
    itNum = 1
    while len(source) > 0:
        for rule in rules:
            conditionTrue = True
            for condition in rule[0]:
                if (condition[0] in source) != condition[1]:
                    conditionTrue = False
                    break
            if conditionTrue:
                for replacement in rule[1]:
                    if replacement[0] != "*":
                        source = source.replace(replacement[0], replacement[1])
                    else:
                        source = replacement[1] * len(source)
                    if len(source) > 0:
                        print(f"--- Iteration {itNum} ---\n{source}")
                        itNum += 1

if __name__ == "__main__":
    sourceFile = evaluateParameters()
    sourceCode = loadSourceFile(sourceFile)
    program = getRules(sourceCode)
    execute(program)
