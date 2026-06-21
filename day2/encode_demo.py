import cantools
import can

db = cantools.database.load_file("vehicle.dbc")

msg = db.get_message_by_name("EngineData")

data = msg.encode({
    "RPM": 3000,
    "Gear": 3
})

print("Encoded bytes:", data)

bus = can.Bus(interface="socketcan", channel="vcan0")
msg_obj = can.Message(
    arbitration_id=msg.frame_id,
    data=data,
    is_extended_id=False
)

bus.send(msg_obj)
print("✅ Sent: RPM=3000, Gear=3")
