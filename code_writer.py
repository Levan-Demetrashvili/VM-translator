from variables import operator_symbols, segment_abbr
import code_arithmetic as arithmetic
import memory_commands as memory

def code_writer(command,fileName):
  instructions = ""
  commandType, arg1, arg2 = command["commandType"], command["arg1"], command["arg2"]
  #* ARITHMETIC
  if commandType == 'C_ARITHMETIC':
    match arg1:
      case 'add' | 'sub' | 'or' | 'and':
        instructions = arithmetic.add_sub_or_and(operator_symbols[arg1])
      case 'neg':
        instructions = arithmetic.neg()
      case 'not':
        instructions = arithmetic.invert()
      case 'eq' | 'gt' | 'lt':
        instructions = arithmetic.compare(arg1.upper())
  #* PUSH
  elif commandType == 'C_PUSH':
     match arg1:
      case 'constant':
        instructions = memory.push_constant(arg2)
      case 'local' | 'argument' | 'this' | 'that':
        instructions = memory.push_local_argument_this_that(segment_abbr[arg1],arg2)
      case 'temp' | 'pointer' | 'static':
        address = 5 + int(arg2) if arg1 == 'temp' else 3 + int(arg2)
        if arg1 == 'static':
          address=f"{fileName}.{arg2}"
        instructions = memory.push_temp_pointer_static(address) 
  #* POP
  elif commandType == 'C_POP':
    match arg1:
      case 'local' | 'argument' | 'this' | 'that' :
        instructions = memory.pop_local_argument_this_that(segment_abbr[arg1],int(arg2))
      case 'temp' | 'pointer' | 'static':
        address = 5 + int(arg2) if arg1 == 'temp' else 3 + int(arg2)
        if arg1 == 'static':
          address=f"{fileName}.{arg2}"
        instructions = memory.pop_temp_pointer_static(address) 
  
  print( f"// {commandType} {arg1} {arg2 if arg2 else ""}"+ "\n"+instructions)
  return instructions