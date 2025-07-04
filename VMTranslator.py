import sys
import os
from trimmer import trimmer 
from parser import parser
from code_writer import code_writer
from code_function_commands import write_call as init

commands = []
multi_line_comment = False

def process_file(filepath,file_stem):
  global multi_line_comment
  with open(filepath, "r") as f:
    for line in f:
      (command,multi_line_comment) = trimmer(line,multi_line_comment)
      if not command:
        continue
      commands.append({**parser(command),"file_stem":file_stem})

def main():
  programName = sys.argv[1].split('/')[-1].split('.')[0]
  need_init = False

  #* Handling input file/directory
  if os.path.isfile(sys.argv[1]):
    process_file(sys.argv[1],programName)
  else:
    for file in os.listdir(sys.argv[1])[::-1]:
      if file.endswith('.vm'):
        filepath = os.path.join(sys.argv[1],file)
        file_stem = file.split('.')[0]
        process_file(filepath,file_stem)
        if file_stem == 'Sys':
          need_init = True
  
  #* Translate commands to Assembly
  with open(f"{programName}.asm", "w") as f:
    need_init and f.write(init("INIT",0,"Sys.init",0) + '\n') #* initialize
    for command in commands:
      assembly_code = code_writer(command)
      f.write(assembly_code + '\n')

if __name__ == "__main__":
  main()