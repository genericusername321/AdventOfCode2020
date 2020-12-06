import re

def parsePassport(passport):
    # parse passport string
    passport = passport.replace('\n', ' ').rstrip()
    fields = passport.split(' ')
    keyValList = [tuple(field.split(':')) for field in fields]

    try: 
        return dict(keyValList)
    except ValueError:
        print(passport)
        print(fields)
        print(keyValList)


def validatePassport1(passport):
    # Validate passport for part 1
    reqKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in reqKeys:
        if key not in passport:
            return False

    return True

def validateNumeric(val, low, high):
    if val is None: 
        return False

    val = int(val)
    if val < low or val > high:
        return False
    return True

def validateHairColour(hcl):
    if hcl is None:
        return False
    
    if len(hcl) > 7:
        return False

    pat = re.compile('#([0-9a-f]{6})')
    if pat.match(hcl) is None:
        return False
    return True
    
def validateEyeColour(ecl):
    if ecl is None:
        return False

    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    return True

def validatePid(pid):
    if pid is None:
        return False
    if len(pid) > 9:
        return False

    pat = re.compile('[0-9]{9}')
    if not pat.match(pid):
        return False
    return True

def validateHeight(hgt):
    if hgt is None: 
        return False

    pat1 = re.compile('([0-9]{2}in)')
    pat2 = re.compile('([0-9]{3}cm)')
    if pat1.match(hgt):
        height = int(hgt[:-2])
        unit = hgt[-2:]
        if height >= 59 and height <= 76:
            return True
    
    if pat2.match(hgt):
        height = int(hgt[:-2])
        unit = hgt[-2:]
        if height >= 150 and height <= 193:
            return True

    return False

def validatePassport2(passport):
    # Validate passport for part 2
    if not validatePassport1(passport):
        return False
    
    byr = passport.get('byr')
    if not validateNumeric(byr, 1920, 2002):
        return False

    iyr = passport.get('iyr')
    if not validateNumeric(iyr, 2010, 2020):
        return False

    eyr = passport.get('eyr')
    if not validateNumeric(eyr, 2020, 2030):
        return False

    hgt = passport.get('hgt')
    if not validateHeight(hgt):
        return False

    hcl = passport.get('hcl')
    if not validateHairColour(hcl):
        return False

    ecl = passport.get('ecl')
    if not validateEyeColour(ecl):
        return False

    pid = passport.get('pid')
    if not validatePid(pid):
        return False

    return True

if __name__ == "__main__":
    with open('day4.in') as f:
        data = f.read()
        passports = data.split('\n\n')

    numValid = 0
    for p in passports:
        passport = parsePassport(p)
        if validatePassport2(passport):
            numValid += 1

    print(numValid)
        
