import csv




monday = ["SE1","SE16","EC1W","E1","E2","N1","N1C","NW1","N19","W2","FW1","W1","WC1","WC2","EC1","EC2","EC3","EC4","SW1A","SW1E","SW1H","SW1P","SW1V","SW1W","SW1X","SW1Y","W1B","W1C","W1D","W1F","W1G","W1H","W1J","W1K","W1S","W1T","W1U","W1W","WC1A","WC1B","WC1E","WC1H","WC1N","WC1R","WC1V","WC1X","WC2A","WC2B","WC2E","WC2H","WC2R","EC1A","EC1M","EC1N","EC1R","EC1V","EC1Y","EC2A","EC2M","EC2N","EC2R","EC2V","EC2Y","EC3A","EC3M","EC3N","EC3R","EC3V","EC4A","EC4M","EC4N","EC4R","EC4V","EC4Y","NW5","SE11","SE17","N4","N15","N5","N7","CM15","CM14","RM3","RM2","RM1","RM6","CM13","CM12","CM4","RM7","IG2","IG4","E11","E17","CM11","TN15","TN14"]
tuesday = ["CM1","CM2","CM3","CM6","SE1","EC1W","E1","E2","N1C","NW1","W2","FW1","W1","WC1","WC2","EC1","EC2","EC3","EC4","SW1A","SW1E","SW1H","SW1P","SW1V","SW1W","SW1X","SW1Y","W1B","W1C","W1D","W1F","W1G","W1H","W1J","W1K","W1S","W1T","W1U","W1W","WC1A","WC1B","WC1E","WC1H","WC1N","WC1R","WC1V","WC1X","WC2A","WC2B","WC2E","WC2H","WC2R","EC1A","EC1M","EC1N","EC1R","EC1V","EC1Y","EC2A","EC2M","EC2N","EC2R","EC2V","EC2Y","EC3A","EC3M","EC3N","EC3R","EC3V","EC4A","EC4M","EC4N","EC4R","EC4V","EC4Y","SE11","N5","N7","CM15","CM14","RM3","RM2","RM1","RM6","CM13","CM12","CM4","RM7","IG2","IG4","E11","E10","E9","SW13","SW6","SW10","SW3","SW11","SW8","RM18","RM16","RM14","CM11"]
wednesday = ["SE1","SE16","EC1W","E1","E2","N1","N1C","NW1","N19","W2","FW1","W1","WC1","WC2","EC1","EC2","EC3","EC4","SW1A","SW1E","SW1H","SW1P","SW1V","SW1W","SW1X","SW1Y","W1B","W1C","W1D","W1F","W1G","W1H","W1J","W1K","W1S","W1T","W1U","W1W","WC1A","WC1B","WC1E","WC1H","WC1N","WC1R","WC1V","WC1X","WC2A","WC2B","WC2E","WC2H","WC2R","EC1A","EC1M","EC1N","EC1R","EC1V","EC1Y","EC2A","EC2M","EC2N","EC2R","EC2V","EC2Y","EC3A","EC3M","EC3N","EC3R","EC3V","EC4A","EC4M","EC4N","EC4R","EC4V","EC4Y","NW5","SE11","SE17","N4","N15","N5","N7","CM15","CM14","RM3","RM2","RM1","RM6","CM13","CM12","CM4","RM7","IG2","IG4","E11","E17"]
thursday = ["CM1","CM2","CM3","CM6","SE1","EC1W","E1","E2","N1C","NW1","W2","FW1","W1","WC1","WC2","EC1","EC2","EC3","EC4","SW1A","SW1E","SW1H","SW1P","SW1V","SW1W","SW1X","SW1Y","W1B","W1C","W1D","W1F","W1G","W1H","W1J","W1K","W1S","W1T","W1U","W1W","WC1A","WC1B","WC1E","WC1H","WC1N","WC1R","WC1V","WC1X","WC2A","WC2B","WC2E","WC2H","WC2R","EC1A","EC1M","EC1N","EC1R","EC1V","EC1Y","EC2A","EC2M","EC2N","EC2R","EC2V","EC2Y","EC3A","EC3M","EC3N","EC3R","EC3V","EC4A","EC4M","EC4N","EC4R","EC4V","EC4Y","SE11","N5","N7","CM15","CM14","RM3","RM2","RM1","RM6","CM13","CM12","CM4","RM7","IG2","IG4","E11","E10","E9","SW13","SW6","SW10","SW3","SW11","SW8","RM18","RM16","RM14","CM11"]
friday = ["EC1","EC2","EC3","EC4","WC1A","WC1B","WC1E","WC1H","WC1N","WC1R","WC1V","WC1X","WC2A","WC2B","WC2E","WC2H","WC2R","E1","E2","NW1","SE1","SW1A","SW1E","SW1H","SW1P","SW1V","SW1W","SW1X","SW1Y","W1","WC1","WC2","W1B","W1C","W1D","W1F","W1G","W1H","W1J","W1K","W1S","W1T","W1U","W1W","E1W","CM4","CM5","CM11","CM12","CM13","CM14","CM15","CM16","RM1","RM2","RM3","RM4","RM5","RM6","RM7","RM8","RM9","RM10","RM11","RM12","RM13","RM14","RM15","RM16","RM17","RM18","RM19","RM20","SE16","SE17","SW10","SS14","SS15","SS16","SS17","E3","E4","E5","E6","E7","E8","E9","E10","E11","E12","E13","E14","E15","E16","E17","E18","E19","E20","SW8","SE11","SE3","SE4","SE5","SE13","SE14","SE15","N4","N5","N6","N7","N8","SW3","SW4","SW5","SW6","SW7","SW9","SW11","SW12","SW13","SW14","SW15","SW16","SW17","SW18","SW19","W2","NW2","NW3","SW1","EC1A","EC1M","EC1N","EC1R","EC1V","EC1Y","EC2A","EC2M","EC2N","EC2R","EC2V","EC2Y","EC3A","EC3M","EC3N","EC3R","EC3V","EC4A","EC4M","EC4N","EC4R","EC4V","EC4Y","CM1","CM2","CM3","IG1","IG2","IG3","IG5","IG6","IG11","N15","N16","N19","NW5","NW6","NW8","W4","W6","W8","W9","W10","W11","W12","SE7","SE8","SE21","SE22","SE24","SE27","SE28"]
saturday = ["CM2","CM4","CM15","CM11","CM12","CM13","CM14","CM15","EC3M","EC3N","EC3R","NW2","NW3","NW4","NW6","NW7","NW8","NW9","NW10","NW11","IG2","IG4","RM3","RM6","RM7","SS12","SS13","SS14","SS15","SE1"]


