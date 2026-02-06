app.get("/", (_, res) => {
  res.send(`
<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <title>ThaiPay</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f6f8;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .app {
      background: #fff;
      width: 360px;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    h1 {
      text-align: center;
      margin-bottom: 20px;
    }
    button {
      width: 100%;
      padding: 12px;
      margin-top: 10px;
      border: none;
      border-radius: 8px;
      background: #0d6efd;
      color: white;
      font-size: 16px;
      cursor: pointer;
    }
    button.secondary {
      background: #198754;
    }
    .box {
      margin-top: 12px;
      padding: 10px;
      background: #f1f1f1;
      border-radius: 8px;
      font-size: 14px;
      word-break: break-all;
    }
    .balance {
      font-size: 22px;
      text-align: center;
      margin-top: 10px;
    }
  </style>
</head>
<body>

<div class="app">
  <h1>ThaiPay</h1>

  <button onclick="register()">สร้างกระเป๋าเงิน</button>

  <div id="userBox" class="box" style="display:none;"></div>

  <button class="secondary" onclick="checkBalance()">เช็กยอดเงิน</button>

  <div id="balance" class="balance">0 THB</div>
</div>

<script>
let userId = "";

async function register() {
  const r = await fetch("/api/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({})
  });
  const d = await r.json();
  userId = d.userId;
  document.getElementById("userBox").style.display = "block";
  document.getElementById("userBox").innerText = "User ID: " + userId;
}

async function checkBalance() {
  if (!userId) {
    alert("กรุณาสร้างกระเป๋าเงินก่อน");
    return;
  }
  const r = await fetch("/api/balance/" + userId);
  const d = await r.json();
  document.getElementById("balance").innerText = d.balance + " THB";
}
</script>

</body>
</html>
  `);
});
