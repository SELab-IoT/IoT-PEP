* 주의사항
Thonny에서 파이썬 실행시키지 말것
서버 실행시에 server.sh를 이용하고 
만약 필요하다면 bluetooth-server.sh, http-server.sh 따로 작성해서 이 디렉토리에서 사용할 것
(resources 읽을 때 상대경로로 읽기 때문에 문제가 발생한다.)

* Notice
Don't Run PEP using Thonny.
When you start Server, use server.sh
and If you need, you can make bluetooth-server.sh and http-server.sh for each server in THIS directory.
(Because, python reads resources in canonical path, it cause problem.)

* 숙지
bluetooth-server는 오로지 Application과의 페어링(및 프로필 제공)을 위해 계속 돌아가는 서버이며 
Device와는 아무 연관이 없다.
Device와 관련된 블루투스 기능은 http-server/service/device_manager.py에 구현되어있다.

* You shoud Know
bluetooth-server is only for Pairing with App(and give PEP profile to App), not related with Device.
Bluetooth commnumcation function for Device is implemented in http-server/service/device_manager.py.

* 숙지2
인테그레이션 과정에서 위키에 정의된 프로토콜과 다소 달라진 부분이 존재한다.
차후 위키 수정 예정.

* You should know 2.
When I doing integration App<->PEP<->PlatformManager, I change some protocol but it's not reflected on Wiki... I'll fix it later.
