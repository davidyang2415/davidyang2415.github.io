# Java专题之网络
--------------------------------------

## BIO,基础IO通信模型
- Socket和ServerSocket实现
- 一般采用One connection one thread，或socket pool

## NIO通信模型
- 采用Reactor模式
- 使用Channel(SocketChannel和ServerSocketChannel)和Selector

## AIO通信模型
- 采用Proactor模式