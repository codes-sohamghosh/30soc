from re import sub

def camel(s):
    s = (
        sub(r"(_|-)+", " ", s)            # replaces dashes and underscores with space
         .title()                         # capitalizes first letter of each word
         .replace(" ", "")                # removes spaces
        )
    return s[0].lower()+s[1:]             # lowers the first character of the string

print(camel('some_database_field_name'))
# 'someDatabaseFieldName'
print(camel('Some label that needs to be camelized'))
# 'someLabelThatNeedsToBeCamelized'
print(camel('some-javascript-property'))
# 'someJavascriptProperty'
print(camel('some-mixed_string with spaces_underscores-and-hyphens'))
# 'someMixedStringWithSpacesUnderscoresAndHyphens'