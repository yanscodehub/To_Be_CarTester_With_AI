import time
import math
import cantools
import can

db = cantools.database.load_file("vehicle.dbc")
msg = db.get_message_by_name("EngineData")

bus = can.Bus(interface="socketcan", channel="vcan0")

rpm = 800          # 初始转速
gear = 1           # 初始挡位
delta = 100        # 每次增加量
direction = 1      # 1=加速, -1=减速

print("🚗 Virtual Engine ECU started...")

try:
    while True:
        # 编码数据
        data = msg.encode({
            "RPM": rpm,
            "Gear": gear
        })

        # 发送
        bus.send(can.Message(
            arbitration_id=msg.frame_id,
            data=data,
            is_extended_id=False
        ))

        print(f"Sent -> RPM: {rpm}, Gear: {gear}")

        # 简单换挡逻辑
        if rpm >= 4000 and gear < 6:
            gear += 1
            rpm = 2000
        elif rpm <= 1000 and gear > 1:
            gear -= 1
            rpm = 3000

        # 模拟加速 / 减速
        rpm += delta * direction

        if rpm >= 5000:
            direction = -1
        elif rpm <= 800:
            direction = 1

        time.sleep(0.1)  # 100 ms

except KeyboardInterrupt:
    print("ECU stopped.")
