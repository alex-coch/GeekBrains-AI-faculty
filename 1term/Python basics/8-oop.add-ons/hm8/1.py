class OurDate:
    d_str = ''

    def __init__(self, in_str):
        OurDate.d_str = in_str

    @classmethod
    def transform_it(cls):
        return int(cls.d_str[:1]) + (int(cls.d_str[3:4]) - 1) * 30 + (int(cls.d_str[6:]) - 1) * 365

    @staticmethod
    def valid(in_str):
        return True if (int(in_str[:2]) >= 1 and int(in_str[:2]) <= 31) and \
                       (int(in_str[3:5]) >= 1 and int(in_str[3:5]) <= 12) and \
                       int(in_str[6:]) >= 1 else False


our_date = OurDate('01-09-2021')
if OurDate.valid(OurDate.d_str):
    print(our_date.transform_it())
