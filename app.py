<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Finance Tracker</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f0f4f8;
      color: #1a1a2e;
      min-height: 100vh;
    }

    /* ── Auth Screen ── */
    #auth-screen {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      background: linear-gradient(135deg, #1a1a2e, #0f3460);
    }

    .auth-box {
      background: white;
      border-radius: 16px;
      padding: 40px;
      width: 380px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }

    .auth-box h1 {
      text-align: center;
      font-size: 22px;
      color: #1a1a2e;
      margin-bottom: 6px;
    }

    .auth-box p.subtitle {
      text-align: center;
      color: #888;
      font-size: 13px;
      margin-bottom: 24px;
    }

    .tab-btns {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
    }

    .tab-btn {
      flex: 1;
      padding: 8px;
      border: 2px solid #e0e0e0;
      background: white;
      border-radius: 8px;
      font-size: 13px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .tab-btn.active {
      background: #1a1a2e;
      color: white;
      border-color: #1a1a2e;
    }

    .auth-form { display: none; }
    .auth-form.active { display: block; }

    .form-group { margin-bottom: 14px; }

    .form-group label {
      display: block;
      font-size: 12px;
      font-weight: 600;
      color: #555;
      margin-bottom: 5px;
    }

    .form-group input, .form-group select {
      width: 100%;
      padding: 10px 12px;
      border: 1.5px solid #e0e0e0;
      border-radius: 8px;
      font-size: 14px;
      transition: border 0.2s;
      outline: none;
    }

    .form-group input:focus { border-color: #0f3460; }

    .btn-primary {
      width: 100%;
      padding: 12px;
      background: #1a1a2e;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      margin-top: 6px;
      transition: background 0.2s;
    }

    .btn-primary:hover { background: #0f3460; }

    .auth-msg {
      text-align: center;
      font-size: 13px;
      margin-top: 12px;
      min-height: 20px;
    }

    .auth-msg.error { color: #c0392b; }
    .auth-msg.success { color: #2b8a3e; }

    /* ── App Screen ── */
    #app-screen { display: none; }

    header {
      background: #1a1a2e;
      color: white;
      padding: 14px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    header h1 { font-size: 18px; }

    .header-right {
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 13px;
    }

    .btn-logout {
      background: #e94560;
      color: white;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 13px;
    }

    /* ── Warning Banner ── */
    #warning-banner {
      display: none;
      background: #fff3cd;
      border-left: 4px solid #f0a500;
      padding: 10px 24px;
      font-size: 13px;
      color: #856404;
    }

    /* ── Stats Bar ── */
    .stats-bar {
      display: flex;
      gap: 16px;
      padding: 16px 24px;
      background: white;
      border-bottom: 1px solid #e0e0e0;
    }

    .stat-card {
      flex: 1;
      background: #f8faff;
      border: 1px solid #e0e8ff;
      border-radius: 10px;
      padding: 14px 18px;
      text-align: center;
    }

    .stat-card .label {
      font-size: 11px;
      color: #888;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .stat-card .value {
      font-size: 22px;
      font-weight: 700;
      color: #1a1a2e;
      margin-top: 4px;
    }

    .stat-card .value.danger { color: #c0392b; }
    .stat-card .value.success { color: #2b8a3e; }

    /* ── Main Layout ── */
    .main {
      display: flex;
      gap: 20px;
      padding: 20px 24px;
      max-width: 1200px;
      margin: 0 auto;
    }

    /* ── Add Expense Form ── */
    .add-panel {
      width: 300px;
      flex-shrink: 0;
    }

    .panel {
      background: white;
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      margin-bottom: 16px;
    }

    .panel h2 {
      font-size: 14px;
      font-weight: 700;
      color: #1a1a2e;
      margin-bottom: 14px;
      border-bottom: 2px solid #f0f4f8;
      padding-bottom: 8px;
    }

    .btn-add {
      width: 100%;
      padding: 11px;
      background: #2b8a3e;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      margin-top: 6px;
    }

    .btn-add:hover { background: #237832; }

    .btn-budget {
      width: 100%;
      padding: 11px;
      background: #0f3460;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      margin-top: 6px;
    }

    /* ── Expenses Table ── */
    .expenses-panel { flex: 1; }

    .expenses-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }

    thead th {
      background: #1a1a2e;
      color: white;
      padding: 10px 12px;
      text-align: left;
      font-weight: 600;
    }

    tbody tr { transition: background 0.15s; }
    tbody tr:nth-child(even) { background: #f8faff; }
    tbody tr:hover { background: #e8f0fe; }

    tbody td {
      padding: 10px 12px;
      border-bottom: 1px solid #f0f0f0;
      vertical-align: middle;
    }

    .category-badge {
      display: inline-block;
      padding: 2px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 600;
      background: #e8f0fe;
      color: #0f3460;
    }

    .btn-delete {
      background: #fdecea;
      color: #c0392b;
      border: none;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 12px;
    }

    .btn-delete:hover { background: #c0392b; color: white; }

    /* ── Chart ── */
    .chart-container {
      position: relative;
      height: 220px;
    }

    #empty-state {
      text-align: center;
      color: #aaa;
      padding: 40px 20px;
      font-size: 14px;
    }
  </style>
</head>
<body>

<!-- ══════════════ AUTH SCREEN ══════════════ -->
<div id="auth-screen">
  <div class="auth-box">
    <h1>💰 Finance Tracker</h1>
    <p class="subtitle">Manage your expenses securely</p>

    <div class="tab-btns">
      <button class="tab-btn active" onclick="switchTab('login')">Login</button>
      <button class="tab-btn" onclick="switchTab('register')">Register</button>
      <button class="tab-btn" onclick="switchTab('recover')">Recover</button>
    </div>

    <!-- Login -->
    <div class="auth-form active" id="form-login">
      <div class="form-group">
        <label>Username</label>
        <input type="text" id="login-username" placeholder="Enter username"/>
      </div>
      <div class="form-group">
        <label>6-Digit PIN</label>
        <input type="password" id="login-pin" maxlength="6" placeholder="••••••"/>
      </div>
      <button class="btn-primary" onclick="login()">Login</button>
      <p class="auth-msg" id="login-msg"></p>
    </div>

    <!-- Register -->
    <div class="auth-form" id="form-register">
      <div class="form-group">
        <label>Username</label>
        <input type="text" id="reg-username" placeholder="Choose a username"/>
      </div>
      <div class="form-group">
        <label>6-Digit PIN</label>
        <input type="password" id="reg-pin" maxlength="6" placeholder="••••••"/>
      </div>
      <div class="form-group">
        <label>Recovery Word</label>
        <input type="text" id="reg-recovery" placeholder="A word to recover your account"/>
      </div>
      <button class="btn-primary" onclick="register()">Create Account</button>
      <p class="auth-msg" id="reg-msg"></p>
    </div>

    <!-- Recover -->
    <div class="auth-form" id="form-recover">
      <div class="form-group">
        <label>Username</label>
        <input type="text" id="rec-username" placeholder="Your username"/>
      </div>
      <div class="form-group">
        <label>Recovery Word</label>
        <input type="text" id="rec-word" placeholder="Your recovery word"/>
      </div>
      <div class="form-group">
        <label>New 6-Digit PIN</label>
        <input type="password" id="rec-pin" maxlength="6" placeholder="••••••"/>
      </div>
      <button class="btn-primary" onclick="recover()">Reset PIN</button>
      <p class="auth-msg" id="rec-msg"></p>
    </div>
  </div>
</div>

<!-- ══════════════ APP SCREEN ══════════════ -->
<div id="app-screen">
  <header>
    <h1>💰 Finance Tracker</h1>
    <div class="header-right">
      <span id="header-username"></span>
      <button class="btn-logout" onclick="logout()">Logout</button>
    </div>
  </header>

  <div id="warning-banner"></div>

  <!-- Stats -->
  <div class="stats-bar">
    <div class="stat-card">
      <div class="label">Total Spent</div>
      <div class="value danger" id="stat-total">₹0.00</div>
    </div>
    <div class="stat-card">
      <div class="label">Budget Limit</div>
      <div class="value" id="stat-budget">Not Set</div>
    </div>
    <div class="stat-card">
      <div class="label">Remaining</div>
      <div class="value success" id="stat-remaining">—</div>
    </div>
    <div class="stat-card">
      <div class="label">Total Expenses</div>
      <div class="value" id="stat-count">0</div>
    </div>
  </div>

  <div class="main">

    <!-- Left Panel -->
    <div class="add-panel">

      <!-- Add Expense -->
      <div class="panel">
        <h2>➕ Add Expense</h2>
        <div class="form-group">
          <label>Title *</label>
          <input type="text" id="exp-title" placeholder="e.g. Lunch, Rent"/>
        </div>
        <div class="form-group">
          <label>Amount (₹) *</label>
          <input type="number" id="exp-amount" placeholder="0.00" min="1"/>
        </div>
        <div class="form-group">
          <label>Category</label>
          <select id="exp-category">
            <option>Food</option>
            <option>Transport</option>
            <option>Shopping</option>
            <option>Entertainment</option>
            <option>Education</option>
            <option>Health</option>
            <option>Utilities</option>
            <option>General</option>
          </select>
        </div>
        <div class="form-group">
          <label>Date</label>
          <input type="date" id="exp-date"/>
        </div>
        <div class="form-group">
          <label>Description</label>
          <input type="text" id="exp-desc" placeholder="Optional note"/>
        </div>
        <button class="btn-add" onclick="addExpense()">Add Expense</button>
        <p class="auth-msg" id="exp-msg"></p>
      </div>

      <!-- Set Budget -->
      <div class="panel">
        <h2>🎯 Set Monthly Budget</h2>
        <div class="form-group">
          <label>Budget Limit (₹)</label>
          <input type="number" id="budget-input" placeholder="e.g. 10000"/>
        </div>
        <button class="btn-budget" onclick="setBudget()">Set Budget</button>
      </div>

      <!-- Chart -->
      <div class="panel">
        <h2>📊 Spending by Category</h2>
        <div class="chart-container">
          <canvas id="pie-chart"></canvas>
        </div>
      </div>
    </div>

    <!-- Expenses Table -->
    <div class="expenses-panel">
      <div class="panel">
        <div class="expenses-header">
          <h2 style="margin:0; border:none; padding:0;">📋 Expense Records</h2>
        </div>
        <div id="expense-table-wrapper">
          <div id="empty-state">No expenses yet. Add your first expense!</div>
          <table id="expense-table" style="display:none;">
            <thead>
              <tr>
                <th>#</th>
                <th>Title</th>
                <th>Amount</th>
                <th>Category</th>
                <th>Date</th>
                <th>Description</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody id="expense-tbody"></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  let USER_ID = null;
  let USERNAME = "";
  let BUDGET = 0;
  let pieChart = null;

  // ── Set today's date ──────────────────────────────────────────────────────
  document.getElementById("exp-date").value = new Date().toISOString().split("T")[0];

  // ── Tab Switching ─────────────────────────────────────────────────────────
  function switchTab(tab) {
    document.querySelectorAll(".tab-btn").forEach((b, i) => {
      b.classList.toggle("active", ["login","register","recover"][i] === tab);
    });
    document.querySelectorAll(".auth-form").forEach(f => f.classList.remove("active"));
    document.getElementById("form-" + tab).classList.add("active");
  }

  // ── Auth ──────────────────────────────────────────────────────────────────
  async function register() {
    const res = await fetch("/register", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        username:      document.getElementById("reg-username").value,
        pin:           document.getElementById("reg-pin").value,
        recovery_word: document.getElementById("reg-recovery").value
      })
    });
    const data = await res.json();
    const msg  = document.getElementById("reg-msg");
    msg.textContent = data.message || data.error;
    msg.className   = "auth-msg " + (res.ok ? "success" : "error");
    if (res.ok) setTimeout(() => switchTab("login"), 1200);
  }

  async function login() {
    const res = await fetch("/login", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        username: document.getElementById("login-username").value,
        pin:      document.getElementById("login-pin").value
      })
    });
    const data = await res.json();
    if (!res.ok) {
      const msg = document.getElementById("login-msg");
      msg.textContent = data.error;
      msg.className   = "auth-msg error";
      return;
    }
    USER_ID  = data.user_id;
    USERNAME = data.username;
    BUDGET   = data.budget_limit || 0;
    document.getElementById("auth-screen").style.display = "none";
    document.getElementById("app-screen").style.display  = "block";
    document.getElementById("header-username").textContent = "👤 " + USERNAME;
    if (BUDGET > 0) document.getElementById("budget-input").value = BUDGET;
    loadExpenses();
  }

  async function recover() {
    const res = await fetch("/recover", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        username:      document.getElementById("rec-username").value,
        recovery_word: document.getElementById("rec-word").value,
        new_pin:       document.getElementById("rec-pin").value
      })
    });
    const data = await res.json();
    const msg  = document.getElementById("rec-msg");
    msg.textContent = data.message || data.error;
    msg.className   = "auth-msg " + (res.ok ? "success" : "error");
  }

  function logout() {
    USER_ID  = null;
    USERNAME = "";
    BUDGET   = 0;
    document.getElementById("app-screen").style.display  = "none";
    document.getElementById("auth-screen").style.display = "flex";
    document.getElementById("login-username").value = "";
    document.getElementById("login-pin").value      = "";
  }

  // ── Expenses ──────────────────────────────────────────────────────────────
  async function loadExpenses() {
    const res      = await fetch(`/expenses/${USER_ID}`);
    const expenses = await res.json();
    const tbody    = document.getElementById("expense-tbody");
    const table    = document.getElementById("expense-table");
    const empty    = document.getElementById("empty-state");

    tbody.innerHTML = "";

    if (expenses.length === 0) {
      table.style.display = "none";
      empty.style.display = "block";
    } else {
      table.style.display = "";
      empty.style.display = "none";
      expenses.forEach((e, i) => {
        tbody.innerHTML += `
          <tr>
            <td>${i + 1}</td>
            <td><b>${e.title}</b></td>
            <td><b>₹${e.amount.toFixed(2)}</b></td>
            <td><span class="category-badge">${e.category}</span></td>
            <td>${e.date}</td>
            <td>${e.description || "—"}</td>
            <td><button class="btn-delete" onclick="deleteExpense(${e.id})">🗑 Delete</button></td>
          </tr>`;
      });
    }

    document.getElementById("stat-count").textContent = expenses.length;
    await loadTotal();
    await loadChart();
  }

  async function addExpense() {
    const title  = document.getElementById("exp-title").value.trim();
    const amount = document.getElementById("exp-amount").value;
    const msg    = document.getElementById("exp-msg");

    if (!title || !amount) {
      msg.textContent = "Title and amount are required.";
      msg.className   = "auth-msg error";
      return;
    }

    const res  = await fetch(`/expenses/${USER_ID}`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        title,
        amount: parseFloat(amount),
        category:    document.getElementById("exp-category").value,
        description: document.getElementById("exp-desc").value,
        date:        document.getElementById("exp-date").value
      })
    });
    const data = await res.json();

    msg.textContent = data.message || data.error;
    msg.className   = "auth-msg " + (res.ok ? "success" : "error");

    if (res.ok) {
      document.getElementById("exp-title").value  = "";
      document.getElementById("exp-amount").value = "";
      document.getElementById("exp-desc").value   = "";
      if (data.warning) showWarning(data.warning);
      await loadExpenses();
    }
  }

  async function deleteExpense(id) {
    if (!confirm("Delete this expense?")) return;
    await fetch(`/expenses/${id}`, { method: "DELETE" });
    document.getElementById("warning-banner").style.display = "none";
    await loadExpenses();
  }

  async function loadTotal() {
    const res  = await fetch(`/expenses/total/${USER_ID}`);
    const data = await res.json();
    const total   = data.total_spent;
    const budget  = data.budget_limit;
    BUDGET = budget;

    document.getElementById("stat-total").textContent = "₹" + total.toFixed(2);

    if (budget > 0) {
      document.getElementById("stat-budget").textContent    = "₹" + budget.toFixed(2);
      const remaining = budget - total;
      const remEl = document.getElementById("stat-remaining");
      remEl.textContent = "₹" + Math.abs(remaining).toFixed(2) + (remaining < 0 ? " over" : " left");
      remEl.className   = "value " + (remaining < 0 ? "danger" : "success");
    } else {
      document.getElementById("stat-budget").textContent    = "Not Set";
      document.getElementById("stat-remaining").textContent = "—";
    }
  }

  async function setBudget() {
    const limit = parseFloat(document.getElementById("budget-input").value);
    if (!limit || limit <= 0) return alert("Enter a valid budget amount.");
    await fetch(`/budget/${USER_ID}`, {
      method: "PUT",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ budget_limit: limit })
    });
    BUDGET = limit;
    await loadTotal();
  }

  async function loadChart() {
    const res  = await fetch(`/expenses/summary/${USER_ID}`);
    const data = await res.json();

    const labels = data.map(d => d.category);
    const values = data.map(d => d.total);
    const colors = ["#1a1a2e","#0f3460","#e94560","#2b8a3e","#f0a500","#533483","#16213e","#237832"];

    if (pieChart) pieChart.destroy();

    if (data.length === 0) return;

    pieChart = new Chart(document.getElementById("pie-chart"), {
      type: "doughnut",
      data: {
        labels,
        datasets: [{
          data: values,
          backgroundColor: colors.slice(0, labels.length),
          borderWidth: 2,
          borderColor: "#fff"
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { position: "bottom", labels: { font: { size: 11 } } }
        }
      }
    });
  }

  function showWarning(msg) {
    const banner = document.getElementById("warning-banner");
    banner.textContent    = msg;
    banner.style.display  = "block";
  }
</script>
</body>
</html>
