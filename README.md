day1 安装环境，启动虚拟总线，验证两个终端发送和查看数据
day2 理解DBC文件的作用，写一个最小 vehicle.dbc，用 Python 把“物理值（8000rpm）”编码成 CAN 帧，再把它解码回“8000rpm”
	基于 python-can + cantools 实现 DBC 驱动的信号编码与解码，支持 RPM / Gear 信号。
day3 写一个每 100ms​ 自动发送一帧 CAN 的Python 脚本，RPM 随时间变化（模拟加速 / 减速），Gear 随 RPM 变化（模拟换挡逻辑），日志可观测、可复现
	实现虚拟 Engine ECU，支持 RPM/Gear 动态变化与时序注入。
	我构建了一个虚拟 ECU，通过 Python 驱动 SocketCAN，按 100ms 周期注入动态信号，并实现了基于 RPM 的换挡状态机。