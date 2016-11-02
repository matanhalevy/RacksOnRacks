import csv
import json
import xml.etree.cElementTree as ADD
import xml.etree.ElementTree as ET
import urllib2



racks = []

class BikeRack:

    def __init__(self, address, number, lat, lon, skytrain):
        self.address = address
        self.number = number
        self.lat = lat
        self.lon = lon
        self.skytrain = skytrain

addresses = ADD.Element("addresses")


def makexml(addr, numracks, lat, lon, skytrain):
        address = ADD.SubElement(addresses, "address")
        ADD.SubElement(address, "name").text = addr
        ADD.SubElement(address, "number").text = numracks
        ADD.SubElement(address, "lat").text = str(lat)
        ADD.SubElement(address, "lon").text = str(lon)
        ADD.SubElement(address, "skytrain").text = skytrain

        return

def makexmlfromcvs():
    with open('bikeracktest.csv', 'rb') as csvfile:
        z = 0 # for testing
        m = 0
        urlbase = "https://maps.googleapis.com/maps/api/geocode/json?address="
        key = ",+Vancouver,+BC&key=AIzaSyArAbpS-93zrpjYALdVSJ7H0ZJN9NA6mjg"
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            m += 1
            i = 0
            if (m > 2):
                address = row[0] + " " + row[1] + " " + row[2]            # address
                numrack = row[5]                                          # number of bike racks
                side = row[2]
                skytrain = row[3]                                         # skytrain station

                middle = row[0] + "+" + row[1] + "+" + row[2]             # making url for google api
                middle1 = middle.replace(" ", "+")
                url = urlbase + middle1 + key

                data = json.load(urllib2.urlopen(url))                    # returns json response for given url

                lat = data['results'][0]['geometry']['location']['lat']     # gets lat from json
                lon = data['results'][0]['geometry']['location']['lng']     # gets lon from json



                # got an error for 1148 Homer Street when trying to cache whole thing, not sure why
                makexml(address,numrack,lat,lon,skytrain)

    tree = ADD.ElementTree(addresses)
    tree.write("file.xml")

def parsexml():
    tree = ET.parse('storage.xml')
    root = tree.getroot()
    for address in root.findall('address'):
      name = address.find('name').text
      number = address.find('number').text
      lat = address.find('lat').text
      lon = address.find('lon').text
      # test = float(lat) + float(lon)
      skytrain = address.find('skytrain').text
      br = BikeRack(name, number, float(lat), float(lon), skytrain)
      racks.append(br)

     # print racks[i].address
     # print racks[i].number
     # print racks[i].lat
     # print racks[i].lon
     # print racks[i].skytrain
     # i += 1


def main():

   # makexmlfromcvs()
    parsexml()

if __name__ == "__main__":
    main()




