import currentreader

reader = currentreader.CurrentReader(voltage=230)

reader.readChannel(chan=0,ampFactor=0.0026,ampExponent=1.0206,ampMinimum=0.020)
print("Power: {0}".format(reader.lastPower()))
reader.readChannel(chan=1,ampFactor=0.0026,ampExponent=1.0206,ampMinimum=0.020)
print("Power: {0}".format(reader.lastPower()))
#reader.readChannel(chan=2,ampFactor=0.0026,ampExponent=1.0206,ampMinimum=0.020)
#print("Power: {0}".format(reader.lastPower()))
#reader.readChannel(chan=3,ampFactor=0.0026,ampExponent=1.0206,ampMinimum=0.020)
#print("Power: {0}".format(reader.lastPower()))
