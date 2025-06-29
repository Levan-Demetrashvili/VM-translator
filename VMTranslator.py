import sys
from trimmer import trimmer 
from parser import parser
from code_writer import code_writer

def main():
  programName = sys.argv[1].split('/')[-1].split('.')[0]
  multi_line_comment = False
  commands = []
  
  with open(sys.argv[1], "r") as f:
    for line in f:
      (command,multi_line_comment) = trimmer(line,multi_line_comment)
      if not command:
        continue
      commands.append(parser(command))

  with open(f"./translated/{programName}.asm", "w") as f:
    for command in commands:
      assembly_code = code_writer(command,programName)
      f.write(assembly_code + '\n')

if __name__ == "__main__":
  main()