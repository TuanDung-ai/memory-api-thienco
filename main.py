from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Web App Google Script URL của bạn
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbygeT-0ny4KHv_ZJJpK4j5BdizfGVbZ6yjzEBh7Duz9FoUza8CeUzETSOfa0uAd0YhF/exec"

@app.route('/ghi_nho', methods=['POST'])
def ghi_nho():
    try:
        data = request.get_json()
        thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        chu_de = data.get('chu_de', 'Không rõ')
        noi_dung = data.get('noi_dung', 'Không có nội dung')
        ghi_chu = data.get('ghi_chu', '')

        # Gửi tới Google Apps Script Web App
        payload = {
            'thoiGian': thoi_gian,
            'chuDe': chu_de,
            'noiDung': noi_dung,
            'ghiChu': ghi_chu
        }
        response = requests.get(GOOGLE_SCRIPT_URL, params=payload)
        
        return jsonify({'status': 'ok', 'sheet_response': response.text}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
