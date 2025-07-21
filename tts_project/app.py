import os
import base64
from flask import Flask, request, render_template, send_from_directory, flash, url_for
from gtts import gTTS
from datetime import datetime

# Flask 앱 인스턴스 생성
app = Flask(__name__,
            template_folder='david/templates',  # 템플릿 파일 경로 지정
            static_folder='david/static')      # 정적 파일 (이미지 등) 경로 지정
app.secret_key = 'your_super_secret_key' # flash 메시지를 위한 비밀 키 (아무거나 설정해도 됨)

# 지원하는 언어 목록
SUPPORTED_LANGS = {'ko', 'en', 'ja', 'es'}

# 로그 파일 경로
LOG_FILE = 'input_log.txt'

# 80번 포트 고정
PORT = 80

# 루트 URL ('/')에 대한 라우트 정의
@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    audio_base64 = None
    download_link = None # 보너스 과제: 다운로드 링크 변수 추가

    if request.method == 'POST':
        input_text = request.form['input_text']
        lang = request.form['lang']

        # 보너스 과제: 언어 유효성 검증
        if lang not in SUPPORTED_LANGS:
            error = "지원하지 않는 언어입니다. ko, en, ja, es 중 하나를 선택해주세요."
            # 유효하지 않은 언어 선택 시 로그는 남기지 않음
            return render_template('index.html', error=error)

        # 사용자의 입력 내역을 로그 파일로 저장 (보너스 과제)
        try:
            with open(LOG_FILE, 'a', encoding='utf-8') as f:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"[{timestamp}] Text: '{input_text}', Language: '{lang}'\n")
        except IOError as e:
            print(f"로그 파일 저장 중 오류 발생: {e}")
            # 사용자가 볼 오류 메시지는 아니므로 print로만 처리

        if not input_text.strip(): # strip()으로 공백만 있는 경우도 체크
            error = "텍스트를 입력해주세요!"
        else:
            try:
                # gTTS (Google Text-to-Speech) 객체 생성
                # slow=False는 음성 속도를 빠르게 합니다.
                tts = gTTS(text=input_text, lang=lang, slow=False)
                
                # 음성 데이터를 메모리에 저장 (파일로 저장하지 않음)
                # BytesIO를 사용하면 파일을 실제로 생성하지 않고 메모리에서 다룰 수 있습니다.
                from io import BytesIO
                mp3_fp = BytesIO()
                tts.write_to_fp(mp3_fp)
                mp3_fp.seek(0) # 스트림의 시작으로 커서 이동

                # base64 인코딩
                # 웹에서 오디오를 재생하기 위해 binary 데이터를 base64 문자열로 변환
                audio_base64 = base64.b64encode(mp3_fp.read()).decode('utf-8')

                # 보너스 과제: MP3 다운로드 링크 제공
                # 여기서는 바로 base64 인코딩된 데이터를 넘겨주므로, 실제 파일은 아니지만
                # 클라이언트 측에서 base64 데이터를 파일로 저장할 수 있도록 유도
                # HTML <audio> 태그의 src에 직접 base64 데이터를 넣었기 때문에
                # 별도의 다운로드 라우트 없이도 브라우저는 base64 데이터를 파일처럼 다룰 수 있습니다.
                # 그러나 명시적인 다운로드 링크를 위해 data URI를 사용
                download_link = f"data:audio/mpeg;base64,{audio_base64}"

            except Exception as e:
                # gTTS 변환 실패 시 예외 처리
                error = f"음성 변환 중 오류가 발생했습니다: {e}"
                # 특정 에러 메시지는 gTTS 라이브러리에 따라 다를 수 있음
                # 예: 언어 지원 오류, 네트워크 오류 등

    # GET 요청이거나 POST 요청 처리 후 결과를 렌더링
    return render_template('index.html', error=error, audio=audio_base64, download_link=download_link)

# 서버 실행 (디버그 모드 활성화)
if __name__ == '__main__':
    # 80번 포트로 실행 (관리자 권한 필요할 수 있음)
    app.run(host='0.0.0.0', port=PORT, debug=True)
    # debug=True는 개발 중 코드 변경 시 서버가 자동으로 재시작되게 합니다.
    # 실제 운영 환경에서는 debug=False로 설정해야 합니다.