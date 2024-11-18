# 🤖 XMRig Telegram Monitor

Monitor performa mining XMRig Anda secara real-time melalui Telegram bot. Dapatkan informasi lengkap tentang hashrate, penggunaan sistem, dan status mining dalam format yang mudah dibaca.

## ✨ Fitur Utama

- 📊 Monitoring hashrate real-time
- 🖥️ Informasi penggunaan CPU & Memory
- 📈 Statistik shares dan performa
- ⚡ Alert status koneksi pool
- 🕒 Laporan uptime mining
- 📱 Notifikasi melalui Telegram

## 🛠️ Persyaratan Sistem

- Python 3.6+
- XMRig dengan API aktif
- Bot Telegram
- Paket Python yang diperlukan:
  - requests
  - datetime

## 📦 Instalasi

1. Clone repository
```bash
git clone https://github.com/classyid/xmrig-telegram-monitor.git
cd xmrig-telegram-monitor
```

2. Install dependencies
```bash
pip3 install -r requirements.txt
```

3. Konfigurasi bot Telegram:
   - Buat bot baru melalui [@BotFather](https://t.me/botfather)
   - Salin token bot
   - Dapatkan chat ID Anda
   - Update konfigurasi di `monitor.py`

## ⚙️ Konfigurasi

1. Buka file `monitor.py`
2. Update variabel berikut:
```python
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
XMRIG_API_URL = "http://localhost:18000/1/summary"
```

## 🚀 Penggunaan

### Menjalankan Script
```bash
python3 monitor.py
```

### Mengatur Jadwal Monitoring
Tambahkan ke crontab untuk monitoring otomatis:
```bash
# Monitor setiap 30 menit
*/30 * * * * /usr/bin/python3 /path/to/monitor.py
```

## 📊 Contoh Output
```
📊 Status Mining XMRig

🖥️ Informasi Sistem:
• Worker: worker01
• CPU: AMD EPYC 7402P
• Threads: 48
• Memory Total: 62.52 GB
• Memory Tersedia: 5.82 GB

⚡ Performa Mining:
• Hashrate Saat Ini: 8623.33 H/s
• Hashrate Tertinggi: 8711.24 H/s
• Hash Terbaik: 79952045
• Shares Diterima: 82
• Total Shares: 82

🌐 Informasi Koneksi:
• Pool: pool.hashvault.pro:80
• Waktu Aktif: 0d 0h 30m
```

## 📝 Catatan Penting

- Pastikan API XMRig sudah diaktifkan
- Jaga keamanan token bot Telegram
- Monitor penggunaan bandwidth
- Sesuaikan interval monitoring dengan kebutuhan
