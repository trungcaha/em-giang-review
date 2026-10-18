import time, json, subprocess, os, datetime, glob, re

os.environ["POSTIZ_API_URL"] = "https://mlabai.uk/api"
os.environ["POSTIZ_API_KEY"] = subprocess.run(
    ["powershell", "-NoProfile", "-c", "[Environment]::GetEnvironmentVariable('POSTIZ_API_KEY','User')"],
    capture_output=True, text=True).stdout.strip()
FB = "cmtrkr9c10001r07vahsxtm3g"  # Căn Bếp Nhỏ
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos", "giot-lanh")
DONE = os.path.join(DIR, "_posted.json")
COMMENT = "Bộ 3 Gội Xả Xịt bưởi - Chăm sóc toàn diện cho tóc khỏe mạnh và mềm mượt Giọt Lành\n\nhttps://s.shopee.vn/7VGi0zRRhq"
HOOKS = [
    "Tóc xù rối, khô xơ như rơm, chải mãi không vào nếp? 😩",
    "Gội xong tóc vẫn bết, rụng cả nắm mỗi lần chải? 😰",
    "Tóc khô xơ chẻ ngọn, ra đường gió thổi là rối bù? 😣",
    "Muốn tóc xoăn xù hóa suôn mềm, thơm dịu cả ngày? 🌿",
]
BODY = ("\n\nBí quyết là dầu gội dừa oliu Giọt Lành:\n"
        "✅ Gội sạch dịu nhẹ, giảm gãy rụng\n✅ Xả mềm, gỡ rối ngay lập tức\n"
        "✅ Tóc bóng mượt, thơm lâu\n\n"
        "👇 Link sản phẩm ở phần bình luận\n\n#giotlanh #duongtoc #duaoliu #tockhoe #canbepnho")

done = json.load(open(DONE, encoding="utf-8")) if os.path.exists(DONE) else {}
start = datetime.datetime.now(datetime.UTC).replace(tzinfo=None).replace(second=0, microsecond=0) + datetime.timedelta(minutes=5)
if done:
    start = datetime.datetime.strptime(max(done.values()), "%Y-%m-%dT%H:%M:00Z") + datetime.timedelta(hours=3)
vids = [v for v in sorted(glob.glob(os.path.join(DIR, "*.mp4")), key=os.path.getmtime) if os.path.basename(v) not in done]
for n, video in enumerate(vids):
    while True:
        up = subprocess.run(["postiz.cmd", "upload", video], capture_output=True, text=True, encoding="utf-8")
        try:
            js = json.loads(up.stdout[up.stdout.index("{"):])
            break
        except ValueError:
            print("upload retry", (up.stdout + up.stderr)[:80].replace("\n", " "), flush=True)
            time.sleep(120)
    when = (start + datetime.timedelta(hours=3 * n)).strftime("%Y-%m-%dT%H:%M:00Z")
    post = {"type": "schedule", "date": when, "shortLink": False, "tags": [], "posts": [{
        "integration": {"id": FB},
        "value": [
            {"content": HOOKS[n % len(HOOKS)] + BODY, "image": [{"id": js["id"], "path": js["path"]}]},
            {"content": COMMENT, "image": [], "delay": 1},
        ],
        "settings": {"__type": "facebook", "post_type": "reel", "commentStrategy": "root"}}]}
    fn = os.path.join(DIR, "_post.json")
    json.dump(post, open(fn, "w", encoding="utf-8"), ensure_ascii=False)
    for _ in range(100):
        r = subprocess.run(["postiz.cmd", "posts:create", "--json", fn], capture_output=True, text=True, encoding="utf-8")
        if "Failed" not in r.stdout + r.stderr and "<html" not in r.stdout:
            break
        time.sleep(120)
    ok = r.returncode == 0 and "rror" not in r.stdout + r.stderr
    print(n + 1, when, os.path.basename(video)[-30:], "OK" if ok else r.stdout[-200:] + r.stderr[-200:], flush=True)
    if ok:
        done[os.path.basename(video)] = when
        json.dump(done, open(DONE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
