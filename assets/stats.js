/* =====================================================================
   Thống kê lượt đọc CODEPLUS Books  (Firebase Realtime Database)
   - Tổng lượt truy cập, số người truy cập khác nhau, số người đang online
   - Từng tập sách: lượt mở đọc trên web, số người đọc khác nhau,
     lượt bấm "Mở đọc toàn màn hình" (sang Google Drive), thời gian đọc thật
   - Chỉ tài khoản quản trị (Firebase Authentication) mới XEM được số liệu.
     Người đọc chỉ CỘNG được lượt đếm, không xem / sửa / xóa được.
   ===================================================================== */
import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js';
import { getDatabase, ref, set, get, update, onValue, onDisconnect, increment, serverTimestamp }
  from 'https://www.gstatic.com/firebasejs/10.12.2/firebase-database.js';
import { getAuth, signInWithEmailAndPassword, signOut, onAuthStateChanged, setPersistence, browserSessionPersistence }
  from 'https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js';

const firebaseConfig = {
  apiKey: 'AIzaSyBzaYyW8yyDCY4FgsS55GNLK0BvW3-6d4I',
  authDomain: 'website-d9529.firebaseapp.com',
  databaseURL: 'https://website-d9529-default-rtdb.asia-southeast1.firebasedatabase.app',
  projectId: 'website-d9529',
  storageBucket: 'website-d9529.firebasestorage.app',
  messagingSenderId: '166077487269',
  appId: '1:166077487269:web:b5f48ffd4cee9400fb554c'
};
const READ_TICK = 15;          // giây: mỗi 15 giây đang đọc thật thì cộng 15 giây

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const auth = getAuth(app);

/* ---------------- ai được đếm ---------------- */
function store(k, v) { try { if (v === undefined) return localStorage.getItem('cp.' + k); if (v === null) localStorage.removeItem('cp.' + k); else localStorage.setItem('cp.' + k, v); } catch (e) { return null; } }
const BOT = /bot|crawl|spider|slurp|facebookexternalhit|zalo|preview|headless|lighthouse|pingdom|curl|wget|python|axios/i;
const isBot = navigator.webdriver || BOT.test(navigator.userAgent || '');
const isAdminDevice = () => store('noTrack') === '1';   // máy quản trị không tự đếm mình
const tracking = () => !isBot && !isAdminDevice();

function rid(n) { const a = new Uint8Array(n); crypto.getRandomValues(a); return Array.from(a, x => (x % 36).toString(36)).join(''); }
let VID = store('vid');
const newVisitor = !VID;
if (!VID) { VID = rid(20); store('vid', VID); }
const SID = rid(20);                                     // mỗi tab một phiên
const today = () => { const d = new Date(Date.now() + 7 * 3600e3); return d.toISOString().slice(0, 10); }; // giờ Việt Nam

