import unittest
from mainDR import convert_decimal_to_roman

class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        roman_number = convert_decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')
    def test_2(self):
        roman_number = convert_decimal_to_roman(2)
        self.assertEqual(roman_number, 'II')
    def test_3(self):
        roman_number = convert_decimal_to_roman(3)
        self.assertEqual(roman_number, 'III')
    def test_4(self):
        roman_number = convert_decimal_to_roman(4)
        self.assertEqual(roman_number, 'IV')
    def test_5(self):
        roman_number = convert_decimal_to_roman(5)
        self.assertEqual(roman_number, 'V')
    def test_6(self):
        roman_number = convert_decimal_to_roman(6)
        self.assertEqual(roman_number, 'VI')
    def test_7(self):
        roman_number = convert_decimal_to_roman(7)
        self.assertEqual(roman_number, 'VII')
    def test_8(self):
        roman_number = convert_decimal_to_roman(8)
        self.assertEqual(roman_number, 'VIII')
    def test_9(self):
        roman_number = convert_decimal_to_roman(9)
        self.assertEqual(roman_number, 'IX')
    def test_10(self):
        roman_number = convert_decimal_to_roman(10)
        self.assertEqual(roman_number, 'X')
    def test_11(self):
        roman_number = convert_decimal_to_roman(11)
        self.assertEqual(roman_number, 'XI')
    def test_12(self):
        roman_number = convert_decimal_to_roman(12)
        self.assertEqual(roman_number, 'XII')
    def test_13(self):
        roman_number = convert_decimal_to_roman(13)
        self.assertEqual(roman_number, 'XIII')
    def test_14(self):
        roman_number = convert_decimal_to_roman(14)
        self.assertEqual(roman_number, 'XIV')
    def test_15(self):
        roman_number = convert_decimal_to_roman(15)
        self.assertEqual(roman_number, 'XV')
    def test_16(self):
        roman_number = convert_decimal_to_roman(16)
        self.assertEqual(roman_number, 'XVI')
    def test_17(self):
        roman_number = convert_decimal_to_roman(17)
        self.assertEqual(roman_number, 'XVII')
    def test_18(self):
        roman_number = convert_decimal_to_roman(18)
        self.assertEqual(roman_number, 'XVIII')
    def test_19(self):
        roman_number = convert_decimal_to_roman(19)
        self.assertEqual(roman_number, 'XIX')
    def test_20(self):
        roman_number = convert_decimal_to_roman(20)
        self.assertEqual(roman_number, 'XX')
    def test_21(self):
        roman_number = convert_decimal_to_roman(21)
        self.assertEqual(roman_number, 'XXI')
    def test_22(self):
        roman_number = convert_decimal_to_roman(22)
        self.assertEqual(roman_number, 'XXII')
    def test_23(self):
        roman_number = convert_decimal_to_roman(23)
        self.assertEqual(roman_number, 'XXIII')
    def test_24(self):
        roman_number = convert_decimal_to_roman(24)
        self.assertEqual(roman_number, 'XXIV')
    def test_25(self):
        roman_number = convert_decimal_to_roman(25)
        self.assertEqual(roman_number, 'XXV')
    def test_26(self):
        roman_number = convert_decimal_to_roman(26)
        self.assertEqual(roman_number, 'XXVI')
    def test_27(self):
        roman_number = convert_decimal_to_roman(27)
        self.assertEqual(roman_number, 'XXVII')
    def test_28(self):
        roman_number = convert_decimal_to_roman(28)
        self.assertEqual(roman_number, 'XXVIII')
    def test_29(self):
        roman_number = convert_decimal_to_roman(29)
        self.assertEqual(roman_number, 'XXIX')
    def test_30(self):
        roman_number = convert_decimal_to_roman(30)
        self.assertEqual(roman_number, 'XXX')
    def test_30(self):
        roman_number = convert_decimal_to_roman(30)
        self.assertEqual(roman_number, 'XXX')
    def test_31(self):
        roman_number = convert_decimal_to_roman(31)
        self.assertEqual(roman_number, 'XXXI')
    def test_32(self):
        roman_number = convert_decimal_to_roman(32)
        self.assertEqual(roman_number, 'XXXII')
    def test_33(self):
        roman_number = convert_decimal_to_roman(33)
        self.assertEqual(roman_number, 'XXXIII')
    def test_34(self):
        roman_number = convert_decimal_to_roman(34)
        self.assertEqual(roman_number, 'XXXIV')
    def test_35(self):
        roman_number = convert_decimal_to_roman(35)
        self.assertEqual(roman_number, 'XXXV')
    def test_36(self):
        roman_number = convert_decimal_to_roman(36)
        self.assertEqual(roman_number, 'XXXVI')
    def test_37(self):
        roman_number = convert_decimal_to_roman(37)
        self.assertEqual(roman_number, 'XXXVII')
    def test_38(self):
        roman_number = convert_decimal_to_roman(38)
        self.assertEqual(roman_number, 'XXXVIII')
    def test_39(self):
        roman_number = convert_decimal_to_roman(39)
        self.assertEqual(roman_number, 'XXXIX')
    def test_40(self):
        roman_number = convert_decimal_to_roman(40)
        self.assertEqual(roman_number, 'XL')
    def test_41(self):
        roman_number = convert_decimal_to_roman(41)
        self.assertEqual(roman_number, 'XLI')
    def test_42(self):
        roman_number = convert_decimal_to_roman(42)
        self.assertEqual(roman_number, 'XLII')
    def test_43(self):
        roman_number = convert_decimal_to_roman(43)
        self.assertEqual(roman_number, 'XLIII')
    def test_44(self):
        roman_number = convert_decimal_to_roman(44)
        self.assertEqual(roman_number, 'XLIV')
    def test_45(self):
        roman_number = convert_decimal_to_roman(45)
        self.assertEqual(roman_number, 'XLV')
    def test_46(self):
        roman_number = convert_decimal_to_roman(46)
        self.assertEqual(roman_number, 'XLVI')
    def test_47(self):
        roman_number = convert_decimal_to_roman(47)
        self.assertEqual(roman_number, 'XLVII')
    def test_48(self):
        roman_number = convert_decimal_to_roman(48)
        self.assertEqual(roman_number, 'XLVIII')
    def test_49(self):
        roman_number = convert_decimal_to_roman(49)
        self.assertEqual(roman_number, 'XLIX')
    def test_50(self):
        roman_number = convert_decimal_to_roman(50)
        self.assertEqual(roman_number, 'L')
    def test_51(self):
        roman_number = convert_decimal_to_roman(51)
        self.assertEqual(roman_number, 'LI')
    def test_52(self):
        roman_number = convert_decimal_to_roman(52)
        self.assertEqual(roman_number, 'LII')
    def test_53(self):
        roman_number = convert_decimal_to_roman(53)
        self.assertEqual(roman_number, 'LIII')
    def test_54(self):
        roman_number = convert_decimal_to_roman(54)
        self.assertEqual(roman_number, 'LIV')
    def test_55(self):
        roman_number = convert_decimal_to_roman(55)
        self.assertEqual(roman_number, 'LV')
    def test_56(self):
        roman_number = convert_decimal_to_roman(56)
        self.assertEqual(roman_number, 'LVI')
    def test_57(self):
        roman_number = convert_decimal_to_roman(57)
        self.assertEqual(roman_number, 'LVII')
    def test_58(self):
        roman_number = convert_decimal_to_roman(58)
        self.assertEqual(roman_number, 'LVIII')
    def test_59(self):
        roman_number = convert_decimal_to_roman(59)
        self.assertEqual(roman_number, 'LIX')
    def test_60(self):
        roman_number = convert_decimal_to_roman(60)
        self.assertEqual(roman_number, 'LX')
    def test_70(self):
        roman_number = convert_decimal_to_roman(70)
        self.assertEqual(roman_number, 'LXX')
    def test_80(self):
        roman_number = convert_decimal_to_roman(80)
        self.assertEqual(roman_number, 'LXXX')
    def test_90(self):
        roman_number = convert_decimal_to_roman(90)
        self.assertEqual(roman_number, 'XC')
    def test_91(self):
        roman_number = convert_decimal_to_roman(91)
        self.assertEqual(roman_number, 'XCI')
    def test_92(self):
        roman_number = convert_decimal_to_roman(92)
        self.assertEqual(roman_number, 'XCII')
    def test_93(self):
        roman_number = convert_decimal_to_roman(93)
        self.assertEqual(roman_number, 'XCIII')
    def test_94(self):
        roman_number = convert_decimal_to_roman(94)
        self.assertEqual(roman_number, 'XCIV')
    def test_95(self):
        roman_number = convert_decimal_to_roman(95)
        self.assertEqual(roman_number, 'XCV')
    def test_96(self):
        roman_number = convert_decimal_to_roman(96)
        self.assertEqual(roman_number, 'XCVI')
    def test_97(self):
        roman_number = convert_decimal_to_roman(97)
        self.assertEqual(roman_number, 'XCVII')
    def test_98(self):
        roman_number = convert_decimal_to_roman(98)
        self.assertEqual(roman_number, 'XCVIII')
    def test_99(self):
        roman_number = convert_decimal_to_roman(99)
        self.assertEqual(roman_number, 'XCIX')
if __name__ == '__main__':
    unittest.main()

