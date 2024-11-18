import requests
import datetime

# Konfigurasi API Xmrig
xmrig_api_url = "http://localhost:18000/1/summary"
# Konfigurasi bot Telegram 
telegram_token = "YOUR_TELEGRAM_TOKEN"
chat_id = "YOUR_CHAT_ID"

def get_xmrig_status():
    try:
        response = requests.get(xmrig_api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching Xmrig data: {e}")
        return None

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(telegram_url, data=payload)
    except requests.RequestException as e:
        print(f"Error sending message to Telegram: {e}")

def format_bytes(bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} TB"

def format_timespan(seconds):
    """Convert seconds to readable time format"""
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    return f"{days}d {hours}h {minutes}m"

def main():
    xmrig_status = get_xmrig_status()
    if xmrig_status:
        # Sistem Info
        worker_id = xmrig_status.get("worker_id", "Unknown")
        cpu_info = xmrig_status.get("cpu", {})
        cpu_name = cpu_info.get("brand", "Unknown CPU")
        threads = cpu_info.get("threads", 0)
        
        # Mining Info
        hashrate_data = xmrig_status.get("hashrate", {})
        current_hashrate = hashrate_data.get("total", [0])[0]
        highest_hashrate = hashrate_data.get("highest", 0)
        
        # Memory Info
        memory = xmrig_status.get("resources", {}).get("memory", {})
        total_memory = format_bytes(memory.get("total", 0))
        free_memory = format_bytes(memory.get("free", 0))
        
        # Connection Info
        conn = xmrig_status.get("connection", {})
        pool = conn.get("pool", "Unknown")
        uptime = format_timespan(conn.get("uptime", 0))
        
        # Performance Info
        results = xmrig_status.get("results", {})
        shares_good = results.get("shares_good", 0)
        shares_total = results.get("shares_total", 0)
        best_hash = max(results.get("best", [0]))
        
        # Format pesan dengan informasi lengkap
        message = (
            f"*📊 Status Mining XMRig*\n\n"
            f"*🖥️ Informasi Sistem:*\n"
            f"• Worker: `{worker_id}`\n"
            f"• CPU: `{cpu_name}`\n"
            f"• Threads: `{threads}`\n"
            f"• Memory Total: `{total_memory}`\n"
            f"• Memory Tersedia: `{free_memory}`\n\n"
            
            f"*⚡ Performa Mining:*\n"
            f"• Hashrate Saat Ini: `{current_hashrate:.2f} H/s`\n"
            f"• Hashrate Tertinggi: `{highest_hashrate:.2f} H/s`\n"
            f"• Hash Terbaik: `{best_hash}`\n"
            f"• Shares Diterima: `{shares_good}`\n"
            f"• Total Shares: `{shares_total}`\n\n"
            
            f"*🌐 Informasi Koneksi:*\n"
            f"• Pool: `{pool}`\n"
            f"• Waktu Aktif: `{uptime}`\n\n"
            
            f"_🕒 Update terakhir: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_"
        )
        
        # Kirim pesan ke Telegram
        send_telegram_message(message)

if __name__ == "__main__":
    main()  # Sudah diperbaiki
