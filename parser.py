def parser(command):
  type_, arg1, arg2 = (command.split() + [None, None, None])[:3]
  match type_:
    case 'push' | 'pop' | 'goto' | 'function' | 'call' | 'return' | 'label' :
      commandType = f"C_{type_.upper()}"
    case 'if-goto':
      commandType = f"C_IF"
    case _:
      commandType="C_ARITHMETIC"
      arg1 = type_
  return {"commandType": commandType,"arg1": arg1,"arg2": arg2}
    