import re

def main():
  course = [row.strip() for row in open('input.txt').readlines()]

  passport = {}
  passports = []
  for line in course:
    if not line:
      passports.append(passport)
      passport = {}
      continue
    tuples = line.split(' ')
    for clause in tuples:
      key, val = clause.split(':')
      passport[key] = val
  if passport: 
    passports.append(passport)

  valids = 0
  for passport in passports: 
    if all([(k in passport) for k in ['byr','iyr','eyr','hgt','hcl','ecl','pid']]):
      byr = passport['byr'] 
      if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
        continue
      iyr = passport['iyr']
      if len(iyr) !=4 or int(iyr) < 2010 or int(iyr) > 2020:
        continue
      eyr = passport['eyr']
      if len(eyr) !=4 or int(eyr) < 2020 or int(eyr) > 2030:
        continue
      hgt = passport['hgt']
      if 'cm' in hgt:
        cm = int(re.findall(r"-?\d+",hgt)[0])
        if cm < 150 or cm > 193: 
          continue
      elif 'in' in hgt:
        cm = int(re.findall(r"-?\d+",hgt)[0])
        if cm < 59 or cm > 76: 
          continue
      else:
        continue
      hcl = passport['hcl']
      if not re.match('#[0-9a-f]{6}',hcl):
        continue
      ecl = passport['ecl']
      if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue
      pid = passport['pid']
      if not re.match('^[0-9]{9}$',pid):
        continue
      else:
        print(pid)
      valids+=1
      print(byr, iyr, eyr, hgt, hcl, ecl, pid)
      print(valids)
  print(valids)

main()