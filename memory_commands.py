
def push_constant(value):
    return "\n".join([
        f"@{value}",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
    ])
    
def push_local_argument_this_that(segmentAbbr,index):
  return "\n".join([
        f"@{segmentAbbr}",
        "D=M",
        f"@{index}",
        "D=D+A",
        "A=D",
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"])
    
def push_temp_pointer_static(address):
  return "\n".join([
        f"@{address}",
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"])
  
  
def pop_local_argument_this_that(segmentAbbr,index):
  return "\n".join([
      f"@{segmentAbbr}",
      "D=M",
      f"@{index}",
      "D=D+A",
      "@13",
      "M=D",
      "@SP",
      "M=M-1",
      "A=M",
      "D=M",
      "@13",
      "A=M",
      "M=D"
    ])


def pop_temp_pointer_static(address):
  return "\n".join([
      "@SP",
      "M=M-1",
      "A=M",
      "D=M",
      f"@{address}",
      "M=D",
    ])