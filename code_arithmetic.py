label_id = 0

def add_sub_or_and(operator):
  return "\n".join([
        "@SP",
        "A=M-1",
        "A=A-1",
        "D=M ",
        "A=A+1",
        f"D=D{operator}M", 
        "A=A-1",
        "M=D",
        "@SP",
        "M=M-1"
    ])
  
def neg():
  return  "\n".join([
        '@SP',
        'A=M-1',
        'D=M',
        'M=M-D',
        'M=M-D'
    ])

def invert():
  return "\n".join([
        '@SP',
        'A=M-1',
        'M=!M'
    ])
  
def compare(symbol):
  global label_id
  label_id+=1
  return "\n".join([
    "@SP",
    "A=M-1",
    "A=A-1",
    "D=M",
    "A=A+1",
    "D=D-M",
    f"@IF_TRUE_{label_id}",
    f"D;J{symbol}",
    "@SP",
    "A=M-1",
    "A=A-1",
    "M=0",
    f"@UPDATE_SP_{label_id}",
    "0;JMP",
    f"(IF_TRUE_{label_id})",
    "@SP",
    "A=M-1",
    "A=A-1",
    "M=-1",
    f"(UPDATE_SP_{label_id})",
    "@SP",
    "M=M-1"
      
  ])