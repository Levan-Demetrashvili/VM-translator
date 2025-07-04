def write_label(file_stem,label):
  return "\n".join([f"({file_stem}${label})"])

def write_goto(file_stem,label):
  return "\n".join([f"@{file_stem}${label}","0;JMP"])

def write_if(file_stem,label):
  return "\n".join([
    "@SP",
    "M=M-1",
    "A=M",
    "D=M",
    f"@{file_stem}${label}",
    "D;JNE"
  ])