# 尝试在AI的帮助学习车载测试
## Day 1 · CAN 环境与虚拟总线验证

安装 Python CAN 开发环境，启动虚拟 CAN 总线（vcan0）。  
在两个终端中分别发送和接收 CAN 帧，验证总线通信正常，确保数据可被观测与复现。

---

## Day 2 · DBC 文件与信号编解码

理解 DBC 文件的作用，编写最小 `vehicle.dbc`，定义 RPM 与 Gear 信号。  
基于 `python-can` 与 `cantools` 实现 DBC 驱动的信号编码与解码：  
将物理值 `8000 rpm` 编码为 CAN 帧，再从 CAN 帧成功解码回 `8000 rpm`。

---

## Day 3 · 虚拟 Engine ECU 与时序注入

实现每 100ms 自动发送一帧 CAN 数据的 Python 脚本。  
RPM 随时间变化，模拟加速与减速过程；Gear 根据 RPM 自动切换，模拟真实换挡逻辑。  

构建虚拟 Engine ECU：  
- 使用 SocketCAN 驱动虚拟总线  
- 支持动态信号注入  
- 实现基于 RPM 的换挡状态机  

所有行为可通过日志观测，具备可复现性与调试能力。