// cộng trên máy chủ (không cần quyền đọc; quy tắc chỉ cho phép +1 hoặc +15 giây)
function inc(path, by = 1) {
  return update(ref(db), { [path]: increment(by) }).catch(e => console.warn('stats', path, e.message));
}
function once(path) {      // ghi một lần (người khác nhau); đã có thì thôi
  return set(ref(db, path), true).catch(() => {});
}
const key = (bookId, vIdx) => String(bookId).replace(/[.#$\[\]\/]/g, '_') + '_v' + (Number(vIdx) + 1);

/* ---------------- 1. lượt truy cập + đang online ---------------- */
function trackVisit() {
  if (!tracking()) return;
  // chỉ tính 1 lượt / tab / 30 phút (tải lại trang không bị cộng dồn)
  let last = 0; try { last = +sessionStorage.getItem('cp.visitAt') || 0; } catch (e) {}
  if (Date.now() - last > 30 * 60e3) {
    try { sessionStorage.setItem('cp.visitAt', String(Date.now())); } catch (e) {}
    inc('c/visits'); inc('c/day/' + today() + '/visits');
    if (newVisitor) { once('u/visitors/' + VID); inc('c/day/' + today() + '/newVisitors'); }
    else once('u/visitors/' + VID);
    once('u/day/' + today() + '/' + VID);
    const q = new URLSearchParams(location.search), src = q.get('sach');
    if (src) inc('c/landing/' + src.replace(/[.#$\[\]\/]/g, '_'));
  }
  const me = ref(db, 'presence/' + SID);
  onValue(ref(db, '.info/connected'), s => {
    if (s.val() !== true) return;
    onDisconnect(me).remove().then(() => set(me, serverTimestamp())).catch(() => {});
  });
}

/* ---------------- 2. đọc sách ---------------- */
const opened = new Set();
function trackRead(bookId, vIdx, frameBox) {
  if (!tracking()) return;
  const k = key(bookId, vIdx);
  if (!opened.has(k)) {               // mở lại cùng tập trong 1 phiên không cộng thêm
    opened.add(k);
    inc('c/vol/' + k + '/reads'); inc('c/day/' + today() + '/reads');
    once('u/readers/' + k + '/' + VID);
  }
  if (frameBox) watchTime(k, frameBox);
}
function trackFull(bookId, vIdx) {
  if (!tracking()) return;
  const k = key(bookId, vIdx);
  inc('c/vol/' + k + '/full'); inc('c/day/' + today() + '/full');
  once('u/readers/' + k + '/' + VID);
}
// thời gian đọc: chỉ cộng khi khung đọc đang hiện ≥ 50% trên màn hình VÀ tab đang được xem
function watchTime(k, box) {
  if (box.__cpWatch) return; box.__cpWatch = true;
  let visible = false, acc = 0;
  new IntersectionObserver(es => { visible = es[0].isIntersecting && es[0].intersectionRatio >= 0.5; }, { threshold: [0, 0.5, 1] }).observe(box);
  setInterval(() => {
    if (!visible || document.visibilityState !== 'visible') return;
    acc += 1;
    if (acc >= READ_TICK) { acc = 0; inc('c/vol/' + k + '/sec', READ_TICK); }
  }, 1000);
}

/* ---------------- 3. quản trị: đăng nhập + bảng thống kê ---------------- */
setPersistence(auth, browserSessionPersistence).catch(() => {});
let adminUser = null;
onAuthStateChanged(auth, u => { adminUser = u; });

async function adminLogin(email, pass) {
  const cred = await signInWithEmailAndPassword(auth, email.trim(), pass);
  // kiểm tra thật sự có quyền đọc số liệu (quy tắc trên máy chủ chỉ cho UID quản trị)
  await get(ref(db, 'c/visits'));
  store('noTrack', '1');
  return cred.user;
}
async function adminLogout() { await signOut(auth); }

const fmt = n => (n || 0).toLocaleString('vi-VN');
const mins = s => { s = s || 0; const h = Math.floor(s / 3600), m = Math.round((s % 3600) / 60); return h ? `${h} giờ ${m} phút` : `${m} phút`; };
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const count = o => (o ? Object.keys(o).length : 0);

let liveUnsub = null;
function closeStats() {
  const m = document.getElementById('cpStatsModal'); if (m) m.remove();
  if (liveUnsub) { liveUnsub(); liveUnsub = null; }
}
async function openStats() {
  closeStats();
  const wrap = document.createElement('div');
  wrap.id = 'cpStatsModal';
  wrap.className = 'fixed inset-0 bg-slate-900/80 z-50 flex items-start justify-center p-3 sm:p-6 overflow-y-auto';
  wrap.innerHTML = `<div class="bg-white rounded-2xl shadow-2xl max-w-5xl w-full my-4 border border-slate-200 overflow-hidden">
    <div class="px-6 py-4 bg-slate-900 text-white flex items-center justify-between">
      <div class="flex items-center gap-2.5"><i class="fas fa-chart-line text-emerald-400 text-xl"></i>
        <div><h2 class="text-base sm:text-lg font-extrabold">Thống kê người đọc</h2>
        <p class="text-xs text-slate-400" id="cpStUser"></p></div></div>
      <div class="flex gap-2">
        <button id="cpStReload" class="px-3 h-8 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold"><i class="fas fa-rotate-right mr-1"></i>Làm mới</button>
        <button id="cpStClose" class="w-8 h-8 rounded-full bg-slate-800 hover:bg-red-500 text-slate-300 hover:text-white"><i class="fas fa-times"></i></button></div>
    </div>
    <div class="p-5 sm:p-6" id="cpStBody"><p class="text-sm text-slate-500"><i class="fas fa-circle-notch fa-spin mr-2"></i>Đang tải số liệu…</p></div></div>`;
  document.body.appendChild(wrap);
  wrap.querySelector('#cpStClose').onclick = closeStats;
  wrap.querySelector('#cpStReload').onclick = openStats;
  wrap.querySelector('#cpStUser').textContent = adminUser ? 'Đăng nhập: ' + adminUser.email : '';
  try {
    const [cS, uS] = await Promise.all([get(ref(db, 'c')), get(ref(db, 'u'))]);
    renderStats(cS.val() || {}, uS.val() || {});
    const pres = ref(db, 'presence');
    liveUnsub = onValue(pres, s => {
      const el = document.getElementById('cpOnline');
      if (el) el.textContent = fmt(count(s.val()));
    });
  } catch (e) {
    wrap.querySelector('#cpStBody').innerHTML = `<div class="p-4 rounded-xl bg-red-50 text-red-700 text-sm font-bold">Không đọc được số liệu: ${esc(e.message)}</div>`;
  }
}

function renderStats(c, u) {
  const books = window.BOOKS_DATA_REF ? window.BOOKS_DATA_REF() : [];
  const vol = c.vol || {}, readers = u.readers || {};
  const rows = books.map(b => {
    const vols = b.vols.map((v, i) => {
      const k = key(b.id, i), x = vol[k] || {};
      return { name: v.name || `TẬP ${i + 1}`, reads: x.reads || 0, full: x.full || 0, sec: x.sec || 0, uniq: count(readers[k]) };
    });
    const uni = new Set(); b.vols.forEach((v, i) => Object.keys(readers[key(b.id, i)] || {}).forEach(id => uni.add(id)));
    const sum = f => vols.reduce((a, v) => a + v[f], 0);
    return { title: b.title, vols, reads: sum('reads'), full: sum('full'), sec: sum('sec'), uniq: uni.size, landing: (c.landing || {})[b.id] || 0 };
  });
  const by = window.__cpSort || 'uniq';
  rows.sort((a, b) => b[by] - a[by] || b.reads - a.reads);
  const days = Object.keys(c.day || {}).sort().slice(-14);
  const dmax = Math.max(1, ...days.map(d => (c.day[d].visits || 0)));
  const t = today(), td = (c.day || {})[t] || {};
  const card = (label, val, icon, color, id) => `<div class="p-4 rounded-2xl border border-slate-200 bg-slate-50">
      <div class="text-xs font-bold text-slate-500 flex items-center gap-1.5"><i class="fas ${icon} ${color}"></i>${label}</div>
      <div class="text-2xl font-black text-slate-900 mt-1" ${id ? `id="${id}"` : ''}>${val}</div></div>`;
  const th = (f, label) => `<th class="py-2 px-2 text-right cursor-pointer select-none ${by === f ? 'text-emerald-700' : ''}" data-sort="${f}">${label}${by === f ? ' ▼' : ''}</th>`;
  document.getElementById('cpStBody').innerHTML = `
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-6">
      ${card('Tổng lượt truy cập', fmt(c.visits), 'fa-eye', 'text-blue-600')}
      ${card('Số người truy cập (khác nhau)', fmt(count(u.visitors)), 'fa-users', 'text-purple-600')}
      ${card('Đang online', '…', 'fa-circle', 'text-emerald-500', 'cpOnline')}
      ${card('Hôm nay: lượt / người', fmt(td.visits) + ' / ' + fmt(count((u.day || {})[t])), 'fa-calendar-day', 'text-orange-500')}
    </div>
    <h3 class="text-sm font-black uppercase tracking-wider text-emerald-700 mb-2"><i class="fas fa-trophy mr-1.5"></i>Sách được đọc nhiều nhất</h3>
    <p class="text-xs text-slate-500 mb-3">Bấm tiêu đề cột để xếp hạng theo cột đó. <b>Người đọc</b> = số người khác nhau đã mở ít nhất một tập (mỗi người chỉ tính 1 lần cho mỗi bộ).</p>
    <div class="overflow-x-auto rounded-xl border border-slate-200 mb-6"><table class="w-full text-sm">
      <thead class="bg-slate-100 text-xs text-slate-600"><tr><th class="py-2 px-2 text-left">#</th><th class="py-2 px-2 text-left">Bộ sách</th>
        ${th('uniq', 'Người đọc')}${th('reads', 'Lượt mở trên web')}${th('full', 'Mở Google Drive')}${th('sec', 'Thời gian đọc')}${th('landing', 'Vào từ link riêng')}</tr></thead>
      <tbody>${rows.map((r, i) => `
        <tr class="border-t border-slate-200 ${i < 3 ? 'bg-emerald-50/50' : ''}">
          <td class="py-2 px-2 font-black ${i < 3 ? 'text-emerald-700' : 'text-slate-400'}">${i + 1}</td>
          <td class="py-2 px-2"><details><summary class="font-bold text-slate-800 cursor-pointer">${esc(r.title)}</summary>
            <table class="w-full text-xs mt-1 text-slate-600">${r.vols.map(v => `<tr><td class="py-0.5 pr-2">${esc(v.name)}</td>
              <td class="text-right pr-2">${fmt(v.uniq)} người</td><td class="text-right pr-2">${fmt(v.reads)} lượt</td>
              <td class="text-right pr-2">${fmt(v.full)} Drive</td><td class="text-right">${mins(v.sec)}</td></tr>`).join('')}</table></details></td>
          <td class="py-2 px-2 text-right font-black">${fmt(r.uniq)}</td><td class="py-2 px-2 text-right">${fmt(r.reads)}</td>
          <td class="py-2 px-2 text-right">${fmt(r.full)}</td><td class="py-2 px-2 text-right">${mins(r.sec)}</td><td class="py-2 px-2 text-right">${fmt(r.landing)}</td></tr>`).join('')}
      </tbody></table></div>
    <h3 class="text-sm font-black uppercase tracking-wider text-emerald-700 mb-3"><i class="fas fa-chart-column mr-1.5"></i>Lượt truy cập 14 ngày gần nhất</h3>
    <div class="space-y-1.5 mb-4">${days.length ? days.map(d => { const x = c.day[d]; return `
      <div class="flex items-center gap-2 text-xs"><span class="w-20 text-slate-500 shrink-0">${d.slice(8)}/${d.slice(5, 7)}</span>
        <div class="flex-1 bg-slate-100 rounded h-5 overflow-hidden"><div class="h-5 bg-emerald-500 rounded" style="width:${Math.round(100 * (x.visits || 0) / dmax)}%"></div></div>
        <span class="w-40 text-right text-slate-700 shrink-0"><b>${fmt(x.visits)}</b> lượt · ${fmt(count((u.day || {})[d]))} người · ${fmt(x.reads)} lượt đọc</span></div>`; }).join('') : '<p class="text-xs text-slate-400">Chưa có số liệu.</p>'}</div>
    <div class="text-xs text-slate-500 bg-slate-50 border border-slate-200 rounded-xl p-3 leading-relaxed">
      <b>Cách đếm:</b> 1 lượt truy cập / tab / 30 phút (tải lại trang không cộng thêm). "Người" được nhận theo trình duyệt: cùng một người dùng điện thoại và máy tính được tính là 2.
      "Lượt mở trên web" chỉ tính khi bấm <i>Đọc</i>. "Thời gian đọc" chỉ tính khi khung đọc đang hiện trên màn hình và tab đang mở. Bot và máy đã đăng nhập quản trị không được đếm.
      Lượt mở link Google Drive gửi trực tiếp (không qua website) không đếm được.
    </div>`;
  document.querySelectorAll('#cpStBody [data-sort]').forEach(h => h.onclick = () => { window.__cpSort = h.dataset.sort; renderStats(c, u); });
}

/* ---------------- công khai cho trang chính ---------------- */
window.cpStats = { read: trackRead, full: trackFull, login: adminLogin, logout: adminLogout, openStats, closeStats, user: () => adminUser };
trackVisit();
document.dispatchEvent(new Event('cpstats-ready'));