charge = ["NW1","SW10","E3","E4","E5","E6","E7","E8","E9","E10","E11","E12","E13","E14","E15","E16","E17","E18","SE3","SE4","SE5","SE13","SE14","SE15","SE18","N4","N5","N6","N7","N8","E4","SW3","SW4","SW5","SW6","SW7","SW9","SW10","SW11","SW12","SW13","SW14","SW15","SW16","SW17","SW18","SW19","W2","NW2","NW3","NW5","TW1","RM15","N15","N16","N19","NW5","NW6","W4","W6","W8","W9","W10","W11","W12","SE7","SE8","SE21","SE22","SE24"]
chargeAmt = 7.50


def postCodeSorter(day, zones, array):
    for postcode in array:
        found = False
        for i in range(len(zones)):
            if (zones[i][0] == postcode):
                zones[i][1].append(day)
                found = True
        if (found == False):
            if (charge.__contains__(postcode)):
                zones.append([postcode, [day], chargeAmt])
            else:
                zones.append([postcode, [day], 0])
    return zones        

def zoneCreater(zones):
    newZones = []
    counter = 0
    for i in range(len(zones)):
        found = False
        for z in range(len(newZones)):
            if (newZones[z][2] == zones[i][1]):
                if newZones[z][3] == zones[i][2]:
                    newZones[z][1].append(zones[i][0])
        if (found == False):
            counter += 1
            newZones.append([counter, [zones[i][0]], zones[i][1], zones[i][2]])
    return newZones

def zone_delivery_days():
    zone_delivery_days = [0,1,2,3,4,5,6]
    return    
        
def suttonsilver_bobtailmanagment_zones(zones):
    #Days that require a delivery should not be included in the list so keys need to be swaped.
    
    tableHeaders = ["zones_id", "zone_name", "price_default", "zone_times", "status", "zone_delivery_days"]
    
    return

def suttonsilver_bobtailmanagment_postcodes():
    tableHeaders = ["postcodes_id", "zone_id", "postcode_range_start", "postcode_range_end", "postcode_name", "status"]
    return 

def __main__():
    zones = []
    zones = postCodeSorter("1", zones, monday)
    zones = postCodeSorter("2", zones, tuesday)
    zones = postCodeSorter("3", zones, wednesday)
    zones = postCodeSorter("4", zones, thursday)
    zones = postCodeSorter("5", zones, friday)
    zones = postCodeSorter("6", zones, saturday)

    

__main__()