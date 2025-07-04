
def write_call(function_name,index,callee_name,nArgs):
  segments = ['LCL','ARG','THIS','THAT']
  result = []
  init = []
  for segment in segments:
    result.extend([
    f"@{segment}",
    "D=M",
    "@SP",
    "A=M",
    "M=D",
    "@SP",
    "M=M+1",
    ])
  if function_name == 'INIT':
    init = ["@256",
    "D=A",
    "@SP",
    "M=D",]
  return "\n".join([
    *init,
    f"@{function_name}$ret.{index}",
    "D=A",
    "@SP",
    "A=M",
    "M=D",
    "@SP",
    "M=M+1",
    *result,
    "@SP",
    "D=M",
    "@5",
    "D=D-A",
    f"@{nArgs}",
    "D=D-A",
    "@ARG",
    "M=D",
    "@SP",
    "D=M",
    "@LCL",
    "M=D",
    f"@{callee_name}",
    "0;JMP",
    f"({function_name}$ret.{index})"
  ])

def write_function(function_name,nLocalVars):
  return  "\n".join(
    [f"({function_name})"] + [
      "@0",
      "D=A",
      "@SP",
      "A=M",
      "M=D",
      "@SP",
      "M=M+1"
] * int(nLocalVars)
)

def write_return():
  segments = ['LCL','ARG','THIS','THAT']
  result = []
  for i,segment in enumerate(segments[::-1]):
    result.extend([
    f"@{i + 1}",
    "D=A",
    "@14",
    "D=M-D",
    "A=D",
    "D=M",
    f"@{segment}",
    "M=D",
    
    ])
  return "\n".join([
"@LCL",
"D=M",
"@14",
"M=D",
"D=M",
"@5",
"D=D-A",
"A=D",
"D=M",
"@15",
"M=D",
"// *ARG = pop()",
"@SP",
"M=M-1",
"A=M",
"D=M",
"@ARG",
"A=M",
"M=D",
"//SP = ARG + 1",
"@ARG",
"D=M",
"@SP",
"M=D+1",
*result,
"@15",
"A=M",
"0;JMP"
])
 
