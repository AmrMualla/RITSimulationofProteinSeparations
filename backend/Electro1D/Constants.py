class Constants:
    low = 0.75
    medium = 1.0
    high = 1.5
    highX2 = 2.0
    slow = "Slow"
    moderate = "Moderate"
    fast = "Fast"
    wellCount = 10
    dyeColor = (132, 50, 237)
    dyes = [("Dye", "Dye", "Dye", 6000, (132, 50, 237)) for i in range(wellCount)]
    gels = [
        ("7.5%", 7.5),
        ("10%", 10),
        ("12%", 12),
        ("15%", 15)
    ]
    gelPercents = [gel[0] for gel in gels]
    fiftyV = "50V"
    hundredV = "100V"
    oneFiftyV = "150V"
    twoHundredV = "200V"
    voltageList = [fiftyV, hundredV, oneFiftyV, twoHundredV]
    std1Ref = 0
    std2Ref = 1
    std3Ref = 2
    std4Ref = 3
    std5Ref = 4
    std6Ref = 5
    std7Ref = 6
    standardIndices = [std1Ref, std2Ref, std3Ref, std4Ref, std5Ref, std6Ref, std7Ref]

