주소변경하기
---
1. hosts 파일로 접근 (터미널에 입력)
<pre><code>jeongsc@jeongsecBookAir ~ % sudo vim /private/etc/hosts 
</code></pre>

2. localhost 이름 변경 (localhost -> my-domain.com)
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
