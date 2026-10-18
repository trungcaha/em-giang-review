# -*- coding: utf-8 -*-
import json, datetime as dt
import data as D


def _d(x):
    return x.strftime("%d/%m") if isinstance(x, (dt.date, dt.datetime)) else x


def payload():
    prods = D.load_products()
    return dict(
        project={**D.PROJECT, "start": _d(D.PROJECT["start"]), "today": D.PROJECT["today"].isoformat()},
        channel=D.CHANNEL, pillars=D.PILLARS, maxDay=D.MAX_DAY, subPrefix=D.SUB_PREFIX,
        weeks=[{**w, "start": _d(w["start"]), "end": _d(w["end"]), "startIso": w["start"].isoformat()} for w in D.WEEKS],
        phases=D.PHASES,
        products=prods,
        ideas=[dict(pl=i[0], type=i[1], title=i[2], hook=i[3], scene=i[4], sp=i[5]) for i in D.IDEAS],
        roles=D.ROLES, capacity=D.CAPACITY,
        sop=[dict(n=s[0], task=s[1], when=s[2], r=s[3], c=s[4], inp=s[5], out=s[6]) for s in D.SOP],
        raci=D.RACI, raciRoles=D.RACI_ROLES,
        qc=D.QC_CHECK,
        rhythm=[dict(t=x[0], task=x[1], who=x[2], note=x[3]) for x in D.DAILY_RHYTHM],
        rituals=[dict(when=x[0], what=x[1], who=x[2]) for x in D.RITUALS],
        slots=[dict(t=x[0], type=x[1], goal=x[2], prod=x[3]) for x in D.SLOTS],
        themes=[dict(day=x[0], theme=x[1], color=x[2], prod=x[3]) for x in D.WEEKDAY_THEMES],
        season=[dict(when=x[0], ev=x[1], dir=x[2]) for x in D.SEASON],
        kpi=[dict(m=x[0], where=x[1], th=x[2], act=x[3]) for x in D.KPI_RULES],
        risks=[dict(risk=x[0], lvl=x[1], fix=x[2], owner=x[3]) for x in D.RISKS],
        resources=[dict(name=x[0], path=x[1], use=x[2]) for x in D.RESOURCES],
        tasks=[dict(id=t[0], task=t[1], role=t[2], due=t[3].isoformat(), dueTxt=_d(t[3]), phase=t[4]) for t in D.TASKS],
        forecast=D.FORECAST,
        sources=D.SOURCES, sourceTypes=D.SOURCE_TYPES, sourceStatuses=D.SOURCE_STATUSES,
    )


