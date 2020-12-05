import re

# Return list of dictionary with present passport fields as keys and passport values as values
def getInputData(fileName):
    groupedPassportData =[x.split() for x in open(fileName).read().split("\n\n")]
    return [{y.split(":")[0]: y.split(":")[1] for y in x} for x in groupedPassportData]

# Check if passport contains all mandatory fields and satisfies all validation rules and return true for valid, and false for invalid passport
def isValidPassport(passport, requiredFields, runValueValidation, validationRules):
    for r in requiredFields:
        if (r not in passport) and requiredFields[r]:
            return False
        if(runValueValidation and r in validationRules and not validationRules[r](passport[r])):
            return False
    
    return True
# Check if passport is valid when only requiring mandatory fields are present
def areRequiredFieldsPresent(passport, requiredFields):
    return isValidPassport(passport, requiredFields, False, {})

def solve4b(passportList, requiredFields, runValueValidation, validationRules):
    numOfValidPp = 0

    for p in passportList:
        if (runValueValidation and isValidPassport(p, requiredFields, runValueValidation, validationRules)) or (not runValueValidation and areRequiredFieldsPresent(p, requiredFields)):
            numOfValidPp += 1

    return numOfValidPp

def solve4a(passportList, requiredFields):
    return solve4b(passportList, requiredFields, False, {})



# Dictionary with passport fieldd as key, and bool "isMandatory" as value
requiredFields = {
    'byr': True,
    'iyr': True,
    'eyr': True,
    'hgt': True,
    'hcl': True,
    'ecl': True,
    'pid': True,
    'cid': False
}

# dictionary of validationrules to be run on the different passport fields
validationRules = {
    'byr': lambda x: re.match("^[0-9]{4}$", x) and int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: re.match("^[0-9]{4}$", x) and int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: re.match("^[0-9]{4}$", x) and int(x) >= 2020 and int(x) <= 2030,
    'hgt': lambda x: (re.match("^[0-9]{2}in$", x) and int(x[0:2]) >= 59 and int(x[0:2]) <= 76) or (re.match("^[0-9]{3}cm$", x) and int(x[0:3]) >= 150 and int(x[0:3]) <= 193),
    'hcl': lambda x: re.match("^#[a-f0-9]{6}$", x) is not None,
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.match("^[0-9]{9}$", x) is not None
}

#Answer problem 1
print(solve4a(getInputData("input.txt"), requiredFields))

print(solve4b(getInputData("input.txt"), requiredFields, True, validationRules))
