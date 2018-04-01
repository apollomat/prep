def run_length_encoding(s):
  #aaaabcccaa = 4a1b3c2a
  curr_char = s[0]
  count = 0
  formed_str = ""
  for i in s:
    if(i == curr_char):
      count = count + 1
      
    else:
      formed_str += str(count) + curr_char
      curr_char = i
      count = 1
  
  formed_str += str(count) + curr_char
  if len(formed_str) < s:
    return formed_str
  return s
  
  
print run_length_encoding("aaaabcccaa")
    
