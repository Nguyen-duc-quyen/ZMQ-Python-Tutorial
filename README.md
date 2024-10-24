# Hướng dẫn sử dụng thư viện ZMQ

## 1. Socket là gì?

- Socket là cổng giao tiếp giữa các ứng dụng trên mạng.
- Cho phép các thiết bị trao đổi thông tin với nhau thông qua một kết nối đã định sẵn.
- Thường được sử dụng với framework client-server. Trong đó server sẽ thực hiện một số chức năng yêu cầu từ client

**Phân loại Socket - 4 loại:**
1. Stream Socket: Sử dụng giao thức TCP, trong môi trường mạng được đảm bảo. Nghĩa là nếu gửi 3 gói tin A, B, C thì nó sẽ tới đúng theo thứ tự A, B, C. Nếu không thì phía client sẽ nhận được thông báo lỗi.
2. Datagram Socket: Sử dụng giao thức UDP, không đảm bảo thứ tự như Stream Socket
3. Raw Socket
4. Sequenced Packet Socket

## 2. PyZMQ library

### 2.1 PyZMQ context:
- Trước khi sử dụng bất kì API nào của thư viện PyZMQ ta cần khởi tạo ZMQ context.
- Context là một object chứa tất cả các socket của một process nào đó. 
- Context trong ZMQ là "thread-safe" tức là nó có thể được chia sẻ giữa nhiều threads. Socket ngược lại không có "thread-safe"

```
import zmq
import time
context = zmq.Context()
```

### 2.2 PyZMQ socket:
- Trong ZMQ, socket được tạo ra từ context

```
socket = context.socket(zmq.REP)
```
- Socket trong ZMQ bao gồm một số kiểu nhất định, mỗi kiểu cho phép giao tiếp theo 1 pattern nhất định.
- Type của socket cần được định nghĩa ngay khi khởi tạo

## 3. Messaging Patterns
- Trong các hệ thóng phân tán, các phần khác nhau giao tiếp với nhau tạo thành một **network topology**
- Mỗi pattern trong ZMQ định nghĩa các ràng buộc trong network topology đó, quy định cách hệ thống được kết nối với nhau và flow của dữ liệu giữa các phần của hệ thống.
- Trong ZMQ hỗ trợ 4 loại message patterns

### 3.1. PAIR

### 3.2. Client-Server

### 3.3. Publish-Subscribe

### 3.4. Push-Pull