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

Tuy nhiên, đối với thư viện ZMQ, các sockets được thiết kế khác so với các socket truyền thống.

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
- Trong ZMQ hỗ trợ 4 loại message patterns:

### 3.1. PAIR
- Socket thuộc loại PAIR khá tương đồng với các socket thông thường, ngoại trừ việc nó chỉ cho phép kết nối giữa 2 máy (strict one-to-one).
- Thường được dùng trong trường hợp ta chỉ muốn làm việc với 2 máy.
- *Xem thêm ví dụ 03-01-PAIR cho client và server*.

### 3.2. Client-Server
- Là một trong những message pattern đơn giản nhất, client sẽ gửi request (REQ) đến server và server sẽ gửi phản hổi (REP) về cho client.
- Khác với pattern PAIR, một client có thể connect đến nhiều server. Lúc này các requests sẽ được gửi xen kẽ hoặc chia đều đến các server.
- socket.zmq.REQ sẽ block các request sau cho đến khi nhận được phản hồi cho request hiện tại.
- socket.zmd.REP sẽ block các reply cho tới khi nó nhận được request
- *Xem thêm ví dụ 03-02-REQ-REP cho client và server*

### 3.3. Publish-Subscribe
- Là một trong những pattern phổ biến khác, trong đó người gửi message (publisher) không lập trình để gửi message đến một người nhận cụ thể nào (subscriber). Thay vào đó message sẽ được broadcast đến tất cả các subscriber.
- 1 publisher có thể có nhiều subscriber, ngược lại 1 subscriber cũng có thể nhận thông tin từ nhiều publisher (giống YouTube).
- Là kiểu kết nối many-to-many
- *Xem ví dụ 03-03-SUB-PUB cho client và server*
- Chạy thử hệ thống gồm 2 subscriber và 2 publisher
```
python 03-03-SUB-PUB-server.py 5546 # initialize a server on port 5546
python 03-03-SUB-PUB-server.py 5556 # initialize a server on port 5556
python 03-03-SUB-PUB-client.py 5546 5556 # initialize the first subscriber
python 03-03-SUB-PUB-client.py 5546 5556 # initialize the second subscriber
```

### 3.4. Push-Pull
- Push pull socket cho phép phân tán messages cho một số lượng các worker, để hình thành 1 pipeline.
- Push socket sẽ chia đều các messages cho các pull socket
- Điều này tương tự như mô hình producer/consumer, tuy nhiên kết quả trả về bởi consumer sẽ khong được gửi ngược trở về producer (upstream), mà được gửi tiếp xuống một node khác (downstream).
- *Xem ví dụ 03-04*, xây dựng 1 hệ thống gồm 3 node, producer, consumer và result collector. Data sẽ đi theo trình tự producer -> consumer -> result collector.

- Note: the result collector and consumers needed to be started before the producer  

```
python 03-04-result-collector.py
python 03-04-consumer.py
python 03-04-consumer.py
python 03-04-producer.py
```