import smtplib
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

QUOTES = [
    "오늘 하루도 당신은 충분히 잘하고 있습니다.",
    "작은 걸음이라도 앞으로 나아가는 것이 중요합니다.",
    "포기하지 마세요. 지금 이 순간이 가장 힘들 때입니다.",
    "당신이 생각하는 것보다 훨씬 더 강한 사람입니다.",
    "오늘의 노력이 내일의 나를 만듭니다.",
    "실패는 성공으로 가는 과정입니다. 멈추지 마세요.",
    "매일 조금씩 성장하는 것으로 충분합니다.",
    "힘든 길 끝에는 반드시 빛이 있습니다.",
    "당신의 꿈은 충분히 이룰 수 있는 것입니다.",
    "오늘 하루도 최선을 다한 당신을 응원합니다.",
    "어제보다 오늘 조금 더 나아졌다면 그것으로 충분합니다.",
    "자신을 믿는 것이 모든 변화의 시작입니다.",
    "완벽하지 않아도 괜찮습니다. 나아가는 것이 중요합니다.",
    "당신의 존재 자체가 이미 충분한 가치입니다.",
    "오늘 하루도 버텨낸 당신, 정말 대단합니다.",
    "지금 이 순간에도 당신은 성장하고 있습니다.",
    "어려운 상황일수록 더 강해지는 것이 당신입니다.",
    "꾸준함이 재능을 이깁니다. 오늘도 한 걸음씩.",
    "남과 비교하지 마세요. 어제의 나와 비교하세요.",
    "긍정적인 생각이 긍정적인 하루를 만듭니다.",
    "당신이 걷는 길이 곧 당신만의 답입니다.",
    "오늘의 도전이 내일의 자신감이 됩니다.",
    "쉬어가도 괜찮습니다. 포기만 하지 마세요.",
    "작은 성취들이 모여 큰 성공을 만듭니다.",
    "당신의 노력은 반드시 결실을 맺습니다.",
    "오늘 하루도 당신 곁에서 응원하고 있습니다.",
    "두려움을 느끼면서도 행동하는 것이 용기입니다.",
    "지금 시작하는 것이 가장 완벽한 타이밍입니다.",
    "당신의 이야기는 아직 끝나지 않았습니다.",
    "오늘도 살아있다는 것만으로 충분히 감사한 일입니다.",
]


def send_email(quote):
    sender = os.environ["GMAIL_USER"]
    password = os.environ["GMAIL_APP_PASSWORD"]
    receiver = os.environ["RECEIVER_EMAIL"]

    today = datetime.now().strftime("%Y년 %m월 %d일")

    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = f"☀️ 오늘의 명언 - {today}"

    body = f"""\
안녕하세요! 오늘의 명언을 전해드립니다 😊

✨ {quote}

오늘 하루도 화이팅입니다! 💪
"""
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())


if __name__ == "__main__":
    quote = random.choice(QUOTES)
    send_email(quote)
    print(f"전송 완료: {quote}")
