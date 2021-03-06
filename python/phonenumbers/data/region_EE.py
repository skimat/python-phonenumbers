"""Auto-generated file, do not edit by hand. EE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_EE = PhoneMetadata(id='EE', country_code=372, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[3-9]\\d{6,7}|800\\d{6,7}', possible_number_pattern='\\d{7,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3[23589]|4(?:0\\d|[3-8])|6\\d|7[1-9]|88)\\d{5}', possible_number_pattern='\\d{7,8}', example_number='3212345'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5\\d|8[1-5])\\d{6}|5(?:[02]\\d{2}|1(?:[0-8]\\d|95)|5[0-478]\\d|64[0-4]|65[1-589])\\d{3}', possible_number_pattern='\\d{7,8}', example_number='51234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='800(?:0\\d{3}|1\\d|[2-9])\\d{3}', possible_number_pattern='\\d{7,10}', example_number='80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{4}', possible_number_pattern='\\d{7}', example_number='9001234'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='70[0-2]\\d{5}', possible_number_pattern='\\d{8}', example_number='70012345'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11[02]', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='800[2-9]\\d{3}', possible_number_pattern='\\d{7}', example_number='8002123'),
    number_format=[NumberFormat(pattern='([34-79]\\d{2})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[369]|4[3-8]|5(?:[0-2]|5[0-478]|6[45])|7[1-9]', '[369]|4[3-8]|5(?:[02]|1(?:[0-8]|95)|5[0-478]|6(?:4[0-4]|5[1-589]))|7[1-9]']),
        NumberFormat(pattern='(70)(\\d{2})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['70']),
        NumberFormat(pattern='(8000)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['800', '8000']),
        NumberFormat(pattern='([458]\\d{3})(\\d{3,4})', format=u'\\1 \\2', leading_digits_pattern=['40|5|8(?:00|[1-5])', '40|5|8(?:00[1-9]|[1-5])'])])
