import pytest

def test_dev(isDevOrProd, MOCKS):
    resDev = isDevOrProd(MOCKS)
    assert len(resDev) == 2
    assert resDev == ['CUR1', 'CUR2']


def testProd(isDevOrProd):
    expectedResult = ['AED', 'ANG', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BMD', 'BND', 'BOB', 'BRL', 'BSD',
                      'BTC', 'BYN', 'BZD', 'CAD', 'CHF', 'CLF', 'CNY', 'CUC', 'DKK', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL',
                      'GGP', 'GHS', 'GIP', 'GTQ', 'HKD', 'HRK', 'ILS', 'IMP', 'JEP', 'JOD', 'KWD', 'KYD', 'LTL', 'LVL',
                      'LYD', 'MOP', 'MYR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PLN', 'QAR', 'RON', 'SAR', 'SBD', 'SGD',
                      'SHP', 'SVC', 'TMT', 'TND', 'TOP', 'TTD', 'USD', 'WST', 'XAG', 'XAU', 'XCD', 'XDR']


    resProd = isDevOrProd(None)
    assert len(resProd) == 68
    assert resProd == expectedResult

