# 블루투스로 PEP를 검색해서 프로필을 던져주는 서버

# 가정
1. Application이 PEP와 페어링이 되어있다.
2. Application이 PEP 근처에 있다.

# 과정
1. User가 Application에서 페어링 된 PEP 장치를 선택한다.
2. Bluetooth Server는 accept를 기다린다.
3. accept가 되면 resources/profile/pep.profile을 읽어서 그대로 보낸다.
4. Application은 PEP 프로필을 받고나면 서버에 close() 명령을 내린다.
5. Bluetooth Server는 close()를 받으면 연결을 종료하고 다시 accept를 기다린다.