HTML = r"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vận hành Chị Giang</title>
<style>
:root{
  --bg:#f6f7f9; --surface:#ffffff; --surface-2:#f0f3f6; --ink:#16202a; --ink-2:#4b5866; --ink-3:#7a8794;
  --line:#e2e7ec; --brand:#0f4c5c; --brand-ink:#ffffff; --accent:#e36414;
  --ok:#1f8a4c; --ok-bg:#e3f4ea; --warn:#b4610a; --warn-bg:#fdf1dc; --bad:#c0362c; --bad-bg:#fbe5e3;
  --t1:#2563eb; --t2:#db2777; --t3:#ea580c; --t4:#16a34a; --t5:#7c3aed;
  --radius:12px; --shadow:0 1px 2px rgba(16,24,40,.06),0 1px 3px rgba(16,24,40,.08);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0f1418; --surface:#171e24; --surface-2:#1f2830; --ink:#e7edf2; --ink-2:#aab6c1; --ink-3:#7f8c98;
    --line:#2a343d; --brand:#5fb3c4; --brand-ink:#0b1a1e; --accent:#ff8c42;
    --ok:#4cc584; --ok-bg:#163325; --warn:#f0a94b; --warn-bg:#3a2a12; --bad:#ff7b70; --bad-bg:#3d1c19;
    --t1:#6b9cff; --t2:#f472b6; --t3:#fb923c; --t4:#4ade80; --t5:#a78bfa;
    --shadow:none;
  }
}
:root[data-theme="dark"]{
  --bg:#0f1418; --surface:#171e24; --surface-2:#1f2830; --ink:#e7edf2; --ink-2:#aab6c1; --ink-3:#7f8c98;
  --line:#2a343d; --brand:#5fb3c4; --brand-ink:#0b1a1e; --accent:#ff8c42;
  --ok:#4cc584; --ok-bg:#163325; --warn:#f0a94b; --warn-bg:#3a2a12; --bad:#ff7b70; --bad-bg:#3d1c19;
  --t1:#6b9cff; --t2:#f472b6; --t3:#fb923c; --t4:#4ade80; --t5:#a78bfa;
  --shadow:none;
}
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--bg);color:var(--ink);font:15px/1.55 "Segoe UI",system-ui,-apple-system,Roboto,"Helvetica Neue",Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--brand)}
.wrap{max-width:1240px;margin:0 auto;padding:0 16px}
header.top{background:var(--brand);color:var(--brand-ink);padding:28px 0 22px}
header.top h1{margin:0 0 4px;font-size:28px;line-height:1.2;letter-spacing:-.01em}
header.top p{margin:0;opacity:.88}
.toprow{display:flex;justify-content:space-between;gap:16px;align-items:flex-start;flex-wrap:wrap}
.themebtn{background:transparent;border:1px solid currentColor;color:inherit;border-radius:999px;padding:6px 12px;cursor:pointer;font:inherit;font-size:13px;opacity:.9}
.stats{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;margin-top:20px}
.stat{background:rgba(255,255,255,.1);border-radius:10px;padding:10px 12px}
:root[data-theme="dark"] .stat{background:rgba(0,0,0,.12)}
.stat b{display:block;font-size:22px;line-height:1.2}
.stat span{font-size:12.5px;opacity:.85}
nav.tabs{position:sticky;top:0;z-index:5;background:var(--surface);border-bottom:1px solid var(--line)}
nav.tabs .wrap{display:flex;gap:2px;overflow-x:auto;scrollbar-width:none}
nav.tabs .wrap::-webkit-scrollbar{display:none}
nav.tabs button{flex:0 0 auto;border:0;background:none;color:var(--ink-2);font:inherit;font-size:14px;padding:13px 12px;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap}
nav.tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent);font-weight:600}
main{padding:22px 0 60px}
section.tab{display:none}
section.tab.on{display:block}
h2{font-size:21px;margin:0 0 4px;letter-spacing:-.01em}
h3{font-size:16px;margin:24px 0 10px}
.lead{color:var(--ink-2);margin:0 0 18px;max-width:820px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px}
.grid{display:grid;gap:14px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g5{grid-template-columns:repeat(5,minmax(0,1fr))}
.alerts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-bottom:22px}
.alert{border-left:4px solid var(--bad);background:var(--bad-bg);border-radius:10px;padding:12px 14px}
.alert.w{border-color:var(--warn);background:var(--warn-bg)}
.alert.o{border-color:var(--ok);background:var(--ok-bg)}
.alert b{display:block;margin-bottom:4px}
.alert p{margin:0;font-size:14px;color:var(--ink-2)}
.muted{color:var(--ink-3);font-size:13px}
.pill{display:inline-block;border-radius:999px;padding:2px 9px;font-size:12px;font-weight:600;background:var(--surface-2);color:var(--ink-2);white-space:nowrap}
.pill.A{background:var(--ok-bg);color:var(--ok)} .pill.B{background:var(--warn-bg);color:var(--warn)} .pill.C{background:var(--surface-2);color:var(--ink-3)}
.pill.bad{background:var(--bad-bg);color:var(--bad)}
.kdot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:baseline}
.chcard{border-top:4px solid var(--c);display:flex;flex-direction:column;gap:8px}
.chcard h4{margin:0;font-size:17px}
.chcard .code{font-weight:700;color:var(--c)}
.chcard ul{margin:0;padding-left:18px;font-size:14px}
.chcard .lbl{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-3);margin-top:4px}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{font-size:12.5px;background:var(--surface-2);border-radius:6px;padding:3px 8px}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:12.5px;color:var(--ink-3);font-weight:600;text-transform:uppercase;letter-spacing:.03em;background:var(--surface-2);position:sticky;top:0}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface)}
.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.ctr{text-align:center}
.heat td.cell{text-align:center;font-weight:600;font-variant-numeric:tabular-nums;min-width:44px}
.journey{display:flex;align-items:stretch;gap:8px;flex-wrap:wrap}
.jstep{flex:1 1 150px;border-radius:10px;padding:12px;border:1px solid var(--line);background:var(--surface);position:relative}
.jstep b{color:var(--c)}
.jarrow{align-self:center;color:var(--ink-3);font-size:20px}
.hub{margin-top:10px;border:2px dashed var(--k5);border-radius:10px;padding:10px 14px;font-size:14px}
.flow{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
.fstep{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px;position:relative}
.fstep .n{display:inline-flex;width:26px;height:26px;border-radius:50%;background:var(--brand);color:var(--brand-ink);align-items:center;justify-content:center;font-weight:700;font-size:13px;margin-bottom:6px}
.fstep b{display:block;margin-bottom:4px}
.fstep .who{font-size:12.5px;color:var(--accent);font-weight:600}
.fstep p{margin:6px 0 0;font-size:13px;color:var(--ink-2)}
.role{display:flex;flex-direction:column;gap:6px}
.role .head{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.role .cnt{font-size:24px;font-weight:700;color:var(--brand)}
.role p{margin:0;font-size:14px;color:var(--ink-2)}
.calc{display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;margin-bottom:14px}
.calc label{display:flex;flex-direction:column;font-size:13px;color:var(--ink-2);gap:4px}
.calc input,.filters input,.filters select{font:inherit;font-size:14px;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);min-width:0}
.calc input{width:110px}
.filters{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:12px}
.filters input{flex:1 1 220px}
.r-R{background:#cfe3ff;color:#123a75} .r-A{background:#ffd9a8;color:#6b3a00} .r-C{background:#e2f3fb;color:#14536b} .r-I{background:var(--surface-2);color:var(--ink-3)}
:root[data-theme="dark"] .r-R{background:#1d3557;color:#cfe3ff} :root[data-theme="dark"] .r-A{background:#4a3010;color:#ffd9a8} :root[data-theme="dark"] .r-C{background:#15333f;color:#bfe6f5}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .r-R{background:#1d3557;color:#cfe3ff}:root:not([data-theme="light"]) .r-A{background:#4a3010;color:#ffd9a8}:root:not([data-theme="light"]) .r-C{background:#15333f;color:#bfe6f5}}
.raci td.ctr{font-weight:700}
.check{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px solid var(--line)}
.check:last-child{border-bottom:0}
.check input{margin-top:4px;width:17px;height:17px;accent-color:var(--brand);flex:0 0 auto}
.check.done .t{text-decoration:line-through;color:var(--ink-3)}
.check .meta{font-size:12.5px;color:var(--ink-3)}
.overdue{color:var(--bad);font-weight:600}
.progress{height:8px;background:var(--surface-2);border-radius:999px;overflow:hidden;margin:6px 0 14px}
.progress i{display:block;height:100%;background:var(--ok);width:0;transition:width .25s}
.timeline{display:grid;grid-template-columns:110px 1fr;gap:0}
.timeline div{padding:8px 10px;border-bottom:1px solid var(--line);font-size:14px}
.timeline .t{font-weight:700;color:var(--brand);font-variant-numeric:tabular-nums}
.btn{display:inline-block;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:8px;padding:4px 10px;font-size:13px;cursor:pointer;text-decoration:none;white-space:nowrap;font:inherit;font-size:13px}
.btn:hover{border-color:var(--brand)}
.btn.pri{background:var(--brand);color:var(--brand-ink);border-color:var(--brand)}
.phase{display:grid;grid-template-columns:220px 1fr 1fr;gap:12px;padding:12px 0;border-bottom:1px solid var(--line)}
.phase:last-child{border-bottom:0}
.phase .gate{font-size:14px;color:var(--ink-2)}
.phase .gate::before{content:"Qua cửa: ";font-weight:600;color:var(--ink)}
svg text{fill:var(--ink-2);font-size:11px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:13px;color:var(--ink-2);margin-top:6px}
.small{font-size:13px}
.copied{color:var(--ok)!important;border-color:var(--ok)!important}
footer{color:var(--ink-3);font-size:13px;padding:20px 0 40px;border-top:1px solid var(--line)}
.formgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:8px 0 12px}
.formgrid label{display:flex;flex-direction:column;gap:4px;font-size:13px;color:var(--ink-2)}
.formgrid .full{grid-column:1/-1}
.formgrid input,.formgrid select,.formgrid textarea{font:inherit;font-size:14px;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);width:100%;min-width:0}
.formgrid textarea{resize:vertical}
.srcgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;align-items:start}
.src{display:flex;flex-direction:column;gap:8px;min-width:0}
.src-head{display:flex;flex-wrap:wrap;gap:6px;align-items:baseline}
.src p{margin:0;font-size:14px;overflow-wrap:anywhere}
.src-media{background:var(--surface-2);border-radius:10px;min-height:110px;display:flex;align-items:center;justify-content:center;overflow:hidden;text-align:center;padding:0}
.src-media .hint{padding:14px;font-size:13px;color:var(--ink-3)}
.src-media iframe{border:0;width:100%;display:block;background:#000}
.src-media iframe.tt{height:580px}
.src-media iframe.v{aspect-ratio:9/16;height:auto;max-height:620px}
.src-media iframe.h{aspect-ratio:16/9;height:auto}
.src-media iframe.post{height:520px;background:#fff}
.playbtn{font:inherit;font-weight:600;border:0;background:var(--brand);color:var(--brand-ink);border-radius:999px;padding:10px 18px;cursor:pointer;margin:20px}
.pill.plat-TikTok{background:#111;color:#fff}
.pill.plat-Facebook{background:#1877f2;color:#fff}
.pill.plat-YouTube{background:#d91c12;color:#fff}
.pill.plat-Instagram{background:#b82f7a;color:#fff}
.pill.st-new{background:var(--warn-bg);color:var(--warn)}
.pill.st-done{background:var(--ok-bg);color:var(--ok)}
.src-preview{margin:0 0 12px;max-width:340px}
.src-actions{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.src-actions select{font:inherit;font-size:13px;padding:4px 8px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.tag-local{font-size:11.5px;color:var(--accent);font-weight:600}
@media (max-width:1000px){.srcgrid{grid-template-columns:repeat(2,minmax(0,1fr))}.formgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:760px){.srcgrid{grid-template-columns:1fr}.formgrid{grid-template-columns:1fr}}

@media (max-width:1000px){.g5{grid-template-columns:repeat(2,minmax(0,1fr))}.flow{grid-template-columns:repeat(2,minmax(0,1fr))}.stats{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:760px){.g2,.g3,.alerts{grid-template-columns:1fr}.phase{grid-template-columns:1fr}.g5{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,minmax(0,1fr))}header.top h1{font-size:22px}.timeline{grid-template-columns:92px 1fr}}
@media (max-width:480px){.flow{grid-template-columns:1fr}}
@media print{nav.tabs,.themebtn{display:none}section.tab{display:block!important;page-break-before:always}}
</style>
</head>
<body>
<header class="top">
  <div class="wrap">
    <div class="toprow">
      <div>
        <h1 id="pname"></h1>
        <p id="psub"></p>
      </div>
      <button class="themebtn" id="themebtn" type="button">Giao diện sáng / tối</button>
    </div>
    <div class="stats" id="stats"></div>
  </div>
</header>
<nav class="tabs" aria-label="Mục"><div class="wrap" id="tabbar" role="tablist"></div></nav>
<main class="wrap" id="main"></main>
<footer class="wrap">Bản trực quan để xem và giao việc. Số liệu sống (đơn, hoa hồng, trạng thái từng video) nằm ở file Excel <b>van-hanh-kenh-chi-giang.xlsx</b>. Dấu tick việc làm chỉ lưu trên trình duyệt của máy đang mở.</footer>

<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
const D = JSON.parse(document.getElementById('data').textContent);
const $ = s => document.querySelector(s);
const esc = s => String(s==null?'':s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmt = n => Math.round(n).toLocaleString('vi-VN');
const PL = Object.fromEntries(D.pillars.map(c => [c.code, c]));
const PCODES = D.pillars.map(c => c.code);
const ROLE = Object.fromEntries(D.roles.map(r => [r.code, r]));
const P = Object.fromEntries(D.products.map(p => [p.stt, p]));
const store = {
  get(k, d){ try{ const v = localStorage.getItem('chigiang:'+k); return v ? JSON.parse(v) : d; }catch(e){ return d; } },
  set(k, v){ try{ localStorage.setItem('chigiang:'+k, JSON.stringify(v)); }catch(e){} }
};
const today = new Date(D.project.today + 'T00:00:00');
const realToday = new Date(); realToday.setHours(0,0,0,0);
const now = realToday > today ? realToday : today;

// theme
const savedTheme = store.get('theme', null);
if (savedTheme) document.documentElement.dataset.theme = savedTheme;
$('#themebtn').onclick = () => {
  const cur = document.documentElement.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  const nx = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = nx; store.set('theme', nx);
};

// header
$('#pname').textContent = D.project.name;
$('#psub').textContent = D.project.subtitle + ' · ' + D.project.goal;
const totalVideos = D.weeks.reduce((s,w) => s + 7*w.total, 0);
const fullCap = D.capacity;
const headcount = () => D.roles.reduce((s,r) => s + roleCount(r, fullCap), 0);
function roleCount(r, cap){
  if (r.cap === 'kb') return Math.ceil(cap.target / cap.kb);
  if (r.cap === 'dung') return Math.ceil(cap.target / cap.dung);
  if (r.cap === 'qc') return Math.ceil(cap.target / cap.qc);
  return parseInt(r.count, 10) || 1;
}
const stats = [
  ['1', 'page, 5 trụ cột nội dung'],
  [String(D.maxDay), 'video/ngày từ tuần 4'],
  [fmt(totalVideos), 'video trong 12 tuần'],
  [String(D.products.length), 'link Shopee, mỗi video 1 Sub_id'],
  [String(headcount()), 'người khi đủ công suất'],
  ['19/10', 'tuần 1 bắt đầu'],
];
$('#stats').innerHTML = stats.map(s => `<div class="stat"><b>${s[0]}</b><span>${s[1]}</span></div>`).join('');

// tabs
const TABS = [
  ['tong','Tổng quan'],['kenh','Kênh & trụ cột'],['lotrinh','Lộ trình'],['nhansu','Nhân sự & phân việc'],
  ['quytrinh','Quy trình'],['lich','Lịch đăng'],['sanpham','Sản phẩm'],['congviec','Công việc'],
  ['dubao','Dự báo'],['kpi','KPI & rủi ro'],['nguon','Nguồn content']
];
$('#tabbar').innerHTML = TABS.map(t => `<button role="tab" data-t="${t[0]}" aria-selected="false">${t[1]}</button>`).join('');
$('#main').innerHTML = TABS.map(t => `<section class="tab" id="tab-${t[0]}" role="tabpanel"></section>`).join('');
function show(id){
  document.querySelectorAll('nav.tabs button').forEach(b => b.setAttribute('aria-selected', b.dataset.t===id));
  document.querySelectorAll('section.tab').forEach(s => s.classList.toggle('on', s.id==='tab-'+id));
  store.set('tab', id);
  if (location.hash !== '#'+id) history.replaceState(null,'','#'+id);
}
document.querySelectorAll('nav.tabs button').forEach(b => b.onclick = () => { show(b.dataset.t); window.scrollTo({top: document.querySelector('nav.tabs').offsetTop, behavior:'smooth'}); });

const kdot = code => `<span class="kdot" style="background:var(--${code.toLowerCase()})"></span>`;
const currentWeek = () => { let cw = null; D.weeks.forEach(w => { if (new Date(w.startIso+'T00:00:00') <= now) cw = w; }); return cw; };

// ---------- Tổng quan
(function(){
  const cw = currentWeek();
  const phaseNow = cw ? (cw.week<=2?1:cw.week<=4?2:cw.week<=6?3:4) : 0;
  const bars = svgRamp();
  $('#tab-tong').innerHTML = `
  <h2>Tổng quan điều hành</h2>
  <p class="lead">Đang ở <b>${esc(D.phases[phaseNow].phase)}</b>${cw?` – tuần ${cw.week} (${cw.start}–${cw.end})`:''}. Chỉ số chính: <b>${esc(D.project.north_star)}</b>.</p>
  <div class="alerts">
    <div class="alert w"><b>Hoa hồng tính theo Shopee, không theo TikTok</b><p>Thực phẩm chức năng trên Shopee thường chỉ 2,5–7,5%. Hoa hồng/đơn cao nhất: ${D.products.slice().sort((a,b)=>b.per_order-a.per_order).slice(0,4).map(p=>esc(p.name)+' ~'+Math.round(p.per_order/1000)+'k').join(', ')}.</p></div>
    <div class="alert o"><b>Mỗi video một Sub_id</b><p>Link dán ở bình luận có dạng …?sub_id=${esc(D.subPrefix)}-&lt;ID video&gt;-FBReels-SP&lt;mã&gt; (cột I của KHO_KICH_BAN), nên báo cáo Shopee chỉ ra đúng video nào ra đơn.</p></div>
    <div class="alert"><b>Một page, nội dung nhạy cảm</b><p>Bị hạn chế là mất hết. Không xưng bác sĩ, không hình gợi dục, không hứa “tăng sinh lý”; tăng sản lượng theo bậc, qua cửa mới tăng.</p></div>
  </div>
  <div class="grid g2">
    <div class="card">
      <h3 style="margin-top:0">Tệp khán giả</h3>
      <div class="timeline">${D.channel.audience.map(a => `<div class="t" style="font-size:13px">${esc(a[0])}</div><div class="small">${esc(a[1])}</div>`).join('')}</div>
      <p class="muted" style="margin-bottom:0">Viết cho đàn ông 45+ ở Sài Gòn và miền Nam: gọi “anh”, “mấy anh”, giọng miền Nam, nhịp chậm.</p>
    </div>
    <div class="card">
      <h3 style="margin-top:0">Video/ngày theo tuần và trụ cột</h3>
      ${bars}
      <div class="legend">${D.pillars.map(c => `<span>${kdot(c.code)}${c.code} ${esc(c.name)}</span>`).join('')}</div>
    </div>
  </div>
  <h3>5 giai đoạn</h3>
  <div class="card">${D.phases.map((p,i) => `<div class="phase"><div><b>${esc(p.phase)}</b><div class="muted">${esc(p.time)}</div>${i===phaseNow?'<span class="pill A" style="margin-top:6px">Đang ở đây</span>':''}</div><div class="small">${esc(p.goal)}</div><div class="gate">${esc(p.gate)}</div></div>`).join('')}</div>
  <h3>Mỗi ngày của điều phối</h3>
  <div class="grid g3">
    <div class="card"><b>Sáng 08:30</b><p class="small">Mở sheet TONG_QUAN: % hoàn thành, đơn theo trụ cột, prompt chờ duyệt, việc quá hạn. Họp nhanh 10 phút.</p></div>
    <div class="card"><b>Chiều 17:00</b><p class="small">Kiểm tra R4 đã chốt đủ bài cho ngày mai trên Postiz, link kèm Sub_id nằm ở bình luận gốc.</p></div>
    <div class="card"><b>Chủ nhật 19:00</b><p class="small">Review tuần: top 3 video theo Sub_id → 5 biến thể. Cắt sản phẩm hạng C sau 20 video không có đơn. Chốt 56 ý tưởng cho tuần sau.</p></div>
  </div>`;
})();

function svgRamp(){
  const W = 560, H = 230, pad = {l:30,r:8,t:10,b:34};
  const iw = W-pad.l-pad.r, ih = H-pad.t-pad.b, max = D.maxDay;
  const bw = iw / D.weeks.length;
  let s = `<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Biểu đồ sản lượng video mỗi ngày theo tuần">`;
  [0,.25,.5,.75,1].map(f => Math.round(f*max)).forEach(v => { const y = pad.t + ih - v/max*ih; s += `<line x1="${pad.l}" x2="${W-pad.r}" y1="${y}" y2="${y}" stroke="var(--line)"/><text x="${pad.l-6}" y="${y+4}" text-anchor="end">${v}</text>`; });
  D.weeks.forEach((w,i) => {
    let y = pad.t + ih; const x = pad.l + i*bw + 4;
    PCODES.forEach(k => { const h = w[k]/max*ih; if(!h) return; y -= h; s += `<rect x="${x}" y="${y}" width="${bw-8}" height="${h}" fill="var(--${k.toLowerCase()})" rx="2"><title>Tuần ${w.week} · ${k} ${esc(PL[k].name)}: ${w[k]} video/ngày</title></rect>`; });
    const tot = w.total;
    s += `<text x="${x+(bw-8)/2}" y="${y-4}" text-anchor="middle" style="font-weight:600;fill:var(--ink)">${tot}</text>`;
    s += `<text x="${x+(bw-8)/2}" y="${H-pad.b+14}" text-anchor="middle">T${w.week}</text><text x="${x+(bw-8)/2}" y="${H-pad.b+27}" text-anchor="middle" style="font-size:9.5px">${w.start}</text>`;
  });
  return s + '</svg>';
}

// ---------- Kênh
const CHN = D.channel;
$('#tab-kenh').innerHTML = `<h2>Kênh & 5 trụ cột nội dung</h2>
<p class="lead">Một page, nội dung chia 5 trụ cột theo nhu cầu của đàn ông 45+. Mỗi trụ cột có nhóm sản phẩm riêng, số video/ngày lấy từ lộ trình.</p>
<div class="grid g2">
  <div class="card">
    <h3 style="margin-top:0">${esc(CHN.name)}</h3>
    <div class="timeline">
      <div class="t" style="font-size:13px">Nhân vật</div><div class="small">${esc(CHN.host)}</div>
      <div class="t" style="font-size:13px">Định dạng</div><div class="small">${esc(CHN.format)}</div>
      <div class="t" style="font-size:13px">Công cụ</div><div class="small">${esc(CHN.tool)}</div>
      <div class="t" style="font-size:13px">Trạng thái</div><div class="small">${esc(CHN.status)}</div>
      <div class="t" style="font-size:13px">Postiz ID</div><div class="small"><code>${esc(CHN.postiz_id)}</code></div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-top:0">Luật giọng nói (áp vào mọi prompt)</h3>
    <ul style="margin:0;padding-left:18px">${CHN.voice.map(v => `<li class="small" style="margin-bottom:6px">${esc(v)}</li>`).join('')}</ul>
  </div>
</div>
<h3>5 trụ cột</h3>
<div class="grid g5">${D.pillars.map(c => `
  <div class="card chcard" style="--c:var(--${c.code.toLowerCase()})">
    <div><span class="code">${c.code}</span> <span class="muted">· ${D.weeks[D.weeks.length-1][c.code]} video/ngày</span></div>
    <h4>${esc(c.name)}</h4>
    <div class="small">${esc(c.desc)}</div>
    <div class="lbl">Câu hỏi mẫu</div><ul>${c.examples.map(p => `<li>${esc(p)}</li>`).join('')}</ul>
    <div class="lbl">Sản phẩm chủ lực</div>
    <div class="chips">${c.products.filter(n=>P[n]).map(n => `<span class="chip" title="${esc(P[n].shopee)}">${n}. ${esc(P[n].name)}</span>`).join('') || '<span class="muted small">Chưa có link Shopee</span>'}</div>
  </div>`).join('')}</div>
<h3>Ý tưởng khởi đầu (${D.ideas.length} video, đã nạp sẵn vào sheet KHO_KICH_BAN)</h3>
<div class="filters"><select id="idch"><option value="">Tất cả trụ cột</option>${D.pillars.map(c=>`<option value="${c.code}">${c.code} · ${esc(c.name)}</option>`).join('')}</select>
<select id="idty"><option value="">Mọi loại video</option>${[...new Set(D.ideas.map(i=>i.type))].map(t=>`<option>${esc(t)}</option>`).join('')}</select></div>
<div class="tablewrap"><table><thead><tr><th>Trụ cột</th><th>Loại</th><th>Tiêu đề / câu hỏi</th><th>Hook 3 giây</th><th>Bối cảnh</th><th>Sản phẩm</th></tr></thead><tbody id="idbody"></tbody></table></div>`;
function renderIdeas(){
  const f = $('#idch').value, t = $('#idty').value;
  $('#idbody').innerHTML = D.ideas.filter(i => (!f || i.pl===f) && (!t || i.type===t)).map(i => `<tr><td style="white-space:nowrap">${kdot(i.pl)}${i.pl}</td><td><span class="pill">${esc(i.type)}</span></td><td>${esc(i.title)}</td><td class="muted">“${esc(i.hook)}”</td><td class="small">${esc(i.scene)}</td><td class="small">${i.sp&&P[i.sp]?esc(i.sp+'. '+P[i.sp].name):'—'}</td></tr>`).join('');
}
$('#idty').onchange = renderIdeas;
$('#idch').onchange = renderIdeas; renderIdeas();

// ---------- Lộ trình
(function(){
  const cw = currentWeek();
  const cellBg = v => v===0 ? 'background:var(--surface-2);color:var(--ink-3)' : v>=3 ? 'background:var(--ok-bg);color:var(--ok)' : v>=2 ? 'background:var(--warn-bg);color:var(--warn)' : '';
  $('#tab-lotrinh').innerHTML = `<h2>Lộ trình 12 tuần</h2>
  <p class="lead">Số trong ô là video/ngày của từng trụ cột. Muốn đổi thì sửa sheet LO_TRINH; THEO_DOI_NGAY và DU_BAO tự cập nhật theo.</p>
  <div class="tablewrap"><table class="heat"><thead><tr><th>Tuần</th><th>Thời gian</th>${D.pillars.map(c=>`<th class="ctr" title="${esc(c.name)}">${kdot(c.code)}${c.code}</th>`).join('')}<th class="ctr">Tổng/ngày</th><th class="num">Tổng/tuần</th><th>Mốc / sự kiện</th></tr></thead><tbody>
  ${D.weeks.map(w => { const t = w.total; const on = cw && cw.week===w.week; return `<tr${on?' style="outline:2px solid var(--accent);outline-offset:-2px"':''}><td><b>T${w.week}</b>${on?' <span class="pill A">nay</span>':''}</td><td class="muted" style="white-space:nowrap">${w.start} – ${w.end}</td>${PCODES.map(k=>`<td class="cell" style="${cellBg(w[k])}">${w[k]}</td>`).join('')}<td class="cell"><b>${t}</b></td><td class="num">${fmt(t*7)}</td><td class="small">${esc(w.event)}</td></tr>`; }).join('')}
  <tr><td colspan="8"><b>Tổng 12 tuần</b></td><td class="num"><b>${fmt(totalVideos)}</b></td><td></td></tr>
  </tbody></table></div>
  <p class="muted">${D.pillars.map(c=>c.code+' '+esc(c.name)).join(' · ')}</p>
  <h3>Điều kiện qua cửa từng giai đoạn</h3>
  <div class="card">${D.phases.map(p => `<div class="phase"><div><b>${esc(p.phase)}</b><div class="muted">${esc(p.time)}</div></div><div class="small">${esc(p.goal)}</div><div class="gate">${esc(p.gate)}</div></div>`).join('')}</div>`;
})();

// ---------- Nhân sự
(function(){
  $('#tab-nhansu').innerHTML = `<h2>Nhân sự & phân việc</h2>
  <p class="lead">${D.roles.length} vai trò. Số người của biên kịch, sản xuất video và đăng bài tự tính theo công suất. Đổi các ô dưới đây để thử kịch bản nhân sự.</p>
  <div class="card">
    <div class="calc">
      <label>Video/ngày<input type="number" id="c-target" min="1" value="${fullCap.target}"></label>
      <label>Prompt/biên kịch/ngày<input type="number" id="c-kb" min="1" value="${fullCap.kb}"></label>
      <label>Video/người sản xuất/ngày<input type="number" id="c-dung" min="1" value="${fullCap.dung}"></label>
      <label>Bài/người QC/ngày<input type="number" id="c-qc" min="1" value="${fullCap.qc}"></label>
      <div><div class="muted">Tổng nhân sự</div><div id="c-total" style="font-size:28px;font-weight:700;color:var(--brand)"></div></div>
    </div>
    <div class="muted">Giai đoạn 1 (5–6 video/ngày) chỉ cần 2 người: người 1 kiêm R1 + R2 (chọn chủ đề, viết và duyệt prompt), người 2 kiêm R3 + R4 (Viral Studio, QC, đăng, bình luận, số liệu).</div>
  </div>
  <h3>Vai trò</h3>
  <div class="grid g2" id="roles"></div>
  <h3>Ma trận trách nhiệm (RACI)</h3>
  <p class="muted" style="margin-top:-4px">R = làm · A = chịu trách nhiệm cuối · C = tham vấn · I = được báo</p>
  <div class="tablewrap"><table class="raci"><thead><tr><th>Bước</th>${D.raciRoles.map(r=>`<th class="ctr" title="${esc(ROLE[r].role)}">${r}</th>`).join('')}</tr></thead><tbody>
  ${D.sop.map(s => `<tr><td>${s.n}. ${esc(s.task)}</td>${D.raciRoles.map(r => { const v = (D.raci[s.n]||{})[r]||''; return `<td class="ctr ${v?'r-'+v:''}">${v}</td>`; }).join('')}</tr>`).join('')}
  </tbody></table></div>
  <p class="muted">${D.roles.map(r=>`${r.code} ${esc(r.role)}`).join(' · ')}</p>`;
  function render(){
    const cap = { target:+$('#c-target').value||1, kb:+$('#c-kb').value||1, dung:+$('#c-dung').value||1, qc:+$('#c-qc').value||1 };
    let tot = 0;
    $('#roles').innerHTML = D.roles.map(r => { const n = roleCount(r, cap); tot += n; return `<div class="card role"><div class="head"><b>${r.code} · ${esc(r.role)}</b><span class="cnt">${n}</span></div><p>${esc(r.duty)}</p><p><b>Đầu ra:</b> ${esc(r.output)}</p><p><b>KPI:</b> ${esc(r.kpi)}</p><p class="muted">Công cụ: ${esc(r.tools)} · Báo cáo cho: ${esc(r.report)}</p></div>`; }).join('');
    $('#c-total').textContent = tot + ' người';
  }
  ['c-target','c-kb','c-dung','c-qc'].forEach(id => $('#'+id).oninput = render); render();
})();

// ---------- Quy trình
(function(){
  const qcState = store.get('qc', {});
  $('#tab-quytrinh').innerHTML = `<h2>Quy trình một video</h2>
  <p class="lead">10 bước. Trạng thái video ở sheet KHO_KICH_BAN đi theo: Ý tưởng → Đang viết → Chờ duyệt → Đã duyệt → Đang sản xuất → QC → Sẵn sàng đăng → Đã đăng.</p>
  <div class="flow">${D.sop.map(s => `<div class="fstep"><span class="n">${s.n}</span><b>${esc(s.task)}</b><div class="who">${s.r} · ${esc(ROLE[s.r]?ROLE[s.r].role:s.r)}</div><div class="muted">${esc(s.when)}</div><p>${esc(s.out)}</p></div>`).join('')}</div>
  <div class="grid g2" style="margin-top:18px">
    <div class="card"><h3 style="margin-top:0">Checklist QC 10 điểm</h3><p class="muted" style="margin-top:-6px">Đạt hết mới được đăng. Tick để thử với một video, bấm “Làm lại” cho video tiếp theo.</p>
      <div id="qclist"></div><button class="btn" id="qcreset" type="button">Làm lại</button></div>
    <div class="card"><h3 style="margin-top:0">Nhịp làm việc một ngày</h3>
      <div class="timeline">${D.rhythm.map(x => `<div class="t">${esc(x.t)}</div><div>${esc(x.task)} <span class="muted">· ${esc(x.who)}${x.note?' · '+esc(x.note):''}</span></div>`).join('')}</div>
      <h3>Họp định kỳ</h3>
      <div class="timeline">${D.rituals.map(x => `<div class="t" style="font-size:13px">${esc(x.when)}</div><div>${esc(x.what)} <span class="muted">· ${esc(x.who)}</span></div>`).join('')}</div>
    </div>
  </div>
  <div class="card" style="margin-top:14px"><b>Quy tắc đặt tên file:</b> <code>CG-&lt;YYYYMMDD&gt;-&lt;giờ đăng&gt;-&lt;ID video&gt;-&lt;slug&gt;.mp4</code>, ví dụ <code>CG-20261020-0730-T1-002-review-vuong-bao.mp4</code>, lưu vào <code>viral-studio-downloads/videos/gioi-tinh/</code></div>`;
  function render(){
    $('#qclist').innerHTML = D.qc.map((q,i) => `<label class="check ${qcState[i]?'done':''}"><input type="checkbox" data-i="${i}" ${qcState[i]?'checked':''}><span class="t">${i+1}. ${esc(q)}</span></label>`).join('');
    $('#qclist').querySelectorAll('input').forEach(cb => cb.onchange = () => { qcState[cb.dataset.i] = cb.checked; store.set('qc', qcState); render(); });
  }
  $('#qcreset').onclick = () => { Object.keys(qcState).forEach(k => delete qcState[k]); store.set('qc', qcState); render(); };
  render();
})();

// ---------- Lịch đăng
$('#tab-lich').innerHTML = `<h2>Lịch đăng</h2>
<p class="lead">8 khung giờ theo thói quen lướt Facebook của đàn ông 45+: 2 review, 3 hỏi đáp gắn sản phẩm, 1 tình huống vợ chồng, 2 hỏi đáp kéo view. Tuần 1–3 chưa đủ 8 video thì bỏ khung 13:00 và 22:45 trước.</p>
<div class="tablewrap"><table><thead><tr><th>Giờ</th><th>Loại video</th><th>Mục tiêu</th><th>Gắn sản phẩm</th></tr></thead><tbody>
${D.slots.map(s => `<tr><td><b>${s.t}</b></td><td>${esc(s.type)}</td><td class="muted">${esc(s.goal)}</td><td>${esc(s.prod)}</td></tr>`).join('')}</tbody></table></div>
<div class="grid g2" style="margin-top:14px">
<div><h3 style="margin-top:0">Chủ đề theo thứ</h3><div class="tablewrap"><table><thead><tr><th>Thứ</th><th>Chủ đề</th><th>Bối cảnh</th><th>Sản phẩm</th></tr></thead><tbody>${D.themes.map(t=>`<tr><td><b>${esc(t.day)}</b></td><td>${esc(t.theme)}</td><td class="muted">${esc(t.color)}</td><td class="small">${esc(t.prod)}</td></tr>`).join('')}</tbody></table></div></div>
<div><h3 style="margin-top:0">Lịch mùa vụ</h3><div class="tablewrap"><table><thead><tr><th>Khi nào</th><th>Sự kiện</th><th>Hướng nội dung</th></tr></thead><tbody>${D.season.map(t=>`<tr><td><b style="white-space:nowrap">${esc(t.when)}</b></td><td>${esc(t.ev)}</td><td class="small">${esc(t.dir)}</td></tr>`).join('')}</tbody></table></div></div>
</div>`;

// ---------- Sản phẩm
(function(){
  $('#tab-sanpham').innerHTML = `<h2>Sản phẩm affiliate Shopee</h2>
  <p class="lead">${D.products.length} link Shopee, mỗi link có thư mục ảnh. Tên, giá, hoa hồng lấy đúng theo sản phẩm của link (crawl bằng PostForge). Hạng xếp theo hoa hồng/đơn: A ≥ 20k, B ≥ 10k. Link riêng của từng video (kèm Sub_id) lấy ở cột I của KHO_KICH_BAN.</p>
  <div class="filters">
    <input id="pq" type="search" placeholder="Tìm tên sản phẩm…">
    <select id="pch"><option value="">Tất cả trụ cột</option>${D.pillars.map(c=>`<option value="${c.code}">${c.code} · ${esc(c.name)}</option>`).join('')}</select>
    <select id="ptier"><option value="">Mọi hạng</option><option>A</option><option>B</option><option>C</option></select>
    <select id="psort"><option value="stt">Sắp theo mã</option><option value="po">Hoa hồng/đơn cao nhất</option><option value="hh">% hoa hồng cao nhất</option></select>
  </div>
  <div class="tablewrap"><table><thead><tr><th>Mã</th><th>Sản phẩm</th><th class="num">Giá</th><th class="num">HH</th><th class="num">HH/đơn</th><th>Trụ cột</th><th>Hạng</th><th>Góc nội dung</th><th>Link</th></tr></thead><tbody id="pbody"></tbody></table></div>
  <p class="muted" id="pcount"></p>`;
  function render(){
    const q = $('#pq').value.trim().toLowerCase(), ch = $('#pch').value, tier = $('#ptier').value, so = $('#psort').value;
    let rows = D.products.filter(p => (!q || (p.name+' '+p.shopee).toLowerCase().includes(q)) && (!ch || p.ch===ch || p.ch2===ch) && (!tier || p.tier===tier));
    if (so==='po') rows.sort((a,b)=>b.per_order-a.per_order); else if (so==='hh') rows.sort((a,b)=>b.hh-a.hh);
    $('#pbody').innerHTML = rows.map(p => {
      return `<tr><td><b>${p.stt}</b></td><td><b>${esc(p.name)}</b><div class="muted">${esc(p.shopee)}</div>${p.note?`<div class="small" style="color:var(--brand);margin-top:3px">${esc(p.note)}</div>`:''}</td><td class="num">${fmt(p.price)}đ</td><td class="num">${(p.hh*100).toFixed(1)}%</td><td class="num"><b>${fmt(p.per_order)}đ</b></td><td style="white-space:nowrap">${kdot(p.ch)}${p.ch}${p.ch2?' <span class="muted">+'+p.ch2+'</span>':''}</td><td><span class="pill ${p.tier}">${p.tier}</span></td><td class="small">${esc(p.angle)}</td><td style="white-space:nowrap"><a class="btn pri" href="${esc(p.link)}" target="_blank" rel="noopener">Mở link</a> <button class="btn" type="button" data-copy="${esc(p.sublink)}" title="${esc(p.sublink)}">Chép link Sub_id</button> <button class="btn" type="button" data-copy="${esc(p.folder)}" title="${esc(p.folder)}">Thư mục ảnh</button></td></tr>`;
    }).join('');
    $('#pcount').textContent = rows.length + ' / ' + D.products.length + ' sản phẩm';
  }
  ['pq','pch','ptier','psort'].forEach(id => $('#'+id).addEventListener('input', render));
  render();
})();
document.addEventListener('click', e => {
  const b = e.target.closest('[data-copy]'); if (!b) return;
  const txt = b.dataset.copy;
  const done = () => { const o = b.textContent; b.textContent = 'Đã chép'; b.classList.add('copied'); setTimeout(()=>{ b.textContent = o; b.classList.remove('copied'); }, 1300); };
  if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(done, () => prompt('Chép thủ công:', txt));
  else prompt('Chép thủ công:', txt);
});

// ---------- Công việc
(function(){
  const st = store.get('tasks', {});
  $('#tab-congviec').innerHTML = `<h2>Công việc & giao việc</h2>
  <p class="lead">Việc thiết lập và các mốc lớn. Tick khi xong (lưu trên trình duyệt này). Bản dùng chung cả team: sheet CONG_VIEC trong Excel, có cột “Người làm”.</p>
  <div class="filters"><select id="trole"><option value="">Tất cả vai trò</option>${D.roles.map(r=>`<option value="${r.code}">${r.code} · ${esc(r.role)}</option>`).join('')}</select>
  <label class="small" style="display:flex;align-items:center;gap:6px"><input type="checkbox" id="thide"> Ẩn việc đã xong</label></div>
  <div class="card"><div class="small" id="tprog"></div><div class="progress"><i id="tbar"></i></div><div id="tlist"></div></div>`;
  function render(){
    const role = $('#trole').value, hide = $('#thide').checked;
    const all = D.tasks.filter(t => !role || t.role===role);
    const done = all.filter(t => st[t.id]).length;
    $('#tprog').textContent = `${done}/${all.length} việc đã xong`;
    $('#tbar').style.width = (all.length? done/all.length*100 : 0) + '%';
    let html = '', ph = '';
    all.forEach(t => {
      if (hide && st[t.id]) return;
      if (t.phase !== ph){ ph = t.phase; html += `<h3 style="margin:14px 0 4px">${esc(ph)}</h3>`; }
      const od = !st[t.id] && new Date(t.due+'T00:00:00') < now;
      html += `<label class="check ${st[t.id]?'done':''}"><input type="checkbox" data-id="${t.id}" ${st[t.id]?'checked':''}><span><span class="t"><b>${t.id}</b> · ${esc(t.task)}</span><div class="meta">${t.role} · ${esc(ROLE[t.role].role)} · <span class="${od?'overdue':''}">hạn ${t.dueTxt}${od?' (quá hạn)':''}</span></div></span></label>`;
    });
    $('#tlist').innerHTML = html || '<p class="muted">Không có việc.</p>';
    $('#tlist').querySelectorAll('input').forEach(cb => cb.onchange = () => { st[cb.dataset.id] = cb.checked; store.set('tasks', st); render(); });
  }
  $('#trole').onchange = render; $('#thide').onchange = render; render();
})();

// ---------- Dự báo
(function(){
  const A = D.products.filter(p => p.tier==='A');
  const avgA = A.reduce((s,p)=>s+p.per_order,0)/(A.length||1);
  $('#tab-dubao').innerHTML = `<h2>Dự báo hoa hồng</h2>
  <div class="alert" style="margin-bottom:14px"><b>Chỉ tăng người khi view thực tế vượt ngưỡng hòa vốn</b><p>Hoa hồng Shopee của thực phẩm chức năng thấp, nên với giả định mặc định hoa hồng chưa đủ trả lương cả đội. Giai đoạn 1 chạy 2 người kiêm nhiệm, nhập số thật của page vào đây rồi mới quyết định.</p></div>
  <p class="lead">Các con số mặc định là <b>giả định</b>. Sau 2 tuần, thay bằng số thực của page (view, click, đơn) từ sheet THEO_DOI_NGAY. Hoa hồng trung bình/đơn lấy theo sản phẩm hạng A.</p>
  <div class="card"><div class="calc">
    <label>View trung bình/video<input type="number" id="f-v" value="${D.forecast.views}" min="0"></label>
    <label>Click/view (%)<input type="number" id="f-c" value="${(D.forecast.ctr*100).toFixed(2)}" step="0.1" min="0"></label>
    <label>Đơn/click (%)<input type="number" id="f-r" value="${(D.forecast.cr*100).toFixed(1)}" step="0.5" min="0"></label>
    <label>HH TB/đơn (đ)<input type="number" id="f-h" value="${Math.round(avgA)}" step="1000" min="0"></label>
    <label>Số người<input type="number" id="f-n" value="${headcount()}" min="1"></label>
    <label>Chi phí/người/tháng (đ)<input type="number" id="f-k" value="${D.forecast.cost}" step="500000" min="0" style="width:140px"></label>
  </div>
  <div class="grid g3" id="f-sum"></div>
  <div id="f-chart" style="margin-top:12px"></div></div>
  <div class="tablewrap" style="margin-top:14px"><table><thead><tr><th>Tuần</th><th class="num">Video/tuần</th><th class="num">View</th><th class="num">Click</th><th class="num">Đơn</th><th class="num">Hoa hồng dự kiến</th></tr></thead><tbody id="f-body"></tbody></table></div>`;
  function render(){
    const v=+$('#f-v').value||0, c=(+$('#f-c').value||0)/100, r=(+$('#f-r').value||0)/100, h=+$('#f-h').value||0;
    let tot=0, rows='', vals=[];
    D.weeks.forEach(w => { const vid=7*w.total, views=vid*v, cl=views*c, od=cl*r, hh=od*h; tot+=hh; vals.push(hh);
      rows += `<tr><td>T${w.week} · ${w.start}</td><td class="num">${fmt(vid)}</td><td class="num">${fmt(views)}</td><td class="num">${fmt(cl)}</td><td class="num">${fmt(od)}</td><td class="num"><b>${fmt(hh)}đ</b></td></tr>`; });
    $('#f-body').innerHTML = rows;
    const M = D.maxDay, full = M*30*v*c*r*h, cost = (+$('#f-n').value||0)*(+$('#f-k').value||0), pl = full-cost, be = (c*r*h)>0 ? cost/(M*30*c*r*h) : 0;
    $('#f-sum').innerHTML = [['Hoa hồng 12 tuần', fmt(tot)+'đ'],['Mỗi tháng khi đủ '+M+' video/ngày', fmt(full)+'đ'],['Đơn/ngày khi đủ công suất', (M*v*c*r).toFixed(1)],['Chi phí nhân sự/tháng', fmt(cost)+'đ'],['Lãi/lỗ mỗi tháng', `<span style="color:${pl<0?'var(--bad)':'var(--ok)'}">${fmt(pl)}đ</span>`],['View TB/video cần để hòa vốn', fmt(be)]].map(x=>`<div class="card" style="background:var(--surface-2);box-shadow:none"><div class="muted">${x[0]}</div><div style="font-size:22px;font-weight:700">${x[1]}</div></div>`).join('');
    const W=560,H=150,max=Math.max(...vals,1),bw=(W-20)/vals.length;
    $('#f-chart').innerHTML = `<svg viewBox="0 0 ${W} ${H+20}" width="100%" role="img" aria-label="Hoa hồng dự kiến theo tuần">${vals.map((x,i)=>{const hh=x/max*H;return `<rect x="${10+i*bw+3}" y="${H-hh}" width="${bw-6}" height="${hh}" fill="var(--brand)" rx="2"><title>T${i+1}: ${fmt(x)}đ</title></rect><text x="${10+i*bw+bw/2}" y="${H+14}" text-anchor="middle">T${i+1}</text>`;}).join('')}</svg>`;
  }
  ['f-v','f-c','f-r','f-h','f-n','f-k'].forEach(id => $('#'+id).oninput = render); render();
})();

// ---------- KPI & rủi ro
$('#tab-kpi').innerHTML = `<h2>KPI & quy tắc cắt / nhân</h2>
<p class="lead">Áp dụng trong buổi review Chủ nhật. Mỗi tuần lấy 3 video ra đơn nhiều nhất (báo cáo Shopee lọc Sub_id) để làm 5 biến thể cho tuần sau.</p>
<div class="tablewrap"><table><thead><tr><th>Chỉ số</th><th>Theo dõi ở</th><th>Ngưỡng</th><th>Hành động</th></tr></thead><tbody>${D.kpi.map(k=>`<tr><td><b>${esc(k.m)}</b></td><td class="muted">${esc(k.where)}</td><td><span class="pill">${esc(k.th)}</span></td><td>${esc(k.act)}</td></tr>`).join('')}</tbody></table></div>
<h3>Sổ rủi ro</h3>
<div class="tablewrap"><table><thead><tr><th>Rủi ro</th><th>Mức</th><th>Phòng tránh</th><th>Chủ quản</th></tr></thead><tbody>${D.risks.map(r=>`<tr><td>${esc(r.risk)}</td><td><span class="pill ${r.lvl==='Cao'?'bad':r.lvl==='Thấp'?'A':'B'}">${esc(r.lvl)}</span></td><td class="small">${esc(r.fix)}</td><td>${r.owner}</td></tr>`).join('')}</tbody></table></div>`;

// ---------- Tài nguyên
if(0)$('#tab-tainguyen').innerHTML = `<h2>Tài nguyên & công cụ</h2>
<p class="lead">Đường dẫn trên máy và skill dùng trong Claude Code. Bấm “Chép” để lấy đường dẫn.</p>
<div class="tablewrap"><table><thead><tr><th>Tài nguyên</th><th>Đường dẫn / tên</th><th>Dùng để</th><th></th></tr></thead><tbody>${D.resources.map(r=>`<tr><td><b>${esc(r.name)}</b></td><td class="small" style="word-break:break-all"><code>${esc(r.path)}</code></td><td class="muted">${esc(r.use)}</td><td>${r.path.startsWith('http')?`<a class="btn" href="${esc(r.path)}" target="_blank" rel="noopener">Mở</a>`:`<button class="btn" type="button" data-copy="${esc(r.path)}">Chép</button>`}</td></tr>`).join('')}</tbody></table></div>`;

// ---------- Nguồn content
(function(){
  let local = store.get('sources', []);
  const save = () => store.set('sources', local);
  const APPLY = PCODES.concat(['Tất cả']);
  const platform = u => { u = (u||'').toLowerCase(); if (u.includes('tiktok')) return 'TikTok'; if (u.includes('facebook') || u.includes('fb.watch') || u.includes('fb.com')) return 'Facebook'; if (u.includes('youtu')) return 'YouTube'; if (u.includes('instagram')) return 'Instagram'; return 'Khác'; };
  function embed(u){
    if (!u) return null; let m;
    if ((m = u.match(/tiktok\.com\/.*?(?:video|v|embed\/v2|photo)\/(\d{8,})/))) return { src:'https://www.tiktok.com/player/v1/'+m[1]+'?description=1&music_info=1&rel=0', cls:'v' };
    if ((m = u.match(/(?:youtube\.com\/(?:shorts\/|watch\?v=|embed\/|live\/)|youtu\.be\/)([\w-]{6,})/))) return { src:'https://www.youtube.com/embed/'+m[1], cls: u.includes('/shorts/') ? 'v' : 'h' };
    if ((m = u.match(/instagram\.com\/(?:reel|reels|p)\/([\w-]+)/))) return { src:'https://www.instagram.com/reel/'+m[1]+'/embed', cls:'v' };
    if (/facebook\.com|fb\.watch|fb\.com/.test(u)) {
      const post = /\/posts\/|permalink|story_fbid|\/photo|\/share\/p\//.test(u);
      return { src:'https://www.facebook.com/plugins/'+(post?'post':'video')+'.php?href='+encodeURIComponent(u)+'&show_text=false&width=320', cls: post ? 'post' : 'v' };
    }
    return null;
  }
  const iframe = e => `<iframe class="${e.cls}" src="${esc(e.src)}" loading="lazy" allow="autoplay; encrypted-media; picture-in-picture; fullscreen; clipboard-write" referrerpolicy="strict-origin-when-cross-origin" title="Video nguồn"></iframe>`;
  const shortHint = u => /vt\.tiktok|vm\.tiktok|tiktok\.com\/t\//.test(u) ? 'Link TikTok rút gọn chưa xem trong trang được. Mở link, bấm Chia sẻ → Sao chép liên kết trên máy tính (dạng tiktok.com/@kenh/video/…) rồi dán lại.' : 'Chưa xem trong trang được với link này – bấm “Mở link gốc”.';
  const stCls = s => s==='Mới' ? 'st-new' : s==='Đã thành kịch bản' ? 'st-done' : '';
  const opts = (arr, sel) => arr.map(x => `<option${x===sel?' selected':''}>${esc(x)}</option>`).join('');

  $('#tab-nguon').innerHTML = `<h2>Nguồn content mục tiêu</h2>
  <p class="lead">Kho học hỏi từ Facebook, TikTok, YouTube: video viral, kênh tham khảo, hook hay. Dán link là xem video ngay trong trang. Mỗi thứ Sáu, R1 lọc nguồn “Mới” và chuyển 10 ý tưởng sang sheet KHO_KICH_BAN.</p>
  <div class="card">
    <h3 style="margin-top:0">Thêm nguồn mới</h3>
    <div class="formgrid">
      <label class="full">Link Facebook / TikTok / YouTube *<input id="s-url" type="url" placeholder="Dán link vào đây, ví dụ https://www.tiktok.com/@kenh/video/123…"></label>
      <label>Kênh / tác giả<input id="s-author" placeholder="@tenkenh"></label>
      <label>Loại<select id="s-type">${opts(D.sourceTypes, 'Video viral')}</select></label>
      <label>Áp dụng cho<select id="s-apply">${opts(APPLY, 'T1')}</select></label>
      <label>View (nếu biết)<input id="s-views" type="number" min="0" placeholder="vd 1200000"></label>
      <label class="full">Học được gì (hook, cấu trúc, nhân vật, câu chốt…)<textarea id="s-learned" rows="2"></textarea></label>
      <label class="full">Ý tưởng chuyển thể cho Chị Giang<textarea id="s-idea" rows="2"></textarea></label>
    </div>
    <div id="s-preview" class="src-preview"></div>
    <button class="btn pri" id="s-add" type="button">Thêm vào danh sách</button> <span class="muted" id="s-msg"></span>
  </div>
  <div class="filters" style="margin-top:18px">
    <input id="sq" type="search" placeholder="Tìm trong ghi chú, tác giả…">
    <select id="splat"><option value="">Mọi nền tảng</option>${opts(['TikTok','Facebook','YouTube','Instagram','Khác'])}</select>
    <select id="sapply"><option value="">Mọi trụ cột</option>${opts(APPLY)}</select>
    <select id="sstat"><option value="">Mọi trạng thái</option>${opts(D.sourceStatuses)}</select>
  </div>
  <div class="src-actions" style="margin-bottom:12px">
    <button class="btn" id="s-copy" type="button">Chép mục mới để gửi Claude</button>
    <button class="btn" id="s-export" type="button">Xuất file .json</button>
    <label class="btn" style="cursor:pointer">Nhập file .json<input id="s-import" type="file" accept=".json,application/json" hidden></label>
    <span class="muted small" id="s-count"></span>
  </div>
  <div class="srcgrid" id="s-list"></div>
  <p class="muted small" style="margin-top:14px">Mục thêm ở đây chỉ lưu trên trình duyệt của máy này. Muốn cả team thấy: bấm “Chép mục mới để gửi Claude” rồi dán vào chat, Claude sẽ lưu vào file gốc (_build/nguon-content.json) và làm mới trang này. Có thể ghi thêm vào sheet NGUON_CONTENT trong Excel.</p>`;

  function all(){ return local.map(s => ({...s, _local:true})).concat(D.sources); }
  function render(){
    const q = $('#sq').value.trim().toLowerCase(), pf = $('#splat').value, ap = $('#sapply').value, st = $('#sstat').value;
    const rows = all().filter(s => (!q || [s.author,s.learned,s.idea,s.url].join(' ').toLowerCase().includes(q)) && (!pf || platform(s.url)===pf) && (!ap || s.apply===ap) && (!st || s.status===st));
    $('#s-count').textContent = `${D.sources.length} nguồn trong file · ${local.length} nguồn thêm trên máy này · đang hiện ${rows.length}`;
    $('#s-list').innerHTML = rows.map(s => {
      const p = platform(s.url), e = embed(s.url);
      return `<div class="card src">
        <div class="src-head"><span class="pill plat-${p}">${p}</span><b>${esc(s.author||'')}</b><span class="muted small">${esc(s.id||'')} · ${esc(s.added||'')}${s.views?` · ${fmt(s.views)} view`:''}</span>${s._local?'<span class="tag-local">mới thêm trên máy này</span>':''}</div>
        <div class="src-media">${e ? `<button class="playbtn" type="button" data-play="${esc(s.url)}">▶ Xem tại đây</button>` : `<div class="hint">${esc(shortHint(s.url))}</div>`}</div>
        <div class="chips"><span class="pill">${esc(s.type||'')}</span><span class="pill">${esc(s.apply||'')}</span><span class="pill ${stCls(s.status)}">${esc(s.status||'Mới')}</span></div>
        ${s.learned?`<p><b>Học được:</b> ${esc(s.learned)}</p>`:''}
        ${s.idea?`<p><b>Ý tưởng:</b> ${esc(s.idea)}</p>`:''}
        <div class="src-actions"><a class="btn" href="${esc(s.url)}" target="_blank" rel="noopener">Mở link gốc</a><button class="btn" type="button" data-copy="${esc(s.url)}">Chép link</button>
        ${s._local?`<select data-st="${esc(s.id)}">${opts(D.sourceStatuses, s.status)}</select><button class="btn" type="button" data-del="${esc(s.id)}">Xóa</button>`:''}</div>
      </div>`;
    }).join('') || '<p class="muted">Chưa có nguồn nào khớp bộ lọc.</p>';
  }
  $('#s-list').addEventListener('click', ev => {
    const pb = ev.target.closest('[data-play]');
    if (pb) { const e = embed(pb.dataset.play); pb.parentElement.innerHTML = iframe(e); return; }
    const del = ev.target.closest('[data-del]');
    if (del && confirm('Xóa nguồn này khỏi máy này?')) { local = local.filter(s => s.id !== del.dataset.del); save(); render(); }
  });
  $('#s-list').addEventListener('change', ev => {
    const sel = ev.target.closest('[data-st]'); if (!sel) return;
    const it = local.find(s => s.id === sel.dataset.st); if (it) { it.status = sel.value; save(); render(); }
  });
  let tmr;
  $('#s-url').addEventListener('input', () => {
    clearTimeout(tmr);
    tmr = setTimeout(() => {
      const u = $('#s-url').value.trim(), e = embed(u);
      $('#s-preview').innerHTML = !u ? '' : e ? `<div class="muted small" style="margin-bottom:6px">Xem trước · ${platform(u)}</div><div class="src-media">${iframe(e)}</div>` : `<div class="src-media"><div class="hint">${esc(shortHint(u))}</div></div>`;
      const m = u.match(/tiktok\.com\/@([\w.\-]+)/); if (m && !$('#s-author').value) $('#s-author').value = '@'+m[1];
    }, 350);
  });
  $('#s-add').onclick = () => {
    const u = $('#s-url').value.trim();
    if (!/^https?:\/\//i.test(u)) { $('#s-msg').textContent = 'Cần dán một link bắt đầu bằng http.'; return; }
    if (all().some(s => s.url === u)) { $('#s-msg').textContent = 'Link này đã có trong danh sách.'; return; }
    const d = new Date();
    local.unshift({ id:'M'+d.getTime().toString(36).slice(-5).toUpperCase(), added:d.toISOString().slice(0,10), url:u,
      author:$('#s-author').value.trim(), type:$('#s-type').value, apply:$('#s-apply').value, views:+$('#s-views').value||null,
      learned:$('#s-learned').value.trim(), idea:$('#s-idea').value.trim(), status:'Mới', by:'' });
    save();
    ['s-url','s-author','s-views','s-learned','s-idea'].forEach(id => $('#'+id).value = '');
    $('#s-preview').innerHTML = ''; $('#s-msg').textContent = 'Đã thêm.'; setTimeout(() => $('#s-msg').textContent = '', 1500);
    render();
  };
  $('#s-copy').onclick = ev => {
    if (!local.length) { alert('Chưa có mục nào thêm trên máy này.'); return; }
    const txt = 'Thêm các nguồn content sau vào nguon-content.json:\n' + JSON.stringify(local, null, 1);
    const b = ev.currentTarget;
    const done = () => { const o = b.textContent; b.textContent = 'Đã chép – dán vào chat với Claude'; setTimeout(() => b.textContent = o, 2000); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(done, () => prompt('Chép thủ công:', txt)); else prompt('Chép thủ công:', txt);
  };
  $('#s-export').onclick = () => {
    const blob = new Blob([JSON.stringify(all().map(({_local, ...s}) => s), null, 2)], {type:'application/json'});
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'nguon-content-' + new Date().toISOString().slice(0,10) + '.json';
    document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  };
  $('#s-import').onchange = ev => {
    const f = ev.target.files[0]; if (!f) return;
    const rd = new FileReader();
    rd.onload = () => {
      try {
        const arr = JSON.parse(rd.result); const known = new Set(all().map(s => s.url)); let n = 0;
        (Array.isArray(arr) ? arr : []).forEach(s => { if (s && s.url && !known.has(s.url)) { local.push({ status:'Mới', ...s, id: s.id || ('M'+(Date.now()+n).toString(36).slice(-5).toUpperCase()) }); known.add(s.url); n++; } });
        save(); render(); alert('Đã nhập ' + n + ' nguồn mới.');
      } catch (e) { alert('File không đúng định dạng .json'); }
      ev.target.value = '';
    };
    rd.readAsText(f);
  };
  ['sq','splat','sapply','sstat'].forEach(id => $('#'+id).addEventListener('input', render));
  render();
})();

const start = (location.hash||'').slice(1) || store.get('tab','tong');
show(TABS.some(t=>t[0]===start) ? start : 'tong');
})();
</script>
</body>
</html>"""


def build(path):
    data = json.dumps(payload(), ensure_ascii=False, default=str).replace("</", "<\\/")
    open(path, "w", encoding="utf-8").write(HTML.replace("__DATA__", data))
    return path
