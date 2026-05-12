import flet as ft
import threading
import time

def main(page: ft.Page):
    page.title = "Bilinçli Tarım Kontrol Paneli"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Sayfa hizalamasını Column içinden değil, doğrudan page üzerinden yapıyoruz
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Gösterge değerleri
    temp_val = ft.Text("0°C", size=40, weight="bold", color="red")
    hum_val = ft.Text("0%", size=40, weight="bold", color="blue")
    water_val = ft.Text("%0", size=40, weight="bold", color="cyan")
    status_msg = ft.Text("Durum: Bekleniyor...", italic=True, color="orange")

    # ARAYÜZÜ OLUŞTURMA
    # Hata veren 'padding' argümanını Column'dan kaldırıp Container içine aldık
    page.add(
        ft.Text("AKILLI TARIM SİSTEMİ", size=30, weight="bold"),
        status_msg,
        ft.Divider(),
        
        # Sıcaklık ve Nem Kartları
        ft.Row([
            ft.Container(
                content=ft.Column([ft.Text("Sıcaklık"), temp_val]),
                padding=20, bgcolor="red50", border_radius=10, expand=True
            ),
            ft.Container(
                content=ft.Column([ft.Text("Nem"), hum_val]),
                padding=20, bgcolor="blue50", border_radius=10, expand=True
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),

        # Su Deposu Kartı
        ft.Container(
            content=ft.Column([ft.Text("Su Deposu"), water_val], horizontal_alignment="center"),
            padding=20, bgcolor="cyan50", border_radius=10, width=400
        ),

        # Kontrol Butonları (Hata riskine karşı ikonları şimdilik kaldırdık, isimleri sadeleştirdik)
        ft.Row([
            ft.Button("Su Pompasını Çalıştır"),
            ft.Button("Gübre Karıştır"),
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    # Bluetooth Simülasyonu (Ekranın çalıştığını kanıtlamak için)
    def update_test():
        time.sleep(2)
        temp_val.value = "24°C"
        hum_val.value = "%45"
        water_val.value = "%75"
        status_msg.value = "Durum: Bluetooth Bağlantısı Kuruldu ✅"
        status_msg.color = "green"
        page.update()

    threading.Thread(target=update_test, daemon=True).start()

# Yeni standartlara göre en güvenli çalıştırma şekli
if __name__ == "__main__":
    ft.run(main)