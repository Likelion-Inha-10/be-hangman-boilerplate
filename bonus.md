주소변경하기
---
1. hosts 파일로 접근 (터미널에 입력)
<pre><code>jeongsc@jeongsecBookAir ~ % sudo vim /private/etc/hosts 
</code></pre>

2. localhost 이름 변경 (localhost -> my-domain.com)

## MAC

<pre><code> 
    ##
    # Host Database
    #
    # localhost is used to configure the loopback interface
    # when the system is booting.  Do not change this entry.
    ##
    127.0.0.1       localhost
    255.255.255.255 broadcasthost
    ::1             localhost
    </pre></code>
    
<pre><code> 
    ##
    # Host Database
    #
    # localhost is used to configure the loopback interface
    # when the system is booting.  Do not change this entry.
    ##
    127.0.0.1       my-domain.com
    255.255.255.255 broadcasthost
    ::1             localhost
    </pre></code>
    
## 윈도우
 
 - 윈도우에서 DNS 를 생성시에 아래와 같은 과정을 따랐습니다.
 
### 1. IP 주소를 도메인 주소(DNS) 로 바꾸기 위해 Host 파일을 수정하기 
 - 1-1. 아래처럼 host 파일이 위치한 경로인 C:\Windows\System32\drivers\etc 경로로 이동했습니다.

![image](https://user-images.githubusercontent.com/88240193/177096372-8e54249b-4a79-4cdd-97ec-81a6bd925d01.png)

- 1-2. host 파일을 텍스트 파일(txt) 로 열어서 아래와 같이 127.0.0.1 IP주소에 대한 도메인 주소를 새롭게 등록했습니다.

![image](https://user-images.githubusercontent.com/88240193/177097001-12cd16fe-32a9-4d01-9213-2c55f2dbabb4.png)

- 1-3. 그러나 "관리자 권한이 필요" 하기 때문에 엑세스 자체가 거부 되어서, hosts 파일 관리자 권한으로 수정할 방법이 필요 했습니다.
-  ( 이거 안되서 해결하는데 몇시간동안 고생했습니다,,, ^_^)

### 2. 관리자 권한으로 Host 파일을 수정하기

- hosts 파일에 대한 속성을 변경했습니다. 
- User 그룹을 선택후, 모든 권한을 허용함
![image](https://user-images.githubusercontent.com/88240193/177098562-f0098642-1d43-4f17-be60-70dad6f6b43a.png)

- 그 뒤로 host 파일을 열고 원하는 도메인 주소(my-domain.com) 을 등록했다.

#### 3. 실행결과

![image](https://user-images.githubusercontent.com/88240193/177099184-651a61c3-7e5b-4f4b-9c45-3a5fab6db5be.png)



---
 
 

3. settings.py 수정 (ALLOWED_HOSTS)
<pre><code>ALLOWED_HOSTS = [
    #기본값은 'localhost', '127.0.0.1', '[::1]'
    
    'my-domain.com',
    '127.0.0.1',
]</code></pre>

4. 결과
<img width="609" alt="스크린샷 2022-07-04 오후 2 14 50" src="https://user-images.githubusercontent.com/96401830/177086010-6164842b-0571-42da-b639-0f045cbcac4c.png">

char 입력값 제한하기 (영문인 1글자만 받도록, 이외에는 400 Bad Request 나타내기)
---
1. 코드입력
<pre><code>from rest_framework.exceptions import ValidationError
..

if len(hm.ans) > 1 or 'z' < hm.ans or hm.ans < 'a':
            raise ValidationError</code></pre>
            
2. 결과 (여러 글자일 때)
<img width="729" alt="스크린샷 2022-07-04 오후 2 37 53" src="https://user-images.githubusercontent.com/96401830/177088668-87994d1a-cb29-4163-9dab-5d109fd1e2f2.png">

3. 결과 (숫자일 때)
<img width="722" alt="스크린샷 2022-07-04 오후 2 38 34" src="https://user-images.githubusercontent.com/96401830/177088846-59c804ae-f543-43d3-9480-f261921fee6d.png">

4. 결과 (한글일 때)
<img width="719" alt="스크린샷 2022-07-04 오후 2 45 51" src="https://user-images.githubusercontent.com/96401830/177089141-cb5ea5aa-b6d3-41b1-94db-1a80db89080f.png">

소문자로 통일하기
---
1. 코드입력
<pre><code>hm.word = str(request.data["word"]).lower()</code></pre>

2. 결과
<img width="412" alt="스크린샷 2022-07-04 오후 2 50 54" src="https://user-images.githubusercontent.com/96401830/177089647-c02267cf-e1c8-46d8-b9b0-3f23fe89fd74.png">

API
---
<img width="414" alt="스크린샷 2022-07-04 오후 1 24 43" src="https://user-images.githubusercontent.com/96401830/177083470-be669270-75cd-4a49-acd2-fac860bb20b1.png">
