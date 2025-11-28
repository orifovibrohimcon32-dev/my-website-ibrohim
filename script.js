// app.js — кор бо Telegram WebApp API
const tg = window.Telegram?.WebApp;
if (tg) {
  tg.expand(); // дар мобайл беҳтар намоиш диҳад
  document.getElementById('status').innerText = 'Кушода дар Telegram: ready';
} else {
  document.getElementById('status').innerText = 'Нотавон ба WebApp API — лутфан дар Telegram кушоед';
}

// Ҳар тугмаи фармоишро гир
document.querySelectorAll('.item button').forEach(btn => {
  btn.addEventListener('click', () => {
    const name = btn.dataset.name;
    const price = btn.dataset.price;

    const order = {
      item: name,
      price: price,
      time: new Date().toISOString()
    };

    // Маъломотро ба бот фиристед — ҳамчун сатр (string)
    if (tg && tg.sendData) {
      tg.sendData(JSON.stringify(order));
      // Опсионал: паёмро дар WebApp нишон деҳ ва пӯш
      tg.close();
    } else {
      alert('Ин WebApp дар Telegram кушода нашудааст. Барои санҷиш — ботро ба кор фармоед ва кнопкаи "Open menu" -ро пахш кунед.');
    }
  });
});