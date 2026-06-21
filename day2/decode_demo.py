import cantools
import can

db = cantools.database.load_file("vehicle.dbc")
msg = db.get_message_by_name("EngineData")

bus = can.Bus(interface="socketcan", channel="vcan0")

for m in bus:
    if m.arbitration_id == msg.frame_id:
        decoded = msg.decode(m.data)
        print("Decoded:", decoded)
        break
