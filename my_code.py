import pytest

def fix_phone_num(phone_num_to_fix):
  # step 7:
  digits_only = ''
  for num in phone_num_to_fix:
    if num.isdigit():
      digits_only += num

  print(digits_only)
  if not digits_only.isdigit() or len(digits_only) != 10:
    raise ValueError("the input must contain only digits and exactly 10 digits")
  
  # given "5125558823". Split the parts, then recombine and return
  area_code = digits_only[0:3] # 512 (first three digits)
  three_part = digits_only[3:6] # 555 (next three digits)
  four_part = digits_only[6:] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  # step 1: 
  assert fix_phone_num('5554429876') == '(555) 442 9876'
  assert fix_phone_num('3216543333') == '(321) 654 3333'

# step 2: this test is expected to fail at first
def test_fix_phone_num_with_bad_formatting():
  assert fix_phone_num('(321) 654 3333') == '(321) 654 3333'

# step 4 & 5:
def test_fix_phone_num_raises_value_error():
  with pytest.raises(ValueError):
    fix_phone_num('test123')

  with pytest.raises(ValueError):
    fix_phone_num('555-442-98761')