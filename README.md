# WiFi Mapper com GPS (Raspberry Pi Zero)

## 📖 Descrição

Projeto para mapear intensidade de sinal Wi-Fi com coordenadas GPS usando um Raspberry Pi Zero, e gerar posteriormente heatmaps em HTML num PC.

---

## 📦 Estrutura

- `src/scan_wifi.py` → corre no Raspberry Pi, regista sinal Wi-Fi e localização GPS num ficheiro CSV.
- `tools/generate_heatmap.py` → corre no PC, lê o CSV e gera um heatmap em HTML com Folium.

---

## 📥 Instalação no Raspberry Pi

```bash
sudo apt-get update
sudo apt-get install -y python3-venv wireless-tools gpsd gpsd-clients python3-gps
python3 -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt
