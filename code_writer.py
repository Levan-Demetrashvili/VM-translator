from variables import operator_symbols, segment_abbr
import code_arithmetic as arithmetic
import memory_commands as memory
import code_branching as branching
import code_function_commands as functions

current_function = None
call_index = 0

def code_writer(command):
  global current_function,call_index
  instructions = ""
  commandType, arg1, arg2,file_stem = command["commandType"], command["arg1"], command["arg2"],command["file_stem"]
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
          address=f"{file_stem}.{arg2}"
        instructions = memory.push_temp_pointer_static(address) 
  #* POP
  elif commandType == 'C_POP':
    match arg1:
      case 'local' | 'argument' | 'this' | 'that' :
        instructions = memory.pop_local_argument_this_that(segment_abbr[arg1],int(arg2))
      case 'temp' | 'pointer' | 'static':
        address = 5 + int(arg2) if arg1 == 'temp' else 3 + int(arg2)
        if arg1 == 'static':
          address=f"{file_stem}.{arg2}"
        instructions = memory.pop_temp_pointer_static(address) 
  #* LABEL
  elif commandType == 'C_LABEL':
    instructions = branching.write_label(current_function,arg1)
  #* GOTO
  elif commandType == 'C_GOTO':
    instructions = branching.write_goto(current_function,arg1)
  #* IF
  elif commandType == 'C_IF':
    instructions = branching.write_if(current_function,arg1)
  #* FUNCTION
  elif commandType == 'C_FUNCTION':
    instructions = functions.write_function(arg1,arg2)
    current_function = arg1
    call_index = 0
  #* RETURN
  elif commandType == 'C_RETURN':
    instructions = functions.write_return()
  #* CALL
  elif commandType == 'C_CALL':
    instructions = functions.write_call(current_function,call_index,arg1,arg2)
    call_index += 1
    
  return instructions
